from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name="home"),
    path('about/', views.about, name="about"),
    path('entity/<int:id>/view', views.entity_view, name="entity_view"),
    path('entity/add', views.entity_add, name="entity_add"),
    path('entity/<int:id>/update', views.entity_update, name="entity_update"),
    path('entity/<int:id>/delete', views.entity_delete, name="entity_delete"),
]