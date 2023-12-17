from django.contrib.auth import logout, authenticate, login
from django.shortcuts import render, redirect
from .forms import AccountCreationForm, LoginForm


def login_page(request):
    if request.method == "POST":
        form = LoginForm(request, data=request.POST)
        if form.is_valid():
            username = form.cleaned_data.get("username")
            password = form.cleaned_data.get("password")
            user = authenticate(username=username, password=password)
            if user is not None:
                login(request, user)
                return redirect("pages:index")
    else:
        form = LoginForm()
    context = {"form": form}
    return render(request, 'account/login_page.html', context)


def registration_page(request):
    if request.method == 'POST':
        form = AccountCreationForm(request.POST)
        if form.is_valid():
            form.save()

            return redirect('account:login')

    else:
        form = AccountCreationForm()
    return render(request, 'account/register_page.html', {'form': form})


def logout_user(request):
    logout(request)
    return redirect('pages:index')
