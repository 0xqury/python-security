# 2. 각 로그 타입별 개수 세기
import re
from collections import defaultdict

def parse_log_to_dict(log):
    logs = {
        "type": re.search(r"\[[A-Z]+\]",log).group(),
        "date": re.search(r"\d{4}-\d{2}-\d{2}",log).group(),
        "time": re.search(r"\d{2}:\d{2}:\d{2}",log).group(),
        "message": re.search(r"- (.+)$",log).group(1)
    }
    return logs

logs = []
type_counts = defaultdict(int)

while True:
    user_input = input("로그를 입력하세요(종료 : stop) : ")
    if user_input == "stop":
        break
    logs.append(parse_log_to_dict(user_input))
        
for log in logs:
    type_counts[log["type"]] += 1

for log_type, count in type_counts.items():
    print(f"{log_type} 로그 수: {count}")
