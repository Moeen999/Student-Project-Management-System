from django.urls import path
from .views import dashboard, add_project, review_project

urlpatterns = [
    path('', dashboard, name='dashboard'),
    path('add/', add_project, name='add_project'),
    path('review/<int:project_id>/', review_project, name='review_project'),
]