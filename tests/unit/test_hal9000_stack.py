"""Unit tests for the Hal9000 stack."""
import os
import aws_cdk as core
import aws_cdk.assertions as assertions
from unittest.mock import patch


@patch.dict(os.environ, {"SLACK_WORKSPACE_ID": "T12345678"})
@patch.dict(os.environ, {"SLACK_CHANNEL_ID": "C12345678"})
def test_sqs_queue_created():
    """Test that an SNS topic are created and a Slack channel configuration is created."""  # noqa: E501
    from app import Hal9000Stack

    app = core.App()
    stack = Hal9000Stack(app, "hal9000")
    template = assertions.Template.from_stack(stack)

    template.resource_count_is("AWS::SNS::Topic", 1)
    template.has_resource(
        "AWS::SNS::Topic",
        {
            "Properties": {
                "DisplayName": "Hal9000",
            }
        },
    )

    template.resource_count_is("AWS::Chatbot::SlackChannelConfiguration", 1)
    template.has_resource(
        "AWS::Chatbot::SlackChannelConfiguration",
        {
            "Properties": {
                "SlackWorkspaceId": "T12345678",
                "SlackChannelId": "C12345678",
                "LoggingLevel": "ERROR",
            }
        },
    )
