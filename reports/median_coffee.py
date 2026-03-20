from collections import defaultdict
from statistics import median
from typing import Any

from reports.base import BaseReport


class MedianCoffeeReport(BaseReport):
    name = "median-coffee"

    def build(self, rows: list[dict[str, Any]]) -> tuple[list[str], list[list[Any]]]:
        student_coffee_spent: dict[str, list[float]] = defaultdict(list)

        for row in rows:
            student_name = row["student"]
            coffee_spent = float(row["coffee_spent"])
            student_coffee_spent[student_name].append(coffee_spent)

        result = []
        for student_name, spends in student_coffee_spent.items():
            result.append([student_name, median(spends)])

        result.sort(key=lambda item: item[1], reverse=True)

        headers = ["student", "median_coffee_spent"]
        return headers, result