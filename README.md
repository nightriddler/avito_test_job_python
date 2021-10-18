# Тестовое задание по Python для Авито

## Задача
Необходимо реализовать Python-библиотеку, которая осуществляет получение квадратной матрицы (NxN) с удалённого сервера и возвращает её пользователю в виде `List[int]`. Этот список должен содержать результат обхода полученной матрицы по спирали: против часовой стрелки, начиная с левого верхнего угла (см. test case ниже).

Пример исходной матрицы:

```
+-----+-----+-----+-----+
|  10 |  20 |  30 |  40 |
+-----+-----+-----+-----+
|  50 |  60 |  70 |  80 |
+-----+-----+-----+-----+
|  90 | 100 | 110 | 120 |
+-----+-----+-----+-----+
| 130 | 140 | 150 | 160 |
+-----+-----+-----+-----+
```

Матрица гарантированно содержит целые неотрицательные числа. Форматирование границ иными символами не предполагается.

## Требования к выполнению и оформлению
- Библиотека содержит функцию со следующим интерфейсом:

```python
async def get_matrix(url: str) -> List[int]:
...
```
- Функция единственным аргументом получает URL для загрузки матрицы с сервера по протоколу HTTP(S).

- Функция возвращает список, содержащий результат обхода полученной матрицы по спирали: против часовой стрелки, начиная с левого верхнего угла.

- Взаимодействие с сервером должно быть реализовано асинхронно - посредством aiohttp, httpx или другого компонента на asyncio.

- В дальнейшем размерность матрицы может быть изменена с сохранением форматирования. Библиотека должна сохранить свою работоспособность на квадратных матрицах другой размерности.

## Проверка решения

- Для проверки решения используются следующие тесты: 

```python
SOURCE_URL = 'https://raw.githubusercontent.com/avito-tech/python-trainee-assignment/main/matrix.txt'

TRAVERSAL = [
    10, 50, 90, 130,
    140, 150, 160, 120,
    80, 40, 30, 20,
    60, 100, 110, 70
]

...

assert loop.run_until_complete(get_matrix(SOURCE_URL)) == TRAVERSAL
    assert get_spiral([
        [10, 20],
        [50, 60]
        ]) == [10, 50, 60, 20]
    assert get_spiral([[10]]) == [10]
    assert get_spiral([[]]) == []
```

## Связаться с автором
>[LinkedIn](http://linkedin.com/in/aizi)

>[Telegram](https://t.me/nightriddler)

>[Портфолио](https://github.com/nightriddler)
