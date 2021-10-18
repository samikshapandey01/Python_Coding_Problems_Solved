inp_filename=input("Enter grade filename :")

try:
    with open(inp_filename,'r') as f:
        studentcount=0
        total_grades=0
        if f.read().strip() == '' :
            raise EOFError("Empty Grades File")
        f.seek(0,0)
        grade=f.readline().split(',')[1]
        max_grade=float(grade)       
        min_grade=max_grade
        f.seek(0,0)
        for stu_rec in f:
            studentcount += 1
            grades=float(stu_rec.split(',')[1])
            student_id=int(stu_rec.split(',')[0])
            total_grades += grades
            if grades > max_grade:
                max_grade=grades
            elif grades < min_grade:
                min_grade=grades

    str1=f"# of students in file: {studentcount}\n"
    str2=f"Average of grades: {(total_grades/studentcount):.2f}\n"
    str3=f"Highest grade: {max_grade}\n"
    str4=f"Lowest grade: {min_grade}\n"
    f = open('results.txt', 'w')
    f.write(str1)
    f.write(str2)
    f.write(str3)
    f.write(str4)
    f.close()
    print(str1,end='') 
    print(str2,end='')
    print(str3,end='')
    print(str4)

except FileNotFoundError:
    print("Invalid File/File does not exists")
except EOFError as e:
    print(e)
except IndexError:
    print("Invalid Grade") 
except ValueError :
    print("Grade/student ID is not numeric")