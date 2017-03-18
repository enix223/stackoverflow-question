from django.shortcuts import render, redirect
from django import forms
from app.models import Event, Book
from django.http import HttpResponse
# from django.core.urlresolvers import reverse
from django.urls import reverse
from django.contrib.postgres.forms import DateRangeField
from django.views.generic import FormView
from django.contrib.auth import authenticate, login
from django.views.generic import View
from psycopg2.extras import DateRange
from rest_framework.generics import GenericAPIView
from rest_framework.mixins import UpdateModelMixin
from rest_framework.viewsets import ModelViewSet
from rest_framework import serializers

from django.core.files import File
from rest_framework import viewsets
from app.models import Image
import base64


class ImageSerializer(serializers.ModelSerializer):

    base64_image = serializers.SerializerMethodField()

    class Meta:
        model = Image
        fields = ('base64_image', 'id')

    def get_base64_image(self, obj):
        f = open(obj.image_file.path, 'rb')
        image = File(f)
        data = base64.b64encode(image.read())
        f.close()
        return data


class ImageViewSet(viewsets.ModelViewSet):
    http_method_names = ['get', 'put', 'post']
    queryset = Image.objects.all()
    serializer_class = ImageSerializer
    pagination_class = None


class ConsoleView(View):
    def get(self, request, *args, **kwargs):
        return HttpResponse(request.user.username)


class LoginForm(forms.Form):
    username = forms.CharField()
    password = forms.CharField()


def login_view(request):
    title = "Login"
    user_form = LoginForm(request.POST or None)
    if user_form.is_valid():
        username = user_form.cleaned_data.get('username')
        password = user_form.cleaned_data.get('password')
        user = authenticate(username=username, password=password)
        login(request, user)
        return redirect(reverse('accounts:index', args=(username, )))
    return render(request, 'login.html', {'user_form': user_form, 'title': title})


class LoginView(FormView):
    form_class = LoginForm
    template_name = 'login.html'

    def post(self, request, *args, **kwargs):
        form = self.get_form()
        if form.is_valid():
            username = form.cleaned_data['username']
            pwd = form.cleaned_data['password']
            user = authenticate(username=username, password=pwd)
            if user is not None:
                login(request, user)
                return redirect(reverse('index', args=(username, )))
            else:
                return HttpResponse('Account/pwd not correct', status=400)
        else:
            return HttpResponse('Account or pwd is empty', status=400)

    def form_valid(self, form):
        super(LoginView, self).form_valid(form)


def detect_dom_change(request):
    return render(request, 'detect_dom_change.html', {})


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
