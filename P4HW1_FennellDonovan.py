# CTI-110
# P4HW1 - Score List
# Donovan Fennell 
# 24MARCH2022
#

def main():
    total = 0
    grade_list = []

    num = int(input("How many scores do you want to enter? "))
    print()
    for i in range (0, num):
        grade = float(input("Enter score #" + str(i+1)+": "))
        while grade < 0 or grade > 100:
            print()
            print("INVALID score entered!!!!")
            print("Score should be between 0 and 100")
            grade = float(input("Enter score #" + str(i+1)+" again: "))
        grade_list.append(grade)
    
    lowest = min(grade_list)
    grade_list.remove(lowest)
    average = sum(grade_list) / (num - 1)
    
    if average >= 90:
        grade = "A"
    elif average >= 80:
        grade = "B"
    elif average >= 70:
        grade = "C"
    elif average >= 60:
        grade = "D"
    else:
        grade = "F"
    
    print()
    print("--------------Results-----------")
    print("Lowest Score  : ", lowest)
    print("Modified List : ", grade_list)
    print("Scores Average: ", average)
    print("Grade         : ", grade)
    print("--------------------------------")




main()
