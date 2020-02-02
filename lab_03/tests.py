from main import *
from time import process_time
import random

REPEATS = 10

def test_sorts():
    a_1 = []
    a_2 = []
    a_3 = []

    b_1 = []
    b_2 = []
    b_3 = []

    c_1 = []
    c_2 = []
    c_3 = []

    with open('results.txt', 'w') as f:
        for i in range(100, 1100, 100):
            f.write('Testing array {0}'.format(i))
            t1, t2, t3, t4, t5, t6, t7, t8, t9 = 0, 0, 0, 0, 0, 0, 0, 0, 0
            f.write("\n===========================\n")
            for j in range(REPEATS):
                a_1 = get_sorted_array(i)
                a_2 = get_unsorted_array(i)
                a_3 = get_random_array(i)

                b_1 = get_sorted_array(i)
                b_2 = get_unsorted_array(i)
                b_3 = get_random_array(i)

                c_1 = get_sorted_array(i)
                c_2 = get_unsorted_array(i)
                c_3 = get_random_array(i)

                start = process_time()
                a_1 = gnome_sort(a_1)
                end = process_time()
                t1 += (end - start)
        
                start = process_time()
                a_2 = gnome_sort(a_2)
                end = process_time()
                t2 += (end - start)

                start = process_time()
                a_3 = gnome_sort(a_3)
                end = process_time()
                t3 += (end - start)

                start = process_time()
                b_1 = insert_sort(b_1)
                end = process_time()
                t4 += (end - start)
        
                start = process_time()
                b_2 = insert_sort(b_2)
                end = process_time()
                t5 += (end - start)

                start = process_time()
                b_3 = insert_sort(b_3)
                end = process_time()
                t6 += (end - start)

                start = process_time()
                c_1 = bubble_sort(c_1)
                end = process_time()
                t7 += (end - start)
        
                start = process_time()
                c_2 = bubble_sort(c_2)
                end = process_time()
                t8 += (end - start)

                start = process_time()
                c_3 = bubble_sort(c_3)
                end = process_time()
                t9 += (end - start)

                a_1, a_2, a_3, b_1, b_2, b_3, c_1, c_2, c_3 = [], [], [], [], [], [], [], [], []

            f.write('Gnome sorted array: {0:<.5f}\n'.format(t1 * 1000/REPEATS))
            f.write('Gnome unsorted array: {0:<.5f}\n'.format(t2 * 1000/REPEATS))
            f.write('Gnome random array: {0:<.5f}\n'.format(t3 * 1000/REPEATS, '\n'))

            f.write('Insert sorted array: {0:<.5f}\n'.format(t4 * 1000/REPEATS))
            f.write('Insert unsorted array: {0:<.5f}\n'.format(t5 * 1000/REPEATS))
            f.write('Insert random array: {0:<.5f}\n'.format(t6 * 1000/REPEATS, '\n'))

            f.write('Bubble sorted array: {0:<.5f}\n'.format(t7 * 1000/REPEATS))
            f.write('Bubble unsorted array: {0:<.5f}\n'.format(t8 * 1000/REPEATS))
            f.write('Bubble random array: {0:<.5f}\n'.format(t9 * 1000/REPEATS))
            f.write("===========================\n\n")


def get_sorted_array(length):
    arr = []
    for i in range(length):
        arr.append(i)
    return arr


def get_unsorted_array(length):
    arr = []
    for i in range(length, 0, -1):
        arr.append(i)
    return arr


def get_random_array(length):
    arr = []
    for i in range(length):
        arr.append(random.randint(-100, 100))
    return arr

if __name__ == '__main__':
    test_sorts()