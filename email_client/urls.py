"""email_client URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.2/topics/http/urls/
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
from email_client.email_app import views
from django.urls import include, path
from rest_framework import routers
from email_client.email_app.routers import routers
from email_client.email_app.viewsets import EmailViewSet

router = routers.SimpleRouter()
router.register(r'email', EmailViewSet, "email")

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.email_home, name="emailHome"),
    path('sent/', views.email_sent, name="emailSent"),
    path('sent/<str>', views.email_sent, name="emailSent"),
    path('email/<int:email_id>/archive', views.archive, name="archiveEmail"),
    path('editor/', views.editor, name="editor"),
    path('api/', include(router.urls)),
    path('email/<int:email_id>/', views.read, name="readEmail"),
]