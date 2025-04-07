# 구조화된 JSON 로그 저장기
"""
- 사용자에게 로그 여러 개 입력받기
- 각 로그를 파싱해 dict 형태로 변환
- 리스트에 저장 후 logs.json 에 저장
- 저장된 파일을 다시 불러와 출력
"""
import re
import json
from datetime import datetime
import os


def parse_log_to_dict(log):
    logs = {
        "type": re.search(r"\[[A-Z]+\]",log).group(),
        "date": re.search(r"\d{4}-\d{2}-\d{2}",log).group(),
        "time": re.search(r"\d{2}:\d{2}:\d{2}",log).group(),
        "message": re.search(r"- (.+)$",log).group(1)
    }
    return logs

log_lines = []
log_list = []
while True:
    user_input = input("로그를 입력하세요 (종료 : stop): ")
    if  user_input == "stop":
        break
    else:
        log_lines.append(user_input)

# 딕셔너리 리스트로 변환
try:
    for log in log_lines:
        log_dict = parse_log_to_dict(log) 
        log_list.append(log_dict)
except:
    print("로그 형식이 잘못되었습니다. 다시 입력해주세요.")

# 저장
# ensure_ascii=False 저장될 시 ascii 변환되지 않음 
filename = f"logs_{datetime.now().strftime('%Y%m%d_%H%M%S')}.json"
os.makedirs("logs", exist_ok=True)

with open(f"logs/{filename}", "w", encoding="utf-8") as f :
    json.dump(log_list, f, indent=2, ensure_ascii=False)


# 불러오기
with open(f"logs/{filename}", "r", encoding="utf-8") as f :
    logs = json.load(f)

for log in logs:
    print(log)