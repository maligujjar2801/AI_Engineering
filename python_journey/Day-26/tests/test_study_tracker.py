"""Unit tests for the study_tracker package."""

import unittest

from study_tracker.records import create_study_session
from study_tracker.reports import format_report


class TestCreateStudySession(unittest.TestCase):
    def test_creates_clean_record(self):
        session = create_study_session(
            "  Python modules  ",
            45,
            "  Practised imports  ",
        )
        self.assertEqual(
            session,
            {
                "topic": "Python modules",
                "minutes": 45,
                "note": "Practised imports",
            },
        )

    def test_rejects_empty_topic(self):
        with self.assertRaises(ValueError):
            create_study_session("   ", 30)

    def test_rejects_non_integer_minutes(self):
        with self.assertRaises(TypeError):
            create_study_session("Python", 30.5)

    def test_rejects_boolean_minutes(self):
        with self.assertRaises(TypeError):
            create_study_session("Python", True)

    def test_rejects_zero_or_negative_minutes(self):
        for minutes in (0, -5):
            with self.subTest(minutes=minutes):
                with self.assertRaises(ValueError):
                    create_study_session("Python", minutes)


class TestFormatReport(unittest.TestCase):
    def test_formats_sessions_and_total(self):
        sessions = [
            create_study_session("Python", 45, "Imports"),
            create_study_session("Math", 30),
        ]
        report = format_report(sessions)

        self.assertIn("1. Python — 45 minutes | Note: Imports", report)
        self.assertIn("2. Math — 30 minutes", report)
        self.assertIn("Sessions: 2", report)
        self.assertIn("Total study time: 75 minutes", report)

    def test_handles_empty_session_list(self):
        self.assertEqual(
            format_report([]),
            "No study sessions recorded yet.",
        )


if __name__ == "__main__":
    unittest.main()
