import json
from collections import defaultdict

# 파일 불러오기
with open("logs/logs.json", "r", encoding="utf-8") as f:
    logs = json.load(f)

# 카운터 딕셔너리 초기화
type_counts = defaultdict(int)
date_counts = defaultdict(int)

# 로그 순회하며 카운트
for log in logs:
    type_counts[log["type"]] += 1
    date_counts[log["date"]] += 1

# 콘솔 출력
print("전체 로그 요약 리포트")
print(f"전체 로그 수: {len(logs)}\n")

print("로그 타입별 개수:")
for t, c in type_counts.items():
    print(f"{t} : {c}개")

print("\n날짜별 로그 개수:")
for d, c in date_counts.items():
    print(f"{d} : {c}개")

# 리포트 파일 저장
with open("logs/report.txt", "w", encoding="utf-8") as f:
    f.write("전체 로그 요약 리포트\n")
    f.write(f"전체 로그 수: {len(logs)}\n\n")

    f.write("로그 타입별 개수:\n")
    for t, c in type_counts.items():
        f.write(f"{t} : {c}개\n")

    f.write("\n날짜별 로그 개수:\n")
    for d, c in date_counts.items():
        f.write(f"{d} : {c}개\n")
