from vpython import *
import math
from fractions import Fraction

# Fraction for sphere
fr1 = Fraction(4, 3)

# Menu for math_shape_calculator
def math_shape_calculator():
    print("\nThis is the math 3D shape calculator")
    print('   1) Cylinder')
    print('   2) Cube')
    print('   3) Sphere')
    print('   4) Trapezoidal Prism')
    print('   5) Cone')
    print('   6) Rectangular Prism')
    print('   7) Pyramid')
    print('   8) Quit\n')
    print('Choose an option regarding the menu')

# Function for the cylinder
def calu_cylinder():
    keep_going = True
    while keep_going:
        print('\nCylinder Options:')
        print(' 1) Surface Area')
        print(' 2) Volume ')
        print(' 3) Return to the main menu')
        choice = int(input("Choose an option: "))
        if choice == 1:
            radius = float(input("Enter the radius of the cylinder: "))
            height = float(input("Enter the height of the cylinder: "))
            surface_area = 2 * math.pi * radius * (radius + height)
            print(f"The surface area of the cylinder is:  {surface_area:.2f}")
            cylinder(pos=vec(0, 0, 0), axis=vec(3, 0, 0), color=color.yellow) # VPython 3D Cylinder
        elif choice == 2:
            radius = float(input("Enter the radius of the cylinder: "))
            height = float(input("Enter the height of the cylinder: "))
            volume_cylinder = math.pi * (radius**2) * height
            print(f'The volume of the cylinder is: {volume_cylinder:.2f}')
            cylinder(pos=vec(0, 0, 0), axis=vec(3, 0, 0), color=color.yellow) # VPython 3D Cylinder
        elif choice ==3:
            keep_going = False
        else:
            print('Invalid choice, please choose 1, 2, or 3.')

# Function for the cube
def calu_cube():
    keep_going = True
    while keep_going:
        print('\nCube Options:')
        print(' 1) Surface Area')
        print(' 2) Volume')
        print(' 3) Return to the main menu')
        choice = int(input("Choose an option: "))
        if choice == 1:
            side = float(input("Enter the side length of the cube: "))
            surface_area = 6 * (side ** 2)
            print(f"The surface area of the cube is: {surface_area:.2f}")
            box(pos=vec(0, 0, 0), length=1, height=1, width=0.5, color=color.cyan)  # VPython 3D cube
        elif choice == 2:
            side = float(input("Enter the side length of the cube: "))
            volume_cube = side ** 3
            print(f'The volume of the cube is: {volume_cube:.2f}')
            box(pos=vec(0, 0, 0), length=1, height=1, width=0.52, color=color.cyan)  # VPython 3D cube
        elif choice == 3:
            keep_going = False
        else:
            print('Invalid choice, please choose 1, 2, or 3.')

# Function for the sphere
def calu_sphere():
    keep_going = True
    while keep_going:
        print('\nSphere Options:')
        print(' 1) Surface Area')
        print(' 2) Volume')
        print(' 3) Return to the main menu')
        choice = int(input("Choose an option: "))
        if choice == 1:
            radius = float(input("Enter the radius of the sphere: "))
            surface_area = 4 * math.pi * (radius**2)
            print(f"The surface area of the sphere is: {surface_area:.2f}")
            sphere(pos=vec(0, 0, 0), radius=2, color=color.cyan) #VPython 3D Sphere
        elif choice == 2:
            radius = float(input("Enter the radius of the sphere: "))
            volume_sphere = float(fr1) * math.pi * (radius**3)
            print(f'The volume of the sphere is: {volume_sphere:.2f}')
            sphere(pos=vec(0, 0, 0), radius=2, color=color.white) #VPython 3D Sphere
        elif choice == 3:
            keep_going = False
        else:
            print('Invalid choice, please choose 1, 2, or 3.')

# Function for the trapezoidal prism
def calu_trapezoid_prism():
    keep_going = True
    while keep_going:
        print('\nTrapezoidal Prism Options:')
        print(' 1) Surface Area')
        print(' 2) Volume')
        print(' 3) Return to the main menu')
        choice = int(input('Choose an option: '))
        if choice == 1:
            a = float(input("Enter the parallel side length a: "))
            b = float(input("Enter the parallel side length b: "))
            h = float(input("Enter the height of the trapezoidal prism: "))
            surface_area = (1/2) * h * (a + b)
            print(f" The surface area of the trapezoidal prism is: {surface_area:.2f}")
            # VPython Trapezoidal Prism (approximated)
            z = shapes.trapezoid(pos=[3, -3], width=3, height=1, top=1)
            trapezoid_1 = extrusion(path=[vector(0, 0, 0), vector(0, 0, 3)], shape=z, color=color.cyan)

        elif choice == 2:
            a = float(input("Enter the parallel side of length a: "))
            b = float(input("Enter the parallel side of length b: "))
            h = float(input("Enter the height of the trapezoidal prism: "))
            l = float(input("Enter the length of the trapezoidal prism: "))
            volume = ((1/2) * h * (a + b)) * l
            print(f"The volume of the trapezoidal prism is: {volume:.2f}")
            # VPython Trapezoidal Prism (approximated)
            z = shapes.trapezoid(pos=[3, -3], width=3, height=1, top=1)
            trapezoid_1 = extrusion(path=[vector(0, 0, 0), vector(0, 0, 3)], shape=z, color=color.cyan)
        elif choice == 3:
            keep_going = False
        else:
            print('Invalid option. Please choose option 1, 2, or 3.')

