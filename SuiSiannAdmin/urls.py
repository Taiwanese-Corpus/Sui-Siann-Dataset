"""SuiSiannAdmin URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path
from kaldi.view import kiamtsa, 傳音檔


urlpatterns = [
    path('admin/', admin.site.urls),
    path('kaldi/<kuid>', kiamtsa),
    path(
        r'音檔/<音檔編號>/<開始時間>/<結束時間>/audio.wav',
        傳音檔
    ),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
