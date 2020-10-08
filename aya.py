def helloworld():
    cool_numbers = [102, 117, 100, 103, 101, 33]
    cool_string = ""
    for n in cool_numbers:
        cool_string = cool_string + chr(n)
    print(cool_string)

helloworld()