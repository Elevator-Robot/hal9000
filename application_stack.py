#!/usr/bin/env python3
from constructs import Construct

from aws_cdk import Stack, aws_chatbot as chatbot, aws_sns as sns


class ChatbotStackProps:
    def __init__(
        self,
        slack_workspace_id: str,
        slack_channel_id: str,
    ):
        self.slack_workspace_id = slack_workspace_id
        self.slack_channel_id = slack_channel_id


class ChatbotStack(Stack):
    def __init__(
        self, scope: Construct, construct_id: str, props: ChatbotStackProps
    ) -> None:
        super().__init__(scope, construct_id)

        slack_workspace_id = props.slack_workspace_id
        slack_channel_id = props.slack_channel_id

        if not slack_workspace_id:
            raise ValueError("SLACK_WORKSPACE_ID is not defined")
        if not slack_channel_id:
            raise ValueError("SLACK_CHANNEL_ID is not defined")

        topic = sns.Topic(
            self,
            "Hal9000Topic",
            display_name="Hal9000",
        )

        chatbot.SlackChannelConfiguration(
            self,
            "Hal9000SlackChannelConfiguration",
            slack_channel_configuration_name="Hal9000",
            slack_workspace_id=slack_workspace_id,
            slack_channel_id=slack_channel_id,
            notification_topics=[topic],
            logging_level=chatbot.LoggingLevel.ERROR,
        )
