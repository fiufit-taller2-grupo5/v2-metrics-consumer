from database.redis_connection import redis_connection
from database.redis_client import RedisClient
from parser.metrics_name_parser import get_metrics_names
from parser.metric_json_parser import parse_metrics_jsons
from metrics.aggregators import aggregate_metrics_by_name
from database.mongo_connection import mongo_client

def get_metrics_and_reset(metric_name: str, redis_client: RedisClient):
    metric_values = redis_client.get_all_from_list(metric_name)
    redis_client.remove_all_from_list(metric_name)
    return metric_values
    

def process_all_metrics(metrics_to_process: list, redis_client: RedisClient):
    for metric_name in metrics_to_process:
        print(f"About to start processing metric {metric_name}")
        metrics_jsons = get_metrics_and_reset(metric_name, redis_client)
        print(f"Fetched and deleted from redis all values of metric: {metric_name}")
        metrics = parse_metrics_jsons(metrics_jsons)
        print(f"Aggregating metric {metric_name}")
        aggregated_metric = aggregate_metrics_by_name(metric_name, metrics)
        print(f"Aggregated metric {metric_name}")

        mongo_client.insert_document(aggregated_metric)
        print(f"Inserted aggregated metric {metric_name} into mongo")


print("Starting stats consumer...")
metrics_to_process = get_metrics_names("resources/metrics.txt")
process_all_metrics(metrics_to_process, RedisClient(redis_connection))
