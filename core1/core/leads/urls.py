from django.contrib import admin
from django.urls import path

from leads.views import (homepage, leaddetail, lead_create, leadUdate, lead_delete,
        LeadListView,LeadDetailView, CreateHome, UpdateHome, DeleteHome, SignupView
    )


app_name = "leads"


urlpatterns = [
    path('', LeadListView.as_view(), name='lead-list'),
    path('<str:pk>/', LeadDetailView.as_view(), name='lead-detail'),
    # path('leadcreate/',  CreateHome.as_view(), name="lead_create"), 
    # path('SignupView/',  SignupView.as_view(), name="SignupView"), 
    # path('<str:pk>/update/', UpdateHome.as_view(), name="leadUdate"),
    # path('<str:pk>/delete/', DeleteHome.as_view(), name="delete"),
    # path('<int:pk>/', LeadDetailView.as_view(), name='lead-detail'),


]
