# from django.db import models
# from users.models import CustomUser

# # Create your models here.
# from django.db import models
# from users.models import CustomUser

# class MedicalRecord(models.Model):
#     patient = models.ForeignKey(CustomUser, on_delete=models.CASCADE, related_name='records')
#     file = models.FileField(upload_to='medical_records/')
#     description = models.TextField(blank=True, null=True)
#     uploaded_at = models.DateTimeField(auto_now_add=True)

#     def __str__(self):
#         return f"{self.patient.username} - {self.file.name}"
from django.db import models

class PatientRecord(models.Model):
    patient_name = models.CharField(max_length=255)
    diagnosis = models.TextField()
    treatment = models.TextField()
    blockchain_tx = models.CharField(max_length=100, blank=True, null=True)  # Store blockchain transaction hash
    timestamp = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Record {self.id} - {self.patient_name}"
