import student_data as data

"""
Contains the functions of the nine queries
"""

__author__ = "Debbie Johnson"
__version__ = "1.0"
_date__ = "2020.11.05"


def list_students(student_ids):
    """
    This function is used by other functions to display a list of student's id & names
    :param student_ids: The list of students to display their names
    :return:
    """
    for student_id in student_ids:
        print(student_id,
              data.students.get(student_id).get('firstName'),
              data.students.get(student_id).get('lastName')
        )


def student_information():
    """
    Display the student information
    :return:
    """
    print('=' * 80)
    print("Student Information")
    print('=' * 80)

    # for loop for displaying the data
    for student_id, student_info in data.students.items():
        print('ID:', student_id, student_info.get('firstName'), student_info.get('lastName'))

        print('\tGroups: ', end='')
        for group in student_info.get('groups'):
            print(group, end=', ')
        print()

        for subject, grades in data.grades.items():
            if student_id in grades:
                print('\t' + subject, grades.get(student_id))
        print()


def all_sports_list():
    """
    Displays all sports
    :return:
    """
    print('=' * 80)
    print("All Sports")
    print('=' * 80)

    all_sports = list()

    for sports in data.sports.values():
        # print('\t' + season + ':')
        all_sports.extend(sports)

    all_sports.sort()
    print(*all_sports, sep='\n')


# building the sports list
# --------------------------------------------------------------------------------------
# for key (season), value (season sports set) in 2D data.sports dict items
# 	append the current season’s sports set (value) to sports list by...
# 	converting the set to a list and using the extend function to append it...
# 	nested the list function inside the extend function to do this with one statement

# sort list

# for loop for displaying the list


def each_class_genders():
    """
    Displays the number of each gender in each class
    :return:
    """
    print('=' * 80)
    print("Each Class Genders")
    print('=' * 80)

    # --------------------------------------------------------------------------------------
    for class_name, class_grades in data.grades.items():
        m = 0
        f = 0

        for student_id, student_grades in class_grades.items():  # dict (value) items
            # get gender for the current student id (key) from data.students:
            gender = data.students.get(student_id).get('gender')
            # if to increment the correct gender counter
            if gender == 'M':
                m += 1
            else:
                f += 1

        # Math: Male = 1 Female = 3
        print(f'{class_name}: Male = {m} Female = {f}')


def sue_smith_class_list():
    """
    Displays Sue Smith's class list
    :return:
    """
    print('=' * 80)
    print("Sue Smith Class List")
    print('=' * 80)

    sue_smith_classes = list()
    first_name = 'empty'
    last_name = 'empty'

    # building the sue_smith_classes list
    # --------------------------------------------------------------------------------------
    # for key (student id), value (student info dict) in 2d data.students dict items
    for student_id, student_info in data.students.items():
        #  get first and last names from the student info dict (value)
        first_name = student_info.get('firstName')
        last_name = student_info.get('lastName')

        # if the first name = Sue and the last name = Smith
        if first_name == 'Sue' and last_name == 'Smith':
            # for key (class), value (class grades dict) in 2D data.grades dict items
            for class_name, class_grades in data.grades.items():
                # if student id (outer key) in class grades dict (value)
                if student_id in class_grades:
                    # add the class name (key) to sue_smith_classes list with the append method
                    sue_smith_classes.append(class_name)

    # sort the list
    sue_smith_classes.sort()

    # for loop for displaying sue_smith_classes list
    print(*sue_smith_classes, sep='\n')

def students_in_science_not_math():
    """
    Displays the students in the science class that aren't in the math class
    :return:
    """
    print('=' * 80)
    print("Students in Science but not in Math")
    print('=' * 80)

    science_not_math = list()

    # building science_not_math list
    # --------------------------------------------------------------------------------------
    # for key (student id) in 2d students dict keys
    for student_id in data.students:
        # if student id (key) in data.grades Science and student id (key) NOT in data.grades Math
        if student_id in data.grades.get('Science') and student_id not in data.grades.get('Math'):
            # append student id (key) to science_not_math list
            science_not_math.append(student_id)

    # sort the list
    science_not_math.sort()

    list_students(science_not_math)


