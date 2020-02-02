#include <chrono>
#include <thread>
#include <queue>
#include <mutex>

#include "num.h"

using namespace std;
using namespace std::chrono;

string get_random_str()
{
    int length_1 = 2 + rand() % 6;
    int length_2 = 3 + rand() % 6;

    std::string s(length_1 + length_2, 0);

    static const char sign[] = "+-";
    s[0] = sign[rand() % 2];

    static const char digits[] = "0123456789";

    for (int i = 1; i < length_1; i++)
    {
        s[i] = digits[rand() % (sizeof(digits) - 1)];
    }

    s[length_1] = 'e';
    s[length_1 + 1] = sign[rand() % 2];

    for (int i = length_1 + 2; i < length_1 + length_2; i++)
    {
        s[i] = digits[rand() % (sizeof(digits) - 1)];
    }

    return s;
}

std::mutex lock_data;
std::mutex lock_output;

queue<std::string> str1, str2;
queue<Long_int> zeros_1;
queue<Long_int> zeros_2;
queue<Long_int> zeros;
queue<Long_int> num_1;
queue<Long_int> num_2;
queue<Long_int> res_num;

int sign = 0;

void thread_read_first()
{
    Build_num bld;

    while (true)
    {
        if (str1.empty())
        {
            sign++;
            return;
        }

        bld.build(str1.front());
        str1.pop();
        lock_output.lock();
        std::cout << "First number: " << bld.get_res() << std::endl;
        lock_output.unlock();

        if (!bld.get_res().error)
        {
            lock_data.lock();
            zeros_1.push(bld.get_res());
            lock_data.unlock();
        }
    }
}

void thread_read_second()
{
    Build_num bld;

    while (true)
    {
        if (str2.empty())
        {
            sign++;
            return;
        }

        bld.build(str2.front());
        str2.pop();
        lock_output.lock();
        std::cout << "Second number: " << bld.get_res() << std::endl;
        lock_output.unlock();

        if (!bld.get_res().error)
        {
            lock_data.lock();
            zeros_2.push(bld.get_res());
            lock_data.unlock();
        }
    }
}

void thread_insig_first()
{
    Long_int num;

    while (true)
    {
        if (zeros_1.empty())
        {
            if (sign >= 2)
            {
                sign++;
                return;
            }
            continue;
        }

        num = zeros_1.front();
        
        lock_data.lock();
        zeros_1.pop();
        lock_data.unlock();
        num.remove_insig();

        lock_output.lock();
        std::cout << "Remove insignificant zeros from first number: " << num << std::endl;
        lock_output.unlock();
        lock_data.lock();
        num_1.push(num);
        lock_data.unlock();
    }
}

void thread_insig_second()
{
    Long_int num;

    while (true)
    {
        if (zeros_2.empty())
        {
            if (sign >= 3)
            {
                sign++;
                return;
            }
            continue;
        }

        num = zeros_2.front();
        
        lock_data.lock();
        zeros_2.pop();
        lock_data.unlock();
        num.remove_insig();

        lock_output.lock();
        std::cout << "Remove insignificant zeros from second number: " << num << std::endl;
        lock_output.unlock();
        lock_data.lock();
        num_2.push(num);
        lock_data.unlock();
    }
}

void thread_divide_nums()
{
    Long_int num;

    while (true)
    {
        if (num_1.empty() || num_2.empty())
        {
            if (sign >= 4)
            {
                sign++;
                return;
            }
            continue;
        }

        num.divide(num_1.front(), num_2.front());

        lock_data.lock();
        num_1.pop();
        num_2.pop();
        lock_data.unlock();

        lock_output.lock();
        std::cout << "Division of two numbers: " << num << std::endl;
        lock_output.unlock();

        if (!num.error)
        {
            lock_data.lock();
            zeros.push(num);
            lock_data.unlock();
        }
    }
}

void thread_insig_result()
{
    Long_int num;

    while (true)
    {
        if (zeros.empty())
        {
            if (sign >= 5)
            {
                sign++;
                return;
            }
            continue;
        }

        num = zeros.front();
        lock_data.lock();
        zeros.pop();
        lock_data.unlock();

        num.remove_insig();

        lock_output.lock();
        std::cout << "Remove insignificant zeros from result number: " << num << std::endl;
        lock_output.unlock();
    }
}

int main(int argc, char *argv[])
{
    std::chrono::high_resolution_clock::time_point first_t, second_t;

    first_t = std::chrono::high_resolution_clock::now();
    second_t = std::chrono::high_resolution_clock::now();

    std::string s;

    auto ms = std::chrono::duration_cast<microseconds>(second_t - first_t);
    std::cout << "Division of numbers\n" << std::endl;

    queue<string> first_str;
    queue<string> second_str;

    if (argc == 1)
    {
        std::cout << "Input first number: " << std::endl;
        std::cin >> s;
        str1.push(s);

        std::cout << "Input second number: " << std::endl;
        std::cin >> s;
        str2.push(s);

        std::thread first_input(thread_read_first);
        std::thread second_input(thread_read_second);

        std::thread first_zeros(thread_insig_first);
        std::thread second_zeros(thread_insig_second);

        std::thread div_nums(thread_divide_nums);
        std::thread res_zeros(thread_insig_result);

        first_input.join();
        second_input.join();
        
        first_zeros.join();
        second_zeros.join();

        div_nums.join();
        res_zeros.join();
    }
    else
    {
        int length = atoi(argv[1]);

        for (int i = 0; i < length; i++)
        {
            s = get_random_str();
            str1.push(s);
            first_str.push(s);

            s = get_random_str();
            str2.push(s);
            second_str.push(s);
        }

        std::thread first_input(thread_read_first);
        std::thread second_input(thread_read_second);

        std::thread first_zeros(thread_insig_first);
        std::thread second_zeros(thread_insig_second);

        std::thread div_nums(thread_divide_nums);
        std::thread res_zeros(thread_insig_result);

        first_t = std::chrono::high_resolution_clock::now();

        first_input.join();
        second_input.join();
        
        first_zeros.join();
        second_zeros.join();

        div_nums.join();
        res_zeros.join();

        second_t = std::chrono::high_resolution_clock::now();
        ms = std::chrono::duration_cast<microseconds>(second_t - first_t);

        std::cout << ms.count() << " ";

        first_t = std::chrono::high_resolution_clock::now();

        Long_int tmp_num;
        Long_int tmp_num_1;
        Long_int tmp_num_2;
        Build_num bld_1;
        Build_num bld_2;

        while (first_str.empty() + second_str.empty() == 0)
        {
            s = first_str.front();
            first_str.pop();

            bld_1.build(s);

            if (!bld_1.get_res().error)
            {
                tmp_num_1 = bld_1.get_res();
                tmp_num_1.remove_insig();
            }

            s = second_str.front();
            second_str.pop();

            bld_2.build(s);

            if (!bld_2.get_res().error)
            {
                tmp_num_2 = bld_2.get_res();
                tmp_num_2.remove_insig();
            }

            if (tmp_num_1.error + tmp_num_2.error == 0)
            {
                tmp_num.divide(tmp_num_1, tmp_num_2);
            }

            if (!tmp_num.error)
            {
                tmp_num.remove_insig();
            }
        }
        second_t = std::chrono::high_resolution_clock::now();

        ms = std::chrono::duration_cast<microseconds>(second_t - first_t);
        std::cout << ms.count() << std::endl;
    }   
}
