"""
집합의 생성
아래 코드의 실행 결과로 생성되는 집합 s의 값은 무엇인가?

python
s = set([1, 2, 3, 2, 1])
print(s)
"""

"""
집합의 연산 결과
다음 중 A와 B의 합집합을 구하는 코드를 모두 고르세요.

python
A = set([1, 2, 3])
B = set([3, 4, 5])
(A) A | B
(B) A.union(B)
(C) A + B
(D) A & B
"""

"""
교집합 구하기
아래 두 set의 교집합 결과를 적으세요.

python
s1 = set([1, 2, 3, 4])
s2 = set([3, 4, 5, 6])
print(s1 & s2)
"""

"""
값 추가/제거
아래 코드의 실행 결과는?

python
s = set([1, 2, 3])
s.add(4)
s.remove(2)
print(s)
"""

"""
집합의 중복 처리
set("Hello")의 결과는 무엇인가?

"""

"""
난이도 있는 문제 (1문제)
응용: 중복 제거 + 차집합
다음 리스트에서 중복을 모두 제거하고,
odds 집합에서 evens 집합을 빼서 남는 값의 합을 구하세요.

python
odds = [1, 3, 5, 7, 3, 1, 9]
evens = [2, 4, 6, 8, 2, 8]
(1) odds와 evens의 중복을 제거해 set으로 만드세요
(2) odds_set에서 evens_set을 빼세요
(3) 남은 값들의 합계는?
"""

"""
2. 불(bool) 자료형 문제
기본 문제 (5문제)
불 변수의 타입과 값
아래 코드의 출력 결과는?

python
a = True
b = False
print(type(a), type(b))
print(a and b)
print(a or b)
"""

"""
조건문의 결과
아래 중 참(True)인 것은 몇 개인가?

"python" 

"" 

`` 

[] 

0 

42 

bool 함수의 결과
아래 값에 대해 bool(x)의 반환값을 적으세요.

bool([])

bool("hello")

bool(0)

bool(3.14)
"""

"""
if 문과 불 자료형
아래 코드 실행 시 어떤 문자열이 출력되는가?

python
s = ""
if s:
    print("참")
else:
    print("거짓")
"""

"""
while문에서 불 자료형 사용
아래 코드가 실행되었을 때 출력되는 값의 마지막은?

python
a = [1, 2, 3]
while a:
    print(a.pop())
"""

