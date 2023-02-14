from django.urls import path
from accounts import views

urlpatterns = [
    path('accounts/', views.AccountsList.as_view()),
    path('accounts/<int:pk>/', views.AccountDetail.as_view()),
]