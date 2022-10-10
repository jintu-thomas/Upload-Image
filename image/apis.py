from django import views
from django.contrib import admin
from django.urls import path
from django.conf.urls.static import static
from django.conf import settings
from . import views

urlpatterns = [
    path('register',views.RegisterView.as_view(),name = 'register'),
    path('login',views.CustomAuthLogin.as_view(),name ="login"),
    path('upload/',views.upload_image,name = 'upload-image'),
    path('logout/',views.LogoutView.as_view(),name = 'logout'),
] + static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)