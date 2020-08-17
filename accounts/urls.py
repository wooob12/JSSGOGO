from django.urls import path
from .views import signup, MyLoginView # loginview를 오버라이딩 했어요
from django.contrib.auth.views import LogoutView


urlpatterns = [
    path('signup/', signup, name='signup'),
    path('login/', MyLoginView.as_view(), name='login'),
    path('logout/', LogoutView.as_view(), name='logout'),
]