from hidden.secret import *
#from config.secret import *

# ccloud config
config = {
    'bootstrap.servers': CCLOUD_CLUSTER,
    'sasl.mechanisms': SASL_MECHANISM,
    'security.protocol': SECURITY_PROTOCOL,
    'sasl.username': SASL_USERNAME,
    'sasl.password': SASL_PASSWORD,
    'ssl.ca.location': '../hidden/cacert.pem',
}

uvicorn_port = 8000