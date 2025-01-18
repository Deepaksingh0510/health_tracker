import matplotlib.pyplot as plt
import csv

def details():
    print("Please provide your details:")
    name = input("Name: ")
    age = int(input("Age (in years): "))
    gender = input("Gender (male/female): ").lower()
    weight = float(input("Weight (in kg): "))
    height = float(input("Height (in cm): "))
    return name, age, gender, weight, height

def calculate_bmi(weight, height):
    height_in_meters = height / 100
    bmi = weight / (height_in_meters**2)
    return bmi

def bmr(gender, height, weight, age):
    if gender == "male":
        basal_metabolic_rate = round(66 + (13.7 * weight) + (5 * height) - (6.8 * age))
    else:
        basal_metabolic_rate = round(655 + (9.6 * weight) + (1.8 * height) - (4.7 * age))
    return basal_metabolic_rate

def calories_req_underweight(bmr):
    calories_req = bmr * 1.55
    calories = calories_req + 500
    return calories

def calories_req_fit(bmr):
    calories = bmr * 1.55
    return calories

def save_user_data(name, age, gender, weight, height, bmi, bmr_value, calories):
    with open('user_data.csv', mode='a', newline='') as file:
        writer = csv.writer(file)
        writer.writerow([name, age, gender, weight, height, bmi, bmr_value, calories])
    print("User data saved successfully.")

def plot_nutritional_requirements(protein, carbs, fats):
    labels = ['Protein', 'Carbohydrates', 'Fats']
    sizes = [protein, carbs, fats]
    colors = ['gold', 'lightcoral', 'lightskyblue']
    explode = (0.1, 0, 0)  # explode 1st slice

    plt.figure(figsize=(8, 6))
    plt.pie(sizes, explode=explode, labels=labels, colors=colors,
            autopct='%1.1f%%', shadow=True, startangle=140)
    plt.axis('equal')  # Equal aspect ratio ensures that pie chart is circular.
    plt.title('Daily Nutritional Requirements')
    plt.show()

def goal(bmi, bmr, gender, weight, height, age):
    print("\n--- Health Assessment ---")
    print(f"Hello {name}! Here are your health details:")
    print(f"Age: {age} years")
    print(f"Gender: {gender}")
    print(f"Weight: {weight} kg")
    print(f"Height: {height} cm")
    
    print("\n--- Body Mass Index (BMI) ---")
    print(f"Your BMI is: {bmi:.2f}")
    
    if bmi < 18.5:
        print("\n--- Health Status ---")
        print("You're Underweight! You need to gain some weight.")
        calories = calories_req_underweight(bmr)
        print(f"Suggested daily calorie intake to gain weight: {calories:.0f} calories")
        weight_goal = float(input("\nEnter your goal weight (in kg): "))
        print(f"Your new weight goal of {weight_goal} kg is set successfully!")
        protein = weight_goal * 2
        carbs = weight_goal * 5
        fats = weight_goal * 1
        print("\n--- Daily Nutritional Requirements ---")
        print(f"Protein requirement: {protein + 14:.0f} grams")
        print(f"Carbohydrates requirement: {carbs + 47:.0f} grams")
        print(f"Fats requirement: {fats + 23:.0f} grams")
        save_user_data(name, age, gender, weight, height, bmi, bmr, calories)
        plot_nutritional_requirements(protein, carbs, fats)
        print("\n--- Fitness Plan ---")
        print("Here's a workout plan to gain weight.")
        
    elif 18.5 <= bmi < 25:
        print("\n--- Health Status ---")
        print("You are Fit!")
        calories = calories_req_fit(bmr)
        print(f"Suggested daily calorie intake to maintain weight: {calories:.0f} calories")
        print("\n--- Fitness Options ---")
        print("1. Gain muscles at the same weight")
        print("2. Gain muscles at a higher weight")
        print("3. Exit")
        choice = int(input("\nEnter your choice: "))
        
        if choice == 1:
            print("\n--- Daily Nutritional Requirements ---")
            protein = weight * 2
            carbs = weight * 5
            fats = weight * 1
            print(f"Protein requirement: {protein:.0f} grams")
            print(f"Carbohydrates requirement: {carbs:.0f} grams")
            print(f"Fats requirement: {fats:.0f} grams")
            save_user_data(name, age, gender, weight, height, bmi, bmr, calories)
            plot_nutritional_requirements(protein, carbs, fats)
            print("\n--- Fitness Plan ---")
            print("Here's a workout plan to gain muscles at the same weight.")
            
        elif choice == 2:
            weight_goal = float(input("\nEnter your desired weight (in kg): "))
            print(f"Your new weight goal of {weight_goal} kg is set successfully!")
            protein = weight_goal * 2
            carbs = weight_goal * 5
            fats = weight_goal * 1
            print("\n--- Daily Nutritional Requirements ---")
            print(f"Protein requirement: {protein + 14:.0f} grams")
            print(f"Carbohydrates requirement: {carbs + 47:.0f} grams")
            print(f"Fats requirement: {fats + 23:.0f} grams")
            save_user_data(name, age, gender, weight, height, bmi, bmr, calories)
            plot_nutritional_requirements(protein, carbs, fats)
            print("\n--- Fitness Plan ---")
            print("Here's a workout plan to gain muscles at a higher weight.")
            
        elif choice == 3:
            print("\nExiting...")

    else:
        print("\n--- Health Status ---")
        print("Oops! You're overweight. You need to do some workout.")
        weight_goal = float(input("\nEnter your goal weight (in kg): "))
        calories = calories_req_underweight(bmr)
        print(f"Suggested daily calorie intake to lose weight: {calories:.0f} calories")
        protein = weight_goal * 2
        carbs = weight_goal * 5
        fats = weight_goal * 1
        print("\n--- Daily Nutritional Requirements ---")
        print(f"Protein requirement: {protein:.0f} grams")
        print(f"Carbohydrates requirement: {carbs:.0f} grams")
        print(f"Fats requirement: {fats:.0f} grams")
        save_user_data(name, age, gender, weight, height, bmi, bmr, calories)
        plot_nutritional_requirements(protein, carbs, fats)
        print("\n--- Fitness Plan ---")
        print("Here's a workout plan to lose weight.")

