from random import *
inf = 999999999999

def calculate_lk(D, visited_cities):
    lk = 0

    for l in range(1, len(visited_cities)):
        i = visited_cities[l-1]
        j = visited_cities[l]
        lk += D[i][j]

    return lk

def ant_alg(D, count_cities): 
    avg = 0
    count = 0
    for i in range(count_cities):
        for j in range(count_cities): 
            if 0 < D[i][j] < inf:
                avg += D[i][j]
                count += 1
    avg /= count
    
    alpha, beta, Q = 2, 3, avg 
    tau0 = randint(2, 10) 
    tau_limit, rho = 0.001, 0.75 
    count_ants = count_cities

    eta = [0]*count_cities 
    tau = [0]*count_cities

    for i in range(count_cities): 
        eta[i] = [0]*count_cities 
        tau[i] = [0]*count_cities

    for i in range(count_cities):
        for j in range(count_cities):
            if i != j:
                eta[i][j] = 1/D[i][j]
                tau[i][j] = tau0
            else:
                tau[i][j] = 0

    t = 0
    tmax = 10 
    L_best = inf

    while t < tmax:
        l = list(range(count_cities)) 
        shuffle(l)

        visited_cities = [0]*count_ants 
        for i in range(count_ants):
            visited_cities[i] = [] 
            visited_cities[i].append(l[i])


        for k in range(count_ants):
            while len(visited_cities[k]) != count_cities:
                Pk = [0]*count_cities
                for i in range(count_cities):
                    if i in visited_cities[k]: 
                        Pk[i] = 0
                    else:
                        cur_i = visited_cities[k][-1]
                        Pk[i] = (tau[cur_i][i]**alpha) * (eta[cur_i][i]**beta)

                summ = sum(Pk)
                for i in range (count_cities):
                    Pk[i] /= summ

                coin = random()
                summ, i = 0, 0
                while (i < len(Pk)) and summ < coin:
                    summ += Pk[i]
                    i += 1 
                visited_cities[k].append(i-1)

            visited_cities[k].append(visited_cities[k][0])
            Lk = calculate_lk(D, visited_cities[k])

            if Lk < L_best: 
                L_best = Lk
                best_route = visited_cities[k]

        for i in range(count_cities):
            for j in range(count_cities):
                summ = 0
                for k in range(count_ants):
                    Lk = calculate_lk(D, visited_cities[k])
                    fl = False
                    for m in range(1, len(visited_cities[k])):
                        if ((visited_cities[k][m]== i and 
                            visited_cities[k][m-1] == j)
                            or (visited_cities[k][m]==j and
                                visited_cities[k][m-1] == i)): 
                            fl = True
                    
                    if fl:
                        summ += Q/Lk

                delta_tau = summ
                tau[i][j] = tau[i][j]*(1 - rho) + delta_tau 
                if tau[i][j] < tau_limit:
                    tau[i][j] = tau_limit
        
        t += 1
    return L_best, best_route

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

    result = ant_alg(ed_matrix, count_cities)

    print("Муравьиный алгоритм:\n", result)

if __name__ == '__main__':
    main()