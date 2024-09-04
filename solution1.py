import operator

my_dict = {
    'apple': 5,
    'banana': 2,
    'orange': 8,
    'grape': 3,
    'pear': 6
}
print(my_dict)
#sorted(dictionary,(index)value which will be sorted upon,revers for ascending or descending)
sorted_d = dict(sorted(my_dict.items(),key=operator.itemgetter(1),reverse=False))
print(sorted_d)