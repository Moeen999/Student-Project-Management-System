from django.urls import path
from .views import dashboard, add_project, edit_project, delete_project, review_project

urlpatterns = [
    path('', dashboard, name='dashboard'),
    path('add/', add_project, name='add_project'),
    path('project/<int:project_id>/edit/', edit_project, name='edit_project'),
    path('project/<int:project_id>/delete/', delete_project, name='delete_project'),
    path('review/<int:project_id>/', review_project, name='review_project'),
]