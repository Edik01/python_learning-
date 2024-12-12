from eralchemy import render_er

# Define the ERD schema for Dollege of the Cesert
erd_schema = """
[Students] {
    StudentID PK
    FirstName
    LastName
    DateOfBirth
    Email
    PhoneNumber
    Major
    EnrollmentDate
}
[Courses] {
    CourseID PK
    CourseName
    Credits
    Department
    Description
}
[Professors] {
    ProfessorID PK
    FirstName
    LastName
    Email
    PhoneNumber
    Department
}
[Classrooms] {
    ClassroomID PK
    RoomNumber
    BuildingName
    Capacity
}
[Enrollment] {
    EnrollmentID PK
    StudentID FK
    CourseID FK
    EnrollmentDate
    Grade
}
Students ||--o{ Enrollment
Courses ||--o{ Enrollment
Professors ||--o{ Courses
Classrooms ||--o{ Courses
"""

# Generate the ERD diagram
output_path = "/mnt/data/Dollege_of_the_Cesert_ERD.png"
render_er(erd_schema, output_path)
output_path
