from hidden.secret import *
#from config.secret import *

# ccloud config
config = {
    'bootstrap.servers': CCLOUD_CLUSTER,
    'sasl.mechanisms': SASL_MECHANISM,
    'security.protocol': SECURITY_PROTOCOL,
    'sasl.username': SASL_USERNAME,
    'sasl.password': SASL_PASSWORD,
    'ssl.ca.location': '../hidden/cacert.pem'
}

config_avro = {
    'bootstrap.servers': CCLOUD_CLUSTER,
    'sasl.mechanisms': SASL_MECHANISM,
    'security.protocol': SECURITY_PROTOCOL,
    'sasl.username': SASL_USERNAME,
    'sasl.password': SASL_PASSWORD,
    'ssl.ca.location': '../hidden/cacert.pem',
    'schema.registry.url': SCHEMA_REGISTRY_URL,
    'schema.registry.basic.auth.credentials.source': SCHEMA_REGISTRY_CREDENTIALS_SOURCE,
    'schema.registry.basic.auth.user.info': SCHEMA_REGISTRY_AUTH_INFO
}

uvicorn_port = 8000
