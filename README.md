<!-- add a badge to the tests gh pipeline -->
[![Tests](https://github.com/Elevator-Robot/hal9000/actions/workflows/tests.yml/badge.svg)](https://github.com/Elevator-Robot/hal9000/actions/workflows/tests.yml)

## HAL9000

HAL9000 is a chatbot client integration for slack. It's deployed with CDK & the app is written in Python.

## Deployment

### Prerequisites

- [AWS CLI](https://docs.aws.amazon.com/cli/latest/userguide/cli-chap-install.html)
- [AWS CDK](https://docs.aws.amazon.com/cdk/latest/guide/getting_started.html)
- [Python 3.6+](https://www.python.org/downloads/)
- [Node.js 10.3.0+](https://nodejs.org/en/download/)
- [Docker](https://docs.docker.com/get-docker/)
- [Slack App](https://api.slack.com/start/overview)

### Steps

1. Clone the repository

    ```bash
    git clone
    ```
2. Install dependencies

    ```bash
    npm install
    ```
3. Make sure you have the right AWS profile set up

    ```bash
    export AWS_PROFILE=your-profile
    ```
    or however you set up your profile ;) 

4. Deploy the stack

    ```bash
    cdk deploy
    ```
