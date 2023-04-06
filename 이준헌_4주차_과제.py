# # your code 를 지우고 그 부분에 본인의 코드를 작성해주세요.
# 4주차 과제에는 출력이나 입력을 요구하는 문제가 없습니다. print(), input() 사용하지 마세요.
# 코드 실행 시 컴파일 에러, 런타임 에러가 발생하면 해당 문제 0점 처리하겠습니다.
# 함수 이름 변경하지 마세요. 변경 시 해당 문제 0점 처리 하겠습니다.
# 제출 기한 : 2023년 4월 10일 23시 59분
# 지각 제출 기한 : 2023년 4월 11일 23시 59분

# 1번
def double(lst):
    sum = 0
    l = len(lst)
    for i in range(l):
        n = lst[i] * 2
        for j in range(l):
            if lst[j] == n:
                sum += 1
    return sum

# 2번
def pascal(n):
    pas = [1]
    pas_1 = [1]
    if n != 1:
        pas.append(1)
        for i in range(n-2):
            for j in range(len(pas) - 1):
                a = pas[j] + pas[j+1]
                pas_1.append(a)
            pas_1.append(1)
            pas = pas_1
            pas_1 = [1]
    return pas

# 3번
def beerRefrigerator(n):
    list_1 = []
    list_2 = []
    
    for i in range(1, n+1):
        if n % i == 0:
            a = i
            n1 = int(n/i)
            for j in range(1, n1+1):
                if n1 % j == 0:
                    b = j
                    c = int(n1/j)
                    s = a*b + b*c + c*a
                    st = str(a) + ' X ' + str(b) + ' X ' + str(c)
                    list_1.append(s)
                    list_2.append(st)
    for i in range(len(list_1)-1):
        if list_1[i] == min(list_1):
            result = list_2[i]
    return result

# 4번
def matrixMul(mat1, mat2):
    hard = 0
    result_1 = []
    result_2 = []
    for n in range(len(mat1)):
        for k in range(len(mat2[0])):
            for m in range(len(mat2)):
                hard += mat1[n][m] * mat2[m][k]
            result_1.append(hard)
            hard = 0
        result_2.append(result_1)
        result_1 = []
            
    return result_2