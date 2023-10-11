def distance(m, f, count):
    initial_m = m  # Store the initial distance
    while m < initial_m + 50:
        f = m / 100 * f
        m = m + f
        count += 1
    return count