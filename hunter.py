sum = 3420
n1 = round((sum//1000),0)
n2 = round((sum - (n1*1000)) // 100, 0 )
n3 = round((sum - (n1*1000) - (n2*100)) // 10, 0)

print(sum,'원을 계산하려면')
print('1000원 지폐', n1,'장')
print('100원 동전', n2,'개')
print('10원 동전', n3,'개가 필요합니다')
