from django.urls import path
from . import views

urlpatterns = [
    path('analyze/<int:claim_id>/', views.analyze_claim, name='analyze_claim'),
]
