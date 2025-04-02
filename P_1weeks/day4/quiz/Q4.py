# 4. 시스템 상태 점검기 함수
"""
목적:
- CPU 사용률과 메모리 사용량을 기반으로 시스템 상태를 평가하는 함수
- IR 또는 보안 운영 자동화 스크립트에서 활용 가능

기능 요약:
- 입력: CPU 점수, 메모리 점수 (0~10 스케일 또는 정규화된 값)
- 계산: CPU 60%, 메모리 40% 가중 평균
- 출력: 소수점 둘째 자리까지 반올림된 시스템 점수
"""

def get_system_score(cpu, mem):
    score = (cpu * 0.6) + (mem * 0.4)
    return round(score, 2)

def get_status(score):
    if score >= 8:
        return "양호"
    elif score >= 5:
        return "주의"
    else:
        return "위험"
    
score = get_system_score(7, 16)
print(f"시스템의 상태 점수 = {score}")
print(f"시스템의 상태 = {get_status(score)}")


