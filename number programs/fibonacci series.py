def generate_fibonacci_series(num_terms):
    fibonacci_series = []
    a, b = 0, 1

    for _ in range(num_terms):
        fibonacci_series.append(a)

        a, b = b, a + b

    return fibonacci_series


num_terms = 100
fibonacci_series = generate_fibonacci_series(num_terms)
print(f"the fibonacci series  are:{fibonacci_series}")
