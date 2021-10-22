from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('<int:problem_id>/', views.detail, name='detail'),
    path('<int:problem_id>/<int:form_id>/', views.finalpage, name='finalpage'),
]   