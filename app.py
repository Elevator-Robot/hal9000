#!/usr/bin/env python3
import os

import aws_cdk as cdk
import aws_cdk.aws_chatbot as chatbot
import aws_cdk.aws_sns as sns
from constructs import Construct

app = cdk.App()


class Hal9000Stack(cdk.Stack):
    def __init__(self, scope: Construct, construct_id: str, **kwargs) -> None:
        super().__init__(scope, construct_id, **kwargs)

        topic = sns.Topic(
            self,
            "Hal9000Topic",
            display_name="Hal9000",
        )

        # environments

        chatbot.SlackChannelConfiguration(
            self,
            "Hal9000SlackChannelConfiguration",
            slack_channel_configuration_name="Hal9000",
            slack_workspace_id=os.environ["SLACK_WORKSPACE_ID"],
            slack_channel_id=os.environ["SLACK_CHANNEL_ID"],
            notification_topics=[topic],
            logging_level=chatbot.LoggingLevel.ERROR,
        )


Hal9000Stack(app, "Hal9000Stack")

app.synth()
