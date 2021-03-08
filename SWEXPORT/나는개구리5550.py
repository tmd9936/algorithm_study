# tn = int(input())
# fSounds = list()

# for i in range(tn):
#     fSounds.append(input())

# flogSound = "croak"

# def check(ss):
#     cache = list()
#     onk = False
#     result = 0
#     for ss in sound:
#         if ss == 'c':
#             cache.append(['c'])
#             if onk is False:
#                 result += 1
#         else:
#             if ss == 'k':
#                 onk = True
#             index = flogSound.index(ss)
#             # 들어갈 자리가 있는지 체크
#             for i in range(len(cache)):
#                 if len(cache[i]) == index:
#                     cache[i].append(ss)
#                     break
#             else:
#                 return -1
    
#     # 딱 맞는지 계산
#     for ss in cache:
#         if len(ss) != 5:
#             return -1
#     else:
#         return result
    

# for sound in fSounds:
#     print("#1", check(sound))
             
# flogSound = "croak"
# dd = flogSound.index('r')
# print(dd)


# 매 상황마다 몇 마리의 개구리가 우는지 체크하고 이 값이 최대가 되는 시점
T = int(input())

flogSound = "croak"


for test_case in range(1, T + 1):
    sound = input()
    croak = [0]*5
    count = 0
    isError = False

    for ch in sound:
        index = flogSound.index(ch)
        if ch == 'c':
            croak[index] += 1
        else:
            if ch != 'k':
                croak[index] += 1

            croak[index-1] -= 1
            if croak[index-1] == -1:
                count = -1
                break     
        
        count = max(count, sum(croak))
    
    for c in croak:
        if c != 0:
            count = -1
            break
    
    print("#{} {}".format(test_case, count))

    

