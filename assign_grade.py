def assign_grade(score):
    """
    Function to calculate student's grade based on the score.
    :param score: A student's score
    """
    if score >= 90:
        grade = 'A'
    elif score >= 80:
        grade = 'B'
    elif score >= 70:
        grade = 'C'
    elif score >= 60:
        grade = 'D'
    else:
        grade = 'F'
    return grade
