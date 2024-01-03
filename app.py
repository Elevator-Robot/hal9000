#!/usr/bin/env python3
from aws_cdk import App

from application_stack import ChatbotStack, ChatbotStackProps

app = App()

chatbot_props = ChatbotStackProps(
    slack_workspace_id="T069D8YS4MP",
    slack_channel_id="C068L3YPX7H",
)

ChatbotStack(
    app,
    "hal9000-chatbot",
    props=chatbot_props,
)

app.synth()
