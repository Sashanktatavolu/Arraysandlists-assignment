def most_frequent(List):
    return max(set(List), key = List.count)
 
List = list(map(int,input().split())) 
print(most_frequent(List))