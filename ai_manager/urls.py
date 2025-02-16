from django.urls import path
from . import views

# NOTE: the API Urls
urlpatterns = [
    path('', views.ai_model_list, name='ai_model_list'),
    path('create/', views.ai_model_create, name='ai_model_create'),
    path('<int:pk>/edit/', views.ai_model_update, name='ai_model_update'),
    path('<int:pk>/delete/', views.ai_model_delete, name='ai_model_delete'),
]
