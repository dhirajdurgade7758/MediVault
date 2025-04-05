
# # Create your views here.
# from django.shortcuts import render, redirect
# from django.contrib.auth.decorators import login_required
# from .forms import MedicalRecordForm
# from .models import MedicalRecord

# @login_required
# def upload_record(request):
#     if request.method == 'POST':
#         form = MedicalRecordForm(request.POST, request.FILES)
#         if form.is_valid():
#             record = form.save(commit=False)
#             record.patient = request.user
#             record.save()
#             return redirect('view_records')
#     else:
#         form = MedicalRecordForm()
#     return render(request, 'records/upload_record.html', {'form': form})

# @login_required
# def view_records(request):
#     if request.user.role == 'doctor':
#         # Show all patient records (for demo, or later filter by patient)
#         records = MedicalRecord.objects.all()
#     else:
#         # Only show their own
#         records = MedicalRecord.objects.filter(patient=request.user)
#     return render(request, 'records/view_records.html', {'records': records})
from django.shortcuts import render, get_object_or_404
from .models import PatientRecord
from .services import store_record_on_blockchain, get_record_from_blockchain

def store_patient_record(request):
    if request.method == "POST":
        patient_name = request.POST.get("patient_name")
        diagnosis = request.POST.get("diagnosis")
        treatment = request.POST.get("treatment")
        ipfs_hash = request.POST.get("ipfs_hash")  # Store large files on IPFS

        # Store on blockchain
        tx_hash = store_record_on_blockchain(patient_name, diagnosis, treatment, ipfs_hash)

        # Store minimal data in DB
        record = PatientRecord.objects.create(
            patient_name=patient_name,
            diagnosis=diagnosis,
            treatment=treatment,
            blockchain_tx=tx_hash
        )

        return render(request, "records/success.html", {"record": record})

    return render(request, "records/store_record.html")

def view_patient_record(request, record_id):
    record_data = get_record_from_blockchain(record_id)
    return render(request, "records/view_record.html", {"record": record_data})
