n_lines=int(input())

#longest_intersection = {key: 0}
longest_intersection=set()
for _ in range(n_lines):

    first_set,second_set=input().split('-')

    first_set=first_set.split(',')
    second_set=second_set.split(',')

    first_start = int(first_set[0])
    first_end = int(first_set[1])

    second_start = int(second_set[0])
    second_end = int(second_set[1])

    first_set={i for i in range(first_start,first_end+1)}
    second_set={i for i in range(second_start,second_end+1)}

    current_intersection = first_set & second_set
    if len(current_intersection) > len(longest_intersection):

        longest_intersection=current_intersection


key_print=list(longest_intersection)

print(f"Longest intersection is {key_print} with length {len(longest_intersection)}")
