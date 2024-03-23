from django.shortcuts import render, get_object_or_404, reverse
from django.shortcuts import render
from .forms import UserReviewForm
from django.contrib.messages.views import SuccessMessageMixin
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.views import generic, View
from .models import UserReview
# Create your views here.

def index(request):
    return render(request, 'home/index.html')


class AddUserReview(LoginRequiredMixin, SuccessMessageMixin, generic.CreateView):
    """This view is used to allow logged in users to create a recipe"""
    form_class = UserReviewForm
    template_name = 'add_userreview.html'
    success_message = "%(calculated_field)s was created successfully"

    def form_valid(self, form):
        """
        This method is called when valid form data has been posted.
        The signed in user is set as the author of the recipe.
        """
        form.instance.user = self.request.user
        return super().form_valid(form)

    def get_success_message(self, cleaned_data):
        """
        This function overrides the get_success_message() method to add
        the recipe title into the success message.
        source: https://docs.djangoproject.com/en/4.0/ref/contrib/messages/
        """
        return self.success_message % dict(
            cleaned_data,
            calculated_field=self.object.title,
        )


class UserReviewDetail(View):
    """
    This view is used to display the full recipe details including comments.
    It also includes the comment form and add to meal plan form
    """
    def get(self, request, pk):
        """
        Retrives the recipe and related comments from the database
        """
        queryset = UserReview.objects.all()
        review = get_object_or_404(queryset, pk=pk)
        

        return render(
            request,
            "review_detail.html",
            {
                "review": review,
            },
        )