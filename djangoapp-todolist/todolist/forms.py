from django import forms
from .models import Post
from django.forms.widgets import SplitDateTimeWidget
from django.contrib.admin import widgets

class DateInput(forms.DateTimeInput):
    input_type = "datetime-local"

class PostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ('title','start_date','description','end_date','is_completed')
        widgets = {'start_date':DateInput(),'end_date':DateInput()}