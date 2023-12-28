#!/usr/bin/env python3
from aws_cdk import App

from pipeline_stack import PipelineStack
from application_stack import ChatbotStack, ChatbotStackProps

app = App()

chatbot_props = ChatbotStackProps(
    slack_workspace_id="T12345678",
    slack_channel_id="C12345678",
)

PipelineStack(
    app,
    "hal9000-pipeline",
)

ChatbotStack(
    app,
    "hal9000-chatbot",
    props=chatbot_props,
)

app.synth()
