from . import views
from django.contrib import admin
from django.urls import path

app_name ='users'

urlpatterns = [
    path('',views.index,name='index'),
    path('registeration/',views.registerion,name='registration'),
    path('users/',views.user_list,name='all_users'),
    path('users/<int:user_id>/update/', views.update_user, name='update_user'),
    path('users/<int:user_id>/delete/', views.delete_user, name='delete_user'),
    path('login/', views.user_login, name='login'),
    path('logout/', views.user_logout, name='logout'),
    path('profile/',views.profile,name='profile'),

]