"""
URL configuration for web project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.0/topics/http/urls/
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
from webapp import views
from webapp.views import *
from django.conf import settings
from django.conf.urls.static import static
from django.contrib.auth.decorators import login_required

urlpatterns = [
    path('admin/', admin.site.urls),
    path('home/', login_required(home)),
    path('', signin_or_home),  # Default to the signin page if not authenticated, otherwise go to home
     path('dashboard/', views.dash, name='dash'), 
    path('signin/', signin),
    path('signout/', views.signout, name='signout'),
    path('signup/', views.signup, name='signup'),
    path('insertdata/', insertdata),
    # path('insertbook/',insertbook),
    path('viewusers/', viewusers),
    path('harini/', views.harini, name='harini'),
    path('john/', views.john, name='john'),
    path('api/userdata/', userdata_api, name='userdata-api'),
    path('faculty/',views.faculty,name='faculty'),
    path('view/',views.view),
    path('paper/', views.paper_presentation, name='paper-presentation'),
    path('insertbook/',views.insertbook,name='insertbook'),
    path('insertjournal',views.insertjournal,name='insertjournal'),
     path('insertpatent',views.insertpatent,name='insertpatent'),
    path('adminlogin/', views.adminlogin, name='adminlogin'),
    path('adminfun/', views.adminfun, name='adminfun'),
    path('accept_submission/', views.accept_submission, name='accept_submission'),
    path('reject_submission/', views.reject_submission, name='reject_submission'),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

