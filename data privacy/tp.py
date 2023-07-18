def processArray():
    arr = []
    num = int(input())
    while(num>=0):
        arr.append(num)
        num = int(input())
    for i in range(len(arr)-1):
        if(arr[i]>=100):
            for j in range(i+1,len(arr)):
                if(arr[j]>=100):
                    arr[j] = -1
                else:
                    break
        else:
            continue
    count = 0      
    for i in arr:
        if(i>=0):
            print(i)
            count += 1
    return count
res = processArray()