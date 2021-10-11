from django.urls import path

from . import views

app_name='user'
urlpatterns = [
    path('', views.index, name='Index'),
    path('register', views.register, name='register'),
    path('loggout', views.loggout, name='loggout'),
    path('edit/profile/', views.editUser, name='user_update'),
    path('edit/password/', views.password, name='password_update')
]