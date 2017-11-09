"""masailing URL Configuration

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
from django.views.generic.base import TemplateView

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^$', TemplateView.as_view(template_name='pages/index.html')),
    url(r'^general/$', TemplateView.as_view(template_name='pages/general.html')),
    url(r'^sfyc/$', TemplateView.as_view(template_name='pages/sfyc.html')),
    url(r'^costs/$', TemplateView.as_view(template_name='pages/costs.html')),
    url(r'^roster/$', TemplateView.as_view(template_name='pages/roster.html')),
    url(r'^hssailing/$', TemplateView.as_view(template_name='pages/hssailing.html')),
    url(r'^recruiting/$', TemplateView.as_view(template_name='pages/recruiting.html')),
    url(r'^schedule/$', TemplateView.as_view(template_name='pages/schedule.html')),
    url(r'^test/$', TemplateView.as_view(template_name='pages/test.html')),
    url(r'^test2/$', TemplateView.as_view(template_name='pages/test2.html')),
]
