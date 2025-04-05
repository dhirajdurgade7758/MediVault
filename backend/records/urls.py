# from django.urls import path
# from . import views

# urlpatterns = [
#     path('upload/', views.upload_record, name='upload_record'),
#     path('view/', views.view_records, name='view_records'),
# ]
from django.urls import path
from . import views

urlpatterns = [
    path('store/', views.store_patient_record, name='store_patient_record'),
    path('view/<int:record_id>/', views.view_patient_record, name='view_patient_record'),
]
