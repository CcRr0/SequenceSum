_trans = str.maketrans("0123456789", "₀₁₂₃₄₅₆₇₈₉")  # 수열의 항을 표기하기 위한 아래첨자 변환

print("등차수열의 합 계산기 (aₙ=a+d(n-1))")
a = int(input("초항(a)을 입력하세요: "))
d = int(input("공차(d)를 입력하세요: "))
n = int(input("제 1항부터 제 몇(n)항까지 더할지 입력하세요: "))

sum = 0
for k in range(1, n+1):  # k를 1부터 n까지 1씩 더해가며 반복
    ak = a+d*(k-1)  # aₖ=a+d(k-1)
    k_sub = str(k).translate(_trans)  # 아래첨자 변환
    print("a"+k_sub+"="+str(ak), end=" ")  # aₖ의 값 출력
    sum = sum + ak  # 합에 aₖ 추가

n_sub = str(n).translate(_trans)  # 아래첨자 추가
print("\nS"+n_sub+"="+str(sum))  # 수열의 합 Sₙ 출력

