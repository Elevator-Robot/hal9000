import aws_cdk as core
import aws_cdk.assertions as assertions

from hal9000.hal9000_stack import Hal9000Stack


def test_sqs_queue_created():
    app = core.App()
    stack = Hal9000Stack(app, "hal9000")
    template = assertions.Template.from_stack(stack)

    template.has_resource("AWS::SNS::Topic")
    template.has_resource("AWS::Chatbot::SlackChannelConfiguration")
