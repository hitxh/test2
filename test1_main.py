from itertools import chain


def recoverSecret(triplets):
    'triplets is a list of triplets from the secrent string. Return the string.'
    #   print(triplets)
    row_num = len(triplets)
    column_num = len(triplets[0])  # 3

    column_one = [triplets[x][0] for x in range(row_num)]
    column_two = [triplets[x][1] for x in range(row_num)]
    column_thr = [triplets[x][2] for x in range(row_num)]

    triplets_one = list(chain.from_iterable(triplets))
    #   print(triplets_one)
    print(set(triplets_one))
    output = ''
    word_value = []
    while column_one != list('0' * len(column_one)):
        for i in set(triplets_one):
            if i in column_one and i not in column_two and i not in column_thr:
                word_value.append(i)
                while i in column_one:
                    char_index = column_one.index(i)
                    column_one[char_index] = column_two[char_index]
                    column_two[char_index] = column_thr[char_index]
                    column_thr[char_index] = '0'
    return ''.join(word_value)

triplets = [
  ['t','u','p'],
  ['w','h','i'],
  ['t','s','u'],
  ['a','t','s'],
  ['h','a','p'],
  ['t','i','s'],
  ['w','h','s']
]

print(recoverSecret(triplets))