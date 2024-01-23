#!/usr/bin/env python3
""" Returns all students sorted by average score
"""
list_all = __import__('8-all').list_all


def top_students(mongo_collection):
    """ Top Students Function """
    students = list(list_all(mongo_collection))
    students_len = len(students)

    for student in students:
        topics = student.get("topics", None)

        total_score = 0.0
        topics_len = 0
        avaraaverageScore = 0.0

        if topics:
            topics_len = len(topics)

            for topic in topics:
                total_score += topic.get("score", 0)

        if total_score > 0:
            averageScore = (total_score) / (topics_len)

        student["averageScore"] = averageScore

    sort_students = sorted(
            students,
            key=lambda obj: obj['averageScore'], reverse=True
    )
    return (sort_students)
