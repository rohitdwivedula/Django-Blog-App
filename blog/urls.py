from django.urls import path
from . import views

urlpatterns = [
    path('', views.post_list, name='post_list'),
    path('post/<int:post_id>/', views.post_detail, name='post_detail'),
    path('about', views.about, name='about'),
    path('privacy-policy', views.privacy_policy, name='privacy_policy'),
    path('contact', views.contact, name='contact'),
]