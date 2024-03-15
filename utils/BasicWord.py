class BasicWord:

    def __init__(self, question, correct_answer):
        self.question = question
        self.correct_answer = correct_answer
        self.user_response = None

    def __repr__(self):
        return f'{self.question}'

    def is_correct(self) -> bool:
        """ Возвращает True, если ответ пользователя совпадает
            с верным ответов иначе False.
        """
        if self.user_response in self.correct_answer:
            return True
        return False

    def count_correct_answer(self) -> int:
        """Вернет количество возможных верных ответов"""
        return len(self.correct_answer)
