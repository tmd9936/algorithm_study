# 1~9의 숫자를 중복해서 6개 뽑았을 때 
# 각각 숫자를 3개로 나누는 모든 경우의 수 중에 아래 2가지가 성립하면 베이비진 (중복 성립도 가능)
# 1. triplete -> 같은 숫자가 3개 ex) 333
# 2. run -> 숫자가 연속 ex) 456
# 

# 그리디 알고리즘

def babygin(num):
    # run 검사를 위해 0 ~ 11까지 생성
    lis_ = [0] * 12
    for _ in range(6):
        lis_[num%10] += 1
        num //= 10

    i = 0
    tri = run = 0
    while i < 10:
        if lis_[i] >= 3:
            lis_[i]-= 3
            tri += 1
            continue
        if lis_[i] >= 1 and lis_[i+1] >= 1 and lis_[i+2] >=1:
            lis_[i] = -1
            lis_[i+1] = -1
            lis_[i+2] = -1
            run += 1
        i += 1
    
    if tri + run >= 2:
        print("Baby gin")
    else:
        print("Lose")

