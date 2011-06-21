#
# recursive factorial
#
def f(n):
	n = int(n)
	return n if n < 2 else n*f(n-1)

print(f(4))

