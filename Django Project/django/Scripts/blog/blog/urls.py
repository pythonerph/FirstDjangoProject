"""blog URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.11/topics/http/urls/
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
from django.conf.urls import url
from django.contrib import admin
from blog import views         # 导入新建的views.py文件，文件中定义了home方法。

urlpatterns = [
    #url(r'^admin/', admin.site.urls),
    url(r'^blog/(?P<id>[\w]+)$', views.home,name='home'),]        #将首页访问修改为home方法返回字符串
	#该正则将'[\w]+'匹配到的字符串传给参数'id'