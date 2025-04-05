from django.urls import path
from . import views

urlpatterns = [
    path('submit/', views.submit_claim, name='submit_claim'),
    path('my/', views.my_claims, name='my_claims'),
    path('<int:claim_id>/', views.claim_detail, name='claim_detail'),
]
