# Lists for Storage Student Data and Attendance

students = [[569873624,"9864215963","Kasun ","Weerasinghe","2007/02/14","Kuliyapitiya","0765968423","A","Kurunegala"],
            [697412385,"6542198753","Nadun ","Gunarathne ","2005/08/20","Anuradhapura","0743875213","C","Colombo"],
            [124698536,"5416872316","Pramud","Kulaweera  ","2004/11/05","Nikawaratiya","0713697874","A","Kurunegala"]]
attendance = []

# Figure 1:- Main Menu

running = True
while running :
    print("_" * 153)
    print()
    print("IIT Campus".center(75))
    print()
    print("Main Menu".center(77))
    print()
    print("1) Enroll a new student")
    print("2) View details of a student")
    print("3) View details of all students")
    print("4) Update student details")
    print("5) Mark attendance")
    print("6) View attendance")
    print("7) Exit")
    print()
    
    choice = input("                                                              Your Choice : ")
    
    # Figure 2:- Enroll a New Student
    
    if (choice == "1") :  
        student = []
        print("_" * 153)
        print()
        print("IIT Campus".center(75))
        print()
        print("Enroll a New Student".center(75))
        print()
        student_id = (input("Student ID        : "))
        while len(student_id)!= 9 :
            student_id = (input ("Invalid ID,Enter 9 Digits : "))
        nic = (input("NIC               : "))
        while len(nic)!= 10 :
            nic = (input ("Invalid NIC,Enter 10 Characters : "))
        first_name = input("First Name        : ")
        while len(first_name)> 10 :
            first_name = input ("Invalid First Name,Enter 10 Characters : ")
        last_name = input("Last Name         : ")
        while len(last_name)> 15 :
            last_name = input ("Invalid Last Name,Enter 15 Characters : ")
        birth_date = input("Birth Date        : ")
        address = input("Permanent Address : ")
        while len(address)> 15 :
            address = input ("Invalid Address,Enter 15 Characters : ")
        phone = input("Phone Number      : ")
        while len(phone)!=10 :
            phone = input ("Invalid Phone Number,Enter 10 Characters : ")
        tutorial_group = input("Tutorial Group    : ")
        centre = input("Centre            : ")

        student.append(int(student_id))
        student.append(nic)
        student.append(first_name)
        student.append(last_name)
        student.append(birth_date)
        student.append(address)
        student.append(phone)
        student.append(tutorial_group)
        student.append(centre)

        print()
        confirm = input("Do you want to save the details (Yes/No)? : ").lower()
        print()
        if (confirm == "yes") :
            students.append(student)
            print()
            print("Student Details Saved Successfully.".center(75))
        else :
            print()
            print("Student Details not Saved.".center(75))
            
    # Figure 3:- View Details of a Student
    
    elif (choice == "2") :
        while True :
            print("_" * 153)
            print()
            print("IIT Campus".center(75))
            print()
            print("View Details of a Student".center(75))
            print()
            student_id = int(input("Enter Student ID : "))
        
            for student in students :
                if (student[0] == int(student_id)) :
                    print("NIC : ", student[1])
                    print("Phone Number : ", student[6])
                    print("First Name : ", student[2])
                    print("Last Name : ", student[3])
                    print("Tutorial Group : ", student[7])
                    print("Centre : ", student[8])
                    break
            else :
                    print("Student not Found".center(75))

            print()


            save = input("Do you Want to View Another Student's Details (Yes/No)? : ").lower()
            if (save == "yes") :
                continue
            if (save == "no") :
                print()
                print("Canceled View Another Student's Details".center(75))
                break
            else :
                print()
                print("Invalid Choice,Try Again".center(75))
                break
            
    # Figure 4:- View Details of All the Students
    
    elif (choice == "3") :
        print("_" * 153)
        print()
        print("IIT Campus".center(75))
        print()
        print("View Details of All Students".center(75))
        print()

        branch = input("Branch Name : ")
        
        if (students) :
            print("|NIC|             |Student ID|         |First Name|         |Last Name|        |Tutorial Group|")
            for student in students :
                if (branch.lower() in student[8].lower() or not branch) :
                    print(f"{student[1]}         {student[0]}             {student[2]}              {student[3]}              {student[7]}")
        print()
        confirm = input("Do you want to update student details (Yes/No)? : ").lower()
        if (confirm == "yes") :
            print()
            print("Please Select Choice = 4 to Update Student Details".center(75))
            continue
        if (confirm == "no") :
            continue
        else :
            print()
            print("Invalid Choice,Try Again".center(75))
            continue
            
            
        
                    
    # Figure 5:- Update Student Details
    
    elif (choice == "4") :
        print("_" * 153)
        print()
        print("IIT Campus".center(75))
        print()
        print("Update Student Details".center(75))
        print()
        student_id = input("Enter Student ID  : ")
        
        for student in students :
            if (student[0] == int(student_id)) :

                new_nic = input("New NIC         : ") 
                while len(new_nic)!= 10 :
                    if (new_nic == "") :
                        new_nic = student[1]
                        break
                    new_nic = input ("Invalid NIC,Enter 10 Characters : ")
                
                new_first_name = input("New First Name    : ")
                while len(new_first_name)>10 :
                    if (new_first_name == "") :
                        new_first_name = student[2]
                        break
                    new_first_name = input ("Invalid First name,Enter less than 10 Characters : ")
                
                new_last_name = input("New Last Name     : ")
                while len(new_last_name)>15 :
                    if (new_last_name == "") :
                        new_last_name = student[3]
                        break
                    new_last_name = input ("Invalid Last name,Enter less than 15 Characters : ")

                new_birth_date = input("New Birth date    : ")
                if (new_birth_date == "") :
                    new_birth_date = student[4]

                new_address = input("New Address       : ")
                while len(new_address)> 15 :
                    if (new_address == "") :
                        new_address = student[5]
                        break
                    new_address = input ("Invalid Address,Enter 15 Characters : ")
                

                new_phone_number = input("New phone number  : ")
                while len(new_phone_number)!=10 :
                    if new_phone_number == "":
                        new_phone_number = student[6]
                        break
                    new_phone_number = input ("Invalid phone number,Enter 10 digits : ")

                print()
                confirm = input("Do you want to save the details (Yes/No)? : ").lower()
                if (confirm == "yes") :
                    student[1] = new_nic
                    student[2] = new_first_name
                    student[3] = new_last_name
                    student[4] = new_birth_date
                    student[5] = new_address
                    student[6] = new_phone_number
                    print()
                    print("Student Details Updated Successfully.".center(75))
                else :
                    print()
                    print("Student Details not Saved.".center(75))
                break
        else :
            print()
            print("Student not Found".center(75))
            
    # Figure 6:- Mark Attendance
    
    elif (choice == "5") :
        print("_" * 153)
        print()
        print("IIT Campus".center(75))
        print()
        print("Mark Attendance".center(75))
        print()
        centre = input("Enter Centre        : ")
        tutorial_group = input("Enter Tutorial Group : ")
        date = input("Enter Date          : ")
        group_attendance = []
        for student in students :
            if (student[7] == tutorial_group and student[8].lower() == centre.lower()) :
                print()
                status = input(f"Student ID = {student[0]} - Present/Absent? : ").lower()
                group_attendance.append([student[0],date,status])
        if len(group_attendance)==0 :
            print("Invalid centre or tutorial group.... No student found")
        print()
        confirm = input("Do you Want to Save the Attendance Details (Yes/No)? : ").lower()
        if (confirm == "yes") :
            print()
            attendance.extend(group_attendance)
            print("Action Completed.".center(75))
        else :
            print()
            print("Action Not Completed.".center(75))
            
    # Figure 7:- View Attendance
    
    elif (choice == "6") :
        print("_" * 153)
        print()
        print("IIT Campus".center(75))
        print()
        print("View Attendance".center(75))
        print()
        student_id = int(input("Student ID : "))
        from_date = input("From Date  : ")
        to_date = input("To Date   : ")
        print()
        print("Date       | Present/Absent")
        for record in attendance:
            if (record[0] == student_id and (from_date) <= (record[1]) and (record[1]) <= (to_date)) :
                print(record[1], "       |" , record[2])
        print()
        return_main = input("Do you want to Direct to the Main Menu (Yes/No)? : ").lower()
        if (return_main == "no") :
            print()
            print("...Exited...".center(75))
            break
        
    # Exit from Main Menu
    
    elif (choice == "7") :
        print("_" * 153)
        print()
        print("...Exited...".center(75))
        running = False

    # Invalid Choice
    
    else :
        print("Invalid Choice. Please Try Again.".center(75))
