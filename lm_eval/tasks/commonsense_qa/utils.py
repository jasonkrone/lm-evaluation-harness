
def doc_to_text(doc):
    question = doc["question"]
    choices = doc["choices"]["text"]
    n_choices = len(choices)
    letters = ["a", "b", "c", "d", "e", "f"]
    assert n_choices <= len(letters)
    choices_str = "\n".join([f"({l}) {c}" for c, l in zip(choices, letters)])
    text = f"Q: {question.strip()} Answer Choices: \n{choices_str}\nA:"
    return text
