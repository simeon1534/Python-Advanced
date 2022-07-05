inp = list(map(int, input().split(' ')))

negative_sum = sum(list(filter(lambda x: x < 0, inp)))
positive_sum = sum(list(filter(lambda x: x > 0, inp)))

print(negative_sum)
print(positive_sum)

if abs(negative_sum) > positive_sum:
    print("The negatives are stronger than the positives")
elif abs(negative_sum) < positive_sum:
    print("The positives are stronger than the negatives")
