# 2. "로그인 실패"로그만 따로 failed.txt 파일에 저장
"""
사용 함수 정리
with open() as f
for line in f:
"문자열" in line
line.strip()
f.write(line)
"""
logs = []
with open("./log.txt", "r") as f:
    for line in f:
        if "로그인 실패" in line: 
            logs.append(line.strip())
        
with open("./failed.txt", "w", encoding="utf-8") as f:
    for line in logs:
        f.write(line + "\n")