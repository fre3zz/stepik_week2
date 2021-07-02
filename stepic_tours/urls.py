"""stepic_tours URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
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
from tours import views as tour_views

# Error 404 and 500 custom handlers for tour_views

handler404 = tour_views.custom_handler404
handler500 = tour_views.custom_handler500

urlpatterns = [
    path('', tour_views.main_view),
    path('departure/<str:departure>/', tour_views.departure_view),
    path('tour/<int:id>/', tour_views.tour_view),
    path('admin/', admin.site.urls),
]

