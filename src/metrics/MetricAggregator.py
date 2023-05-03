from datetime import datetime

class MetricAggregator:

    def aggregate(self):
        raise NotImplementedError("Subclasses should implement this!")
    

    def current_time(self):
        return datetime.now().strftime("%Y%m%d_%H%M%S%f")