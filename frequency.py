#find the frequency of element in array



arr = [10, 30, 10, 20, 10, 20, 30, 10]
new_lst=[]
count=1
for i in range(len(arr)):
    if arr[i] not in new_lst:
        a=arr.count(arr[i])
        new_lst.append(arr[i])
        print("{} {}".format(arr[i],a))
    
    
