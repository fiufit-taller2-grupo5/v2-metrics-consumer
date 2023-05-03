from typing import List
from metrics.Metric import Metric
from metrics.UserCreatedAgreggator import UserCreatedAggregator
from metrics.TrainingPlanCreatedAggregator import TrainingPlanCreatedAggregator
from metrics.MetricAggregator import MetricAggregator

def get_aggregator_by_metric_name(metric_name: str, metrics_list: List[Metric]) -> MetricAggregator:
    if metric_name == "user_created":
        return UserCreatedAggregator(metrics_list)
    elif metric_name == "training_plan_created":
        return TrainingPlanCreatedAggregator(metrics_list)    
    else:
        return None
    

def aggregate_metrics_by_name(metric_name: str, metrics_list: List[Metric]) -> dict:
    aggregator = get_aggregator_by_metric_name(metric_name, metrics_list)
    if aggregator is None:
        print(f"Unknown metric name: {metric_name}")
    
    return aggregator.aggregate()
    
