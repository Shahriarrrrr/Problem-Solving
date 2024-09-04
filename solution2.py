my_dict = {
    0: 10,
    1: 20
}

#Both ways are correct:

# my_dict[2] = 30
# print(my_dict)

my_dict.update({2: 30})
print(my_dict)
