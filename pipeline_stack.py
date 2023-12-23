#!/usr/bin/env python3
from constructs import Construct

from aws_cdk import Stack, Stage, CfnOutput

from aws_cdk.pipelines import (
    CodePipeline,
    CodePipelineSource,
    ShellStep,
)

from application_stack import ChatbotStack


class ApplicationStageChatbot(Stage):
    def __init__(self, scope: Construct, construct_id: str, **kwargs) -> None:
        super().__init__(scope, construct_id, **kwargs)

        ChatbotStack(self, "hal9000-chatbot")


class PipelineStack(Stack):
    def __init__(self, scope: Construct, construct_id: str, **kwargs) -> None:
        super().__init__(scope, construct_id, **kwargs)
        pipeline = CodePipeline(
            self,
            "Pipeline",
            synth=ShellStep(
                "Synth",
                input=CodePipelineSource.connection(
                    "elevator-robot/hal9000",
                    "dev",
                    connection_arn="arn:aws:codestar-connections:us-east-1:764114738171:connection/ea715684-208a-4756-ac77-b1ab5acd5dfe",  # noqa
                ),
                commands=["npm ci", "npm run build", "npx cdk synth"],
            ),
        )

        pipeline.add_stage(
            ApplicationStageChatbot(
                self,
                "ChatbotStage",
                env={
                    "slack_workspace_id": "T069D8YS4MP",
                    "slack_channel_id": "C068L3YPX7H",
                },
            )
        )

        CfnOutput(self, "PipelineStack", value="PipelineStack")
