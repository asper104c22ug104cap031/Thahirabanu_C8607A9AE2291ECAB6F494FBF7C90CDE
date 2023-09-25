def sort_students(student_list):
    sorted_students = sorted(student_list, key=lambda student: student.cgpa, reverse=True)
    return sorted_student