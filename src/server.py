import random
import uuid
from datetime import time

import uvicorn
from fastapi import FastAPI, HTTPException
from fastapi.security import HTTPBasic

from src.aio_confluent import AIOProducer, AvroAIOProducer, KafkaException
from src.item_pb2 import ProtobufItem
from src.settings import uvicorn_port
from src.settings import config, config_avro
from google.protobuf.json_format import MessageToJson, MessageToDict

app = FastAPI()
security = HTTPBasic()

aio_producer = None
avro_producer = None

@app.on_event("startup")
async def startup_event():
    global aio_producer, avro_producer
    aio_producer = AIOProducer(config)
    avro_producer = AvroAIOProducer(config_avro)

@app.on_event("shutdown")
def shutdown_event():
    aio_producer.close()
    avro_producer.close()

def ack(err, msg):
    print('producer acknowledged {}'.format(msg))

def random_record():
    key = str(uuid.uuid4())
    payload = ProtobufItem()
    payload.id = key
    payload.item = random.choice(['Apple', 'Banana', 'Pear', 'Strawberry'])
    payload.count = random.randint(1, 10)
    return (key, payload)

def serialize_protobuf(item):
    byte_str = item.SerializeToString()
    return byte_str

@app.get("/")
async def root():
    return {"message": "server is up"}

@app.post("/report/avro")
async def produce_json(id: str, ):
    try:
        key, payload = random_record()
        aio_producer.produce(topic="json_item", key=key, value=MessageToJson(payload), on_delivery=ack)
        return {"timestamp": time()}
    except KafkaException as ex:
        raise HTTPException(status_code=500, detail=ex.args[0].str())

@app.post("/report/avro")
async def produce_avro():
    try:
        key, payload = random_record()
        avro_producer.produce(topic="avro_item", key=key, value=MessageToDict(payload), on_delivery=ack)
        return {"timestamp": time()}
    except KafkaException as ex:
        raise HTTPException(status_code=500, detail=ex.args[0].str())

@app.post("/report/avro")
async def produce_protobuf():
    try:
        key, payload = random_record()
        byte_str = serialize_protobuf(payload)
        aio_producer.produce(topic="proto_item", key=key, value=byte_str, on_delivery=ack)
        return {"timestamp": time()}
    except KafkaException as ex:
        raise HTTPException(status_code=500, detail=ex.args[0].str())

def main():
    uvicorn.run(app, host='127.0.0.1', port=uvicorn_port)