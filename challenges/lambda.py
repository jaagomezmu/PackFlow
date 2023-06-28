# Lambda demostration

calculate_rectangle_area = lambda length, width: length * width
calculate_triangle_area = lambda base, height: (base * height) / 2

import math
calculate_circle_area = lambda radius: math.pi * (radius ** 2)

# Main program
def main():
    print("Welcome to the Area Calculator!")

    while True:
        print("\nSelect a shape:")
        print("1. Rectangle")
        print("2. Triangle")
        print("3. Circle")
        print("4. Exit")

        choice = input("\nEnter your choice (1-4): ")

        if choice == "1":
            length = float(input("Enter the length of the rectangle: "))
            width = float(input("Enter the width of the rectangle: "))
            area = calculate_rectangle_area(length, width)
            print(f"The area of the rectangle is: {area}")
        elif choice == "2":
            base = float(input("Enter the base length of the triangle: "))
            height = float(input("Enter the height of the triangle: "))
            area = calculate_triangle_area(base, height)
            print(f"The area of the triangle is: {area}")
        elif choice == "3":
            radius = float(input("Enter the radius of the circle: "))
            area = calculate_circle_area(radius)
            print(f"The area of the circle is: {area}")
        elif choice == "4":
            print("Exiting...")
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == '__main__':
    main()
