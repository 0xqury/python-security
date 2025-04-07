# 3. 전체 딕셔너리 리스트를 JSON으로 저장하고 다시 불러오기
import re
import json

def parse_log_to_dict(log):
    logs = {
        "type": re.search(r"\[[A-Z]+\]",log).group(),
        "date": re.search(r"\d{4}-\d{2}-\d{2}",log).group(),
        "time": re.search(r"\d{2}:\d{2}:\d{2}",log).group(),
        "message": re.search(r"- (.+)$",log).group(1)
    }
    return logs

log_lines = [
    "[INFO] 2025-04-03 13:11:22 - 로그인 성공",
    "[ERROR] 2025-04-03 13:12:00 - 접근 거부",
    "[INFO] 2025-04-03 13:13:33 - 로그아웃"
]

# 딕셔너리 리스트로 변환
log_list = [parse_log_to_dict(log) for log in log_lines]
    
# 저장
# ensure_ascii=False 저장될 시 ascii 변환되지 않음 
with open("logs.json", "w") as f :
    json.dump(log_list, f, indent=2, ensure_ascii=False)

# 불러오기
with open("logs.json", "r") as f :
    logs = json.load(f)