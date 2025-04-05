from openai import OpenAI
from django.conf import settings

client = OpenAI(api_key=settings.OPENAI_API_KEY)

def analyze_claim_with_ai(claim):
    prompt = f"""
You are an AI model trained to detect fraud in insurance claims.
Claim Details:
- Hospital Name: {claim.hospital_name}
- Treatment Details: {claim.treatment_details}
- Claimant Username: {claim.claimant.username}

Based on this information, analyze and rate the likelihood of this claim being fraudulent on a scale from 0 to 100.
Also give a brief explanation.
Return the result in the format:
Score: <score>
Reason: <your explanation>
"""

    response = client.chat.completions.create(
        model="gpt-3.5-turbo",
        messages=[
            {"role": "user", "content": prompt}
        ],
        max_tokens=300
    )

    content = response.choices[0].message.content
    try:
        score_line, reason_line = content.strip().split("\n", 1)
        score = float(score_line.split(":", 1)[1].strip())
        reason = reason_line.split(":", 1)[1].strip()
    except Exception:
        score = None
        reason = "AI response formatting issue."

    return score, reason
