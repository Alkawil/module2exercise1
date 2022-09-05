def get_combined_dict(my_dict_1,my_dict_2):
    my_dict_3 ={}
    for x in my_dict_2:
        for y in my_dict_1:
            if x == y and x not in my_dict_3:
                my_dict_3[x] = my_dict_2[x] + my_dict_1[y]
    return my_dict_3
my_dict_1 = {'a': 5, 'b': 12, 'c': 3, 'd': 9}
my_dict_2 = {'b': 4, 'c': 9, 'd': 10, 'e': 16}
combined_dict = get_combined_dict(my_dict_1, my_dict_2)
print(combined_dict) 
     



