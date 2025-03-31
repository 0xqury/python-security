# 리스트 생성 및 접근
nums = [10, 20, 30]
print(nums[1]) # nums의 인덱스 1 = 20 출력

# 추가 / 삭제 / 길이 확인
nums.append(40)
nums.remove(20)
print(len(nums)) # 3 확인 가능.

scores = [85, 54, 67, 75]
total = 0

for score in scores:
    total += score

print("총합 = ", total)
print("평균 = ",total/len(scores))