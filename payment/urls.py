from django.urls import path
from . import views

app_name = 'payment'

urlpatterns = [
    path('', views.MainPageView.as_view(), name='main_page'),
    path('buy-object/<int:pk>', views.BuyObjectView.as_view(), name='buy_object'),
    path('verify/', views.VerifyPayView.as_view()),
    path('test/', views.TestView.as_view())
]