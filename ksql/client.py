import asyncio
import json

import aiohttp
import pandas as pd

df = pd.DataFrame(columns=['item', 'count'])

async def run_request():

    query = "select id, item, count from AVRO_STREAM emit changes;"

    url = 'http://127.0.0.1:8088/query'

    payload = json.dumps({
        "ksql": query,
        "streamsProperties": {
            "ksql.streams.auto.offset.reset": "earliest",
        },
    })

    headers= {
        "Accept": "application/vnd.ksql.v1+json",
        "Content-Type": "application/vnd.ksql.v1+json",
        "Accept-Encoding": "chunked",
    }

    async with aiohttp.ClientSession() as session:
        async with session.post(url=url, data=payload, headers=headers) as response:
            while not response.closed:
                chunk, _ = await response.content.readchunk()
                msg = json.dumps(chunk.decode("utf-8"))
                data = pd.Series(msg)
                df.append(data, ignore_index=True)
                pretty_print(df)


def pretty_print(df: pd.DataFrame):
    print(df.to_json())

def main():
    loop = asyncio.get_event_loop()
    loop.run_until_complete(run_request())