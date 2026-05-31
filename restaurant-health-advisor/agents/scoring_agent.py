def recommendation(score):
    if score <= 20:
        return 'Can Have Without Any Risk'
    elif score <= 40:
        return 'Low Risk'
    elif score <= 60:
        return 'Moderate Risk'
    elif score <= 80:
        return 'High Risk'
    return 'Very High Risk'
