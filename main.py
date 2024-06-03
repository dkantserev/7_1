n=int(input())
while(n<1 or n>100000):
	print('incorrect number')
	n=int(input())
	
m=list(map(int,input().split(' ')))
s=set()

if len(m)>n:
	r=[]
	for i in range(n):
		r.append(m[i])
	m=r
	
if len(m)<n:
		print('Not enough numbers')
		exit()
		
for i in  m:
	if i > 2e9:
		print(f'The array contains an invalid number {i}')	
			
for i in range(n):
	s.add(m[i])

print(m)
print(len(s))
