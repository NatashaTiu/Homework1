def  check_isIntercalary(year):
    aa = year
    if aa % 400 == 0:
        return True

    elif aa % 100 == 0:
        return False

    elif aa % 4 == 0 and not aa % 100 == 0:
        return True

    else:
        return False


def check_is_triangle(first, second, third):
    listOfNum = [first, second, third]
    listofNumNew = sorted(listOfNum)
    if listofNumNew[-1] >= listofNumNew[0]+listofNumNew[1]:
        answer = "False"
    else:
        answer = "True"
    return answer


a = 3
b = 4
c = 5


def check_type_triangle(first, second, third):
    list_of_num = [first, second, third]
#    print(list_of_num)
    listof_num_new = sorted(list_of_num)
    if listof_num_new[-1] >= listof_num_new[0]+listof_num_new[1]:
        answer = "Not a triangle"
    else:
        if first == second == third:
            answer = "Equilateral triangle."
        elif first == second or first == third or second == third:
            answer = "Isosceles triangle."
        else:
            answer = "Versatile triangle."

    return answer


#answer_TypeTriangle = check_type_triangle(a, b, c)

#print(answer_TypeTriangle)



#answer_isTriangle = check_is_triangle(3, 5, 9)

#print(answer_isTriangle)