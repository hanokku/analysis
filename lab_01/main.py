import string
import random
import time
import matplotlib.pyplot as plt


def get_random_string(string_len):
    letters = string.ascii_lowercase
    return ''.join(random.choice(letters) for i in range(string_len))


def levenshtein_matrix(string_1, string_2):
    len_i = len(string_1) + 1
    len_j = len(string_2) + 1
    matrix = [[i + j for j in range(len_j)] for i in range(len_i)]
    
    for i in range(1, len_i):
        for j in range(1, len_j):
            penalty = 0 if (string_1[i - 1] == string_2[j - 1]) else 1
            matrix[i][j] = min(matrix[i - 1][j] + 1,
                               matrix[i][j - 1] + 1,
                               matrix[i - 1][j - 1] + penalty)
    return(matrix[-1][-1])


def damerau_levenshtein_matrix(string_1, string_2):
    len_i = len(string_1) + 1
    len_j = len(string_2) + 1
    matrix = [[i + j for j in range(len_j)] for i in range(len_i)]
    
    for i in range(1, len_i):
        for j in range(1, len_j):
            penalty = 0 if (string_1[i - 1] == string_2[j - 1]) else 1
            matrix[i][j] = min(matrix[i - 1][j] + 1,
                               matrix[i][j - 1] + 1,
                               matrix[i - 1][j - 1] + penalty)
            if (i > 1 and j > 1) and string_1[i-1] == string_2[j-2] and string_1[i-2] == string_2[j-1]:
                matrix[i][j] = min(matrix[i][j], matrix[i-2][j-2] + 1)
    return(matrix[-1][-1])


def damerau_levenshtein_recursion(string_1, string_2):
    if string_1 ==  '' or string_2 == '':
        return abs(len(string_1) - len(string_2))
    penalty = 0 if (string_1[-1] == string_2[-1]) else 1
    res = min(damerau_levenshtein_recursion(string_1, string_2[:-1]) + 1,
              damerau_levenshtein_recursion(string_1[:-1], string_2) + 1,
              damerau_levenshtein_recursion(string_1[:-1], string_2[:-1]) + penalty)
    if (len(string_1) >= 2 and len(string_2) >= 2 and string_1[-1] == string_2[-2] and string_1[-2] == string_2[-1]):
        res = min(res, damerau_levenshtein_recursion(string_1[:-2], string_2[:-2]) + 1)
    return res


def time_check_matrix(function, string_len):
    iters = 100
    t = 0
    tb = time.process_time()
    for i in range(iters):
        string_1 = get_random_string(string_len)
        string_2 = get_random_string(string_len)
        function(string_1, string_2)
    te = time.process_time()
    t += (te - tb)
    return (t) / iters


def time_check_recursion(function, string_len):
    iters = 100
    t = 0    
    tb = time.process_time()
    for i in range(iters):
        string_1 = get_random_string(string_len)
        string_2 = get_random_string(string_len)
        function(string_1, string_2)
    te = time.process_time()
    t += (te - tb)
    return (t) / iters


def main():
    flag = True
    time_recursion = []
    time_matrix_lev = []
    time_matrix_dam_lev = []

    while(flag):
        choice = input('''
1. Расстояние Левенштейна (матрично)\n\
2. Расстояние Дамерау-Левенштейна (матрично)\n\
3. Расстояние Дамерау-Левенштейна (рекурсивно)\n\
4. Замер времени\n
Ваш ответ: ''')
        if (choice == "1"):
            string_1 = input("Введите первую строку: ")
            string_2 = input("Введите вторую строку: ")
            res = levenshtein_matrix(string_1, string_2)
            print("Расстояние Левенштейна (матрично):", res)
        elif (choice == "2"):
            string_1 = input("Введите первую строку: ")
            string_2 = input("Введите вторую строку: ")
            res = damerau_levenshtein_matrix(string_1, string_2)
            print("Расстояние Дамерау-Левенштейна (матрично):", res)
        elif (choice == "3"):
            string_1 = input("Введите первую строку: ")
            string_2 = input("Введите вторую строку: ")
            res = damerau_levenshtein_recursion(string_1, string_2)
            print("Расстояние Дамерау-Левенштейна (рекурсивно):", res)
        elif (choice == "4"):
            for i in range(1, 11):
                print("\nДлина строки: ", i)
                time_res = time_check_recursion(damerau_levenshtein_recursion, i)
                print("Дамерау-Левенштейн (рекурсивно): ", "%.6f" %(time_res))
                #time_recursion.append(round(time_res, 5))
            for i in range(100, 1100, 100):
                print("\nДлина строки: ", i)
                time_res = time_check_matrix(levenshtein_matrix, i)
                print("Левенштейн (матрично): ", "%.6f" %(time_res))
                #time_matrix_lev.append(round(time_res, 5))
                time_res = time_check_matrix(damerau_levenshtein_matrix, i)
                print("Дамерау-Левенштейн (матрично): ", "%.6f" %(time_res))
                #time_matrix_dam_lev.append(round(time_res, 5))
            #print(time_recursion)
            #print(time_matrix_lev)
            #print(time_matrix_dam_lev)
            
            '''a = [i for i in range(1, 11)]
            b = [i for i in range(0, 1200, 200)]
            plt.plot(a, time_recursion, '-g', label = "Алгоритм Дамерау -Левенштейна (рекурсивно)")
            plt.legend(loc = 'upper left')
            plt.grid()
            plt.xlabel('длина строки, символы')
            plt.ylabel('время')
            plt.show()'''
        else:
            flag = False


if __name__ == "__main__":
    main()
