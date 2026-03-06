def grades_to_gpa(grades):
  
    # 4.0 GPA scale mapping
    grade_map = {
        "A+": 4.0, "A": 4.0, "A-": 3.7,
        "B+": 3.3, "B": 3.0, "B-": 2.7,
        "C+": 2.3, "C": 2.0, "C-": 1.7,
        "D+": 1.3, "D": 1.0, "D-": 0.7,
        "F": 0.0
    }

    # Print entire gpa map
    print("Grade to GPA")
    for letter, points in grade_map.items():
        print(f"{letter}: {points}")

    gpa_values = []

    # Use a loop to handle each grade input
    for grade in grades:
        
        # Retrieve gpa, default 0.0
        points = grade_map.get(new_grade, 0.0)
        gpa_values.append(points)
        
        print(f"Grade: {new_grade} GPA: {points}")

    return gpa_values
