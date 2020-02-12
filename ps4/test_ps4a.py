import ps4a

test_1 = ps4a.get_permutations("abc")

print(test_1)


first_letter = 'a'
remaining_perm = ['bc', 'cb']

        ## insert letter into each position of every word and return the modified list
perm_list = []
        
for perm in remaining_perm:
    temp_perm = []
    for idx in range(len(perm)+1):
        print(idx)
        new_perm = perm[:idx] +first_letter + perm[idx:]
        temp_perm.append(new_perm)
    perm_list.extend(temp_perm)
print(perm_list)