# Main program flow
name, age, gender, weight, height = details()
bmi = calculate_bmi(weight, height)
bmr_value = bmr(gender, height, weight, age)
goal(bmi, bmr_value, gender, weight, height, age)
import matplotlib.pyplot as plt
import csv

def details():
    print("Please provide your details:")
    name = input("Name: ")
    age = int(input("Age (in years): "))
    gender = input("Gender (male/female): ").lower()
    weight = float(input("Weight (in kg): "))
    height = float(input("Height (in cm): "))
    return name, age, gender, weight, height

def calculate_bmi(weight, height):
    height_in_meters = height / 100
    bmi = weight / (height_in_meters**2)
    return bmi

def bmr(gender, height, weight, age):
    if gender == "male":
        basal_metabolic_rate = round(66 + (13.7 * weight) + (5 * height) - (6.8 * age))
    else:
        basal_metabolic_rate = round(655 + (9.6 * weight) + (1.8 * height) - (4.7 * age))
    return basal_metabolic_rate

def calories_req_underweight(bmr):
    calories_req = bmr * 1.55
    calories = calories_req + 500
    return calories

def calories_req_fit(bmr):
    calories = bmr * 1.55
    return calories

def save_user_data(name, age, gender, weight, height, bmi, bmr_value, calories):
    with open('user_data.csv', mode='a', newline='') as file:
        writer = csv.writer(file)
        writer.writerow([name, age, gender, weight, height, bmi, bmr_value, calories])
    print("User data saved successfully.")

def plot_nutritional_requirements(protein, carbs, fats):
    labels = ['Protein', 'Carbohydrates', 'Fats']
    sizes = [protein, carbs, fats]
    colors = ['gold', 'lightcoral', 'lightskyblue']
    explode = (0.1, 0, 0)  # explode 1st slice

    plt.figure(figsize=(8, 6))
    plt.pie(sizes, explode=explode, labels=labels, colors=colors,
            autopct='%1.1f%%', shadow=True, startangle=140)
    plt.axis('equal')  # Equal aspect ratio ensures that pie chart is circular.
    plt.title('Daily Nutritional Requirements')
    plt.show()

