from django.urls import path
from rest_framework.authtoken import views
from currency.views import AddCurrency,UpdateCurrency,DeleteCurrency,CurrencyView

urlpatterns = [
    path('add/',AddCurrency.as_view(),name='add'),
    path('currencies/',CurrencyView.as_view(),name='currencies'),
    path('update/<int:pk>', UpdateCurrency.as_view(), name='update'),
    path('delete/<int:pk>', DeleteCurrency.as_view(), name='delete')


]
