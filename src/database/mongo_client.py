import pymongo

class MongoMetricsClient:
    def __init__(self, mongo_uri):
        self.client = pymongo.MongoClient(mongo_uri)
        self.db = self.client.metrics
        self.collection = self.db.metrics_agg
        
    def get_document_by_id(self, document_id):
        return self.collection.find_one({"_id": document_id})
    
    def insert_document(self, document):
        result = self.collection.insert_one(document)
        return result.inserted_id
