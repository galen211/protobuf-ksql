from confluent_kafka import avro

schema_key = avro.loads('{"type": "string"}')

schema_value = avro.loads("""
    {
      "fields": [
        {
          "name": "device_key",
          "type": "string"
        },
        {
          "name": "ca",
          "type": "string"
        },
        {
          "name": "unit",
          "type": "string"
        },
        {
          "name": "scp",
          "type": "string"
        },
        {
          "name": "station",
          "type": "string"
        },
        {
          "name": "linename",
          "type": "string"
        },
                {
          "name": "division",
          "type": "string"
        },
        {
          "name": "desc",
          "type": "string"
        },
        {
          "name": "counter_entries",
          "type": "int"
        },
        {
          "name": "counter_exits",
          "type": "int"
        },
        {
          "name": "time",
          "type": "int"
        },
        {
          "name": "period_entries",
          "type": "int"
        },
        {
          "name": "period_exits",
          "type": "int"
        }
      ],
      "name": "TurnstileReport",
      "type": "record"
    }
""")


