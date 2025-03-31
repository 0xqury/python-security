# 사용자로부터 5개의 숫자를 입력받아 리스트에 저장하고,
# 입력된 숫자 리스트 출력, 최대값, 최소값, 평균 출력
arr = []
h, l, sum = 0,0,0

try:    # 예외처리를 통해 숫자만 입력 되게끔 처리.
    for i in range(0,5):    # 0부터 4까지의 반복문 
        arr.append(int(input(f"{i+1}번. 숫자를 입력하세요 : ")))    # 배열에 입력값을 추가. 
        sum += arr[i]
        if i == 0:  # 초기 최대, 최소값 셋팅 
            h = arr[0]
            l = h
        else:
            if h < arr[i]: h = arr[i]   # 최대값 설정 
            elif l > arr[i]: l = arr[i] # 최소값 설정 

    # 숫자 리스트 출력
    for i in range(0,5):
        print(f"{i+1}번 인덱스 : {arr[i]}")

    # 최대값, 최소값 출력
    print(f"최대값 : {h}")
    print(f"최소값 : {l}")

    # 평균값 출력
    print(f"평균값 : {sum/len(arr)}")
except:
    print("숫자만 입력하세요.")