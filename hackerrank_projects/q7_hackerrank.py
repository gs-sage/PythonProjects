# creating an empty list to hold values
new_list = []

for i in range(int(input())):
    name = input()
    score = float(input())
    new_list.append([name, score])

print(new_list)

for new_list_element in new_list:
    for inner_new_list_element in new_list_element:
        print(inner_new_list_element)
        if(isinstance(inner_new_list_element, float)):
            print("****************")
            print(inner_new_list_element)

# for j in range(len(new_list)):
#     for ele in new_list:
#         for inner_el in ele:
#             if(isinstance(inner_el, float)):

# the program is not yet complete