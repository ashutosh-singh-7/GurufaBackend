"""
URL configuration for GurufaBackend project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
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
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from user.verifyViews import verify_email, resetKeyView
from django.contrib.auth import views as auth_views
from django.views.generic import TemplateView




urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/', include('api.urls')),
    path('', TemplateView.as_view(template_name='index.html'), name='index-page'),
    path('verify/<str:uidb64>/<str:token>/', verify_email, name='verify_email'),
    path('reset/<uidb64>/<token>/', resetKeyView, name='password_reset_confirm'),

    ] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)


admin.site.site_header = "Gurufa Administration"
admin.site.site_title = "Gurufa Admin Panel"
admin.site.index_title = ""
