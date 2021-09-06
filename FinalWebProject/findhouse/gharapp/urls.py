from django.urls import path
from .import views
from django.contrib.auth import views as auth_views
urlpatterns=[
    path('index',views.index),
    path('registeropt', views.registeroption),
    path('contactus', views.contact),
    path('room', views.room),
    path('flat', views.flat),
    path('password_change', auth_views.PasswordChangeView.as_view(template_name='gharapp/passwordChange.html')),
    path('password_change_done', auth_views.PasswordChangeView.as_view(template_name='gharapp/passwordChangeDone.html'),name='password_change_done'),
    path('view_detail', views.viewdetail)

]