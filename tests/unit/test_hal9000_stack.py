"""Unit tests for the Hal9000 stack."""
import aws_cdk as core
import aws_cdk.assertions as assertions

from application_stack import ChatbotStack, ChatbotStackProps


def test_sqs_queue_created():
    """Test that an SNS topic and a Slack channel configuration are created."""

    chatbot_props = ChatbotStackProps(
        slack_workspace_id="T12345678",
        slack_channel_id="C12345678",
    )

    app = core.App()
    stack = ChatbotStack(app, "test-hal9000-stack", props=chatbot_props)
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
