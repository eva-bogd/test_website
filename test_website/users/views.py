from django.contrib.auth import get_user_model
from django.contrib.auth.decorators import login_required
from django.http import HttpResponseForbidden
from django.shortcuts import get_object_or_404, redirect, render
from django.urls import reverse_lazy
from django.views.generic import CreateView

from .forms import CreationForm, ProfileUpdateForm


User = get_user_model()


class SignUp(CreateView):
    form_class = CreationForm
    success_url = reverse_lazy('services:home')
    template_name = 'users/signup.html'


def profile(request, username):
    user = get_object_or_404(User, username=username)
    my_list_services = []
    my_list_orders = []
    if user == request.user:
        if user.role == 'executor':
            my_list_services = user.services.all()
            my_list_orders = user.executor_orders.all()
        else:
            my_list_orders = user.customer_orders.all()
    else:
        my_list_services = user.services.all()
    context = {
        'user': user,
        'my_list_services': my_list_services,
        'my_list_orders': my_list_orders,
    }
    return render(request, 'users/profile.html', context)


@login_required
def change_role(request, username):
    user = get_object_or_404(User, username=username)
    if user == request.user:
        new_role = request.POST.get('new_role')
        user.role = new_role
        user.save()
    return redirect('users:profile', username=user.username)


@login_required
def profile_settings(request, username):
    user = get_object_or_404(User, username=username)
    profile_form = ProfileUpdateForm(instance=user)
    context = {
        'user': user,
        'profile_update_form': profile_form,
    }
    return render(request, 'users/profile_settings.html', context)


@login_required
def update_profile(request, username):
    user = get_object_or_404(User, username=username)
    if user != request.user:
        return HttpResponseForbidden(
            "Вы не можете редактировать этот профиль.")
    profile_form = ProfileUpdateForm(
        request.POST,
        request.FILES,
        instance=user)
    if profile_form.is_valid():
        profile_form.save()
        return redirect('users:profile', username=user.username)
    context = {
        'user': user,
        'profile_update_form': profile_form,
    }
    return render(request, 'users/profile_settings.html', context)
