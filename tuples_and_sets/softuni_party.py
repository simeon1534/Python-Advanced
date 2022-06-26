invited_guests = int(input())

set_invited = set()

for _ in range(invited_guests):
    reservation_num = input()
    set_invited.add(reservation_num)

who_came=set()

guest_who_came=input()
while not guest_who_came  =='END':
    who_came.add(guest_who_came)
    guest_who_came = input()

who_didnt_come=sorted(set_invited ^ who_came)
print(len(who_didnt_come))
for el in who_didnt_come:
    print(el)