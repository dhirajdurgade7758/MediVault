from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from .forms import InsuranceClaimForm
from .models import InsuranceClaim

@login_required
def submit_claim(request):
    if request.method == 'POST':
        form = InsuranceClaimForm(request.POST, request.FILES)
        if form.is_valid():
            claim = form.save(commit=False)
            claim.claimant = request.user
            claim.save()
            return redirect('my_claims')
    else:
        form = InsuranceClaimForm()
    return render(request, 'claims/submit_claim.html', {'form': form})

@login_required
def my_claims(request):
    claims = InsuranceClaim.objects.filter(claimant=request.user)
    return render(request, 'claims/my_claims.html', {'claims': claims})

@login_required
def claim_detail(request, claim_id):
    claim = InsuranceClaim.objects.get(id=claim_id)
    return render(request, 'claims/claim_detail.html', {'claim': claim})
