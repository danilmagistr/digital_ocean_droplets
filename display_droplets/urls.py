from django.urls import path
# from .views import HomePageView
from display_droplets import views
from django.conf.urls import url

app_name = 'display_droplets'

# urlpatterns = [
#     path('', HomePageView.as_view(), name='home'),
# ]
urlpatterns=[
    url(r'^register/$',views.register,name='register'),
    url(r'^user_login/$',views.user_login,name='user_login'),
]