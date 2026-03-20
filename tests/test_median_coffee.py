import csv

from main import read_data
from reports.registry import get_report


def test_read_data_from_multiple_files(tmp_path):
    file1 = tmp_path / "data1.csv"
    file2 = tmp_path / "data2.csv"

    rows1 = [
        {
            "student": "Алексей Смирнов",
            "date": "2024-06-01",
            "coffee_spent": "450",
            "sleep_hours": "4.5",
            "study_hours": "12",
            "mood": "норм",
            "exam": "Математика",
        }
    ]
    rows2 = [
        {
            "student": "Дарья Петрова",
            "date": "2024-06-01",
            "coffee_spent": "200",
            "sleep_hours": "7.0",
            "study_hours": "6",
            "mood": "отл",
            "exam": "Математика",
        }
    ]

    with open(file1, "w", encoding="utf-8", newline="") as f:
        writer = csv.DictWriter(f, fieldnames=rows1[0].keys())
        writer.writeheader()
        writer.writerows(rows1)

    with open(file2, "w", encoding="utf-8", newline="") as f:
        writer = csv.DictWriter(f, fieldnames=rows2[0].keys())
        writer.writeheader()
        writer.writerows(rows2)

    rows = read_data([str(file1), str(file2)])

    assert len(rows) == 2
    assert rows[0]["student"] == "Алексей Смирнов"
    assert rows[1]["student"] == "Дарья Петрова"


def test_get_report_returns_median_coffee_report():
    report = get_report("median-coffee")
    assert report.name == "median-coffee"


def test_get_report_raises_for_unknown_report():
    try:
        get_report("unknown-report")
        assert False, "Expected ValueError"
    except ValueError as error:
        assert "Неизвестный отчет" in str(error)