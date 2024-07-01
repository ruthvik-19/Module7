
# dictionary for room numbers
rooms = {
    "CSC101": "3004",
    "CSC102": "4501",
    "CSC103": "6755",
    "NET110": "1244",
    "COM241": "1411"
}

# dictionary for course instructors
instructors = {
    "CSC101": "Haynes",
    "CSC102": "Alvarado",
    "CSC103": "Rich",
    "NET110": "Burke",
    "COM241": "Lee"
}

# dictionary for course timings
timings = {
    "CSC101": "8:00 A.M.",
    "CSC102": "9:00 A.M.",
    "CSC103": "10:00 A.M.",
    "NET110": "11:00 A.M.",
    "COM241": "1:00 P.M."
}

# function to print course info
def print_info(course_number):
    # if course_number is found in rooms dictionary
    if course_number in rooms:
        # set each key-value as a new variable
        room = rooms[course_number]
        instructor = instructors[course_number]
        time = timings[course_number]
        
        # print course values
        print("Course Number: {}".format(course_number))
        print("Room Number: {}".format(room))
        print("Instructor: {}".format(instructor))
        print("Meeting Time: {}".format(time))
    else:
        # input validation
        print("Course number {} not found.".format(course_number))

# main - takes user input and calls print_info function
def main():
    course_number = input("Enter a course number: ")
    print_info(course_number)

# runs program
if __name__ == "__main__":
    main()
