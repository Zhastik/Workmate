from reports.median_coffee import MedianCoffeeReport


def test_median_coffee_report_build():
    rows = [
        {"student": "Алексей Смирнов", "coffee_spent": "450"},
        {"student": "Алексей Смирнов", "coffee_spent": "500"},
        {"student": "Алексей Смирнов", "coffee_spent": "550"},
        {"student": "Дарья Петрова", "coffee_spent": "200"},
        {"student": "Дарья Петрова", "coffee_spent": "250"},
        {"student": "Дарья Петрова", "coffee_spent": "300"},
        {"student": "Иван Кузнецов", "coffee_spent": "600"},
        {"student": "Иван Кузнецов", "coffee_spent": "650"},
        {"student": "Иван Кузнецов", "coffee_spent": "700"},
    ]

    report = MedianCoffeeReport()
    headers, table_data = report.build(rows)

    assert headers == ["student", "median_coffee_spent"]
    assert table_data == [
        ["Иван Кузнецов", 650.0],
        ["Алексей Смирнов", 500.0],
        ["Дарья Петрова", 250.0],
    ]