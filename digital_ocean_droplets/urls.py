"""digital_ocean_droplets URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.0/topics/http/urls/
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
from django.contrib import admin
from django.urls import path
from display_droplets.views import GetDroplets
from django.views.generic.base import TemplateView
from display_droplets import views
from django.conf.urls import url, include

# urlpatterns = [
#     path('admin/', admin.site.urls),
#     # path('', GetDroplets.as_view(template_name='droplets.html'), name='Droplet View'),
#     path('', TemplateView.as_view(template_name='home.html'), name='home'),
#     path('accounts/', include('django.contrib.auth.urls')),
# ]

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.index, name='index'),    
    path('special/', views.special, name='special'),    
    path('display_droplets/', include('display_droplets.urls')),
    path('logout/', views.user_logout, name='logout'),
    path('droplets/', GetDroplets.as_view(template_name='droplets.html'), name='Droplet View'),
    # url(r'^$',views.index,name='index'),
    # path('', TemplateView.as_view(template_name='index.html'), name='index'),
    # url(r'^special/',views.special,name='special'),
    # url(r'^display_droplets/',include('display_droplets.urls')),
    # url(r'^logout/$', views.user_logout, name='logout'),    
]