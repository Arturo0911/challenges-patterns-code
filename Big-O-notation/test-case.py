#!/usr/bin/python3



try:
    side_1 = int(input("side1: "))
    side_2 = int(input("side2: "))
    side_3 = int(input("side3: "))

    equilateral = (side_1 == side_2 == side_3)

    isosceles = (side_1 == side_2 != side_3)  \
            or (side_2 == side_1 != side_3)\
            or (side_3 == side_1 != side_2) \
            or (side_2 == side_3 != side_1)

    if side_1 <0 or side_2 < 0 or side_3 <0:
        raise ValueError("The measures can't be lesser than 0")
    if equilateral:
        print("triange it's equilateral")
    elif isosceles:
        print("triangle is isosceles")
    else:
        print("triangle is scalene")
except Exception as e:
    raise ValueError("The values should be integers or floating ")
    exit(1)
except KeyboardInterrupt:
    exit(1)

