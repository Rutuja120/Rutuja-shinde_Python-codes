class Student:
    def Student_Info(stud,rollno,name,course,m1,m2,m3):
        stud.rollno = rollno
        stud.name = name
        stud.course = course
        stud.m1 = m1
        stud.m2 = m2
        stud.m3 = m3

rollno = int(input("Enter RollNo of Student: "))
name = str(input("Enter Name of Student : "))
course = str(input("Enter Course of student : "))
m1 = int(input("Enter Marks1 of student : "))
m2 = int(input("Enter Marks2 of student : "))
m3= int(input("Enter Marks3 of student : "))
total = m1+m2+m3
avg = total/3

s1 = Student()
s1.Student_Info(rollno,name,course,m1,m2,m3)
print("Roll No : -> ",s1.rollno)
print("Name :-> ",s1.name)
print("Course :-> ",s1.course)
print("Marks1 :-> ",s1.m1)
print("Marks2 :-> ",s1.m2)
print("Marks3:-> ",s1.m3 )
print("TOtal ",total)
print("Average ", avg)