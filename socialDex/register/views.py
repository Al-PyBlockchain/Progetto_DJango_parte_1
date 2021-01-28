from django.shortcuts import render, redirect
from .forms import RegisterForm
from django.contrib.auth.forms import UserCreationForm


def register(response):
    if response.method == 'POST':
        form = UserCreationForm(response.POST)
        if form.is_valid():
            form.save()

        return redirect('/post_list')
    else:
        form = RegisterForm()
    return render(response, 'register/register.html', {'form':form})