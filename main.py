from lingua import Language, LanguageDetectorBuilder  # pip install lingua-language-detector
import enchant  # pip install pyenchant


def validate_language(code_validate):  # Определяет смешан ли тут англ и русс. Если смешан, возвращает ошибку, если нет, то название языка
    validate_list = []
    languages = [Language.ENGLISH, Language.RUSSIAN]
    detector = LanguageDetectorBuilder.from_languages(*languages).build()
    for result in detector.detect_multiple_languages_of(code_validate):
        validate_list.append(str(f"{result.language.name}: '{code_validate[result.start_index:result.end_index]}'")[:7])
    if len(validate_list) != 1:
        return ['Ошибка']
    else:
        return validate_list


def validate_language_lvl_2(lvl1_result):     # Второй уровень валидации текста. Вызывается только если длинна текста менее 20 символов. В противном случае первый уровень и так справится
    for i in lvl1_result.lower():
        if not i.isalpha():
            continue
        if i == ' ':
            continue
        if lang_name == ['ENGLISH'] and i not in abs_eng_case:
            return True
        if lang_name == ['RUSSIAN'] and i not in abs_rus_case:
            return True
    return False


# Модуль проверки правописания текста. Что бы это работа с Русским текстом необходимо скачать
# от сюда https://github.com/LibreOffice/dictionaries/tree/master/ru_RU ,файлы:  ru_RU.aff и ru_RU.dic
# и поместить по пути PycharmProjects\pythonProject\venv\Lib\site-packages\enchant\data\mingw64\share\enchant\hunspell
def is_text_or_not(text):
    if lang_name == ['ENGLISH']:
        test = enchant.Dict("en_US")
        return test.check(text)
    else:
        test = enchant.Dict("ru_RU")
        return test.check(text)


def isspace(answer):  # Функция проверяющая, что пользователь не ввел пустую строку или только пробелы
    while True:
        if answer.isspace():
            answer = input('Ваша строка содержит только пробелы. Повторите ввод: ')
            print()
        elif answer == '':
            answer = input('Вы ничего не написали Повторите ввод: ')
            print()
        else:
            return answer


def plus_or_minus_validate(answer):  # Функция проверяющая, что пользователь ввел + или -
    while True:
        if answer == '+' or answer == '-':
            return answer
        else:
            answer = input('Пожалуйста дайте ответ в формате: "+" или "-" без кавычек: ')
            print()


def numbers(numb):  # Функция проверяющая, что пользователь ввел цифру
    while not numb.isdigit():
        numb = input('Пожалуйста дайте ответ целой цифрой: ')
    numb = int(numb)
    return numb


def plus_or_isdigit_validate(answer):  # Функция проверяющая, что пользователь ввел + или цифру
    while True:
        if answer == '+' or answer == '++' or answer.isdigit():
            return answer
        else:
            answer = input('Пожалуйста дайте ответ в формате: "+" или "цифра" без кавычек и пробелов: ')
            print()


def key_validate(validate_key):  # Модуль валидации ключа сдвига, на случай если пользователь даст ключ превышающий мощность алфавита
    if lang_name == ['ENGLISH'] and int(validate_key) > 25:
        return int(validate_key) % 26
    elif lang_name == ['RUSSIAN'] and int(validate_key) > 33:
        return int(validate_key) % 32
    else:
        return int(validate_key)


def max_str(str):  # Модуль возвращающий первое и второе самое длинное слово из строки, без знаков препинания
    str = str.split()
    str = sorted(str, key=len, reverse=True)
    return str[0], str[1]

def ASCII_validate(ASCII_validate):  # Модуль валидации сдвига алфавита по ASCII
    if lang_name == ['ENGLISH']:
        if ASCII_validate < 97:
            ASCII_validate += 26
            return ASCII_validate
        elif ASCII_validate > 122:
            ASCII_validate -= 26
            return ASCII_validate
        else:
            return ASCII_validate
    if lang_name == ['RUSSIAN']:
        if ASCII_validate < 1072:
            ASCII_validate += 32
            return ASCII_validate
        elif ASCII_validate > 1103:
            ASCII_validate -= 32
            return ASCII_validate
        else:
            return ASCII_validate


def key_len_word(text):   # Модуль возвращающий список, равные длине каждого слова строки, не считая знаков препинания
    final_text = ''
    final_list = []
    for i in text:
        if i.isalpha() or i.isspace():
            final_text += i
    final_text = final_text.split()
    for i in final_text:
        final_list.append(len(i))
    return final_list


def only_abc(text):   # Модуль удаляющий из строки всё кроме букв
    final_text = ''
    for i in text:
        if i.isalpha():
            final_text += i

    return final_text


