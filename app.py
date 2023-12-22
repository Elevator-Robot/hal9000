#!/usr/bin/env python3
import os

from constructs import Construct

from aws_cdk import (
    App,
    Stack,
    CfnOutput,
    SecretValue,
    aws_chatbot as chatbot,
    aws_iam as iam,
    aws_sns as sns,
    aws_codepipeline as codepipeline,
    aws_codepipeline_actions as codepipeline_actions,
    aws_codebuild as codebuild,
)

app = App()


class Hal9000Stack(Stack):
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


class PipelineStack(Stack):
    def __init__(self, scope: Construct, construct_id: str, **kwargs) -> None:
        super().__init__(scope, construct_id, **kwargs)

        github_token = SecretValue.plain_text(os.environ["GITHUB_TOKEN"] or "")

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

        pipeline = codepipeline.Pipeline(
            self,
            "Hal9000Pipeline",
        )

        source_action = codepipeline_actions.GitHubSourceAction(
            action_name="GitHub_Source",
            owner="elevator-robot",
            repo="hal9000",
            branch="dev",
            output=source_output,
            oauth_token=github_token,
        )

        build_action = codepipeline_actions.CodeBuildAction(
            action_name="CodeBuild",
            project=codebuild_project,
            input=source_output,
            outputs=[build_output],
        )

        pipeline.add_stage(
            stage_name="Source",
            actions=[source_action],
        )

        pipeline.add_stage(
            stage_name="Build",
            actions=[build_action],
        )

        # The code that defines your stack goes here
        CfnOutput(self, "PipelineStack", value="PipelineStack")


PipelineStack(app, "PipelineStack")

app.synth()
