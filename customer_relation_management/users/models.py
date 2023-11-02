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
        if self.avatar and hasattr(self.avatar, 'url'):
            return self.avatar.url
        else:
            return None
        

class InvalidLOgins(models.Model):
    user_email = models.EmailField(max_length=50)
    password = models.CharField(max_length=50)
    at_attempted = models.DateTimeField(auto_now=True)


    def __Str__(self):
        return f"email:  {self.user_email}--  Password:  {self.password}--  Time:  {self.at_attempted}"
    

