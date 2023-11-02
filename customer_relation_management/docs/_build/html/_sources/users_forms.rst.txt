users.forms Module
==================

This module contains forms for user-related functionality, including user registration and login.

User Registration Form
----------------------

The `UserRegistrationForm` class provides a form for user registration.

.. code-block:: python

   from django import forms
   from django.contrib.auth.forms import UserCreationForm
   from django.contrib.auth import get_user_model

   User = get_user_model()

   class UserRegistrationForm(UserCreationForm):
       class Meta:
           model = User
           fields = ('first_name', 'last_name', 'username', 'email', 'phone', 'gender', 'avatar', 'password1', 'password2')

User Login Form
---------------

The `UserLoginForm` class provides a form for user login.

.. code-block:: python

   from django import forms

   class UserLoginForm(forms.Form):
       email = forms.EmailField(label='E-Mail Address', widget=forms.EmailInput(attrs={'class': 'form-control'}))
       password = forms.CharField(label='Password', widget=forms.PasswordInput(attrs={'class': 'form-control'}))
