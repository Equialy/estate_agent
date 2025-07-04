from django.contrib.auth.views import LogoutView
from django.urls import path

from users import views

app_name = "users"


urlpatterns = [
    path('registration/', views.SignUpUser.as_view(), name='registration' ),
    path('', views.IndexView.as_view(), name='index' ),
    path('login/', views.LoginUser.as_view(), name='login' ),
    path('logout/', LogoutView.as_view(next_page='users:login'), name='logout'),
]