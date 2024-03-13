arr = []

for i in range(int(input("enter the lenght of arr:"))):
    arr.append(int(input("enther the number:")))

def second_lar(arr):
    S_num = arr[0]
    l_num = arr[0]
    for i in range(len(arr)):
        if arr[i] > l_num:
            l_num =arr[i]
    
    for i in range(len(arr)):
        if arr[i] > S_num and arr[i]!= l_num :
            S_num =arr[i]
    return S_num

print(second_lar(arr))
