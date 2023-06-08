class Subject:
    def __init__(self):
        self.score = None
        self.subject_name = None
        self.max_score = None

    def get_subject_name(self):
        return self.subject_name
        pass

    def set_score(self, score):
        self.score = score
        pass

    def get_score(self):
        return self.score
        pass

    def get_max_score(self):
        return self.max_score
        pass

class Korean(Subject):
    def __init__(self):
        self.subject_name = "국어"
        self.max_score = 100
        pass

class Math(Subject):
    def __init__(self):
        self.subject_name = "수학"
        self.max_score = 100
        pass

class History(Subject):
    def __init__(self):
        self.subject_name = "역사"
        self.max_score = 50
        pass

class Student:
    def __init__(self, name):
        self.name = name
        self.kor = Korean()
        self.math = Math()
        self.his = History()
        self.subjects = [self.kor, self.math, self.his]
        pass

    def get_name(self):
        return self.name
        pass
    
    def make_sum(self):
        sum = 0
        for n in self.subjects:
            sum += n.get_score()
        return sum
        pass
    
    def print(self):
        print('===== Student {} ====='.format(self.get_name()))
        for subject in self.subjects:
            print('{} : {} / {}'.format(subject.get_subject_name(), subject.get_score(), subject.get_max_score()))
        pass

def print_rank(students):
    scores = []
    for i in students:
        scores.append(i.make_sum())
    scores = sorted(scores, reverse = True)
    print(scores)
    for j in range(len(scores)):
        for i in students:
            if i.make_sum() == scores[j]:
                print('Rank {} : {} ( {} / 250)'.format(j+1, i.get_name(), i.make_sum()))
    pass

# 실행 함수 (수정하지 마세요. 코드 테스트용 함수입니다.)
def Test():
    n = int(input("How many students: "))

    students = []

    for i in range(n):
        name = input("Name of Student: ")

        student = Student(name)

        for subject in student.subjects:
            score = int(input("Score of %s : " %subject.get_subject_name()))
            subject.set_score(score)

        print()
        student.print()
        print()
        students.append(student)

    print("===== Rank =====")
    print_rank(students)

Test()