from django.urls import path
from .views import AgentListView, AgentCreateView, AgentDetailView, AgentupdateView, AgentDeleteView

app_name = 'agents'

urlpatterns = [
    path('', AgentListView.as_view(), name='agent-list'),
    path('create/', AgentCreateView.as_view(), name='agent-create' ),
    path('<int:pk>', AgentDetailView.as_view(), name='agent-detail'),
    path('<int:pk>/delete', AgentDeleteView.as_view(), name='agent-delete'),
    path('<int:pk>/update', AgentupdateView.as_view(), name='agent-update'),
]