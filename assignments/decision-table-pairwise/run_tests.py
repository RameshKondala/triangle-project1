from triangle_classifier import classify_triangle

test_cases = [
    ("P1", 3, 4, 5, "Scalene"),
    ("P2", 5, 5, 5, "Equilateral"),
    ("P3", 5, 5, 8, "Isosceles"),
    ("P4", 1, 2, 10, "Invalid"),
    ("P5", 0, 4, 5, "Invalid"),
    ("P6", -1, 4, 5, "Invalid"),
    ("P7", 2, 2, 4, "Invalid"),
    ("P8", 100, 100, 150, "Isosceles"),
]

print("Decision Table / Pairwise Testing Results")
print("-" * 50)

for case_id, a, b, c, expected in test_cases:
    actual = classify_triangle(a, b, c)
    status = "PASS" if actual == expected else "FAIL"
    print(f"{case_id}: ({a}, {b}, {c}) -> expected={expected}, actual={actual} [{status}]")
