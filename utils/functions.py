from utils.Player import Player
from utils.BasicWord import BasicWord
from random import shuffle
import requests


def get_data(url) -> list[dict]:
    """принмает ссылку на json и отдает список со словарями"""
    data = requests.get(url)
    data.raise_for_status()
    return data.json()


def get_random_word(list_) -> dict:
    """возвращает рандомный элемент списка"""
    shuffle(list_)
    return list_[0]


def load_word(dict_):
    """создает экземпляр класса"""
    return BasicWord(dict_['word'], dict_['subwords'])


def load_player(name):
    """создает экземпляр класса"""
    return Player(name)


def len_word(word) -> bool:
    """проверка длины слова, если меньше 3 букв вернет False"""
    if len(word) < 3:
        return False
    return True
