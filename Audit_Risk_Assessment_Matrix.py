# Audit Risk Assessment Matrix
# Automatically categorizes audit risks
# based on likelihood and impact scores

def assess_risk(risk_name, likelihood, impact):
    """
    Risk scoring:
    - Likelihood: 1-5 (1=rare, 5=almost certain)
    - Impact: 1-5 (1=negligible, 5=critical)
    """
    risk_score = likelihood * impact
    
    if risk_score >= 15:
        risk_level = "HIGH"
    elif risk_score >= 8:
        risk_level = "MEDIUM"
    else:
        risk_level = "LOW"
    
    return {
        "Risk": risk_name,
        "Likelihood": likelihood,
        "Impact": impact,
        "Score": risk_score,
        "Risk Level": risk_level
    }

# Example audit risks
risks = [
    assess_risk("Unauthorized Access", 4, 5),
    assess_risk("Data Entry Errors", 3, 3),
    assess_risk("System Downtime", 2, 4),
    assess_risk("Fraud Risk", 2, 5),
    assess_risk("Compliance Breach", 3, 4)
]

# Print Risk Assessment Report
print("=" * 50)
print("INTERNAL AUDIT RISK ASSESSMENT REPORT")
print("=" * 50)
for risk in risks:
    print(f"\nRisk: {risk['Risk']}")
    print(f"Score: {risk['Score']} — {risk['Risk Level']} RISK")