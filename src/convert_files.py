def generate_summary(text):
    sentences = text.split(". ")
    # Nur die ersten 3 Sätze
    first_three = ". ".join(sentences[:3])
    return first_three + "."
