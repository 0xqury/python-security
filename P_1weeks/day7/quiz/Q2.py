# 2. 파싱한 딕셔너리들을 리스트에 저장
import re

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

# 확인 출력
for log in log_list:
    print(log)