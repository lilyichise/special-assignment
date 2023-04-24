import os.path

# Loops as long as user wants to continue
while True:
    # Required variables
    totalGrade = 0
    count = 0
    passed = 0
    failed = 0

    # Prints the greeting message
    print("Course Grades Summary Report ...\n")

    while True:
        # Takes file name from the user
        fileName = input("Enter name of course file: ")
        if not os.path.isfile(fileName):
            print("Error: file does not exist.")
            continue  # continue with the loop
        else:
            break

    # Prints the header of the report
    print()
    print("-" * 60)
    print("{0:>41}".format("Broward College Grades Summary"))
    print("-" * 60)

    # Reads the entire file lines into a list
    with open(fileName, "r") as f:
        content = f.readlines()

        # Check if the file has at least 3 lines
        if len(content) < 3:
            print("Error: invalid file format.")
            continue  # continue loop

        # Reads course name, professor name and term values
        courseName = content[0].replace("\n", "")
        professor = content[1].replace("\n", "")
        term = content[2].replace("\n", "")

        # Displays course name, professor and term values
        print()
        print(courseName)
        print("Professor: {0:<32} Term:{1}".format(professor, term))

        # Displays student name and grade header
        print("{0:<32}{1}".format("\nStudent Name", "Grade"))
        print("-"*40)

        # Loops through every line further
        for i in range(3, len(content), 2):
            # Check if there are enough lines left
            if i+1 >= len(content):
                print("Error: invalid file format.")
                break  # exit loop

            # Reads student name and grade
            name = content[i].replace("\n", "")
            grade = int(content[i+1].replace("\n", ""))

            # Calculates total of grades,number of students,
            # number of students passed and number of students failed
            totalGrade += grade
            count += 1
            if grade < 60:
                failed += 1
            else:
                passed += 1

            # Displays name and grade
            print("{0:<32}{1}".format(name, grade))

        # Calculates average grade and passing percentage
        averageGrade = totalGrade/count
        passingPercentage = (passed / (passed + failed))*100

        # Displays output
        print("\nStudents' Performance")
        print("-"*40)
        print("Passed: {0:<25}Failed: {1}".format(passed, failed))
        print("Passing Percent: {0:.0f}%".format(passingPercentage))
        print("Average Grade: {0:.0f}".format(averageGrade))

    # Reads whether user wants to continue or not
    choice = input("Would you like to process another file (y/n)? ")
    if choice.lower() == 'n':
        break
