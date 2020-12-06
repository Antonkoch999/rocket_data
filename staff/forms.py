from django import forms
from django.contrib.auth.models import User
from mptt.forms import TreeNodeChoiceField

from .models import EmployeeMptt


class ProductModelInlineForm(forms.ModelForm):
    parent = TreeNodeChoiceField(queryset=EmployeeMptt.objects.all(),
                                 required=False)

    class Meta:
        model = EmployeeMptt
        fields = '__all__'


class UserChangeForm(forms.ModelForm):
    """Creates form for change user, using model User."""

    class Meta:
        model = User
        fields = ('email', 'username', 'password')
