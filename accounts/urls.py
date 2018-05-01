from django.urls import path

from accounts import views as d

app_name = 'auth'
urlpatterns = [
    path('login/', d.login_view, name='login'),
    path('logout/', d.logout_view, name='logout'),
    path('register/', d.register, name='register'),
]
