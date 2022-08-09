from django.urls import path
from .views import addDocument, deleteDocument, verifyDocument, viewDocument

urlpatterns = [
    path('', viewDocument.as_view(), name='viewDocuments'),
    path('addDocument/', addDocument.as_view(), name='addDocument'),
    path('verifyDocument/<int:pk>',
         verifyDocument.as_view(), name='verifyDocument'),
    path('deleteDocument/<int:pk>',
         deleteDocument.as_view(), name='deleteDocument'),
]
