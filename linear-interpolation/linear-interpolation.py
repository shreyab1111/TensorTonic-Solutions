def linear_interpolation(values):
    """
    Fill missing (None) values using linear interpolation.
    """
    # Write code here
    n = len(values)
    for i in range(n):
        if values[i] is None:
            j = i
            while j < n and values[j] is None:
                j += 1

            if i > 0 and j < n:
                left = values[i-1]
                right = values[j]
                step = (right - left) / (j - (i-1))

                for k in range(i, j):
                    values[k] = left + step * (k - (i-1))

            i = j

    return values