from django.shortcuts import render, redirect, resolve_url
from django.contrib.auth.views import LoginView, logout_then_login, LogoutView
from django.contrib.auth import login as auth_login
from django.contrib import messages
from django.conf import settings
from .forms import SignupForm

login = LoginView.as_view(
    template_name = 'accounts/login.html',
)

logout = LogoutView.as_view(
    http_method_names = ['get'],
    next_page = settings.LOGIN_URL
)

# def logout(request):
#     messages.success(request, '로그아웃 되었습니다.')
#     return logout_then_login(request)

# Create your views here.
def signup(request):
    if request.method == 'POST':
        form = SignupForm(request.POST)
        if form.is_valid():
            signed_user = form.save()
            auth_login(request, signed_user)
            messages.success(request, '회원가입 환영합니다.')
            return redirect('/')
    else:
        form = SignupForm()
        
    return render(request, 'accounts/signup_form.html', {
        'form': form,
    })