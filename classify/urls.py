from django.urls import path
from . import views

urlpatterns = [
    path('<str:file_path>', views.classify_req, name='request'),
]