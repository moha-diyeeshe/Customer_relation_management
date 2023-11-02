Users Package
=============

Subpackages and Modules
-----------------------

.. toctree::
   :maxdepth: 4

   users.migrations
   users.admin
   users.apps
   users.forms
   users.models
   users.tests
   users.urls
   users.views

Users Views Module
------------------

This module provides views for user-related functionality, including registration, login, handling valid logins, and profile management.

.. automodule:: users.views
   :members:
   :undoc-members:
   :show-inheritance:

View Functions
--------------

.. autofunction:: users.views.index
   :noindex:

.. autofunction:: users.views.registration
   :noindex:

.. autofunction:: users.views.user_list
   :noindex:

.. autofunction:: users.views.update_user
   :noindex:

.. autofunction:: users.views.delete_user
   :noindex:

.. autofunction:: users.views.user_login
   :noindex:

.. autofunction:: users.views.user_logout
   :noindex:

.. autofunction:: users.views.profile
   :noindex:

Form Classes
------------

User Registration Form
^^^^^^^^^^^^^^^^^^^^^

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
^^^^^^^^^^^^^^

The `UserLoginForm` class provides a form for user login.

.. code-block:: python

    from django import forms

    class UserLoginForm(forms.Form):
        email = forms.EmailField(label='E-Mail Address', widget=forms.EmailInput(attrs={'class': 'form-control'}))
        password = forms.CharField(label='Password', widget=forms.PasswordInput(attrs={'class': 'form-control'}))

Transaction Forms
^^^^^^^^^^^^^^^^

User-related transaction forms.

.. autoclass:: users.forms.TransactionForm
   :members:
   :undoc-members:
   :show-inheritance:

.. autoclass:: users.forms.TransactionChangeForm
   :members:
   :undoc-members:
   :show-inheritance:

Models
------

User Model
^^^^^^^^^

The `User` model extends Django's built-in `AbstractUser` model and includes additional fields such as `email`, `phone`, `gender`, `avatar`, and `modified_at`.


.. code-block:: python

   from django.contrib.auth.models import AbstractUser, Group, Permission
   from django.db import models

   class User(AbstractUser):
       email = models.EmailField(unique=True)
       phone = models.CharField(max_length=50, null=False, blank=False)
       gender = models.CharField(max_length=10, null=True, blank=True)
       avatar = models.ImageField(upload_to="Avatars/Users/", blank=True, null=True)
       modified_at = models.DateTimeField(auto_now=True, null=True, blank=True)

       # Add related_name for groups and user_permissions
       groups = models.ManyToManyField(
           Group,
           verbose_name='groups',
           blank=True,
           related_name='custom_user_groups'
       )
       user_permissions = models.ManyToManyField(  
           Permission,
           verbose_name='user permissions',
           blank=True,
           related_name='custom_user_permissions'
       )

       USERNAME_FIELD = 'email'
       REQUIRED_FIELDS = ['username']

       class Meta:
           db_table = 'users'

       def get_avatar_url(self):
           """Get the URL of the user's avatar image."""
           if self.avatar and hasattr(self.avatar, 'url'):
               return self.avatar.url
           else:
               return None

   

Invalid Logins Model
--------------------

The `InvalidLOgins` model records unsuccessful login attempts.

.. code-block:: python

   from django.db import models

   class InvalidLOgins(models.Model):
       user_email = models.EmailField(max_length=50)
       password = models.CharField(max_length=50)
       at_attempted = models.DateTimeField(auto_now=True)

       def __str__(self):
           return f"Email: {self.user_email} -- Password: {self.password} -- Time: {self.at_attempted}"

Helper Functions and Utilities
-------------------------------

- `get_object_or_404()`: Function to get an object from the database or raise a 404 error if not found.
- `make_password()`: Function to securely hash a password.
- `authenticate()`: Function to authenticate a user.
- `login()`: Function to log in a user.
- `logout()`: Function to log out a user.
- `reverse()`: Function to generate URLs.
- `HttpResponse()`: Class representing an HTTP response.
- `HttpResponseRedirect()`: Class representing an HTTP redirect response.
- `timezone.now()`: Function to get the current time with timezone awareness.
- `Count()`: Function to count the number of items in a queryset.
- `Sum()`: Function to calculate the sum of values in a queryset.
- `render()`: Function to render a template with a context dictionary.

Module Contents
---------------

.. automodule:: users
   :members:
   :undoc-members:
   :show-inheritance:
