def binary(li,val):
    l = 0
    u= len(li)-1
    while l<=u:
        mid = (l+u)//2
        if li[mid] == val:
            return mid
        if li[mid] >val:
            l = mid+1
        else:
            u = mid-1
    return -1


li = list(map(int,input().split()))
val = int(input())
li.sort()
print(li)
print(binary(li,val))