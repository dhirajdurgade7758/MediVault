from django.db import models
from users.models import CustomUser

class InsuranceClaim(models.Model):
    CLAIM_STATUS = (
        ('pending', 'Pending'),
        ('approved', 'Approved'),
        ('rejected', 'Rejected'),
        ('under_review', 'Under Review'),
    )

    claimant = models.ForeignKey(CustomUser, on_delete=models.CASCADE, null=True, blank=True)
    hospital_name = models.CharField(max_length=255, null=True, blank=True)
    treatment_details = models.TextField(null=True, blank=True)
    document = models.FileField(upload_to='claim_docs/', null=True, blank=True)
    status = models.CharField(max_length=20, choices=CLAIM_STATUS, default='pending', null=True, blank=True)
    submitted_at = models.DateTimeField(auto_now_add=True, null=True, blank=True)

    def __str__(self):
        return f"Claim #{self.id} by {self.claimant.username}"
