def binary_search(data: list, number:int)->int:
    if len(data)==0:
        return -1
    first=0
    last=len(data)-1
    while first<=last:
        mid=(first+last)//2
        if data[mid]==number:
            return mid
        if data[mid]>number:
            last=mid-1
        else:
            first=mid+1
    return -1
        


print(binary_search([1,2,3,4],4))