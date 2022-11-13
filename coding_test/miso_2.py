"""
Task score : 100%

">" : 우회전하는 자동차
"<" : 자회전하는 자동차
"." : 과속 카메라

모든 자동차가 과속카메라에 찍히는 횟수 구하기
ex.
- ">..<" -> 우회전하는 자동차 과속카메라 2회, 좌회전하는 자동차 과속카메라 2회해서 총 4회 촬영
"""
def solution(S):
    
    car_num = 0
    for i, char in enumerate(S):
        if char == ">":
            car_num += S[(i+1):].count(".")
        elif char == "<":
            car_num += S[:i].count(".")

    return car_num


S = ".>>...<"
print(solution(S))