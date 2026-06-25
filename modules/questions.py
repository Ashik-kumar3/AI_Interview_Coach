def load_questions(filepath):

    with open(filepath, "r", encoding="utf-8") as file:
        content = file.read()

    questions = [
        line.strip()
        for line in content.splitlines()
        if line.strip()
    ]

    return questions