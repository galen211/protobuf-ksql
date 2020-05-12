# ksqldb: New Features
This demo extends Matt Howlett's blog post [**Integrating Apache Kafka With Python Asyncio Web Applications**](https://www.confluent.io/blog/kafka-python-asyncio-integration/) to demonstrate schema registry support for `avro`, `json`, and `protocol buffers` in ksqldb (as of version 0.8.0).

# About the Demo
This demo posits a common problem faced by financial institutions processing millions of daily payments:

How can various payment initiation systems be integrated into a centralized anti-fraud engine that can capture details about each payment, perform anti-fraud checks, and surface a queue of payments requiring manual inspection to an end-user interface?

Given the variety of payment types, having a validated schema for each type of payment event is an important safeguard for companies that need to evolve their payments infrastructure to become more agile and loosely coupled through microservices.

In this demo we expose three `http/1.1` endpoints that we call using a loadtesting tool (`locust`), which simulates thousands of incoming payment orders per second.  For each endpoint, a successful API call will produce a single payment instruction in a specified format (json, avro, protobuf) that is sent to a kafka topic as an event to initiate "payment processing".

- `/payment_json` : endpoint that produces a json-formatted payment instruction to the `payment_json` topic in Kafka
- `/payment_avro` : endpoint that produces an avro-formatted payment instruction to the `payment_avro` topic in Kafka
- `/payment_protobuf` : endpoint that produces a protobuf-formatted payment instruction to the `payment_profobuf` topic in Kafka

Each (simplified) payment instruction contains the following fields:
- `id` (string) -> uuid used as a unique key for the payment
- `payee_bank` (string) -> the name of the payee's bank
- `payee_account_no` (int) -> the account number of the payee at the payee bank
- `payment_amount` (double) -> the amount of the payment
- `payment_method` (string) -> the payment rail used for the payment (i.e. ACH, Wire, Check, etc)
- `payor_account_no` (int32) -> the payor's account number at the bank

While we load the asyncio microservice (and our Kafka cluster) with payment instructions simulating various systems initiating payments, we will simultaneously perform **anti-fraud** checks on payment instructions using ksqldb, a real-time streaming database that exposes a SQL-like language to construct streaming queries.

## Setting up the demo
- Add your kafka cluster credentials to the `config/secret.py` file
- Add your kafka cluster credentials to the `docker-compose.yml` file
- Ensure that you have created three empty kafka topics on your cluster: `payment_json`, `payment_avro`, `payment_protobuf`

## Running the API server
- First, install the project dependencies by downloading [poetry](https://python-poetry.org/), running `poetry shell` to create a new virtual environment, and poetry update to install the project dependencies into the virtual environment
- Start the `uvicorn` server by running `python -m src` from within the virtual environment
- Once started, the server should be running at http://127.0.0.1:8000/
- You can manually produce a single payment instruction by simply navigating to http://127.0.0.1:8000/payment_json to test that the server is working
- **Simulating thousands of payments per second**: you can generate load on the `/payment_*` endpoints using the provided locustfile (`scripts/locustfile`).  To start it, run `locust -f scripts/locustfile.py`
- Once started, locust should be running at http://127.0.0.1:8089.  To start loading the servers, open a browser window and provide a configuration
- Below is are some sensible defaults to start the loadtest:

<img src="img/loadtest.png" width="400">

## Seeing the results in `ksqldb`
- First, start your ksqldb server by running `docker-compose up -d`
- Then, open a `ksqldb-cli` session by running `docker exec -it ksqldb-cli ksql http://ksqldb-server:8088`

You should see the following prompt:

<img src="img/ksql-cli.png" width="400">

### Creating the payment streams
We need to create a stream for the `payment` kafka topics.  We can use the command below to do so
```sql
// Create the json stream
CREATE STREAM payment_stream_json (id VARCHAR, name VARCHAR, count INT)
WITH (kafka_topic='payment_json', value_format='JSON', partitions=1);

// Create the avro stream
CREATE STREAM payment_stream_avro (id VARCHAR, name VARCHAR, count INT)
WITH (kafka_topic='payment_avro', value_format='AVRO', partitions=1);

// Create the protobuf stream
CREATE STREAM payment_stream_proto (id VARCHAR, name VARCHAR, count INT)
WITH (kafka_topic='payment_protobuf', value_format='PROTOBUF', partitions=1);
```
Verify that you have created the payment topics and streams by running `LIST TOPICS;` and `LIST STREAMS;` respectively

# Pick out suspicious payments from the stream
31 U.S. Code Section 5324 requires financial institutions to establish reasonable procedures to detect structuring of payment transactions to avoid detection.  Common criminal tactics for structuring payments include making multiple payments under the $10,000 reporting threshold established by the Bank Secrecy Act.

A financial institution must therefore be able to identify payment structuring by matching a pattern of payments designed to avoid reporting threshold.  A simple rule to detect this pattern might be a sequence of payments (same payor and payee) with payment amounts under $10,000 that cumulatively sum to much larger amount.  In otherwords, aggregate payments between two parties that, in aggregate exceed the $10,000 reporting threshold, but which individually would not trigger reporting requirements under the Bank Secrecy Act.

With ksqldb, executing this query is exceedingly easy:
```sql
SELECT * FROM payment_json
  WHERE count >= 5 EMIT CHANGES;
```


```
//TODO: add more complex examples of payment anti-fraud
```