# Function for the cone
def calu_cone():
    keep_going = True
    while keep_going:
        print('\nCone Options:')
        print(' 1) Surface Area')
        print(' 2) Volume')
        print(' 3) Return to the main menu')
        choice = int(input('Choose an option: '))
        if choice == 1:
            radius = float(input("Enter the radius of the cone: "))
            height = float(input("Enter the height of the cone: "))
            surface_area = math.pi * radius * (radius + math.sqrt((radius**2) + (height**2)))
            print(f'The surface area of the cone is {surface_area:.2f}')
            cone(pos=vec(5, 2, 0), axis=vec(3, 0, 0), radius=1, color=color.red)  # VPython 3D cone
        elif choice == 2:
            radius = float(input("Enter the radius of the cone: "))
            height = float(input("Enter the height of the cone: "))
            volume = (1/3) * math.pi * (radius**2) * height
            print(f"The volume of the cone is {volume:.2f}")
            cone(pos=vec(5, 2, 0), axis=vec(3, 0, 0), radius=1, color=color.orange)  # VPython 3D cone
        elif choice == 3:
            keep_going = False
        else:
            print("Invalid option. Choose option 1 , 2 or 3")

# Function for the rectangular prism
def calu_rectangular_prism():
    keep_going = True
    while keep_going:
        print('\nRectangular Prism Options:')
        print(' 1) Surface Area')
        print(' 2) Volume')
        print(' 3) Return to the main menu')
        choice = int(input("Choose an option: "))
        if choice == 1:
            height = float(input("Enter the height of the rectangular prism: "))
            length = float(input("Enter the length of the rectangular prism: "))
            width = float(input("Enter the width of the rectangular prism: "))
            surface_area = 2 * ((length * width) + (length * height) + (width * height))
            print(f'The surface area of the rectangular prism is: {surface_area:.2f}')
            box(pos=vec(4, 4, 6), length=3, height=3, width=4, color=color.cyan)  # VPython 3D rectangular prism
        elif choice == 2:
            height = float(input("Enter the height of the rectangular prism: "))
            length = float(input("Enter the length of the rectangular prism: "))
            width = float(input("Enter the width of the rectangular prism: "))
            volume = length * width * height
            print(f'The volume of the rectangular prism is: {volume:.2f}')
            box(pos=vec(4, 4, 6), length=4, height=6, width=4, color=color.cyan)  # VPython 3D rectangular prism
        elif choice == 3:
            keep_going = False
        else:
            print("Invalid option. Choose 1, 2, or 3.")

# Function for the pyramid
def calu_pyramid():
    keep_going = True
    while keep_going:
        print("\nPyramid Options:")
        print(" 1) Surface Area")
        print(" 2) Volume")
        print(" 3) Return to the main menu")
        choice = int(input("Choose an option: "))
        if choice == 1:
            lateral_sa = float(input("Enter the lateral surface area of the pyramid: "))
            base_area = float(input("Enter the base area of the pyramid: "))
            surface_area = base_area + lateral_sa
            print(f"The surface area of the pyramid is: {surface_area:.2f}")
            pyramid(base=vector(4, 4, 0), height=5, color=color.purple)  # VPython 3D pyramid
        if choice == 2:
            height = float(input("Enter the height of the pyramid: "))
            base_area = float(input("Enter the base area of the pyramid: "))
            volume = (1/3) * base_area * height
            print(f"The volume of the pyramid is: {volume:.2f}")
            pyramid(base=vector(4, 4, 0), height=5, color=color.purple)  # VPython 3D pyramid
        elif choice == 3:
            keep_going = False
        else:
            print("Invalid choice. Please choose 1, 2, or 3.")

# Main loop
quit_program = False
while not quit_program:
    math_shape_calculator()
    try:
        choice = int(input('Enter choice: '))
        if choice == 8:
            print('Goodbye')
            quit_program = True
        elif choice == 1:
            calu_cylinder()
        elif choice == 2:
            calu_cube()
        elif choice == 3:
            calu_sphere()
        elif choice == 4:
            calu_trapezoid_prism()
        elif choice == 5:
            calu_cone()
        elif choice == 6:
            calu_rectangular_prism()
        elif choice == 7:
            calu_pyramid()
        else:
            print("Invalid choice. Please choose a valid option.")
    except ValueError:
        print("Invalid input. Please enter a number.")
