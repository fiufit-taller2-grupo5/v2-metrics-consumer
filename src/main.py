from database.redis_connection import redis_connection
from database.redis_client import RedisClient
from parser.metrics_name_parser import get_metrics_names


def get_metrics_and_reset(metric_name: str, redis_client: RedisClient):
    metric_values = redis_client.get_all_from_list(metric_name)
    redis_client.remove_all_from_list(metric_name)
    return metric_values
    

def process_all_metrics(metrics_to_process: list, redis_client: RedisClient):
    for metric_name in metrics_to_process:
        print(f"About to start processing metric {metric_name}")
        get_metrics_and_reset(metric_name, redis_client)
        print(f"Fetched and deleted from redis all values of metric: {metric_name}")
        print("Starting to process and save to Mongo...")


print("Starting stats consumer...")
metrics_to_process = get_metrics_names("resources/metrics.txt")
process_all_metrics(metrics_to_process, RedisClient(redis_connection))
