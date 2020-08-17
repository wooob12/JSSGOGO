"""JssProject URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('앱이름.urls'))
"""
from django.contrib import admin
from django.urls import path, include
# from main.views import index, create, detail, delete, update -> main 아래로 옮김


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('main.urls')),
    path('', include('accounts.urls')),    
    # path('', index, name="index"),
    # path('create/', create, name="create"),
    # path('detail/<int:jss_id>', detail, name="detail"),
    # path('delete/<int:jss_id>', delete, name="delete"),    
    # path('update/<int:jss_id>', update, name="update"), 필요 없어져서 버림
]
