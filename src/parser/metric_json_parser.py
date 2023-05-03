from typing import List
from models.Metric import Metric
import json

def parse_metric_json(metric_json: str) -> Metric:
    metric_dict = json.loads(metric_json)
    metric_name = metric_dict['name']
    metric_payload = metric_dict['payload']
    if metric_name is None or metric_payload is None:
        raise ValueError("Metric name or payload is None")

    return Metric(metric_name, metric_payload)

def parse_metrics_jsons(metrics_jsons: List[str]) -> List[Metric]:
    metrics = []
    for metric_json in metrics_jsons:
        try:
            metric = parse_metric_json(metric_json)
            metrics.append(metric)
        except Exception as e:
            print(f"Error parsing metric: {metric_json}")
            print(e)
            continue
    
    return metrics