#!/bin/bash
export AWS_CODEGURU_PROFILER_GROUP_NAME=sample-python-app
export AWS_CODEGURU_PROFILER_TARGET_REGION=us-east-1

python3 -m codeguru_profiler_agent producer.py
