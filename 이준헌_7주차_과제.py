# your code 를 지우고 코드를 작성하세요.
# 7주차 과제에는 출력이나 입력을 요구하는 문제가 없습니다. print(), input() 사용하지 마세요.
# 코드 실행 시 컴파일 에러, 런타임 에러가 발생하면 해당 문제 0점 처리하겠습니다.
# 함수 이름 변경하지 마세요. 변경 시 해당 문제 0점 처리 하겠습니다.
# 제출 기한: 2023년 5월 15일 23시 59분
# 지각 제출 기한: 2023년 5월 16일 23시 59분
# 3번 문제는 table을 사용해 풀이해주세요. (dictionary 활용) 다른 방법으로 구현하면 감점 또는 0점 처리하겠습니다.

# 1번
def relativeComp(a, b):
    set1 = a-b
    if set1 == set():
        result = 0
    else:
        list1 = []
        for i in set1:
            list1.append(i)
        result = sorted(list1)
    return result

# 2번
def alphabetFreq(word):
    table = {}
    set1 = set()
    for i in word:
        countWord = word.count(i.lower()) + word.count(i.upper())
        table[i.upper()] = countWord
        set1.add(countWord)
    list1 = []
    for alp in table:
        if table[alp] == max(set1):
            list1.append(alp)
    if len(list1) == 1:
        result = list1[0]
    else:
        result = '?'
    return result