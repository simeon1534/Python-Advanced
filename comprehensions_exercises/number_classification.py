nums = input().split(', ')

print(f"Positive: {', '.join([num for num in nums if int(num) >= 0])}")

print(f"Negative: {', '.join([num for num in nums if int(num) < 0])}")

print(f"Even: {', '.join([num for num in nums if int(num) % 2 == 0])}")

print(f"Odd: {', '.join([num for num in nums if int(num) % 2 != 0])}")

