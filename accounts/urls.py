from django.urls import path
from accounts import views

urlpatterns = [
    path('accounts/', views.AccountsList.as_view()),
]