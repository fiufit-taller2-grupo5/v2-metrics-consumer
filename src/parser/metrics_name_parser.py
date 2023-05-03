from typing import List


def get_metrics_names(path: str) -> List[str]:
    with open(path, "r") as file:
        metric_names = file.read().split("\n")
        return metric_names
