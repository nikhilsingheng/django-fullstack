from datetime import datetime

from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import TemplateView
from django.contrib.auth.views import LoginView, LogoutView
from django.views.generic.edit import CreateView
from django.contrib.auth.forms import UserCreationForm
from django.shortcuts import redirect

# Create your views here.


class SignUp(CreateView):
    form_class = UserCreationForm
    template_name = 'signup.html'
    success_url = '/stop'

    def get(self, request, * args, **kwargs):
        if self.request.user.is_authenticated:
            return redirect('node.list')
        return super().get(request, *args, **kwargs)


class Lougout(LogoutView):
    template_name = 'lougout.html'


class LoginViewdata(LoginView):
    template_name = 'loginuser.html'


class HomeView(TemplateView):
    template_name = 'index.html'
    extra_context = {"today": datetime.today()}


# def Data(request):
#     return render(request, 'index.html', {'title': "ssss"})

class AuthorizedView(LoginRequiredMixin, TemplateView):
    template_name = 'Login.html'
    login_url = '/admin'


# @login_required(login_url='/admin')
# def Login(request):
#     return render(request, 'Login.html', {})
