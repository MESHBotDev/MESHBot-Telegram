import mesh
from functools import lru_cache


@lru_cache(None)
def get_answers(link: str):
    try:
#         result_answers = []
        result_answers = None
        for all_answers in range(25):
            answers = mesh.get_answers(link)
            result_answers = [answer for answer in answers if answer not in result_answers]
#             for answer in answers:
#                 if answer not in result_answers:
#                     result_answers.append(answer)
        return result_answers
    except:
        return '⚠️Хм странно, но я ничего не нашел. Проверь правильность ссылки или нажми 👉/help👈'
