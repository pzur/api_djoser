from django.urls import path,include
from . import views
from .views import *
from rest_framework import routers

routers=routers.DefaultRouter()
routers.register('cliente',views.ClienteList)
routers.register('mascota',views.MascotaList)
routers.register('paseador',views.PaseadorList)

urlpatterns = [
    path('',include(routers.urls)),
    path('login/',views.LoginView.as_view()),
    path('logout/', views.LogoutView.as_view()),
    #muestra todos los paseadores
    path("all-profiles/",PaseadorProfileListCreateView.as_view(),name="all-profiles"),
    # muestra los detalles de los paseadores
    path("profile/<int:pk>",PaseadorProfileDetailView.as_view(),name="profile"),
]