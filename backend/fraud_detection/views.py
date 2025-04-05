from django.shortcuts import render, get_object_or_404
from django.contrib.admin.views.decorators import staff_member_required
from claims.models import InsuranceClaim
from .models import ClaimAnalysis
from .services import analyze_claim_with_ai

@staff_member_required
def analyze_claim(request, claim_id):
    claim = get_object_or_404(InsuranceClaim, id=claim_id)

    score, reason = analyze_claim_with_ai(claim)

    analysis, created = ClaimAnalysis.objects.get_or_create(claim=claim)
    analysis.fraud_score = score
    analysis.ai_feedback = reason
    analysis.save()

    return render(request, 'fraud_detection/analysis_result.html', {
        'claim': claim,
        'analysis': analysis
    })
