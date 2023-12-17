#!/usr/bin/env python3
import os

import aws_cdk as cdk
import aws_cdk.aws_chatbot as chatbot
import aws_cdk.aws_sns as sns
from constructs import Construct

from aws_cdk import (
    aws_codepipeline as codepipeline,
    aws_codepipeline_actions as codepipeline_actions,
    aws_codebuild as codebuild,
)

app = cdk.App()


class Hal9000Stack(cdk.Stack):
    def __init__(self, scope: Construct, construct_id: str, **kwargs) -> None:
        super().__init__(scope, construct_id, **kwargs)

        topic = sns.Topic(
            self,
            "Hal9000Topic",
            display_name="Hal9000",
        )

        slack_workspace_id = os.environ["SLACK_WORKSPACE_ID"] or ""
        slack_channel_id = os.environ["SLACK_CHANNEL_ID"] or ""

        chatbot.SlackChannelConfiguration(
            self,
            "Hal9000SlackChannelConfiguration",
            slack_channel_configuration_name="Hal9000",
            slack_workspace_id=slack_workspace_id,
            slack_channel_id=slack_channel_id,
            notification_topics=[topic],
            logging_level=chatbot.LoggingLevel.ERROR,
        )


class PipelineStack(cdk.Stack):
    def __init__(self, scope: Construct, construct_id: str, **kwargs) -> None:
        super().__init__(scope, construct_id, **kwargs)

        source_output = codepipeline.Artifact()
        build_output = codepipeline.Artifact()

        codebuild_project = codebuild.PipelineProject(
            self,
            "Hal9000CodeBuildProject",
            build_spec=codebuild.BuildSpec.from_source_filename(
                filename="buildspec.yml"
            ),
            environment=codebuild.BuildEnvironment(
                build_image=codebuild.LinuxBuildImage.STANDARD_5_0
            ),
        )

        codepipeline.Pipeline(
            self,
            "Hal9000Pipeline",
            stages=[
                codepipeline.StageProps(
                    stage_name="Source",
                    actions=[
                        codepipeline_actions.GitHubSourceAction(
                            action_name="GitHub_Source",
                            owner="elevator-robot",
                            repo="hal9000",
                            branch="dev",
                            trigger=codepipeline_actions.GitHubTrigger.WEBHOOK,
                            oauth_token=cdk.SecretValue.unsafe_plain_text(
                                "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"
                            ),
                            output=source_output,
                        )
                    ],
                ),
                codepipeline.StageProps(
                    stage_name="Build",
                    actions=[
                        codepipeline_actions.CodeBuildAction(
                            action_name="CodeBuild",
                            project=codebuild_project,
                            input=source_output,
                            outputs=[build_output],
                        )
                    ],
                ),
            ],
        )

        # The code that defines your stack goes here
        cdk.CfnOutput(self, "PipelineStack", value="PipelineStack")


PipelineStack(app, "PipelineStack")

app.synth()
