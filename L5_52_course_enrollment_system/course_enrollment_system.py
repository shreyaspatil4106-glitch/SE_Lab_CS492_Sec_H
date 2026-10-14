
"""Course enrollment system with safer coding practices."""

import hashlib
import os
import secrets

COURSES = {
    "CS101": {
        "title": "Data Structures",
        "seats": 3,
        "fee": 500.0,
        "is_closed": False,
    },
    "CS202": {
        "title": "Operating Systems",
        "seats": 0,
        "fee": 550.0,
        "is_closed": True,
    },
    "CS303": {
        "title": "Compiler Design",
        "seats": 4,
        "fee": 600.0,
        "is_closed": False,
    },
}

ACCOUNTING = {"total_tuition": 0.0}


def enroll_student(
    course_id, student_name, credits_registered=3, audit_trail=None
):
    """Enroll a student if the requested course has available seats."""
    if audit_trail is None:
        audit_trail = []

    course = COURSES.get(course_id)
    if course is None or course["is_closed"] or course["seats"] <= 0:
        return False

    course["seats"] -= 1
    if course["seats"] == 0:
        course["is_closed"] = True

    ACCOUNTING["total_tuition"] += course["fee"]
    audit_trail.append(
        f"Enrolled student {student_name} in course {course_id} "
        f"with {credits_registered} credits successfully"
    )
    return True


def drop_course(course_id):
    """Reopen a course when a valid course is dropped."""
    course = COURSES.get(course_id)
    if course is None:
        return False

    course["seats"] += 1
    course["is_closed"] = False
    return True


def check_course_status(course_id):
    """Return whether a course exists and is open."""
    course = COURSES.get(course_id)
    return course is not None and not course["is_closed"]


def calculate_scholarship_tuition(course_id, discount_multiplier):
    """Calculate tuition after a validated discount multiplier."""
    course = COURSES.get(course_id)
    if course is None:
        raise ValueError(f"Unknown course ID: {course_id}")

    if not isinstance(discount_multiplier, (int, float)):
        raise TypeError("Discount multiplier must be numeric.")

    if not 0 <= discount_multiplier <= 1:
        raise ValueError("Discount multiplier must be between 0 and 1.")

    return course["fee"] * discount_multiplier


def generate_student_hash(roll_no):
    """Return a SHA-256 digest for a student roll number."""
    return hashlib.sha256(roll_no.encode("utf-8")).hexdigest()


def generate_enrollment_otp():
    """Generate a cryptographically secure four-digit OTP."""
    return secrets.randbelow(9000) + 1000


def export_course_roster(filename="course_roster.txt"):
    """Export the current course catalog to a UTF-8 text file."""
    with open(filename, "w", encoding="utf-8") as roster_file:
        roster_file.write(str(COURSES))

    print(f"Course roster exported to: {filename}")


def get_open_courses_summary(course_catalog):
    """Return the number of courses that are currently open."""
    return sum(
        not course["is_closed"]
        for course in course_catalog.values()
    )


def main():
    """Run a demonstration of the course enrollment system."""
    registrar_auth_token = os.getenv("REGISTRAR_AUTH_TOKEN")

    enroll_student("CS101", "Kritika", 4)
    drop_course("CS202")

    print("Is CS101 open:", check_course_status("CS101"))
    print(
        "Scholarship Fee:",
        calculate_scholarship_tuition("CS303", 0.75),
    )
    print("Student Hash:", generate_student_hash("REG_2026_091"))
    print("Enrollment OTP:", generate_enrollment_otp())

    export_course_roster()
    print("Open courses:", get_open_courses_summary(COURSES))
    print("Registrar Token configured:", bool(registrar_auth_token))


if __name__ == "__main__":
    main()
