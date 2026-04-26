# Use the Conversation API to send a text message to Amazon Nova.

import logging
import boto3
from botocore.exceptions import ClientError

logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(levelname)s - %(message)s',
)
logger = logging.getLogger(__name__)

# Create a Bedrock Runtime client in the AWS Region you want to use.
bedrock_client = boto3.client('bedrock-runtime', region_name='us-east-1')

# Set the model ID
model_id = 'amazon.nova-pro-v1:0'

# Start a conversation with the model using user_message as the input. In this experiment, let's ask the Network Operations Assistant a technical question about AWS Networking.
user_message = "What is the minimum and maximum size of a VPC CIDR block in Amazon VPC? And how many secondary CIDR blocks can I associate with a VPC?"

conversation = [
    {
        "role": "user",
        "content": [{"text": user_message}],
    }
]

# Create a system prompt to provide instructions to the model about its persona and behavior to act like a helpful and engaging Network Operations Assistant for AWS Cloud Network services.
system_prompts = [{"text": "You are a helpful and engaging Network Operations Assistant for AWS Cloud Network services. You have deep knowledge of AWS Cloud Network services such as Amazon VPC, AWS Transit Gateway, AWS Direct Connect, AWS VPNs and more. You can answer questions and provide guidance on these services in a clear and concise manner. You can also provide examples and best practices to help users understand how to use these services effectively. If provided with any errors or logs, you can analyze them and provide troubleshooting steps to resolve the issues."}]

inference_config = {
    "maxTokens": 512,
    "temperature": 0.7,
    "topP": 0.9,
}

# Send the message to the model
try:
    response = bedrock_client.converse(
        modelId=model_id,
        messages=conversation,
        system=system_prompts,
        inferenceConfig=inference_config,
    )

    model_response = response['output']['message']['content'][0]['text']
    logger.info("Model response: %s", model_response)
except ClientError as e:
    logger.error("AWS client error: %s - %s", e.response['Error']['Code'], e.response['Error']['Message'])
    raise
