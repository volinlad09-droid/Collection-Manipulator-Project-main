# Student Data Organizer
# Project: Collection Manipulator


students_list = []

students_dict = {}

unique_subjects = set()

# Welcome Message
print("========================================")
print("  Welcome to the Student Data Organizer!")
print("========================================")

while True:
    # options
    print("\nSelect an option:")
    print("1. Add Student")
    print("2. Display All Students")
    print("3. Update Student Information")
    print("4. Delete Student")
    print("5. Display Subjects Offered")
    print("6. Exit")

    choice = input("Enter your choice: ")

    # OPTION 1: ADD STUDENT
    if choice == "1":
        print("\nEnter student details:")
        
        student_id = int(input("Student ID: "))
        name = input("Name: ")
        
        age = int(input("Age: "))
        grade = input("Grade: ")
        dob = input("Date of Birth (YYYY-MM-DD): ")
        
        subjects_input = input("Subjects (comma-separated): ")
        
        raw_subjects = subjects_input.split(",")
        subjects_list = []
        for sub in raw_subjects:
            clean_sub = sub.strip()
            subjects_list.append(clean_sub)
            # Set: add to unique subjects set (ensures no duplicates)
            unique_subjects.add(clean_sub)

        id_dob_tuple = (student_id, dob)

        student_data = {
            "id": student_id,
            "name": name,
            "age": age,
            "grade": grade,
            "dob": id_dob_tuple[1],
            "subjects": subjects_list
        }

        students_list.append(student_data)
        students_dict[student_id] = student_data

        print("\nStudent added successfully!")

    # OPTION 2: DISPLAY ALL STUDENTS
    elif choice == "2":
        if len(students_list) == 0:
            print("\nNo student records found.")
        else:
            print("\n--- Display All Students ---")
            for student in students_list:
                subjects_str = ", ".join(student["subjects"])
                
                output = "Student ID: {} | Name: {} | Age: {} | Grade: {} | Subjects: {}".format(
                    student["id"], student["name"], student["age"], student["grade"], subjects_str
                )
                print(output)

    # OPTION 3: UPDATE STUDENT INFORMATION
    elif choice == "3":
        search_id = int(input("\nEnter Student ID to update: "))
        found = False

        for student in students_list:
            if student["id"] == search_id:
                found = True
                print("Student found: " + student["name"])
                print("What would you like to update?")
                print("1. Age")
                print("2. Subjects")
                
                update_choice = input("Enter choice (1/2): ")
                
                if update_choice == "1":
                    new_age = int(input("Enter new age: "))
                    # Mutability: updating list and dictionary value
                    student["age"] = new_age
                    students_dict[search_id]["age"] = new_age
                    print("Age updated successfully!")
                
                elif update_choice == "2":
                    new_subs_input = input("Enter new subjects (comma-separated): ")
                    new_subs_raw = new_subs_input.split(",")
                    new_subs_list = []
                    for sub in new_subs_raw:
                        clean_sub = sub.strip()
                        new_subs_list.append(clean_sub)
                        unique_subjects.add(clean_sub)
                    
                    student["subjects"] = new_subs_list
                    students_dict[search_id]["subjects"] = new_subs_list
                    print("Subjects updated successfully!")
                else:
                    print("Invalid option selected.")
                break

        if not found:
            print("Student ID not found.")

    # OPTION 4: DELETE STUDENT
    elif choice == "4":
        delete_id = int(input("\nEnter Student ID to delete: "))
        found_index = -1

        for i in range(len(students_list)):
            if students_list[i]["id"] == delete_id:
                found_index = i
                break

        if found_index != -1:
            del students_list[found_index]
            
            if delete_id in students_dict:
                del students_dict[delete_id]
                
            print(f"Student with ID {delete_id} deleted successfully!")
        else:
            print("Student ID not found.")

    # OPTION 5: DISPLAY SUBJECTS OFFERED
    elif choice == "5":
        print("\n--- Unique Subjects Offered ---")
        if len(unique_subjects) == 0:
            print("No subjects added yet.")
        else:
            for sub in sorted(unique_subjects):
                print(f"- {sub}")

    # OPTION 6: EXIT
    elif choice == "6":
        # Exit message
        print("\nThank you for using the Student Data Organizer. Goodbye!")
        break

    else:
        print("Invalid choice! Please select an option between 1 and 6.")
