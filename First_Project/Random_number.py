import numpy as np

def predict_number(number: int = 1) -> int:
    """Угадывает число от 0 до 100

    Args:
        number (int): заданное число Defaults to 1

    Returns:
        int: Число попыток
    """
    count = 0
    beginning = 1 # начальная граница диапазона поиска
    end = 101     # конечная граница диапазона поиска
    intermediate_number =  np.random.randint(beginning, end) # первая поытка
    
    while True:
        count += 1
        if intermediate_number > number:
            end = intermediate_number
            random_number =  np.random.randint(beginning, end) # предполагаемое число в новой конечной границе при условии, что искомое число меньше предпалагаемого
        elif intermediate_number < number:
            beginning = intermediate_number
            random_number =  np.random.randint(beginning, end) # предполагаемое число новой начальной границе при условии, что искомое число больше предпалагаемого
        else:
            return count                                       # при условии равенства искомого с предпалагаемым функция возвращает количество попыток
        intermediate_number = random_number
    

def average_value_attempt() -> int:
    """ За какое количество попыток в среднем из 1000 подходов угадывает наш алгоритм
        
        Returns:
        int: среднее количество попыток
    
    """      
    count_ls = [] # список для сохранения количества попыток
    np.random.seed(1) # фиксируем сид для воспроизводимости
    random_array = np.random.randint(1, 101, size=(1000)) # загадали список чисел

    for number in random_array:
        count_ls.append(predict_number(number))

    score = int(np.mean(count_ls)) # находим среднее количество попыток

    print(f'Ваш алгоритм угадывает число в среднем за: {score} попыток')
    return(score)

average_value_attempt()            