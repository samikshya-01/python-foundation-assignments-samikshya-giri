"""
Exercise 6: Student Score Dictionary
Store student scores in a dictionary and analyze them.
"""

student_scores = {
    "Anisha": 78,
    "Ravi": 55,
    "Maya": 92,
    "Sagar": 61,
    "Nima": 48
}

# 1. Print every student and score
print("All students and scores:")
for name, score in student_scores.items():
    print(f"{name}: {score}")

# 2. Dictionary comprehension - students who scored at least 60
passing_students = {name: score for name, score in student_scores.items() if score >= 60}
print("\nPassing students (60+):", passing_students)

# 3. Student with the highest score
top_student = max(student_scores, key=student_scores.get)
print(f"\nTop student: {top_student} ({student_scores[top_student]})")

# 4. Average score
average_score = sum(student_scores.values()) / len(student_scores)
print("Average score:", average_score)