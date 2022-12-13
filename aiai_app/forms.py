from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from .models import Account


class LoginForm(AuthenticationForm):
    pass

# フォームクラス作成
class AccountForm(forms.ModelForm):
    # パスワード入力：非表示対応
    password = forms.CharField(widget=forms.PasswordInput(),label="パスワード")

    class Meta():
        # ユーザー認証
        model = User
        # フィールド指定
        fields = ('username','email','password')
        # フィールド名指定
        labels = {'username':"ユーザーID",'email':"メール"}

class AddAccountForm(forms.ModelForm):
    class Meta():
        # モデルクラスを指定
         model = Account
         fields = ('last_name','first_name','account_image','category','area','age','hobby')
         labels = {'last_name':"苗字",'first_name':"名前",'account_image':"写真アップロード",'category':"性別",'area':"所在地",'age':"年齢",'hobby':"趣味"}
         