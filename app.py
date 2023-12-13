#!/usr/bin/env python3
import os

import aws_cdk as cdk
import aws_cdk.aws_chatbot as chatbot
import aws_cdk.aws_sns as sns

app = cdk.App()
Hal9000Stack(
    app,
    "Hal9000Stack",
    env=cdk.Environment(
        account=os.environ["CDK_DEFAULT_ACCOUNT"],
        region=os.environ["CDK_DEFAULT_REGION"],
    ),
)


class Hal9000Stack(cdk.Stack):
    def __init__(
        self, scope: cdk.Construct, construct_id: str, **kwargs
    ) -> None:
        super().__init__(scope, construct_id, **kwargs)

        topic = sns.Topic(
            self, "Hal9000Topic", display_name="Hal9000", topic_name="Hal9000"
        )

    chatbot.SlackChannelConfiguration(
        self,
        "Hal9000SlackChannel",
        slack_channel_configuration_name="Hal9000",
        slack_workspace_id="T01B4JYK3C9",
        slack_channel_id="C01B4JYK3C9",
        logging_level=chatbot.LoggingLevel.ERROR,
        notification_topics=[topic],
    )


app.synth()
