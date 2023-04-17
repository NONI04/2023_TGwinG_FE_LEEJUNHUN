# your code 를 지우고 코드를 작성하세요.
# 5주차 과제에는 출력이나 입력을 요구하는 문제가 없습니다. print(), input() 사용하지 마세요.
# 코드 실행 시 컴파일 에러, 런타임 에러가 발생하면 해당 문제 0점 처리하겠습니다.
# 함수 이름 변경하지 마세요. 변경 시 해당 문제 0점 처리 하겠습니다.
# result, answer 변수를 사용하여 문제를 풀이하세요. 반환값은 result나 answer 변수입니다.
# 제출 기한: 2023년 4월 17일 23시 59분
# 지각 제출 기한: 2023년 4월 18일 23시 59분
import math

def calcCircleArea(r):
    result = float()
    result = math.pow(r, 2) * math.pi
    result = round(result, 2)
    return result

def calcLog(a, b):
    result = float()
    log = math.log(b, a)
    result = round(log, 2)
    return result

def calcSin(x):
    result = float()
    sin = math.sin(x)
    result = round(sin, 2)
    return result

def calcFactorial(x):
    result = int()
    result = math.factorial(x)
    return result

def calcCombination(n, r):
    result = int()
    result = math.comb(n, r)
    return result

def calculator(order):
    answer = 0
    orderList = order.split()
    if orderList[0] == '원넓이:':
        r = float(orderList[1])
        answer = calcCircleArea(r)
    elif orderList[0] == '로그:':
        a = orderList[1]
        if a == 'e':
            a = math.e
        else:
            a = float(a)
        b = orderList[2]
        if b == 'e':
            b = math.e
        else:
            b = float(b)
        answer = calcLog(a, b)
    elif orderList[0] == '사인:':
        x = float(orderList[1])
        answer = calcSin(x)
    elif orderList[0] == '팩토리얼:':
        x = int(orderList[1])
        answer = calcFactorial(x)
    elif orderList[0] == '조합:':
        n = int(orderList[1])
        r = int(orderList[2])
        answer = calcCombination(n, r)
    return answer