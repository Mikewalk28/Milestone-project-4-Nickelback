from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='home'),
    path('addreview/', views.AddUserReview.as_view(), name='add_review'),
    path('reviews/<int:pk>/',
        views.UserReviewDetail.as_view(), name='review_detail'
        ),
]