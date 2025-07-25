# x and y are divided into two parts of equal number of digits like x = a b and y = c d
# x . y = (10^n/2 * a + b) . (10^n/2 * c + d)
# x . y = 10^n * a . c + 10^n/2 * a . d + b . 10^n/2 * c + b . d



def rec_int_mult(x, y, n):

    if n == 1:
        return x * y 

    a = x // (10 ** (n / 2))
    b = x % (10 ** (n / 2))
    
    c = y // (10 ** (n / 2))
    d = y % (10 ** (n / 2))

    return ((10 ** n) * rec_int_mult(a, c, n/2)) + (10 ** (n/2) * rec_int_mult(a, d, n/2)) + (10 ** (n/2) * rec_int_mult(b, c, n/2)) + rec_int_mult(b, d, n/2)

print(rec_int_mult(5678, 1234, 4))
