# Lists and Dictionaries

# last_alpha_lst = ['x', 'y', 'z']
# print(last_alpha_lst)
# print(last_alpha_lst[0])
# print(last_alpha_lst[1])
# print(last_alpha_lst[2])

# ltr_lst = list('abc')
# print(ltr_lst)
# print(ltr_lst[0])
# print(ltr_lst[1])
# print(ltr_lst[2])

oldest_people = [122, 119, 117, 117, 116]  # Source: Wikipedia.org

nth_person = int(input('Enter N (1-5): '))

if (nth_person >= 1) and (nth_person <= 5):
    if nth_person == 1:
        print(
            f'The {nth_person}st oldest person lived {oldest_people[nth_person-1]} years')
    if nth_person == 2:
        print(
            f'The {nth_person}nd oldest person lived {oldest_people[nth_person-1]} years')
    if nth_person == 3:
        print(
            f'The {nth_person}rd oldest person lived {oldest_people[nth_person-1]} years')
    if nth_person == 4 or nth_person == 5:
        print(
            f'The {nth_person}th oldest person lived {oldest_people[nth_person-1]} years')
