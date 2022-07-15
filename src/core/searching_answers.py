import mesh
from functools import cache


@cache
def get_answers(link: str) -> list:
    try:
        result_answers = []
        [result_answers.append(answer) for _ in range(20) for answer in mesh.get_answers(link) if answer not in result_answers]
        return result_answers
    except:
        return '⚠️Хм странно, но я ничего не нашел. Проверь правильность ссылки или нажми 👉/help👈'
