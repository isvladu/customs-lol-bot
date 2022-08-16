import pymongo

from ..configuration.config import cfg

class Connection:
    """
    A class that initializes the connection to the database.
    """

    def __init__(self):
        self.client = pymongo.MongoClient(cfg["database"]["token"])
        self.database = self.client["scrimbot"]

    def getCollection(self, collection_name: str):
        """Returns a collection instance based on the name of the collection.

        Args:
            collection_name (str): Name of the collection to be retrieved

        Returns:
            Collection: Collection object to be returned
        """        
        return self.database[collection_name]