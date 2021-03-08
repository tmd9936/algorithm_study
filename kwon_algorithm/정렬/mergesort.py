


def mergesort(lis):
    if len(lis) == 1:
        return lis
    else:
        tmp = list()
        mid = len(lis)//2
        ls1 = mergesort(lis[0:mid])
        ls2 = mergesort(lis[mid:len(lis)])

        part1 = 0
        part2 = 0

        while (part1 < len(ls1) and part2 < len(ls2)):
            if ls1[part1] <= ls2[part2]:
                tmp.append(ls1[part1])
                part1 += 1
            else:
                tmp.append(ls2[part2])
                part2 += 1
        
        tmp = tmp + ls1[part1:len(ls1)]
        tmp = tmp + ls2[part2:len(ls2)]

        
        return tmp

lis = [10, 2, 50 ,32 ,22 ,4,19, 1, 26, 9]
lis2 = [10, 2, 6, 5]
print(mergesort(lis))
        

        
             

         
        
    
