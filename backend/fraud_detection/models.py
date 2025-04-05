from django.db import models
from claims.models import InsuranceClaim

class ClaimAnalysis(models.Model):
    claim = models.OneToOneField(InsuranceClaim, on_delete=models.CASCADE, related_name='analysis')
    fraud_score = models.FloatField(null=True, blank=True)  # 0 to 100
    ai_feedback = models.TextField(blank=True)
    reviewed_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"Analysis for Claim #{self.claim.id}"
