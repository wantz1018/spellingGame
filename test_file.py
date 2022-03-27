def persistence(n):
    # your code
    if n < 10:
        return 0
    elif n < 100:
        ans = (n % 10) * (n - n % 10 * 10)
        print(ans)
    elif n < 1000:
        ans = n % 100 * (n / 10 - n % 100 * 10) * (n - n / 10)
        print(ans)
    if ans < 10:
        print(ans)
        return ans
    else:
        persistence(ans)


persistence(999)
