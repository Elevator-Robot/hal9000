#!/usr/bin/env python3
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

        slack_workspace_id = "T069D8YS4MP"
        slack_channel_id = "C068L3YPX7H"

        chatbot.SlackChannelConfiguration(
            self,
            "Hal9000SlackChannelConfiguration",
            slack_channel_configuration_name="Hal9000",
            slack_workspace_id=slack_workspace_id,
            slack_channel_id=slack_channel_id,
            notification_topics=[topic],
            logging_level=chatbot.LoggingLevel.ERROR,
        )
