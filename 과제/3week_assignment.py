# 1번
def grade(score):
    if score >= 90 and score <= 100:
        result = 'A'
    elif score >= 80:
        result = 'B'
    elif score >= 70:
        result = 'C'
    elif score >= 60:
        result = 'D'
    else:
        result = 'F'
    return result

# 2번
def quadrant(x, y):
    if x > 0:
        if y > 0:
            result = '제 1사분면'
        else:
            result = '제 4사분면'
    else:
        if y > 0:
            result = '제 2사분면'
        else:
            result = '제 3사분면'
    return result

# 3번
def leapYear(year):
    if year % 400 == 0:
        result = '윤년입니다.'
    elif year % 100 == 0:
        result = '윤년이 아닙니다.'
    elif year % 4 == 0:
        result = '윤년입니다.'
    else:
        result = '윤년이 아닙니다.'
    return result

# 4번
def dice(a, b, c):
    if a == b and b == c:
        result = 10000 + a*1000
    elif a == b or b == c:
        result = 1000 + b*100
    elif c == a:
        result = 1000 + c*100
    else:
        result = max(a, b, c) * 100
    return result

# 5번
def alarm(time):
    hour = str(time)[:-2]
    if hour == '':
        hour = '0'
    hour = int(hour)
    minute = int(str(time)[-2:])
    if minute >= 45:
        minute -= 45
    else:
        hour -= 1
        minute += 15
    if hour < 0:
        hour += 24
    return str(hour) + '시 ' + str(minute) + '분'