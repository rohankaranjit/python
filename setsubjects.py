subjects = [
    "python", "java", "C++", "python", "javascript",
    "java", "python", "java", "C++", "C"
]

# Use a set to get unique subjects
unique_subjects = set(subjects)

print("Unique subjects:", unique_subjects)
print("Number of classrooms needed:", len(unique_subjects))
