from django.urls import path
from likes import views

urlpatterns = [
    path('likes/', views.LikesList.as_view()),
    path('likes/<int:pk>/', views.LikeDetail.as_view()),
]