import math


def prime(n):
    if n <= 1:
        return "false"
    if n == 2:
        return "true"
    n_square = math.sqrt(n)
    for i in range(2, int(n_square)):
        if n % i == 0:
            return "false"
    return "true"


# func checkPrime(n int) bool {
# 	nSquare := int(math.Sqrt(float64(n)))
# 	for i := 2; i <= nSquare; i++ {
# 		if n%i == 0 {
# 			return false
# 		}
# 	}
# 	return true
# }

print(prime(2))
