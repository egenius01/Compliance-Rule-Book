from . import views
# from .views import  RuleDetailView, RulebookDetailView #add_rule_view
from django.urls import path, include


urlpatterns = [
    path('', views.rule_list, name='rule_list'),
    path('alerts/',views.alert,name='alert'),
    path('<int:pk>/', views.rule_detail, name='rule_detail'),
    path('upload/', views.upload, name='upload'),
    path('upload_list/', views.upload_list, name='upload_list'),
    path('rulebooks/', views.rulebook,name='rulebook'),
    path('rulebooks/<int:pk>/', views.rulebook_detail, name='rulebook_detail'),
]


