# 1. [INFO] 로그 개수 세기
import re

def parse_log_to_dict(log):
    logs = {
        "type": re.search(r"\[[A-Z]+\]",log).group(),
        "date": re.search(r"\d{4}-\d{2}-\d{2}",log).group(),
        "time": re.search(r"\d{2}:\d{2}:\d{2}",log).group(),
        "message": re.search(r"- (.+)$",log).group(1)
    }
    return logs

logs = []

while True:
    log = input("로그를 입력하세요(종료 : stop) : ")
    if log == "stop":
        break
    logs.append(parse_log_to_dict(log))
        
info_count = sum(1 for log in logs if log["type"] == "[INFO]")

print(f"INFO 로그 수 : {info_count}")
