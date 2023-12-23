#!/usr/bin/env python3
from aws_cdk import App

from pipeline_stack import PipelineStack

app = App()


PipelineStack(app, "hal9000-pipeline")

app.synth()
