# 1. 로그 한 줄을 딕셔너리로 변환하는 함수 만들기
import re

def parse_log_to_dict(log):
    logs = {
        "type": re.search(r"\[[A-Z]+\]",log).group(),
        "date": re.search(r"\d{4}-\d{2}-\d{2}",log).group(),
        "time": re.search(r"\d{2}:\d{2}:\d{2}",log).group(),
        "message": re.search(r"- (.+)$",log).group(1)
    }
    return logs

logs = parse_log_to_dict("[INFO] 2025-04-03 13:11:22 - 로그인 성공")

print(logs["type"])
print(logs["date"])
print(logs["time"])
print(logs["message"])