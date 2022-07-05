#string=input().split(' ')

#for word in string:
 #   if len(word)%2==0:
   #     print(word)

print('\n'.join([word for word in input().split(' ') if len(word) % 2 == 0]))