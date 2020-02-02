from random import randint
from time import process_time
from main import *


REPEATS = 5


def get_random_matrix(m, n):
    return [[randint(0, 100) for i in range(n)] for j in range(m)]


def test_time():
    with open('results.txt', 'w') as f:
        f.write("Размерность    | Классический | Винограда | Оптимизированный Винограда\n")

        for size in range(100, 1100, 100):
            print('Testing matrix {0} X {0} '.format(size))

            f.write("{0} X {0} |".format(size))

            a = get_random_matrix(size, size)
            b = get_random_matrix(size, size)

            t1, t2, t3 = 0, 0, 0

            for i in range(REPEATS):
                start = process_time()
                res_classic = multiplication_classic(a, b)
                stop = process_time()
                t1 += (stop - start)

                start = process_time()
                res_winograd = multiplication_winograd(a, b)
                stop = process_time()
                t2 += (stop - start)

                start = process_time()
                res_winograd_modified = multiplication_winograd_modified(a, b)
                stop = process_time()
                t3 += (stop - start)

            f.write(" {0:<.5f} | {1:<.5f} | {2:<.5f}\n".format(t1 * 1000/REPEATS, t2 * 1000/REPEATS,
                                                             t3 * 1000/REPEATS))
        
        for size in range(101, 1101, 100):
            print('Testing matrix {0} X {0} '.format(size))

            f.write("{0} X {0} |".format(size))

            a = get_random_matrix(size, size)
            b = get_random_matrix(size, size)

            t1, t2, t3 = 0, 0, 0

            for i in range(REPEATS):
                start = process_time()
                res_classic = multiplication_classic(a, b)
                stop = process_time()
                t1 += (stop - start)

                start = process_time()
                res_winograd = multiplication_winograd(a, b)
                stop = process_time()
                t2 += (stop - start)

                start = process_time()
                res_winograd_modified = multiplication_winograd_modified(a, b)
                stop = process_time()
                t3 += (stop - start)

            f.write(" {0:<.5f} | {1:<.5f} | {2:<.5f}\n".format(t1 * 1000/REPEATS, t2 * 1000/REPEATS,
                                                             t3 * 1000/REPEATS))

        f.close()

if __name__ == '__main__':
    test_time()