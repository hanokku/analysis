#include <iostream>
#include <chrono>
#include <vector>
#include <iomanip>
#include <ctime>
#include <cstdlib>
#include <thread>

using namespace std;

#define SUCCESS 0
#define FAILED 1

typedef std::vector<std::vector<int> > Matrix;
int step_i = 0;

void output_matrix(std::string str, Matrix& matr, int n)
{
    std::cout << str << endl;
    for (auto& row : matr) {
        for (auto& el : row) {
            std::cout << setw(3) << el << ' ';
        }
        std::cout << endl;
    }
}

void create_matrix(Matrix &matr, int n)
{
    for (int i = 0; i < n; i++) {
        std::vector<int> tmp{};
        for (int j = 0; j < n; j++) {
            tmp.push_back(rand() % 10);
        }
        matr.push_back(tmp);
    }
}

void fill_matrix_by_zero(Matrix &matr, int n)
{
    for (int i = 0; i < n; i++) {
        std::vector<int> tmp;
        for (int j = 0; j < n; j++) {
            tmp.push_back(0);
        }
        matr.push_back(tmp);
    }
}

#pragma optimize("", off)
void wino_algo(Matrix &c, Matrix& a, Matrix& b)
{
    int m = a.size(), n = b.size(), q = b[0].size();
    std::vector<int> mulU(m, 0);
    std::vector<int> mulV(q, 0);
    int half = n / 2;

    for (int i = 0; i < m; i++) {
        for (int j = 0; j < half; j++) {
            mulU[i] += a[i][2 * j] * a[i][2 * j + 1];
        }
    }
    for (int j = 0; j < q; j++) {
        for (int i = 0; i < half; i++) {
            mulV[i] += b[2 * j][i] * b[2 * j + 1][i];
        }
    }
    for (int i = 0; i < m; i++) {
        for (int j = 0; j < q; j++) {
            c[i][j] = - mulU[i] - mulV[j];
            for (int k = 0; k < half; k++) {
                c[i][j] += (a[i][2 * k] + b[2 * k + 1][j]) * (a[i][2 * k + 1] + b[2 * k][j]);  
            }
            if (n % 2 == 1) {
                c[i][j] +=  a[i][n - 1] * b[n - 1][j];
            }
        }
    }
}

#pragma optimize("", off)
void wino_algo_threads(Matrix &c, Matrix& a, Matrix& b, int threads_cnt)
{
    int core = step_i++;
    int m = a.size(), n = b.size(), q = b[0].size();
    std::vector<int> mulU(m, 0);
    std::vector<int> mulV(q, 0);
    int half = n / 2;

    for (int i = core * n / threads_cnt; i < (core + 1) * n / threads_cnt; i++) {
        for (int j = 0; j < half; j++) {
            mulU[i] += a[i][2 * j] * a[i][2 * j + 1];
        }
    }
    for (int j = 0; j < q; j++) {
        for (int i = 0; i < half; i++) {
            mulV[j] += b[2 * i][j] * b[2 * i + 1][j];
        }
    }
    for (int i = core * m / threads_cnt; i < (core + 1) * m / threads_cnt; i++) {
        for (int j = 0; j < q; j++) {
            c[i][j] = - mulU[i] - mulV[j];
            for (int k = 0; k < half; k++) {
                c[i][j] += (a[i][2 * k] + b[2 * k + 1][j]) * (a[i][2 * k + 1] + b[2 * k][j]);  
            }
            if (n % 2 == 1) {
                c[i][j] +=  a[i][n - 1] * b[n - 1][j];
            }
        }
    }
}

int main(int argc, char **argv)
{   
    if (argc == 1) {
        //size = atoi(argv[1]);
        //threads_cnt = atoi(argv[2]);
        int size, threads_cnt;
        char output;
        
        std::vector<std::thread> thread_arr;
        chrono::high_resolution_clock::time_point t_beg, t_end;
        std::srand(std::time(nullptr));
        Matrix first_matr{}, second_matr{}, result_matr{};
        std::cout << "Input size of square matrix: ";
        std::cin >> size;
        std::cout << "Input number of threads: ";
        std::cin >> threads_cnt;

        fill_matrix_by_zero(result_matr, size);
        create_matrix(first_matr, size);
        create_matrix(second_matr, size);

        t_beg = chrono::high_resolution_clock::now();        
        for (int i = 0; i < threads_cnt; i++)
            thread_arr.push_back(std::thread(wino_algo_threads, ref(result_matr), ref(first_matr), ref(second_matr), threads_cnt));

        for (auto& thrd : thread_arr)
            thrd.join();
        t_end = chrono::high_resolution_clock::now();
        
        std::cout << "Time: " << chrono::duration_cast<std::chrono::microseconds>(t_end-t_beg).count() << std::endl;
        std::cout << "\nOutput matrixes? (y/n) - ";
        cin >> output;
        if (output == 'y') {
            output_matrix("\nFirst matrix: ", first_matr, size);
            output_matrix("\nSecond matrix: ", second_matr, size);
            output_matrix("\nResult matrix: ", result_matr, size);
        }
        return SUCCESS;
    } else {
        std::cout << "Wrong parametrs!" << endl;
        return FAILED;
    }
}

