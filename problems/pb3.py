def youngest_student(students):
    min = 1
    y= ''
    for name in students:
        if min>students[name]:
            min= students[name]
            y=name

    return y


