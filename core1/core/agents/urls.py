from django.urls import path

from .views import AgentListView, AgentCreateView, AgentDetailView, AgentUpdateView,AgentDeleteView

app_name = 'agents'

urlpatterns = [
    path('', AgentListView.as_view(), name='agent'),
    path('create/', AgentCreateView.as_view(), name='agent_create'),
    path('<int:pk>/', AgentDetailView.as_view(), name='agent_details'),
    path('<int:pk>/update/', AgentUpdateView.as_view(), name='AgentUpdate'),
    path('<int:pk>/delete/', AgentDeleteView.as_view(), name='dagent_delete'),

]