from django.urls import path
from .views import query_set, query_set_serialized, query_detail


urlpatterns = [
    path('', query_set),
    path('drf/', query_set_serialized),
    path('<int:pk>/', query_detail),
]