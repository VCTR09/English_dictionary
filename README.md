<a id="anchor></a>
# Английский тематический словарь / справочник

* Программа принимает слово и выдает его определение на Английском языке(определений может быть несколько).

* В случае если слово введено с ошибкой, программа предложит ближайшее схожее слово: "Did you mean ____ instead? Enter Y if yes, or N if no:". Примерно, как Google поиск.

* В случае если введенное слово не сущесвтвует, будет выведено сообщение: "The word doesn't exist. Please double check it."

* Слова можно вводить как в ВЕРХНЕМ, так и в нижнем регистре, а так же в СмеШАнноМ реГИстрЕ.

![IMG_1889](https://user-images.githubusercontent.com/97599612/167587773-92bdeaec-e037-4da9-b05f-18cd22ecfe79.JPG)

## Создание:

В качестве хранилища слов и определений используется _JSON_ файл (_data.json_), который можно скачать в Интернете.

Загрузим _data.json_ в _Phyton_ в качестве словаря для лекого доступа к ключам и значениям.

> import json

** Чтобы загрузить _JSON_ в _Python_ словарь, имортируем стандартную библиотеку _json_.

> data = json.load(open("data.json"))  

** Сохраняем файл в переменной с помощью метода _load_. Данный метод в качестве аргумента принимает _file-like object_. Чтобы создать _file-like object_, используем метод _open_.


* Создадим функцию, которая принимает ключ и возвращает значение независимо от регистра.
```
def translate(word):
    word = word.lower()
    if word in data:
        return data[word]
    else:
        return "The word doesn't exitst. Please double check it."

word = input("Enter word: ")
print(translate(word))
```

* Вычисление сходства между словами.

> import difflib

** Стандартная библиотека _Python_ для сравнения схожести текста.

> from difflib import get_close_matches

** Метод вернет наиболее похожее слово из ключей словаря _data_.


* Доработка функции
```
elif len(get_close_matches(word, data.keys())) > 0:
    return "Did you mean %s instead?" % get_close_matches(word, data.keys())[0]
```

** Метод _get_close_match()_ создает список. Если этот список пустой, значит длина списка равна нулю. Если в списке есть элементы, длина будет больше нуля. В данном условии мы проверяем, есть ли элементы в этом списке. Если в списке есть элементы, это означает, что в словаре _(data)_ были найдены совпадения для слова.


* Получение подтверждения пользователя
```
    elif len(get_close_matches(word, data.keys())) > 0:
        yn = input("Did you mean %s instead? Enter Y if yes, or N if no: " % get_close_matches(word, data.keys())[0])
        if yn == "Y":
            return data[get_close_matches(word, data.keys())[0]]
        elif yn == "N":
            return "The word doesn't exist. Please double check it."
        else:
            return "We didn't understand your entry."
```

* Убедимся, что программа возвращает определения слов, начинающихся с заглавной буквы (_Paris, Italy_), а также акронимов (_USA, NASA_)
```
    elif word.title() in data:
        return data[word.title()]

    elif word.upper() in data:
        return data[word.upper()]
```

* Оптимизируем выходные данные

На текущий момент определения выводятся в виде списка строк. Мы хотим, чтобы каждое определение выводилось с новой строки. Так же уберем кавычки и квадратные скобки.
```
word = input("Enter word: ")
output = translate(word)

if type(output) == list:
    for item in output:
        print(item)
else:
    print(output)
```

* Добавим нумерацию выводимых определений. Применим бесконечный цикл с возможностью выхода.
```
while True:
    word = input("Enter a word: ")
    output = translate(word)
    if word == "/end":
        break
    else:
        if type(output) == list:
            i = 1
            for item in output:
                print("%s. %s" % (i,item)) 
                i+=1
        else:
            print(output)
```

[Вверх](#anchor)
