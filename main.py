import argparse
import csv
import sys
from typing import Any

from tabulate import tabulate

from reports.registry import get_report


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(
        description="Формирование отчетов по данным подготовки студентов к экзаменам"
    )
    parser.add_argument(
        "--files",
        nargs="+",
        required=True,
        help="Список CSV-файлов с данными",
    )
    parser.add_argument(
        "--report",
        required=True,
        help="Название отчета (например, median-coffee)",
    )
    return parser.parse_args()


def read_data(file_paths: list[str]) -> list[dict[str, Any]]:
    rows: list[dict[str, Any]] = []

    for file_path in file_paths:
        with open(file_path, "r", encoding="utf-8", newline="") as file:
            reader = csv.DictReader(file)
            for row in reader:
                rows.append(row)

    return rows


def print_report(table_data: list[list[Any]], headers: list[str]) -> None:
    print(tabulate(table_data, headers=headers, tablefmt="github"))


def main() -> None:
    args = parse_args()

    try:
        report = get_report(args.report)
        rows = read_data(args.files)
        headers, table_data = report.build(rows)
        print_report(table_data, headers)
    except FileNotFoundError as error:
        print(f"Файл не найден: {error}", file=sys.stderr)
        sys.exit(1)
    except ValueError as error:
        print(f"Ошибка: {error}", file=sys.stderr)
        sys.exit(1)


if __name__ == "__main__":
    main()