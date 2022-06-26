n_lines=int(input())
odd_set=set()
even_set=set()
for i in range(1,n_lines+1):

    sum_ascii=sum(map(ord,input()))
    current_result=sum_ascii // i

    if current_result % 2 == 0:
        even_set.add(current_result)
    else:
        odd_set.add(current_result)

if sum(odd_set)==sum(even_set):
    print(*(odd_set | even_set),sep=', ')
elif sum(odd_set)>sum(even_set):
    print(*(odd_set - even_set),sep=', ')
else:
    print(*(odd_set ^ even_set),sep=', ')
