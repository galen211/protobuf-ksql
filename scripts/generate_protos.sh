#!/bin/bash

python -m grpc_tools.protoc \
    --proto_path=./proto \
    --python_out=./src \
    item.proto