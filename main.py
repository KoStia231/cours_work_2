from config import URL
from utils.functions import get_data
from utils.functions import get_random_word
from utils.functions import load_word
from utils.functions import load_player
from utils.functions import len_word



def __main__():
    data = get_data(URL)
    random_word = get_random_word(data)
    word = load_word(random_word)
    user_name = input('Ввведите имя игрока\n')
    player = load_player(user_name)
    print(f'Привет, {player}!',
          f'Составьте {word.count_correct_answer()} слов из слова {word}',
          f'Слова должны быть не короче 3 букв',
          f'Чтобы закончить игру, угадайте все слова или напишите "stop"',
          f'Поехали, ваше первое слово?', sep='\n')
    p = 1
    while p <= word.count_correct_answer():
        user_input = input('Введите слово\n')
        if user_input in ['stop', 'стоп']:
            break
        word.user_response = user_input
        player.user_response = user_input
        if not len_word(user_input):
            print('Слишком короткое слово')
            continue
        if player.is_correct():
            print('Неверно, такое слово уже угаданно')
            continue
        if word.is_correct():
            p += 1
            player.user_word_ap()
            print('Верно вы угадали!')

    print(f'Игра завершена, вы угадали {player.count_user_words_us()} слов!')


if __name__ == "__main__":
    __main__()
