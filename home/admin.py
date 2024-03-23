from django.contrib import admin
from .models import ReviewCategory, UserReview

# Register your models here.
@admin.register(ReviewCategory)
class ReviewCategoryAdmin(admin.ModelAdmin):
    """Allows admin to manage recipes via the admin panel"""
    list_filter = ('name',)
    list_display = ('name', 'friendly_name')
    search_fields = ('name', 'friendly_name')

@admin.register(UserReview)
class UserReviewAdmin(admin.ModelAdmin):
    """Allows admin to manage recipes via the admin panel"""
    list_filter = ('title',)
    list_display = ('title', 'user')
    search_fields = ('title', 'user')
    