def encoder_decoder(shift, code_txt):  # Основной модуль шифровки / дешифровки
    result = []  # Список с результатом
    flag = False  # Флаг для проверки заглавная буква или нет
    if hard_or_not == '-':
        for i in code_txt:
            if not i.isalpha():
                result.append(i)
                continue
            elif i == ' ':
                result.append(i)
                continue
            if i.isupper():  # Если буква заглавная - поднимает флаг
                flag = True
            if left_or_right == '+':
                ASCII = ord(i.lower()) + shift  # Сдвиг вправо
            else:
                ASCII = ord(i.lower()) - shift  # Сдвиг влево
            ASCII = ASCII_validate(ASCII)
            if flag:
                result.append(chr(ASCII).upper())
                flag = False
            else:
                result.append(chr(ASCII))
        print(*result, sep='')
    elif hard_or_not == '+':
        for i in code_txt:
            if not i.isalpha():
                result.append(i)
                continue
            elif i == ' ':
                result.append(i)
                continue
            if i.isupper():  # Если буква заглавная - поднимает флаг
                flag = True
            if flag_plus:
                if flag:
                    ASCII = ord(i.lower()) + shift  # Сдвиг вправо
                    ASCII = ASCII_validate(ASCII)
                    result.append(chr(ASCII).upper())
                    flag = False
                else:
                    ASCII = ord(i.lower()) + shift  # Сдвиг вправо
                    ASCII = ASCII_validate(ASCII)
                    result.append(chr(ASCII))
            else:
                if flag:
                    ASCII = ord(i.lower()) - shift  # Сдвиг влево
                    ASCII = ASCII_validate(ASCII)
                    result.append(chr(ASCII).upper())
                    flag = False
                else:
                    ASCII = ord(i.lower()) - shift  # Сдвиг влево
                    ASCII = ASCII_validate(ASCII)
                    result.append(chr(ASCII))
        return result
    else:
        break_flag = False
        not_alpha_count = 0
        shift_len = shift
        shift = shift[0]
        while True:
            if break_flag:
                break_flag = False
                code_txt = code_txt[shift_len[0] + not_alpha_count:]
                shift = shift_len[0]
                del shift_len[0]
                not_alpha_count = 0
                if len_code == len(result):
                    print(*result, sep='')
                    return
            for j in range(len(shift_len)):
                if break_flag:
                    break
                for k in range(shift):
                    if break_flag:
                        break
                    while True:
                        if break_flag:
                            break
                        for t in code_txt:
                            if len_code == len(result):
                                print(*result, sep='')
                                return
                            if t == ' ':
                                result.append(t)
                                not_alpha_count += 1
                                continue
                                if len(shift_len) > 0:  # проверяем, что список не пуст
                                    break_flag = True
                                    break
                            elif not t.isalpha():
                                result.append(t)
                                not_alpha_count += 1
                                continue
                            if t.isupper():  # Если буква заглавная - поднимает флаг
                                flag = True
                            if flag_plus:
                                if flag:
                                    ASCII = ord(t.lower()) + shift  # Сдвиг вправо
                                    ASCII = ASCII_validate(ASCII)
                                    result.append(chr(ASCII).upper())
                                    flag = False
                                else:
                                    ASCII = ord(t.lower()) + shift  # Сдвиг вправо
                                    ASCII = ASCII_validate(ASCII)
                                    result.append(chr(ASCII))
                            else:
                                if flag:
                                    ASCII = ord(t.lower()) - shift  # Сдвиг влево
                                    ASCII = ASCII_validate(ASCII)
                                    result.append(chr(ASCII).upper())
                                    flag = False
                                else:
                                    ASCII = ord(t.lower()) - shift  # Сдвиг влево
                                    ASCII = ASCII_validate(ASCII)
                                    result.append(chr(ASCII))


abs_eng_case = 'abcdefghijklmnopqrstuvwxyz'
abs_rus_case = 'абвгдеёжзийклмнопрстуфхцчшщъыьэюя'
error_count = 0   # Количество неудачных попыток авто-дешифровки. Если счётчик дойдет до 2 - то значит не получилось
shift = 1         # Шаг сдвига
flag_plus = True  # Отвечает за направление сдвига


print('Привет. Моя программа поможет расшифровать шифр Цезаря или наоборот, зашифровать')
print()
hard_or_not = input('''Для начала, тебе стоит знать, что если тебе требуется именно расшифровать текст, и при этом ты не знаешь ключ дешифровки, то я все равно смогу тебе помочь.
Но если твой текст довольно длинный, то лучше введи несколько слов из текста (НЕ МЕНЕЕ ДВУХ!) и ты получишь ключ дешифровки.
Если у тебя именно такой запущенный случай, то дай мне знать введя '+'. Если нет, то просто введи '-' и мы пойдём дальше: ''').strip()
hard_or_not = isspace(hard_or_not)
hard_or_not = plus_or_minus_validate(hard_or_not)

