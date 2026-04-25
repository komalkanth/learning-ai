# Use the Conversation API to send a text message to Amazon Nova.

import boto3
from botocore.exceptions import ClientError

# Create a Bedrock Runtime client in the AWS Region you want to use.
bedrock_client = boto3.client('bedrock-runtime', region_name='us-east-1')

# Set the model ID
model_id = 'amazon.nova-pro-v1:0'

# Start a conversation with the model using user_message as the input.
user_message = "Describe Amazon Bedrock in simple terms."

conversation = [
    {
        "role": "user",
        "content": [{"text": user_message}],
    }
]


# Send the message to the model
response = bedrock_client.converse(
    modelId=model_id,
    messages=conversation,
    inferenceConfig={
      "maxTokens": 512,
      "temperature": 0.7,
      "topP": 0.9,
    }
)

# Extract the model's response from the API response
# print(response)

model_response = response['output']['message']['content'][0]['text']
print("Model response:", model_response)
