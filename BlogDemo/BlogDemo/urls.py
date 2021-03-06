"""BlogDemo URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.10/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""

from django.conf.urls import url,include
from django.contrib import admin



urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^',include('blog.urls')),
    url(r'^simditor/', include('simditor.urls')), #富文件本编辑器 上传图片
    # url(r'^users/',include('users.urls')), #用户信息
    #这里是Django自带的登录注册
    # url(r'^users/', include('django.contrib.auth.urls')),  # 将 auth 应用中的 urls 模块包含进来
    url(r'^accounts/', include('allauth.urls')),

]

