a_1 = int(input())
b_1 = int(input())
a_2 = int(input())
b_2 = int(input())

if a_1 < b_1 and a_2 < b_2:
    if a_1 < b_1:
        if b_1 < a_2:
            print('пустое множество')
        elif a_1 < a_2 < b_1 < b_2:
            print(a_2, b_1)
        elif b_2 < b_1:
            print(a_2, b_2)
        elif b_2 == b_1:
            print(a_2, b_1)
        elif b_1 == a_2:
            print(b_1)
    else:
        if a_2 < a_1:
            if b_2 < a_1:
                print('пустое множество')
            elif b_2 > b_1:
                print(a_2, b_2)
            elif b_2 == a_1:
                print(a_1)
            elif b_1 == b_2:
                print(b_1)
        elif a_1 == a_2:
            print(a_1, b_1)