def goal(bmi, bmr, gender, weight, height, age):
    print("\n--- Health Assessment ---")
    print(f"Hello {name}! Here are your health details:")
    print(f"Age: {age} years")
    print(f"Gender: {gender}")
    print(f"Weight: {weight} kg")
    print(f"Height: {height} cm")
    
    print("\n--- Body Mass Index (BMI) ---")
    print(f"Your BMI is: {bmi:.2f}")
    
    if bmi < 18.5:
        print("\n--- Health Status ---")
        print("You're Underweight! You need to gain some weight.")
        calories = calories_req_underweight(bmr)
        print(f"Suggested daily calorie intake to gain weight: {calories:.0f} calories")
        weight_goal = float(input("\nEnter your goal weight (in kg): "))
        print(f"Your new weight goal of {weight_goal} kg is set successfully!")
        protein = weight_goal * 2
        carbs = weight_goal * 5
        fats = weight_goal * 1
        print("\n--- Daily Nutritional Requirements ---")
        print(f"Protein requirement: {protein + 14:.0f} grams")
        print(f"Carbohydrates requirement: {carbs + 47:.0f} grams")
        print(f"Fats requirement: {fats + 23:.0f} grams")
        save_user_data(name, age, gender, weight, height, bmi, bmr, calories)
        plot_nutritional_requirements(protein, carbs, fats)
        print("\n--- Fitness Plan ---")
        print("Here's a workout plan to gain weight.")
        
    elif 18.5 <= bmi < 25:
        print("\n--- Health Status ---")
        print("You are Fit!")
        calories = calories_req_fit(bmr)
        print(f"Suggested daily calorie intake to maintain weight: {calories:.0f} calories")
        print("\n--- Fitness Options ---")
        print("1. Gain muscles at the same weight")
        print("2. Gain muscles at a higher weight")
        print("3. Exit")
        choice = int(input("\nEnter your choice: "))
        
        if choice == 1:
            print("\n--- Daily Nutritional Requirements ---")
            protein = weight * 2
            carbs = weight * 5
            fats = weight * 1
            print(f"Protein requirement: {protein:.0f} grams")
            print(f"Carbohydrates requirement: {carbs:.0f} grams")
            print(f"Fats requirement: {fats:.0f} grams")
            save_user_data(name, age, gender, weight, height, bmi, bmr, calories)
            plot_nutritional_requirements(protein, carbs, fats)
            print("\n--- Fitness Plan ---")
            print("Here's a workout plan to gain muscles at the same weight.")
            
        elif choice == 2:
            weight_goal = float(input("\nEnter your desired weight (in kg): "))
            print(f"Your new weight goal of {weight_goal} kg is set successfully!")
            protein = weight_goal * 2
            carbs = weight_goal * 5
            fats = weight_goal * 1
            print("\n--- Daily Nutritional Requirements ---")
            print(f"Protein requirement: {protein + 14:.0f} grams")
            print(f"Carbohydrates requirement: {carbs + 47:.0f} grams")
            print(f"Fats requirement: {fats + 23:.0f} grams")
            save_user_data(name, age, gender, weight, height, bmi, bmr, calories)
            plot_nutritional_requirements(protein, carbs, fats)
            print("\n--- Fitness Plan ---")
            print("Here's a workout plan to gain muscles at a higher weight.")
            
        elif choice == 3:
            print("\nExiting...")

    else:
        print("\n--- Health Status ---")
        print("Oops! You're overweight. You need to do some workout.")
        weight_goal = float(input("\nEnter your goal weight (in kg): "))
        calories = calories_req_underweight(bmr)
        print(f"Suggested daily calorie intake to lose weight: {calories:.0f} calories")
        protein = weight_goal * 2
        carbs = weight_goal * 5
        fats = weight_goal * 1
        print("\n--- Daily Nutritional Requirements ---")
        print(f"Protein requirement: {protein:.0f} grams")
        print(f"Carbohydrates requirement: {carbs:.0f} grams")
        print(f"Fats requirement: {fats:.0f} grams")
        save_user_data(name, age, gender, weight, height, bmi, bmr, calories)
        plot_nutritional_requirements(protein, carbs, fats)
        print("\n--- Fitness Plan ---")
        print("Here's a workout plan to lose weight.")

# Main program flow
name, age, gender, weight, height = details()
bmi = calculate_bmi(weight, height)
bmr_value = bmr(gender, height, weight, age)
goal(bmi, bmr_value, gender, weight, height, age)
