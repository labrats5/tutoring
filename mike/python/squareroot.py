ε = 1e-7
C = float(input())

bottom = (C/2)**0.5
mid = top = C**0.5

while bottom < top:
	mid = (bottom + top) / 2
	equation = mid**2 + mid**0.5
	if abs(equation - C) < ε:
		break
	if equation < C:
		bottom = mid
	else:
		top = mid
	

print(round(mid, 6))
