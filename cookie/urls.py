
from django.contrib import admin
from django.urls import path
from cooking import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.index, name="home"),
    path('send', views.send, name='send')
]
