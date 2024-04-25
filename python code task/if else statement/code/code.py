name = input("Enter your name: ")
gpa = float(input("Enter your GPA: "))
sat_score = int(input("Enter your SAT score: "))

if gpa >= 4.0:
    print(f"Congratulations {name}! You qualify for a full scholarship.")
elif gpa >= 3.5 and sat_score >= 1500:  
    print(f"{name}, you qualify for a half scholarship.")
else:
    print(f"Sorry {name}, you do not qualify for a scholarship at this time.")
