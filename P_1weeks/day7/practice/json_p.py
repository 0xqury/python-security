import json

logs = {
    "type": "[ERROR]",
    "date": "2025-04-03",
    "time": "13:22:00",
    "message": "로그인 실패"
}

# 저장
with open("logs.json", "w") as f :
    json.dump(logs, f, indent=2)

# 불러오기
with open("logs.json", "r") as f :
    logs = json.load(f)
