"""
프로그래머스 조이스틱 (Level.2) - 그리디
https://school.programmers.co.kr/learn/courses/30/lessons/42860?language=python3
"""


def solution(name):
    answer = 0  # 최종 결과를 저장할 변수
    length = len(name)  # 문자열의 길이를 저장

    move = length - 1  # 좌우 움직임 수를 초기화

    for i in range(length):
        # 현재 문자를 'A'에서 왼쪽으로 이동하는 경우와 오른쪽으로 이동하는 경우 중 작은 값을 더함
        answer += min(ord(name[i]) - ord('A'), ord('Z') - ord(name[i]) + 1)

        idx = i + 1  # 다음 문자를 확인할 인덱스를 설정
        # 연속된 'A' 문자를 찾아 인덱스를 업데이트
        while idx < length and name[idx] == 'A':
            idx += 1

        # 현재 위치에서 왼쪽으로 이동 후, 오른쪽으로 이동하는 경우와
        # 현재 위치에서 오른쪽으로 이동 후, 왼쪽으로 이동하는 경우 중 작은 값을 선택
        move = min(move, i * 2 + length - idx)
        move = min(move, (length - idx) * 2 + i)

    return answer + move


if __name__ == "__main__":
    print(solution("JAN"))
