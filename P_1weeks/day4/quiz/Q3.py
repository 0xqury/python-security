# 3. 로그 메시지 길이 비교 함수
"""
✔ 목적:
- IDS (침입 탐지 시스템) 로그 중에서 alert 메시지 길이를 기준으로 비교
- 평소와 다른 형식의 로그(길이가 긴 메시지 등)를 이상 징후로 판단

✔ 기능 요약:
- 입력: 두 개의 로그 문자열
- 출력: 더 긴 로그 메시지를 반환
"""

# 로그 문자열 길이 비교 함수
def longer_log(msg1, msg2):
    return msg1 if len(msg1) > len(msg2) else msg2

# 샘플 로그 입력
log1 = "GET \\robots.txt"         # 일반적인 요청
log2 = "\\r\\nGET \\robots.txt"   # 예상보다 길거나 특수 문자가 포함된 요청

# 로그 비교 및 결과 출력
if log1 == longer_log(log1, log2):
    print("이상이 없습니다.")
else:
    print("로그가 이상합니다.")
