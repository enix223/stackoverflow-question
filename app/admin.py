from django.contrib import admin
from app.models import FormOne, Background
from django import forms


class FormOneForm(forms.ModelForm):
    class Meta:
        model = FormOne
        fields = ['name', 'background']

    background = forms.ModelChoiceField(widget=forms.RadioSelect, queryset=Background.objects.all(), required=False)


class FormOneAdmin(admin.ModelAdmin):
    fields = ['name', 'background']
    form = FormOneForm


admin.site.register(Background)
admin.site.register(FormOne, FormOneAdmin)
