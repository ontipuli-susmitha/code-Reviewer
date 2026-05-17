def calculate_score(style, security, complexity):
    score = 100

    if style.strip():
        score -= 20

    if "Issue" in security:
        score -= 30

    if "F" in complexity or "E" in complexity:
        score -= 25

    return max(score, 0)
