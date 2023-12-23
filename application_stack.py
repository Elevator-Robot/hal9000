#!/usr/bin/env python3
from os import environ
from constructs import Construct

from aws_cdk import Stack, aws_chatbot as chatbot, aws_sns as sns


class ChatbotStack(Stack):
    def __init__(self, scope: Construct, construct_id: str, **kwargs) -> None:
        super().__init__(scope, construct_id, **kwargs)

        topic = sns.Topic(
            self,
            "Hal9000Topic",
            display_name="Hal9000",
        )

        slack_workspace_id = environ["SLACK_WORKSPACE_ID"]
        if not slack_workspace_id:
            raise ValueError("SLACK_WORKSPACE_ID is not defined")
        slack_channel_id = environ["SLACK_CHANNEL_ID"]
        if not slack_channel_id:
            raise ValueError("SLACK_CHANNEL_ID is not defined")

        chatbot.SlackChannelConfiguration(
            self,
            "Hal9000SlackChannelConfiguration",
            slack_channel_configuration_name="Hal9000",
            slack_workspace_id=slack_workspace_id,
            slack_channel_id=slack_channel_id,
            notification_topics=[topic],
            logging_level=chatbot.LoggingLevel.ERROR,
        )
