from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import redirect
from django.contrib.auth import login as auth_login, logout as auth_logout, authenticate
from django.contrib.auth.models import User
from django.views import generic
from django.contrib import messages


class Login(generic.TemplateView):
    template_name = 'login.html'

    def post(self, request):
        if request.method == 'POST':
            username = request.POST['username']
            password = request.POST['password']
            user = authenticate(request, username=username, password=password)
            if user is not None:

                auth_login(request, user)
                return redirect('notes:index')
            else:
                messages.error(request, 'Incorect username or password')

                return redirect(request.get_full_path())

    def dispatch(self, *args, **kwargs):
        if self.request.user.is_authenticated:
            return redirect('notes:index')
        else:
            return super().dispatch(*args, **kwargs)


class Register(generic.TemplateView):
    template_name = 'register.html'

    def post(self, request):

        username = request.POST['username']
        password = request.POST['password']
        re_password = request.POST['re_password']
        full_name = request.POST['full_name']

        if username == '' or password == '' or full_name == '':
            messages.error(request, 'You must fill all fields')
            return render(request, 'register.html', {'username': username, 'full_name': full_name})
        if password != re_password:
            messages.error(request, 'Password isn\'t matched')
            return render(request, 'register.html', {'username': username, 'full_name': full_name})
        if User.objects.filter(username=username).exists():
            messages.error(request, 'user name existed try another')
            return render(request, 'register.html', {'username': username, 'full_name': full_name})
        User.objects.create_user(username=username, password=password, first_name=full_name)
        messages.success(request, 'Create user {}'.format(username))
        return redirect('register')

    def dispatch(self, *args, **kwargs):
        return super().dispatch(*args, **kwargs)


def logout(request):
    auth_logout(request)
    return redirect('login')
