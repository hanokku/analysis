#include "num.h"

Long_int::Long_int()
{
    error = true;
}

Long_int::Long_int(const Long_int& num)
{
    this->digit.clear();
    this->mantissa = num.mantissa;
    this->sign = num.sign;
    this->error = num.error;

    for (int i = 0; i < num.digit.size(); i++)
    {
        this->digit.push_back(num.digit[i]);
    }
}

Long_int::Long_int(Long_int&& num)
{
    this->digit.clear();
    this->mantissa = num.mantissa;
    this->sign = num.sign;
    this->error = num.error;

    for (int i = 0; i < num.digit.size(); i++)
    {
        this->digit.push_back(num.digit[i]);
    }
}

Long_int& Long_int::operator= (Long_int& num)
{
    this->digit.clear();
    this->mantissa = num.mantissa;
    this->sign = num.sign;
    this->error = num.error;

    for (int i = 0; i < num.digit.size(); i++)
    {
        this->digit.push_back(num.digit[i]);
    }

    num.digit.clear();
    return (*this);
}

Long_int& Long_int::operator= (Long_int&& num)
{
    this->digit.clear();
    this->mantissa = num.mantissa;
    this->sign = num.sign;
    this->error = num.error;

    for (int i = 0; i < num.digit.size(); i++)
    {
        this->digit.push_back(num.digit[i]);
    }

    num.digit.clear();
    return (*this);
}

Long_int Long_int::operator/ (Long_int& num)
{
    Long_int res_num;
    res_num.divide(*this, num);
    return Long_int(res_num);
}

void Long_int::divide(Long_int num_1, Long_int num_2)
{
    int precision = 10;
    this->error = false;

    if (num_2.digit.size() == 1 && num_2.digit[0] == 0)
    {
        this->error = true;
        return;
    }

    while (num_1.digit.size() < precision)
    {
        num_1.digit.push_back(0);
        num_1.mantissa--;
    }

    this->digit.clear();
    this->mantissa = num_1.mantissa - num_2.mantissa + 1;
    this->sign = (num_1.sign + num_2.sign) % 2;

    int count = precision - num_2.digit.size();
    int i = 0, calc = 0, k = 0;

    while (num_2.digit.size() < precision)
    {
        num_2.digit.push_back(0);
    }

    for (int j = 0; j < count; j++)
    {
        calc = 0;
        i = 0;

        while (num_1.digit[k] >= 0)
        {
            for (i = precision - 1; i >= k; i--)
            {
                num_1.digit[i] -= num_2.digit[i];

                if (num_1.digit[i] < 0 && i > k)
                {
                    num_1.digit[i - 1]--;
                    num_1.digit[i] += 10;
                }
            }

            if (num_1.digit[k] >= 0)
            {
                calc++;
            }
        }

        for (i = precision - 1; i >= k; i--)
        {
            num_1.digit[i] += num_2.digit[i];

            if (num_1.digit[i] > 9 && i > 0)
            {
                num_1.digit[i - 1]++;
                num_1.digit[i] -= 10;
            }
        }

        this->digit.push_back(calc);

        for (i = precision - 1; i > 0; i--)
        {
            num_2.digit[i] = num_2.digit[i - 1];
        }

        num_2.digit[k] = 0;

        if (calc && num_1.digit[k] == 0)
        {
            k += 1;

            if (j > 0 && this->digit[j - 1] == 0 && this->digit[k] == 0)
            {
                k++;
            }
        }
    }
}

void Long_int::remove_insig()
{
    int i = 0;

    while (digit[i] == 0 && digit.size() > 1)
    {
        for (int j = 0; j < digit.size(); j++)
        {
            digit[j] = digit[j + 1];
        }
        digit.pop_back();
    }

    i = digit.size() - 1;

    while (digit[i] == 0 && i > 0)
    {
        mantissa++;
        i--;
        digit.pop_back();
    }

    if (digit[0] == 0)
    {
        mantissa = 0;
    }
}

void Build_num::build(std::string s) 
{
    num.digit.clear();
    num.mantissa = 0;
    num.sign = 0;
    num.error = true;

    char c = 0;
    int pos = 0;
    std::vector<char> mantissa_count;

    int point = 0;

    c = s[pos];
    pos++;

    if (c == '-') 
    {
        num.sign = 1;
        c = s[pos];
        pos++;
    } 
    else if (c == '+') 
    {
        c = s[pos];
        pos++;
    } 
    else if (!((c <= '9' && c >= '0') || '.' == c))
    {
        std::cout << "Wrong input!\n" << std::endl;
        return;
    }

    while (pos <= s.size() && c != 'e' && c != 'E') 
    {
        if (c <= '9' && c >= '0') 
        {
            num.digit.push_back((int)c - 48);
            if (point)
            {
                num.mantissa--;
            }
        } 
        else if (c == '.' && 0 == point) 
        {
            point = 1;
        } 
        else 
        {
            std::cout << "Wrong input!\n" << std::endl;
            return;
        }

        c = s[pos];
        pos++;
    }

    while (pos < s.size()) 
    {
        c = s[pos];
        pos++;
        if (!((c <= '9' && c >= '0') || (mantissa_count.size() == 0 && (c == '-' || c == '+')) || c == '\0')) 
        {
            std::cout << "Wrong input!\n" << std::endl;
            return;
        }
        if (c != '\0')
        {
            mantissa_count.push_back(c);    
        }
    }

    // мантисса
    if (mantissa_count.size() > 0) 
    {
        if (mantissa_count[0] == '-') 
        {
            for (int j = 1; j < mantissa_count.size(); j++)
            {
                num.mantissa -= ((int)mantissa_count[j] - 48) * pow(10, mantissa_count.size() - j - 1);
            }
        } 
        else if (mantissa_count[0] == '+') 
        {
            for (int j = 1; j < mantissa_count.size(); j++)
            {
                num.mantissa += ((int)mantissa_count[j] - 48) * pow(10, mantissa_count.size() - j - 1);
            }
        } 
        else 
        {
            for (int j = 0; j < mantissa_count.size(); j++)
            {
                num.mantissa += ((int)mantissa_count[j] - 48) * pow(10, mantissa_count.size() - j - 1);
            }
        }
    }
    num.error = false;
}

Long_int Build_num::get_res() 
{
    return num;
}