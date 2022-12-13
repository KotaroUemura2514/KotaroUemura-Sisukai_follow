from . import login, views
from django.urls import path


urlpatterns = [
    path('login',login.Login,name='Login'),
    path("logout",login.Logout,name="Logout"),
    path('register',login.AccountRegistration.as_view(), name='register'),
    path('',login.home,name=""),

    path('home',views.ListaiView.as_view(), name='home'),
    path('home/<int:pk>',views.DetailView.as_view(), name='detail'),
    path('follow-list/', views.FollowList.as_view(), name='follow-list'),

    path('follow-detail/<int:pk>', views.FollowDetail.as_view(), name='follow-detail'),
    path('follow-home/<int:pk>', views.FollowHome.as_view(), name='follow-home'),
]