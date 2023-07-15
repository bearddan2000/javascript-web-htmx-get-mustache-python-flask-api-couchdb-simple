import types
from typing import Any
import couchdb
import logging

logging.basicConfig(level=logging.INFO)

class DbModel:
    def __init__(self, entity) -> None:
        self.my_id = entity['my_id']
        self.breed = entity['breed']
        self.color = entity['color']

class CouchDbClient:
    
    def __init__(self) -> None:
        self.db = None
        self.DATABASE_NAME = 'animal'
        self.isSeeded = False

    def __connect(self):
        host = 'db'
        port = 5984
        username = 'maria'
        password = 'pass'
        return couchdb.Server(f'http://{username}:{password}@{host}:{port}')

    def select_obj(self, r):
        return DbModel(r).__dict__

    def select_all(self):
        # select all
        results = []
        for d in self.db:
            doc_id = d
            o = self.db[doc_id]
            r = self.select_obj(o)
            results.append(r)
        return results

    def filter_by(self, key:str, value):
        for r in self.db.find({'selector': {key: value}}):
            return self.select_obj(r)
        
    def insert(self, records):
        for record in records:
            self.db.save(record)
        return self.select_all()

    def delete(self, key, value):
        for r in self.db.find({'selector': {key: value}}):
            del self.db[r]
            self.db.save(r)

    def update(self, key, value):
        r = self.filter_by(key, value)
        r['breed'] = 'updated'
        r['color'] = 'updated'
        self.db.save(r)

    def seed(self):
        client = self.__connect()
        if self.isSeeded == True:
            self.db = client[self.DATABASE_NAME]
            return
        
        self.db = client.create(self.DATABASE_NAME)

        self.isSeeded = True
        
        records = [
            { "breed": "Am Bulldog", "color": "White", "my_id": '1' },
            { "breed": "Blue Tick", "color": "Grey", "my_id": '2' },
            { "breed": "Labrador", "color": "Black", "my_id": '3' },
            { "breed": "Gr Shepard", "color": "Brown", "my_id": '4' }
        ]

        return self.insert(records)

class Endpoint:
    """Create singleton"""
    def __new__(cls):
         if not hasattr(cls, 'instance'):
             cls.instance = super(Endpoint, cls).__new__(cls)
         return cls.instance
    
    def __init__(self) -> None:
        self.client = CouchDbClient()

    def get_all(self):
        self.client.seed()
        return self.client.select_all()
    
    def filter_by(self, filter, filter_val):
        self.client.seed()
        return self.client.filter_by(filter, filter_val)        
    
    def delete(self, filter, filter_val):
        self.client.seed()
        self.client.delete(filter, filter_val)
        return self.get_all()
    
    def insert(self, new_breed, new_color):
        self.client.seed()
        records = [
            { "breed": new_breed, "color": new_color, "my_id": '0' }
        ]
        return self.client.insert(records)
    
    def update(self, filter, filter_val):
        self.client.seed()
        self.client.update(filter, filter_val)
        return self.get_all()