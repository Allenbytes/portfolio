# projects/urls.py
from django.urls import path
from . import views
from .views import (
    ProjectListView,
    ProjectDetailView,
    ProjectCreateView,
    ProjectUpdateView,
    ProjectDeleteView,
    contact,
    contact_success_view,
    dashboard
)

urlpatterns = [
    path('', ProjectListView.as_view(), name='project-list'),
    path('project/<int:pk>/', ProjectDetailView.as_view(), name='project-detail'),
    path('project/new/', ProjectCreateView.as_view(), name='project-create'),
    path('project/<int:pk>/update/', ProjectUpdateView.as_view(), name='project-update'),
    path('project/<int:pk>/delete/', ProjectDeleteView.as_view(), name='project-delete'),
    path('contact/', contact, name='contact'),
    path('contact/success/', contact_success_view, name='contact_success'),
    path('dashboard/', dashboard, name='dashboard'),
    path('create/', ProjectCreateView.as_view(), name='project-create'),

]
