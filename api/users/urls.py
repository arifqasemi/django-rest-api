from django.urls import path
from rest_framework.authtoken import views
from users.views import Authentication,RegisterView,LogoutView

urlpatterns = [
    path('login/',Authentication.as_view(),name='login'),
    path('register/',RegisterView.as_view(),name='register'),
    path('logout/',LogoutView.as_view(),name='logout')


]