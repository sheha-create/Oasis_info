


from datetime import datetime


def calculate_bmi(weight, height):
    return weight / (height ** 2)


def get_bmi_category(bmi):
    if bmi < 18.5:
        return "Underweight"
    elif bmi < 25:
        return "Normal weight"
    elif bmi < 30:
        return "Overweight"
    else:
        return "Obese"


def get_positive_float(prompt):
    while True:
        try:
            value = float(input(prompt))
            if value <= 0:
                print("Please enter a value greater than zero.")
            else:
                return value
        except ValueError:
            print("Invalid input. Enter a numeric value.")


def display_bmi_chart(bmi):
    print("\nBMI RANGE CHART")
    print("-------------------------------")
    print("Underweight : < 18.5")
    print("Normal : 18.5 - 24.9")
    print("Overweight : 25 - 29.9")
    print("Obese : >= 30")
    print("-------------------------------")

    scale = int(bmi)
    if scale > 40:
        scale = 40

    print("BMI Value Visualization:")
    print("[" + "#" * scale + " " * (40 - scale) + "]")
    print(f"Your BMI: {bmi:.2f}\n")


def save_to_file(name, weight, height, bmi, category):
    with open("bmi_records.txt", "a") as file:
        file.write("Date: " + datetime.now().strftime("%Y-%m-%d %H:%M:%S") + "\n")
        file.write(f"Name: {name}\n")
        file.write(f"Weight: {weight} kg\n")
        file.write(f"Height: {height} m\n")
        file.write(f"BMI: {bmi:.2f}\n")
        file.write(f"Category: {category}\n")
        file.write("-" * 30 + "\n")


def main():
    print("\n=== BMI Calculator ===\n")

    while True:
        name = input("Enter your name: ").strip()
        weight = get_positive_float("Enter weight (kg): ")
        height = get_positive_float("Enter height (m): ")

        bmi = calculate_bmi(weight, height)
        category = get_bmi_category(bmi)

        print("\n--- BMI RESULT ---")
        print(f"Name: {name}")
        print(f"BMI: {bmi:.2f}")
        print(f"Health Category: {category}")

        display_bmi_chart(bmi)
        save_to_file(name, weight, height, bmi, category)

        choice = input("Do you want to calculate BMI for another person? (yes/no): ").lower()
        if choice != "yes":
            print("\nResults saved to 'bmi_records.txt'")
            print("Thank you for using the BMI Calculator.")
            break


if __name__ == "__main__":
    main()
