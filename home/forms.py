from django import forms
from .models import ReviewCategory, UserReview


class UserReviewForm(forms.ModelForm):
    class Meta:
        """Get comment model, choose fields to display"""
        model = UserReview
        fields = ('title', 'description', 'cover_image', 'category',)