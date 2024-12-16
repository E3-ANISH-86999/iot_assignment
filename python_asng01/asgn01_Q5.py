sub1 = int(input("Enter marks of sub1: "))
sub2 = int(input("Enter marks of sub2: "))
sub3 = int(input("Enter marks of sub3: "))

def avg_fn(p1:int, p2:int, p3:int):
    result = (p1 + p2 + p3) / 3
    return result

avg_marks = avg_fn(sub1, sub2, sub3) 

if avg_marks >= 90:
    print("Grade obtained: 'A'")
elif avg_marks >= 80:
    print("Grade obtained: 'B'")
elif avg_marks >= 70:
    print("Grade obtained: 'C'")
elif avg_marks >= 60:
    print("Grade obtained: 'D'")
else:
    print("Grade obtained: 'F'")


