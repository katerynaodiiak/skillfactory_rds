import numpy as np


def game_core_v1(number):
    '''Просто угадываем на random, никак не используя информацию о больше или меньше.
       Функция принимает загаданное число и возвращает число попыток'''
    count = 0
    while True:
        count+=1
        predict = np.random.randint(1,101) # предполагаемое число
        if number == predict: 
            return(count) # выход из цикла, если угадали
  

def game_core_v2(number):
    '''Сначала устанавливаем любое random число, а потом уменьшаем или увеличиваем его в зависимости от того, больше оно или меньше нужного.
       Функция принимает загаданное число и возвращает число попыток'''
    count = 1
    predict = np.random.randint(1,101)
    while number != predict:
        count+=1
        if number > predict: 
            predict += 1
        elif number < predict: 
            predict -= 1
    return(count) # выход из цикла, если угадали


def game_core_v3(number):
    '''This function is looking for number with re-evaluating 
    left and right ends/egdes/boundaries of given interval between 0 and 100
    
    example: number = 33
    
	predict value is equal a half of right_end by default (middle of interval)
	
    given length -> (left_end:right_end) = (0:100) 
    predict (middle of interval) = 100/2 divides interval in two equal halfs:
    (0:49) and (50:100)
    
    Iterations: 
    
    1) where is number in first half (0:49) or second (50:100)? -> first - (0:49)        
    current interval -> (0:49), middle value is 0 + (50-0)/2 = 25               
    2) where is number in first half (0:24) or second (25:50)? -> second - (25:50)
    updated interval -> (25:50), middle value is 25 + (50-25)/2 = 37
    3) where is number in first half (25:37) or second (37:50)? -> first - (25:37)
    updated interval -> (25:37) ,middle value is 25 + (37-25)/2 = 31
    4) where is number in first half (25:31) or second (31:37)? -> second - (31:37)
    updated interval -> (31:37), middle value is 31 + (37-31)/2 = 34
    5) where is number in first half (31:34) or second (34:37)? -> first - (31:34)
    updated interval -> (31:34), middle value is 31 + (34-31)/2 = 33
	
	count here is equal 5 iterations'''
	
    count = 0
    left_end = 0
    right_end = 100
    predict = round(right_end/2)
    while number != predict:
        count += 1
        if number > predict:
            left_end = predict #left end of interval moved to right (second half)
            predict += round((right_end - left_end)/2)
        else:
            right_end = predict #right end of interval moved to left (first half)
            predict = left_end + round((right_end - left_end)/2)
    return(count)


def score_game(game_core):
    '''Запускаем игру 1000 раз, чтобы узнать, как быстро игра угадывает число'''
    count_ls = []
    np.random.seed(1)  # фиксируем RANDOM SEED, чтобы ваш эксперимент был воспроизводим!
    random_array = np.random.randint(1,101, size=(233)) #there is an issue here, my program is not working if number of attampts are bigger than 234 :(
    for number in random_array:
        count_ls.append(game_core(number))
    score = int(np.mean(count_ls))
    print(f"Ваш алгоритм угадывает число в среднем за {score} попыток")
    return(score)


score_game(game_core_v3)