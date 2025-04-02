# 2. 포트 필터 함수
"""
✔ 목적:
- 포트 번호 리스트 중에서 짝수 포트만 필터링하는 함수 구현
- 보안 도구(예: 포트 스캐너)에서 필터 조건으로 활용 가능

✔ 기능 요약:
- 입력: 포트 번호 리스트 (1~N)
- 출력: 짝수 포트만 담긴 리스트 반환
"""

# 짝수 포트만 필터링하는 함수 정의
def is_even_port(port_list):
    return [port for port in port_list if port % 2 == 0]

# 1~1024번 포트 리스트 생성 (주요 Well-Known 포트 범위)
port_list = [(i + 1) for i in range(1024)]

# 짝수 포트 추출
even_ports = is_even_port(port_list)

# 결과 출력
print("🔍 짝수 포트 출력:")
for port in even_ports:
    print(f"{port}")
