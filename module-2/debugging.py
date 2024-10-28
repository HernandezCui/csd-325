def calculate_area(radius):
    import math

    return math.pi * (radius ** 2)

radius = float(input("Enter the radius: "))
area = calculate_area(radius)
print(f"The area of the circle is: {area}")