from django.urls import path
from post import views

urlpatterns=[
    path('', views.login_user, name="login_user"),
    path('home/', views.home, name="home"),
    path('ragistration/', views.signout_user, name="ragistration"),
    path('logout/', views.logout_user, name="logout_user"),
    path('profile/', views.user_profile, name="profile")
]