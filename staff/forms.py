"""This module create forms."""

from django import forms
from django.contrib.auth.models import User
from mptt.forms import TreeNodeChoiceField

from staff.models import EmployeeMptt


class ProductModelInlineForm(forms.ModelForm):
    """This class create form for model EmployeeMptt."""

    parent = TreeNodeChoiceField(queryset=EmployeeMptt.objects.all(),
                                 required=False)

    class Meta:
        """Metadata of EmployeeMptt."""

        model = EmployeeMptt
        fields = '__all__'


class UserChangeForm(forms.ModelForm):
    """Creates form for change user, using model User."""

    class Meta:
        """Metadata of User."""

        model = User
        fields = ('email', 'username', 'password')
