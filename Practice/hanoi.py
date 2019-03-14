def hanoi(n):
	if n == 1:
		return 1
	return hanoi(n-1) + 1 + hanoi(n-1)


if __name__ == "__main__":
	print(hanoi(3))
	print(hanoi(4))
	print(hanoi(5))
	print(hanoi(6))
	print(hanoi(7))