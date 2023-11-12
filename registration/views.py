from django.shortcuts import render, redirect
from django.views.generic import TemplateView
from registration.forms import LoginForm, AccountForm
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User
from .forms import DeleteForm

#サインアップに関するクラス
class SignUpView(TemplateView):
    template_name = 'signup.html'
    form_class = AccountForm

    #get処理
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        form = self.form_class()
        context['form'] = form
        context['message'] = ''
        return context

    #post処理
    def post(self,request):
        form = self.form_class(request.POST)

        #formから値取得
        if form.is_valid():
            name = form.cleaned_data['username']
            # if User.objects.filter(username = name).exists():
            #     message = "このユーザーネームはすでに登録されています。"
            #     return render(request, "signup.html", {"form":form, "message":message})
            # else:
            account = form.save()
            account.set_password(account.password)
            account.save()
        else:
            message = 'フォームが無効です。'
            return render(request, "signup.html", {'form': form, 'message':message})

        return redirect('login')

#ログインに関するクラス
class LoginView(TemplateView):
    template_name = 'login.html'
    form_class = LoginForm

    #get処理
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        form = self.form_class()
        context['form'] = form
        context['message'] = ''
        return context

    #post処理
    def post(self, request):
        form = self.form_class(request.POST)
        #formから値取得
        if form.is_valid():
            #氏名、パスワードの入力値獲得
            name = form.cleaned_data['name']
            password = form.cleaned_data['password']

            #ログイン
            user = authenticate(username=name, password=password)

            #ユーザが有効かどうか
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
        
#ログアウト
def Logout(request):
    logout(request)
    return redirect("index")

#アカウント削除（厳密にいうとアカウント復旧もかねてアカウントの無効化を行っている）
class DeleteView(TemplateView):
    template_name = "delete.html"
    form_class = DeleteForm

    #get処理
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        form = self.form_class()
        context['form'] = form
        context['message'] = ''
        return context

    #post処理
    def post(self, request):
        form = self.form_class(request.POST)

        #formから値取得
        if form.is_valid():
            #名前、パスワードの入力値を取得
            name = form.cleaned_data['name']
            password = form.cleaned_data['password']

            #ユーザ検証
            user = authenticate(username=name, password=password)

            #ユーザが存在すれば無効化を行う
            if user:
                if user.is_active:
                    user = User.objects.get(username = name)
                    user.is_active = False
                    user.save()
                    logout(request)
                    return redirect('delete_comp')
                else:
                    message="アカウントが有効ではありません。"
                    return render(request, "delete.html", {'form': form, 'message':message})
                
            else:
                message="ユーザ名またはパスワードが間違っています。"
                return render(request, "delete.html", {'form': form, 'message':message})
        else:
            message="フォームが無効です。"
            return render(request, "delete.html", {'form': form, 'message':message})

#削除完了用
def DeleteComp(request):
    return render(request, "delete_comp.html")


 

