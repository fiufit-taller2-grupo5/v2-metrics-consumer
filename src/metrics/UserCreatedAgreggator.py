from metrics.MetricAggregator import MetricAggregator

class UserCreatedAggregator(MetricAggregator):

    def __init__(self, metrics):
        self.metrics = metrics


    def aggregate(self) -> dict:
        print("Starting to aggregate UserCreated metrics...")
        count = 0
        for m in self.metrics:
            if m.get_name() == "user_created":
                count += 1

        return {
            "name": "user_created",
            "total_count": count,
            "timestamp": self.current_time()
        }
    