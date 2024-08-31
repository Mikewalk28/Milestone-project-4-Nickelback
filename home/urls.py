from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='home'),
    path('reviews/', views.ReviewList.as_view(), name='review_list'),
    path('addreview/', views.AddUserReview.as_view(), name='add_review'),
    path('editreview/<int:pk>/', views.EditUserReview.as_view(), name='edit_review'),
    path('deletereview/<int:pk>/', views.DeleteReview.as_view(), name='delete_review'),
    path('reviews/<int:pk>/',
        views.UserReviewDetail.as_view(), name='review_detail'
        ),
]