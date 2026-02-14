# Create your views here.
from django.shortcuts import render, redirect
from django.views import View
from django.contrib.auth import login
from django.contrib.auth.views import LoginView, LogoutView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import UpdateView
from django.urls import reverse_lazy
from .forms import UserRegisterForm, ProfileForm
from .models import Profile
class RegisterView(View):

    def get(self, request):
        user_form = UserRegisterForm()
        profile_form = ProfileForm()
        return render(request, "user/register.html", {
            "user_form": user_form,
            "profile_form": profile_form
        })
    def post(self, request):
        user_form = UserRegisterForm(request.POST)
        profile_form = ProfileForm(request.POST)

        if user_form.is_valid() and profile_form.is_valid():
            user = user_form.save()

            profile = profile_form.save(commit=False)
            profile.user = user
            profile.save()

            login(request, user)
            return redirect("home")

        return render(request, "user/register.html", {
            "user_form": user_form,
            "profile_form": profile_form
        })

class UserLoginView(LoginView):
    template_name = "user/login.html"

class UserLogoutView(LogoutView):
    next_page = "home"
class ProfileUpdateView(LoginRequiredMixin, UpdateView):
    model = Profile
    fields = ["phone_number", "address", "birth_date"]
    template_name = "user/profile.html"
    success_url = reverse_lazy("profile")

    def get_object(self):
        return self.request.user.profile