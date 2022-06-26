def read_matrix():
    rows = int(input())
    cols = rows
    matrix = [
        [n for n in list(input())]
        for _ in range(rows)
    ]
    return matrix


def valid_pattern(matrix, i, j):
    pattern = []

    if i - 1 >= 0 and j - 2 >= 0:
        pattern.append(matrix[i - 1][j - 2])

    if i - 2 >= 0 and j - 1 >= 0:
        pattern.append(matrix[i - 2][j - 1])

    if i + 1 < len(matrix) and j - 2 >= 0:
        pattern.append(matrix[i + 1][j - 2])

    if i + 2 < len(matrix) and j - 1 >= 0:
        pattern.append(matrix[i + 2][j - 1])

    if i - 1 >= 0 and j + 2 < len(matrix):
        pattern.append(matrix[i - 1][j + 2])

    if i - 2 >= 0 and j + 1 < len(matrix):
        pattern.append(matrix[i - 2][j + 1])

    if i + 1 < len(matrix) and j + 2 < len(matrix):
        pattern.append(matrix[i + 1][j + 2])

    if i + 2 < len(matrix) and j + 1 < len(matrix):
        pattern.append(matrix[i + 2][j + 1])

    return pattern


def dictionary_create(matrix):
    dictionary = {}
    for i in range(len(matrix)):
        for j in range(len(matrix[0])):
            if matrix[i][j] == 'K':
                dictionary[f'K{i}{j}'] = 0
    return dictionary


def ordering_dict(dictionary):
    sort_dict = {}
    sort_list = sorted(dictionary.items(), key=lambda x: x[1], reverse=True)
    for key, value in sort_list:
        sort_dict[key] = value
    return sort_dict


def ordering_tuple(dictionary):
    sort_list = sorted(dictionary.items(), key=lambda x: x[1], reverse=True)
    return sort_list


def knight_possible_hits(matrix, dictionary):
    for i in range(len(matrix)):
        for j in range(len(matrix[0])):
            if matrix[i][j] == 'K':
                current_knight = matrix[i][j]

                for ptrn_num in range(len(valid_pattern(matrix, i, j))):

                    if valid_pattern(matrix, i, j)[ptrn_num] == 'K':
                        dictionary[f'K{i}{j}'] += 1

    return dictionary


def knight_actual_hits(matrix, ordered_dictionary, ordered_tuple):  # matrica , tuple ,dictionary
    total_hits = 0
    for key, value in ordered_tuple:
        k, i, j = list(key)
        i = int(i)
        j = int(j)
        for ptrn_num in range(len(valid_pattern(matrix, i, j))):

            if valid_pattern(matrix, i, j)[ptrn_num] == 'K':
                key_to_remove = f"K{str(i)}{str(j)}"
                try:
                    ordered_dictionary.pop(key_to_remove)
                    matrix[i][j] = '0'
                    print(matrix)
                    total_hits += 1
                    break
                except KeyError:
                    total_hits -= 1
                    exit()
    return total_hits


matrix = read_matrix()
dictionary = dictionary_create(matrix)

possible_attacks_per_knight = knight_possible_hits(matrix, dictionary)
ordered_possible_attacks_dict = ordering_dict(possible_attacks_per_knight)
ordered_tuple = ordering_tuple(dictionary)

actual_attack = knight_actual_hits(matrix, ordered_possible_attacks_dict, ordered_tuple)

print(actual_attack)
print(matrix)

# 1.Creating Matrix --->  read(matrix)
# 2.Saving in dictionary coordinates of K's with value 0 by default  --->   dictionary_create(matrix)
# 3.Ordering dictionary so the knight with more posssible actions start first ---> ordering_dict(dictionary_create(matrix))
# 4.all posible patterns completed
