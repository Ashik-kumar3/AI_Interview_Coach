def generate_feedback(
        eye_score,
        head_score,
        posture_score,
        communication_score
):

    feedback = []

    # Eye Contact

    if eye_score >= 80:
        feedback.append(
            "Excellent eye contact maintained throughout the interview."
        )

    elif eye_score >= 60:
        feedback.append(
            "Good eye contact, but try to focus more consistently on the camera."
        )

    else:
        feedback.append(
            "Improve eye contact to appear more confident and engaged."
        )

    # Head Stability

    if head_score >= 80:
        feedback.append(
            "Head movements were well controlled."
        )

    elif head_score >= 50:
        feedback.append(
            "Moderate head movement detected. Try to keep your face centered."
        )

    else:
        feedback.append(
            "Frequent head movements detected. Maintain a more stable posture."
        )

    # Posture

    if posture_score >= 80:
        feedback.append(
            "Professional posture maintained during the interview."
        )

    elif posture_score >= 60:
        feedback.append(
            "Posture was acceptable, but can be improved."
        )

    else:
        feedback.append(
            "Try sitting upright with aligned shoulders."
        )

    # Communication

    if communication_score >= 80:
        feedback.append(
            "Strong communication skills with minimal filler words."
        )

    elif communication_score >= 60:
        feedback.append(
            "Communication was good. Work on improving speaking pace and fluency."
        )

    else:
        feedback.append(
            "Communication needs improvement. Practice speaking clearly and confidently."
        )

    return feedback