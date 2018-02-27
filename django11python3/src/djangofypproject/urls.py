"""djangofypproject URL Configuration

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

from django.views.generic import TemplateView
from django.contrib import admin


from menu.views import (
    # contact_listview,
    ContactListView,
    ContactDetailView,
    ContactCreateView,
)

urlpatterns = [
    # url(r'^$', admin.site.urls),
]


urlpatterns += [
    url(r'catalog/admin/', admin.site.urls),
]


urlpatterns += [
    url(r'^catalog/$', TemplateView.as_view(template_name='home.html')),
    url(r'myprofile/', TemplateView.as_view(template_name='myprofile.html')),
    url(r'recognition/', TemplateView.as_view(template_name='recognition.html')),
    # url(r'contact/$', TemplateView.as_view(template_name='contact.html')),
    url(r'contact/$', ContactListView.as_view()),
    url(r'contact/create/$', ContactCreateView.as_view()),
    url(r'contact/(?P<slug>[\w-]+)/$', ContactDetailView.as_view()),
]
