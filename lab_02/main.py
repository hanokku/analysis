def multiplication_classic(first_matr, second_matr):
    first_rows, first_cols = len(first_matr), len(first_matr[0])
    second_rows, second_cols = len(second_matr), len(second_matr[0])

    result_matr = [[0 for i in range(second_cols)] for j in range(first_rows)]

    for i in range(first_rows):
        for j in range(first_cols):
            for k in range(second_rows):
                result_matr[i][k] += first_matr[i][j] * second_matr[j][k]

    return result_matr


def multiplication_winograd(first_matr, second_matr):
    first_rows, first_cols = len(first_matr), len(first_matr[0])
    second_rows, second_cols = len(second_matr), len(second_matr[0])

    rows_factors = [0 for i in range(first_rows)]
    cols_factors = [0 for i in range(first_cols)]

    for i in range(first_rows):
        for j in range(second_rows // 2):
            rows_factors[i] = rows_factors[i] + first_matr[i][2 * j] * first_matr[i][2 * j + 1]

    for i in range(second_cols):
        for j in range(second_rows // 2):
            cols_factors[i] = cols_factors[i] + second_matr[2 * j][i] * second_matr[2 * j + 1][i]

    result_matr = [[0 for i in range(second_cols)] for j in range(first_rows)]

    for i in range(first_rows):
        for j in range(second_cols):
            result_matr[i][j] = -rows_factors[i] - cols_factors[j]
            for k in range(second_rows // 2):
                result_matr[i][j] = result_matr[i][j] + (first_matr[i][2 * k] + second_matr[2 * k + 1][j]) * \
                                    (first_matr[i][2 * k + 1] + second_matr[2 * k][j])

    if (second_rows % 2 == 1):
        for i in range(first_rows):
            for j in range(second_rows):
                result_matr[i][j] = result_matr[i][j] + first_matr[i][second_rows - 1] * second_matr[second_rows - 1][j]

    return result_matr
        

def multiplication_winograd_modified(first_matr, second_matr):
    first_rows, first_cols = len(first_matr), len(first_matr[0])
    second_rows, second_cols = len(second_matr), len(second_matr[0])

    half = second_rows // 2
    rows_factors = [0 for i in range(first_rows)]
    cols_factors = [0 for i in range(first_cols)]
    is_even = second_rows % 2 == 0

    for i in range(first_rows):
        for j in range(half):
            rows_factors[i] += first_matr[i][2 * j] * first_matr[i][2 * j + 1]

    for i in range(second_cols):
        for j in range(half):
            cols_factors[i] += second_matr[2 * j][i] * second_matr[2 * j + 1][i]

    result_matr = [[0 for i in range(second_cols)] for j in range(first_rows)]

    for i in range(first_rows):
        for j in range(second_cols):
            result_matr[i][j] = -rows_factors[i] - cols_factors[j]
            for k in range(half):
                result_matr[i][j] += ((first_matr[i][2 * k] + second_matr[2 * k + 1][j]) * \
                                    (first_matr[i][2 * k + 1] + second_matr[2 * k][j]))
            if not is_even:
                result_matr[i][j] += first_matr[i][second_rows - 1] * second_matr[second_rows - 1][j]

    return result_matr


def print_matr(string, matr):
    rows = len(matr)
    cols = len(matr[0])
    print(string)
    for i in range(rows):
        for j in range(cols):
            print("%3d" % matr[i][j], end = ' ')
        print()
        

if __name__ == '__main__':
    first_rows, first_cols = map(int, input("Введите количество строк и столбцов в первой матрице (через пробел): ").split())
    first_matr = [[None for i in range(first_cols)] for j in range(first_rows)]
    for i in range(first_rows):
        for j in range(first_cols):
            first_matr[i][j] = int(input())
            
    second_rows, second_cols = map(int, input("\nВведите количество строк и столбцов во второй матрице (через пробел): ").split())
    second_matr = [[None for i in range(second_cols)] for j in range(second_rows)]
    for i in range(second_rows):
        for j in range(second_cols):
            second_matr[i][j] = int(input())

    print_matr("\nКлассический алгоритм:", multiplication_classic(first_matr, second_matr))
    print_matr("\nАлгоритм Винограда:", multiplication_winograd(first_matr, second_matr))
    print_matr("\nОптимизированный алгоритм Винограда:", multiplication_winograd_modified(first_matr, second_matr))



