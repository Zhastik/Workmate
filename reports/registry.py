from reports.base import BaseReport
from reports.median_coffee import MedianCoffeeReport


def get_report(report_name: str) -> BaseReport:
    reports: dict[str, BaseReport] = {
        MedianCoffeeReport.name: MedianCoffeeReport(),
    }

    try:
        return reports[report_name]
    except KeyError as error:
        available_reports = ", ".join(sorted(reports.keys()))
        raise ValueError(
            f"Неизвестный отчет '{report_name}'. Доступные отчеты: {available_reports}"
        ) from error