from django.db import models
from django.contrib.auth.models import User
from django.urls import reverse

# Create your models here.

class ReviewCategory(models.Model):
    name = models.CharField(max_length=254)
    friendly_name = models.CharField(max_length=254, null=True, blank=True)

    def __str__(self):
        return str(self.name)

    def get_friendly_name(self):
        return self.friendly_name

class UserReview(models.Model):
    title = models.CharField(max_length=254)
    description = models.TextField()
    cover_image = models.ImageField(null=True, blank=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    category = models.ForeignKey(ReviewCategory, null=False, blank=False,
        on_delete=models.CASCADE)

    def __str__(self):
        return str(self.title)

    def get_absolute_url(self):
        """Get url after user adds/edits recipe"""
        return reverse('review_detail', kwargs={'pk': self.pk})

    