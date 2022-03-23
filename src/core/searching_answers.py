import mesh


def get_answers(link: str):
    try:
        answers = mesh.get_answers(link)
        temp = answers[0]
        return answers
    except:
        return "Я не могу найти ответы на этот тест. Проверьте правильность ссылки и попробуйте ещё раз."
