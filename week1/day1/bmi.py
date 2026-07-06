"""
BMI Calculator
Day 1 exercise - practicing input/output, type conversion, if/elif/else.
"""


height = float(input("what is your height? "))
weight = float(input("what is your weight? "))
bmi = weight/(height ** 2)
print(f"BMI: {bmi:.2f}")

if bmi< 18.5:
    print("偏瘦")
elif bmi< 25:
    print("正常")
elif bmi< 30:
    print("超重")
else:
    print("肥胖")