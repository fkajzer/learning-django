x = [1, 2, 3, 4]

out = []
#for num in x:
#    out.append(num**2)
#print(out)

#same as
out = [num**2 for num in x]
print("foor loop shorter")
print(out)


#lamda expression
my_list = [1, 2, 3, 4, 5, 6 , 7, 8]

#def even_bool(num):
#    return num%2 == 0

#evens = filter(even_bool, my_list)

#print("even numbers filter")
#print(evens)

print("even numbers filter with lambda")
print(filter(lambda num:num%2 == 0, my_list))


SUITE = 'H D S C'.split()
RANKS = '2 3 4 5 6 7 8 9 10 J Q K A'.split()

#allcards = []
#for r in Ranks:
#   for s in Suite:
#       allcards.append((s,r))
allcards = [(s,r) for s in SUITE for r in RANKS ]

print(allcards)
