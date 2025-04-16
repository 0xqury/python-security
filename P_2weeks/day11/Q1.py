# 1. 로그 중 "로그인 실패"가 포함딘 줄만 출력 
import re

with open("./log.txt", "r") as f:
    for line in f:
        if "로그인 실패" in line : print(line.strip())