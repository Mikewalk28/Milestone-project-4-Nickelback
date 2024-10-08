from django.shortcuts import render, get_object_or_404, reverse
from django.urls import reverse_lazy
from django.shortcuts import render
from django.contrib import messages
from .forms import UserReviewForm
from django.contrib.messages.views import SuccessMessageMixin
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.views import generic, View
from .models import UserReview
# Create your views here.

def index(request):
    return render(request, 'home/index.html')


class ReviewList(LoginRequiredMixin, View):
    """
    This view is used to display the full list of reviews.
    """
    def get(self, request):
        """
        Retrives the review and related comments from the database
        """
        review_list = UserReview.objects.all()

        return render(
            request,
            "review_list.html",
            {
                "review_list": review_list,
            },
        )


class AddUserReview(LoginRequiredMixin, SuccessMessageMixin, generic.CreateView):
    """This view is used to allow logged in users to create a review"""
    form_class = UserReviewForm
    template_name = 'add_userreview.html'
    success_message = "%(calculated_field)s was created successfully"

    def form_valid(self, form):
        """
        This method is called when valid form data has been posted.
        The signed in user is set as the author of the review.
        """
        form.instance.user = self.request.user
        return super().form_valid(form)

    def get_success_message(self, cleaned_data):
        """
        This function overrides the get_success_message() method to add
        the review title into the success message.
        source: https://docs.djangoproject.com/en/4.0/ref/contrib/messages/
        """
        return self.success_message % dict(
            cleaned_data,
            calculated_field=self.object.title,
        )


class EditUserReview(LoginRequiredMixin, SuccessMessageMixin, generic.UpdateView):
    """This view is used to allow logged in users to create a review"""
    model= UserReview
    fields = ["title", "description", "cover_image", "category"]
    template_name = "edit_userreview copy.html"

    def form_valid(self, form):
        """
        This method is called when valid form data has been posted.
        The signed in user is set as the author of the review.
        """
        form.instance.user = self.request.user
        return super().form_valid(form)

    def get_success_message(self, cleaned_data):
        """
        This function overrides the get_success_message() method to add
        the review title into the success message.
        source: https://docs.djangoproject.com/en/4.0/ref/contrib/messages/
        """
        return self.success_message % dict(
            cleaned_data,
            calculated_field=self.object.title,
        )



class UserReviewDetail(View):
    """
    This view is used to display the full review details including comments.
    """
    def get(self, request, pk):
        """
        Retrives the review and related comments from the database
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


class DeleteReview(
        LoginRequiredMixin, UserPassesTestMixin,  generic.DeleteView):
    """
    This view is used to allow logged in users to delete their own review
    """
    model = UserReview
    template_name = 'delete_userreview.html'
    success_message = "Review deleted successfully"
    success_url = reverse_lazy("review_list")
    

    def test_func(self):
        """
        Prevent another user from deleting other's reviews
        """
        review = self.get_object()
        return review.user == self.request.user

    def delete(self, request, pk):
        """
        This function is used to display sucess message given
        SucessMessageMixin cannot be used in generic.DeleteView.
        Credit: https://stackoverflow.com/questions/24822509/
        success-message-in-deleteview-not-shown
        """
        messages.success(self.request, self.success_message)
        return super(DeleteReview, self).delete(request)