FROM apache/couchdb

RUN curl -X PUT http://127.0.0.1:5984/_users -u 'maria:pass'\
    && curl -X PUT http://127.0.0.1:5984/_replicator -u 'maria:pass'