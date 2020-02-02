def get_slide(pattern, m):
    slide = 256 * [-1]
    for i in range(m):
        slide[ord(pattern[i])] = i

    return slide

def bm(pattern, text):
    patternLoc = len(pattern)
    textLoc = len(text)

    slide = get_slide(pattern, patternLoc)
    length = 0

    while(length <= (textLoc - patternLoc)):
        tmp = patternLoc - 1
        while (tmp >= 0 and pattern[tmp] == text[length + tmp]):
            tmp -= 1
        if (tmp < 0):
            return length
        else:
            length += max(1, tmp - slide[ord(text[length + tmp])])
    
    if (length == None):
        return -1

def get_fail(substr):
    fail = [0] * len(substr)
    for i in range(1, len(substr)):
        k = fail[i-1]
        while k > 0 and substr[k] != substr[i]:
            k = fail[k-1]
        if substr[k] == substr[i]:
            k = k + 1
        fail[i] = k

    return fail

def kmp(substr, text):
    index = -1
    f = get_fail(substr)
    print(f)
    k = 0
    for i in range(len(text)):
        while k > 0 and substr[k] != text[i]:
            k = f[k-1]
        if substr[k] == text[i]:
            k = k + 1
        if k == len(substr):
            index = i - len(substr) + 1
            break

    return index

def main(): 
    txt = input("Введите строку: ")
    pat = input("Введите подстроку: ")
    res_bm = bm(pat, txt)
    res_kmp = kmp(pat, txt)

    if (res_bm == None):
        res_bm = -1

    print("Алгоритм Бойера-Мура: ", res_bm)
    print("Алгоритм Кнута-Морриса-Пратта: ", res_kmp)
  
if __name__ == '__main__': 
    main() 
