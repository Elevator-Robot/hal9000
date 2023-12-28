#!/usr/bin/env python3
from aws_cdk import App

from pipeline_stack import PipelineStack
from application_stack import ChatbotStack

app = App()


PipelineStack(
    app,
    "hal9000-pipeline",
)

ChatbotStack(
    app,
    "hal9000-chatbot",
)

app.synth()
