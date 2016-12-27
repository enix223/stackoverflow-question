from django.shortcuts import render
from django import forms
from app.models import Event, Book
from django.http import HttpResponse
from django.contrib.postgres.forms import DateRangeField
from psycopg2.extras import DateRange
from rest_framework.generics import GenericAPIView
from rest_framework.mixins import UpdateModelMixin
from rest_framework.viewsets import ModelViewSet
from rest_framework import serializers


class BookSerializer(serializers.ModelSerializer):
    class Meta:
        model = Book


class BookUpdateView(GenericAPIView, UpdateModelMixin):
    queryset = Book.objects.all()
    serializer_class = BookSerializer

    def put(self, request, *args, **kwargs):
        return self.update(request, *args, **kwargs)

class BookPartialUpdateView(GenericAPIView, UpdateModelMixin):
    queryset = Book.objects.all()
    serializer_class = BookSerializer

    def put(self, request, *args, **kwargs):
        return self.partial_update(request, *args, **kwargs)

class TestForm(forms.Form):
    choices = [('choice1', 'A'), ('choice2', 'B'), ('choice3', 'C')]
    test = forms.MultipleChoiceField(choices=choices, label='Test', initial=['choice3','choice2'])


def webhook(request, token):
    return HttpResponse(0)


def multi(request):
    form = TestForm()
    return render(request, 'multi.html', {'form': form})

class Event_form(forms.ModelForm):
    #datefromto = DateRangeField()

    class Meta:
        model = Event
        fields = ('name','datefromto')

    def clean(self):
        # import pdb; pdb.set_trace()
        print(self.cleaned_data)
        #{"name" : "Test Name"} there should be 'datefromto' key


def test(request):
    date_from = '2011-01-01'
    date_to = '2011-01-31'
    rng = DateRange(date_from, date_to)
    data = {
        "name" : "Test Name",
        "datefromto_0" : date_from,
        "datefromto_1": date_to,
    }

    form = Event_form(data)
    import pdb; pdb.set_trace()
    if form.is_valid():
        form.save()
        return HttpResponse('1')
    else:
        print(form.errors)
        return HttpResponse('0')
