#lis should be sorted
def bs(lis,k):
    l=0;u=len(lis)-1
    while l<=u:
        mid=(u+l)//2
        if k==lis[mid]:
            return True,mid
        else:
            if k<lis[mid]:
                u=mid-1
            else:
                l=mid+1
    return False
print(bs(list(map(int,input().split())),5))
