import random
import uuid
from datetime import time

import uvicorn
from fastapi import FastAPI, HTTPException
from fastapi.security import HTTPBasic

from src.aio_confluent import AIOProducer, KafkaException
from src.item_pb2 import ProtobufItem
from src.settings import uvicorn_port
from src.settings import config

app = FastAPI()
security = HTTPBasic()

aio_producer = None

@app.on_event("startup")
async def startup_event():
    global aio_producer
    aio_producer = AIOProducer(config)

@app.on_event("shutdown")
def shutdown_event():
    aio_producer.close()

def ack(err, msg):
    print('producer acknowledged {}'.format(msg))

@app.get("/")
async def root():
    return {"message": "server is up"}

@app.get("/produce")
async def create_protobuf_item():
    try:
        key = str(uuid.uuid4())
        payload = ProtobufItem()
        payload.id = key
        payload.item = random.choice(['Apple', 'Banana', 'Pear', 'Strawberry'])
        payload.count = random.randint(1,10)
        aio_producer.produce(topic="proto_item", key=key, value=payload.SerializeToString(), on_delivery=ack)
        return {"timestamp": time()}
    except KafkaException as ex:
        raise HTTPException(status_code=500, detail=ex.args[0].str())

def main():
    uvicorn.run(app, host='127.0.0.1', port=uvicorn_port)