def non_sports_groups():
    """
    Displays the groups that aren't sports
    :return:
    """
    print('=' * 80)
    print("NonSports Groups")
    print('=' * 80)

    all_sports = set()
    non_sports = list()


    # build the sports set
    # --------------------------------------------------------------------------------------
    # for key (season), value (season sports set) in 2D data.sports dict items
    for sports_set in data.sports.values():
        # append the season sports set to the sports set using update method (multiple values)
        all_sports.update(sports_set)

    # build the non_sports list
    # --------------------------------------------------------------------------------------
    # for key (student id), value (student info dict) in data.students dict items
    for student_id, student_info in data.students.items():
        # student groups = student info dict groups
        student_groups = student_info.get('groups')
        # whats left = student groups - sports set
        leftovers = student_groups - all_sports
        # if len whats left (not 0)
        if len(leftovers):
            # append *whats left to non_sports list using the * to convert the set to a tuple
            non_sports.extend(leftovers)

    # sort the non_sports list
    non_sports.sort()

    # for loop for displaying the non_sports list
    for student in non_sports:
        print(student)


def all_seasons_sports_students():
    """
    Displays the students in each seasons' sports
    :return:
    """
    print('=' * 80)
    print("All Seasons Sports Students")
    print('=' * 80)

    all_seasons = list()

    # build the all season list
    # --------------------------------------------------------------------------------------
    # for key (student id), value (student info) in 2d data.students items
    for student_id, student_info in data.students.items():
        # student groups = student info dict groups
        student_groups = student_info.get('groups')
        # if student groups & data.sports fall \
        if student_groups & data.sports.get('Fall') \
            and student_groups & data.sports.get('Winter') \
            and student_groups & data.sports.get('Spring') \
            and student_groups & data.sports.get('Summer'):
            # append student id (key) to all_seasons list
            all_seasons.append(student_id)

    # sort the list
    all_seasons.sort()

    list_students(all_seasons)


def student_classes_same_as_sue_smith():
    """
    Displays every student in the same classes as Sue Smith
    :return:
    """
    print('=' * 80)
    print("Students Classes same as Sue Smith")
    print('=' * 80)

    sue_smith_classes = set()
    same_as_sue_smith = list()
    students_classes = dict()

    # build both sue_smith_classes set, and students_classes dict
    # --------------------------------------------------------------------------------------
    # for key (student id), value (student info dict) in 2D data.students dict items
    for student_id, student_info in data.students.items():
        # student_classes = set()
        student_classes = set()
        # first_name = student info dict firstName
        first_name = student_info.get('firstName')
        # last_name = student info dict lastName
        last_name = student_info.get('lastName')
        # for key (class name), value (class grades dict) in 2D data.grades items
        for class_name, class_grades in data.grades.items():
            # if student id (outer key) in class grades dict
            if student_id in class_grades:
                # append class name (key) to student_classes set using add
                student_classes.add(class_name)
        # if name equals Sue Smith
        if first_name == 'Sue' and last_name == 'Smith':
            # set sue_smith_classes list to student_classes
            sue_smith_classes = student_classes
        # else
        else:
            # add the student id (outer key) students_classes value to student_classes
            students_classes[student_id] = student_classes

    # for loop for building same_as_sue_smith list
    # for key (student id), value (classes) in students_classes items
    for student_id, classes in students_classes.items():
        # if classes (value) equals sue_smith_classes
        if classes == sue_smith_classes:
            # append student id (key) to same_as_sue_smith list
            same_as_sue_smith.append(student_id)


    # sort same_as_sue_smith list
    same_as_sue_smith.sort()

    list_students(same_as_sue_smith)


def students_with_low_grades():
    """
    Displays all students with low grades
    :return:
    """
    print('=' * 80)
    print("Students with Low Grades")
    print('=' * 80)

    low_grades = set()

    # building low_grades set
    # --------------------------------------------------------------------------------------
    # for key (student id), value (student info) in 2D data.students items
    for student_id, student_info in data.students.items():
        # for key (class name), value (student grades dict) in data.grades items
        for class_name, student_grades in data.grades.items():
            # if student id (outer key) in student grades dict (value)
            if student_id in student_grades:
                # grade total = sum of student grades student_id (outer key) to grade total
                grade_total = sum(student_grades.get(student_id))
                # grade count = len of student grades student_id (outer key) to grade count
                grade_count = len(student_grades.get(student_id))
                # calculate average
                average = grade_total / grade_count
                if average < 70:
                    # add student id (outer key) to low_grades set
                    low_grades.add(student_id)

    # convert to list and sort
    low_grades = list(low_grades)
    low_grades.sort()

    list_students(low_grades)
