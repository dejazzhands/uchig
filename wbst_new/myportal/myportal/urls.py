"""
URL configuration for myportal project.

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
from . import views  # Add this line

urlpatterns = [
    path('Team/', views.Team, name='Team'),
    path('Research/', views.Research, name='Research'),
    path('News/', views.News, name='News'),
    path('Partners/', views.Partners, name='Partners'),
    path('Repository/', views.Repository, name='Repository'),
    path('Knowledge_Map/', views.Knowledge_Map, name='Knowledge_Map'),
    path('ML_Computing_Toolbox/', views.ML_Computing_Toolbox, name='ML_Computing_Toolbox'),
    path('Upload_Data/', views.Upload_Data, name='Upload_Data'),
    path('Upload_Tutorial/', views.Upload_Tutorial, name='Upload_Tutorial'),
    path('Test_Tagging_System/', views.Test_Tagging_System, name='Test_Tagging_System'),
    path('run_bayesian_optimization/', views.run_bayesian_optimization, name='run_bayesian_optimization'),

    # ... other paths
    path('', include('globus_portal_framework.urls')),
    path('', include('social_django.urls', namespace='social')),
]