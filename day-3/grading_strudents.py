
# n = 4

# grades = 73 67 38 33


def gradingStudents(grades):
    result = []
    for grade in grades:

        if grade < 38:
            result.append(grade)
        else:
            next_multiple = ((grade // 5) + 1)* 5
            if next_multiple - grade < 3:
                result.append(next_multiple)
            else:
                result.append(grade)
    
    return result



if __name__ == "__main__":

    grades_count = int(input("Enter array length: ").strip())

    grades = []

    for _ in range(grades_count):
        grades_item = int(input().strip())
        grades.append(grades_item)

    result = gradingStudents(grades)

    print(result)