if hard_or_not == '+':
    code = input('Ок. В таком случае, предоставь мне текст который требуется расшифровать: ')
    code = isspace(code)  # Валидированная строка для шифровки или расшифровки
    lang_name = (validate_language(code))
    while lang_name == ['Ошибка']:
        print('Ваша строка содержит текст из разных языков. Это недопустимо. Требуется текст одного языка')
        code = input('Пожалуйста, повторить ввод строки которую требуется зашифровать или расшифровать: ')
        code = isspace(code)
        lang_name = validate_language(code)
    max_code_element_1, max_code_element_2 = max_str(code)  # Первое и второе самое длинное слово в шифре, без знаков препинания
    max_code_element_1 = only_abc(max_code_element_1)
    max_code_element_2 = only_abc(max_code_element_2)
    lang_name = (validate_language(max_code_element_1))  # Определяем язык
    lang_name = (validate_language(max_code_element_2))  # Определяем язык
else:
    code = input('Ок. В таком случае, предоставь мне текст который требуется зашифровать или расшифровать. Текст должен полностью состоять из Русского или Английского алфавита: ')
    code = isspace(code)  # Валидированная строка для шифровки или расшифровки
    code = code.replace('ё', 'е')
    lang_name = (validate_language(code))  # Определяем язык
    len_code = len(code)                   # Длина шифрованной строки

while lang_name == ['Ошибка']:
    print('Ваша строка содержит текст из разных языков. Это недопустимо. Требуется текст одного языка')
    code = input('Пожалуйста, повторить ввод строки которую требуется зашифровать или расшифровать: ')
    code = isspace(code)
    lang_name = validate_language(code)
if len(code) < 20:
    while True:
        lvl2 = validate_language_lvl_2(code)
        if lvl2:
            print('Ваша строка содержит текст из разных языков. Это недопустимо. Требуется текст одного языка')
            code = input('Пожалуйста, повторить ввод строки которую требуется зашифровать или расшифровать: ')
            code = isspace(code)
            lang_name = validate_language(code)
            lvl2 = validate_language_lvl_2(code)
        else:
            break

if hard_or_not == '-':
    key = input('''Отлично. Теперь нужно предоставить ключ дешифровки / шифровки (шаг сдвига).
Если в вашем случае, шагом сдвигая является длинна всего шифра, введи '+'.
Если для каждого слова в шифре, ключом сдвига является, длинна этого слова, введите '++'
В противном случае, задайте значение цифрой: ''')
    key = isspace(key)
    key = plus_or_isdigit_validate(key)  # Валидированный ключ сдвига
    if key == '+':
        key = len(code)
        key = key_validate(key)
    elif key == '++':
        key = key_len_word(code)
        hard_or_not = '++'
    else:
        key = key_validate(key)

    left_or_right = input('''Последний шаг. Осталось указать в какую сторону идет сдвиг. Влево или вправо.
Если вправо: введи "+", если влево: введи "-": ''')
    left_or_right = isspace(left_or_right)
    left_or_right = plus_or_minus_validate(left_or_right)
    if left_or_right == '-':
        flag_plus = False
    encoder_decoder(key, code)
elif hard_or_not == '+':
    ok_count = 0
    while True:
        if error_count == 2:
            print('''Подобрать ключ дешифровки не удалось. Скорей всего Вы ввели текст который полностью или частично состоит, не из Английских слов.'
Если Вы ввели очень длинный текст, то это тоже может не сработать. Введите сначала несколько слов из этого текста и тогда вы получите ключ дешифровки
Также, возможен вариант, что каждое слово в списке было зашифровано отдельным ключом, тогда в авто режиме расшифровать опять же, не получится.''')
            break
        if ok_count == 0:
            pre_ok = encoder_decoder(shift, max_code_element_1)
            pre_ok = ''.join(map(str, pre_ok))
            ok_or_no = is_text_or_not(pre_ok)
        if ok_or_no:
            ok_count = 1
            pre_ok = encoder_decoder(shift, max_code_element_2)
            pre_ok = ''.join(map(str, pre_ok))
            ok_or_no = is_text_or_not(pre_ok)
            if ok_or_no:
                ok_count = 2
            if ok_count == 2:
                print('Выявлен ключ сдвига. Влево или вправо, сами уж разберетесь:', shift)
                print('Дешифрованный текст:')
                final = encoder_decoder(shift, code)
                print(*final, sep='')
                break
        else:
            shift += 1
            if shift > 26:
                error_count += 1
                flag_plus = False
                shift = 1
