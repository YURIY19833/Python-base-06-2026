from re import match


def calc(a,b):
    rectangle_result=a*b
    print(f"\nArea of a rectangle with a={a} and b={b} is {rectangle_result}")
    return rectangle_result

calc(10,45)
print('----------')

import  math
def calc2(r):
    result = math.pi *r *r
    print(f"Area of circle with r={r} is {result}")
    return result


calc2(5)
print('----------')

def calc3(r,h):
    cylinder_result = (2 * math.pi * r * r) +(2* math.pi * r* h)
    print(f"The cylinder with r={r} and h={h} has area={cylinder_result}")
    return cylinder_result

calc3(10.5, 8.7)
print('----------')

my_content = [11, 'sunny', 7, 'gold standard', 558, 25, 34, True]
def print_element_in_array(big_arr):
    for element in big_arr:
        print(element)
print_element_in_array(my_content)
print('----------')


arr_num = [22, 10, 5, 17, 30, 11, 9, 8, -50]
def sum_numbers_in_array(arr_num):
    result = sum(arr_num)
    return result
print("The sum of numbers in the array is", sum_numbers_in_array([22, 10, 5, 17, 30, 11, 9, 8, -50]))
