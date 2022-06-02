import mesh
from functools import cache


@cache
def get_answers(link: str):
    try:
        result_answers = []
        for all_answers in range(20):
            answers = mesh.get_answers(link)
            [result_answers.append(answer) for answer in answers if answer not in result_answers]
#             for answer in answers:
#                 if answer not in result_answers:
#                     result_answers.append(answer)
        print(result_answers)
        return result_answers
    except:
        return '⚠️Хм странно, но я ничего не нашел. Проверь правильность ссылки или нажми 👉/help👈'
