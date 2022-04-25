import mesh


def get_answers(link: str):
    try:
        answers = mesh.get_answers(link)
        temp = answers[0]
        return answers
    except:
        return "'Хм странно, но я ничего не нашел." \
               " Проверьте правильность ссылки и попробуйте ещё раз или нажмите /help'."
