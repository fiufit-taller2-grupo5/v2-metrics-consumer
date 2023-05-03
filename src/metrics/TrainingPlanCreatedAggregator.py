from metrics.MetricAggregator import MetricAggregator

class TrainingPlanCreatedAggregator(MetricAggregator):

    def __init__(self, metrics):
        self.metrics = metrics

    
    def aggregate(self):
        print("Starting to aggregate TrainingPlanCreated metrics...")
        training_plans_created_count = 0
        count_per_type = {}
        for m in self.metrics:
            if m.get_name() == "training_plan_created":
                training_plans_created_count += 1

            training_type: str = m.get_payload()["type"]
            if training_type in count_per_type:
                count_per_type[training_type] += 1
            else:
                count_per_type[training_type] = 1


        return {
            "name": "training_plan_created",
            "total_count": training_plans_created_count,
            "count_per_type": count_per_type,
            "timestamp": self.current_time()
        }