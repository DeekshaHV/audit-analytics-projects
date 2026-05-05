# Audit Sample Size Calculator
# Tool for internal auditors to calculate 
# sample sizes for audit testing

def calculate_sample_size(population, confidence_level, error_rate):
    """
    Calculate audit sample size based on:
    - Population size
    - Confidence level
    - Acceptable error rate
    """
    if confidence_level == 95:
        z_score = 1.96
    elif confidence_level == 90:
        z_score = 1.645
    else:
        z_score = 2.576  # 99%
    
    sample_size = (z_score**2 * 0.5 * 0.5) / (error_rate**2)
    
    # Adjust for finite population
    adjusted_sample = sample_size / (1 + (sample_size / population))
    
    return round(adjusted_sample)

# Example usage
population = 1000
confidence = 95
error = 0.05

result = calculate_sample_size(population, confidence, error)
print(f"Population: {population}")
print(f"Confidence Level: {confidence}%")
print(f"Error Rate: {error*100}%")
print(f"Required Sample Size: {result}")