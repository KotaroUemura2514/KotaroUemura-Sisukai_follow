from django.shortcuts import render, redirect
from django.views.generic import (ListView, DetailView, CreateView, DeleteView, UpdateView)
from .models import  Account, Connection
from django.urls import reverse,reverse_lazy
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views import View

class ListaiView(LoginRequiredMixin, ListView):
    template_name = 'pages/home.html'
    model=Account

    def get_queryset(self):
        """リクエストユーザーのみ除外"""
        return Account.objects.exclude(user=self.request.user)

class DetailView(DetailView):
    model = Account
    template_name = 'pages/detail.html'
    
    def get_context_data(self, *args, **kwargs):
        context = super().get_context_data(*args, **kwargs)
        context['connection'] = Connection.objects.get_or_create(user=self.request.user)
        return context


class FollowBase(LoginRequiredMixin, View):
    """フォローのベース。リダイレクト先を以降で継承先で設定"""
    def get(self, request, *args, **kwargs):
        pk = self.kwargs['pk']
        # sawada
        target_user = Account.objects.get(pk=pk).user
        # damin
        my_connection = Connection.objects.get_or_create(user=self.request.user)

        if target_user in my_connection[0].following.all():
            obj = my_connection[0].following.remove(target_user)
        else:
            obj = my_connection[0].following.add(target_user)
        return obj

class FollowDetail(FollowBase):
    """詳細ページでフォローした場合"""
    def get(self, request, *args, **kwargs):
        super().get(request, *args, **kwargs)
        pk = self.kwargs['pk'] 
        return redirect('detail', pk)

class FollowHome(FollowBase):
   """HOMEページでフォローした場合"""
   def get(self, request, *args, **kwargs):
       #FollowBaseでリターンしたobj情報を継承
       super().get(request, *args, **kwargs)
       #homeにリダイレクト
       return redirect('home')

#フォロー一覧表示機能
class FollowList(LoginRequiredMixin, ListView):
    model = Connection
    template_name = 'pages/list.html'

    def get_queryset(self):
        #フォロー内にユーザーが含まれているmy_connection = Connection.object.get_or_create(user=self.request.user)場合のみクエリセットを返す
        my_connection = Connection.objects.get_or_create(user=self.request.user)
        all_follow = my_connection[0].following.all()
        #投稿ユーザがフォローしているユーザに含まれている場合、オブジェクトを返す
        return Account.objects.filter(user__in=all_follow)

    def get_context_data(self, *args, **kwargs):
      """コネクションに関するオブジェクト情報をコンテクストに追加"""
      context = super().get_context_data(*args, **kwargs)
      #コンテクストに追加
      context['connection'] = Connection.objects.get_or_create(user=self.request.user)
      return context
    

