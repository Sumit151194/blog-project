from django.contrib import admin
from django.conf.urls import url, include
from  django.contrib.auth import views
from django.contrib.auth.views import auth_login,auth_logout

urlpatterns = [
    url(r'admin/', admin.site.urls),
    url(r'', include('blogapp.urls')),
]
