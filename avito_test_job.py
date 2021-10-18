import aiohttp
import asyncio
from typing import List


SOURCE_URL = ('https://raw.githubusercontent.com/avito-tech/'
              'python-trainee-assignment/main/matrix.txt')
TRAVERSAL = [
    10, 50, 90, 130,
    140, 150, 160, 120,
    80, 40, 30, 20,
    60, 100, 110, 70
]


def get_spiral(matrix: List[List[int]]) -> List[int]:
    '''
    По двумерному массиву возвращает список
    содержащий результат обхода матрицы по спирали
    (против часовой стрелки, начиная с левого верхнего угла).
    Пример:
    [
        [10, 20, 30, 40],
        [50, 60, 70 ,80],
        [90, 100, 110, 120],
        [130, 140, 150, 160]
    ] ->
    [10, 50, 90, 130, 140, 150, 160, 120, 80, 40, 30, 20,60, 100, 110, 70]
    '''
    if len(matrix) == 0:
        return matrix
    if len(matrix) == 1:
        return matrix[0]
    first_side = [row[0] for row in matrix]
    second_side = matrix[-1][1:-1]
    third_side = [row[-1] for row in matrix[::-1]]
    fourth_side = matrix[0][1:-1]
    fourth_side.reverse()
    first_spiral = first_side + second_side + third_side + fourth_side
    return first_spiral + get_spiral([row[1:-1] for row in matrix[1:-1]])


async def aiohttp_get_text(url: str):
    '''Получаем текст с URL.'''
    async with aiohttp.ClientSession() as session:
        async with session.get(url) as response:
            return await response.text()


async def get_matrix(url: str) -> List[int]:
    '''
    По URL приводим матрицу к формату двумерного массива.
    Пример:
    +-----+-----+-----+-----+
    |  10 |  20 |  30 |  40 |
    +-----+-----+-----+-----+
    |  50 |  60 |  70 |  80 |
    +-----+-----+-----+-----+
    |  90 | 100 | 110 | 120 |
    +-----+-----+-----+-----+
    | 130 | 140 | 150 | 160 |
    +-----+-----+-----+-----+
    ==
    [[10,20,30,40],[50,60,70,80],[90,100,110,120],[130,140,150,160]]
    '''
    text = await aiohttp_get_text(url)
    clear_text = text.replace(
        '\n', '').replace(
            '+', '').replace('-', '').replace(' ', '').replace('||', '|')
    massive = [
        int(i) for i in clear_text[1:len(clear_text)-1].split('|')]
    numbers_in_massive = int(len(massive)**(0.5))
    return get_spiral(
        [massive[
            (i*numbers_in_massive):(
                (i+1)*numbers_in_massive)] for i in range(numbers_in_massive)])


if __name__ == '__main__':
    loop = asyncio.get_event_loop()
    assert loop.run_until_complete(get_matrix(SOURCE_URL)) == TRAVERSAL
    assert get_spiral([
        [10, 20],
        [50, 60]
        ]) == [10, 50, 60, 20]
    assert get_spiral([[10]]) == [10]
    assert get_spiral([[]]) == []
    print('Test done!')
