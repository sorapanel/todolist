from django.shortcuts import render, redirect
from django.views.generic import TemplateView
from registration.forms import LoginForm, AccountForm
from django.contrib.auth import authenticate, login, logout

class SignUpView(TemplateView):
    template_name = 'signup.html'
    form_class = AccountForm

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        form = self.form_class()
        context['form'] = form
        context['message'] = ''
        return context
    
    def post(self,request):
        form = self.form_class(request.POST)

        if form.is_valid():
            account = form.save()
            account.set_password(account.password)
            account.save()
        else:
            message = 'フォームが無効です。'
            return render(request, "signup.html", {'form': form, 'message':message})

        return redirect('login')


class LoginView(TemplateView):
    template_name = 'login.html'
    form_class = LoginForm

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        form = self.form_class()
        context['form'] = form
        context['message'] = ''
        return context
    
    def post(self, request):
        form = self.form_class(request.POST)
        if form.is_valid():
            name = form.cleaned_data['name']
            password = form.cleaned_data['password']
            
            user = authenticate(username=name, password=password)

            if user:
                if user.is_active:
                    login(request, user)
                    request.session['username'] = {'username':name,}
                    return redirect('main')
                else:
                    message="アカウントが有効ではありません。"
                    return render(request, "login.html", {'form': form, 'message':message})
                
            else:
                message="ユーザ名またはパスワードが間違っています。"
                return render(request, "login.html", {'form': form, 'message':message})
        else:
            message="フォームが無効です。"
            return render(request, "login.html", {'form': form, 'message':message})
        

def Logout(request):
    logout(request)
    return redirect("index")
