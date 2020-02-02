#include <iostream>
#include <cmath>
#include <vector>

class Build_num;

class Long_int
{
    friend class Build_num;

    public:
        Long_int();
        Long_int(const Long_int& num);
        Long_int(Long_int&& num);

        ~Long_int() = default;

        Long_int& operator= (Long_int& num);
        Long_int& operator= (Long_int&& num);
        Long_int operator/ (Long_int& num);

        void divide(Long_int num_1, Long_int num_2);
        void remove_insig();

        bool error;

        friend std::ostream& operator<< (std::ostream& out, Long_int num)
        {
            if (num.error == true)
            {
                return out;
            }

            if (num.sign == 0)
            {
                std::cout << "0.";
            }
            else
            {
                std::cout << "-0.";
            }

            for (int i = 0; i < num.digit.size(); i++)
            {
                std::cout << num.digit[i];
            }

            std::cout << "e";
            num.mantissa += num.digit.size();
            std::cout << num.mantissa << std::endl;
            num.mantissa -= num.digit.size();
            return out;
        }

    private:
        int sign;
        long int mantissa;
        std::vector<int> digit;
};

class Build_num
{
    public:
        Build_num() = default;
        ~Build_num() = default;

        void build(std::string s);
        Long_int get_res();
    
    private:
        Long_int num;
};