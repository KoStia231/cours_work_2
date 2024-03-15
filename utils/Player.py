class Player:

    def __init__(self, user_name):
        self.user_name = user_name
        self.user_words_us = []
        self.user_response = None

    def __repr__(self):
        return f'{self.user_name}'

    def count_user_words_us(self) -> int:
        """получение количества использованных слов"""
        return len(self.user_words_us)

    def user_word_ap(self):
        """добавляет слово в список использованных"""
        self.user_words_us.append(self.user_response)

    def is_correct(self) -> bool:
        """ Возвращает True, если такое слово уже было иначе False."""
        if self.user_response in self.user_words_us:
            return True
        return False
