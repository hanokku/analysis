import copy
inf = 999999999999

def generate(t, n, a, array_sequences):
    if t == (n - 1):
        b = copy.deepcopy(a)
        array_sequences.append(b)
    else:
        for j in range(t, n, 1):
            a[j], a[t] = a[t], a[j] 
            generate(t+1, n, a, array_sequences) 
            a[j], a[t] = a[t], a[j]


def full_search(matrix, count_cities): 
    source_seq = list(range(count_cities))
    array_sequences = []
    
    generate(0, count_cities, source_seq, array_sequences)
    min_distance = inf
    
    for i in range(len(array_sequences)): 
        array_sequences[i].append(array_sequences[i][0])
        cur_distance = 0
    
        for j in range(count_cities): 
            first = array_sequences[i][j]
            second = array_sequences[i][j+1]
            cur_distance += matrix[first][second]

        if cur_distance < min_distance: 
            min_distance = cur_distance 
            best_route = array_sequences[i]
    
    return min_distance, best_route


def main():
    matrix = [[0, 5, 8, 2], [5, 0, 10, 1], [8, 10, 0, 4], [2, 1, 4, 0]]
    ed_matrix = [[0, 1, 1, 1, 1, 1], [1, 0, 1, 1, 1, 1], [1, 1, 0, 1, 1, 1],
                 [1, 1, 1, 0, 1, 1], [1, 1, 1, 1, 0, 1], [1, 1, 1, 1, 1, 0]]
    count_cities = 6

    print("Матрица:")
    for i in range(len(ed_matrix)):
        for j in range(len(ed_matrix[0])):
            print("%3d" % ed_matrix[i][j], end = ' ')
        print()

    result = full_search(ed_matrix, count_cities)

    print("Муравьиный алгоритм:\n", result)

if __name__ == '__main__':
    main()