def print_digits_reversed(n):
    if not isinstance(n, int):
        raise TypeError("Входное значение должно быть целым числом.")
    if n <= 0:
        raise ValueError("Входное значение должно быть положительным числом.")
def _print_digits_reversed(n):
        if n < 10:
            print(n, end=" ")
            return
        else:
            print(n % 10, end=" ")
            _print_digits_reversed(n // 10)
print_digits_reversed(n)
print() 
