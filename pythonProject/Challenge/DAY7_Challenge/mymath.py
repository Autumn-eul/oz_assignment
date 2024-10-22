import math

def 삼각형_넓이(밑변, 높이):
    return 0.5 * 밑변 * 높이

def 원_넓이(반지름):
    return math.pi * 반지름 ** 2

def 직육면체_겉넓이(가로, 세로, 높이):
    return 2 * (가로 * 세로 + 세로 * 높이 + 가로 * 높이)