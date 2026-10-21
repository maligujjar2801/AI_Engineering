def build_report(title,*score , student = "Unknown", **metadata):
    average_score = sum(score) / len(score) if score else 0
    
    report = {
        "title": title,
        "student": student,
        "average_score": f"{average_score:.2f}",
        "scores": score,
        "metadata": metadata
    }
    return report # Returns a report dictionary with title, student name, scores, and metadata.)
print(build_report("Math Test", 85, 90, 78, student="Alice", teacher="Mr. Smith"))