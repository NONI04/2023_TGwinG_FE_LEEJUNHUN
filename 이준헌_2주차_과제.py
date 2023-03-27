# 1번
def sum(a, b):
    return a + b

# 2번
def sub(a, b):
    return a - b

# 3번
def mul(a, b):
    return a * b

# 4번
def div(a, b):
    return a / b

# 5번
def distance(x1, y1, x2, y2):
    d1 = (x1 - x2) ** 2
    d2 = (y1 - y2) ** 2
    return (d1 + d2) ** (1/2)

# 6번
def title():
    lylics = "Switch sides and I'm beside you."
    b_y = lylics[-11:-1]
    return b_y

# 7번
def reverseStr(string):
    return string[::-1]

# 8번
def introduce():
    name = input('이름이 무엇인가요? : ')
    hobby = input('취미가 무엇인가요? : ')
    school = input('재학 중인 학교는 어디인가요? : ')
    birth = input('생년월일을 알려주세요 : ')
    birth_1 = int(birth[2:4])
    birth_2 = int(birth[4:6])

    print('제 이름은 {0}입니다. 취미는 {1}입니다. 저는 {2}를 다니고 있습니다.\n제 생일은 {3}월 {4}일입니다.'.format(name, hobby, school, birth_1, birth_2))
    return

# 9번
def calc():
    x = int(input('첫 번째 수를 입력하세요 : '))
    y = int(input('두 번째 수를 입력하세요 : '))
    
    print('두 수의 합 :', x + y)
    print('두 수의 차 :', x - y)
    print('두 수의 곱 :', x * y)
    print('첫 번째 수를 두 번째 수로 나눈 몫 :', x // y)
    return