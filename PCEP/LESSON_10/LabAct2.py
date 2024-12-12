def recursive_sum(n):
    if n:
        return n + recursive_sum(n - 1)
    else :
        return 0
result = recursive_sum(10)
print(result)


