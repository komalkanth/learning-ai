# Basic interaction with Amazon Bedrock

Amazon Bedrock is a fully managed AWS service that provides secure, enterprise-grade access to select foundation models through a single API. There are two ways to interact with Amazon Bedrock API: Converse API and Invoke API. The Converse API is a high level API that allows you to have a conversation with a foundation model and has a consistent interface to interact with multiple models. The Invoke API is a low level API that allows you to invoke a specific function on a foundation model, using a request body specific to different models.

In this "fundamentals" project, we will use the Converse API to have a conversation with a foundation model. We will use the `amazon-bedrock` Python SDK to interact with the Amazon Bedrock API.

The `main.py` file contains the code to send a text message to Amazon Nova Pro, which is a foundation model available on Amazon Bedrock. The code creates a conversation with the model and prints the response.

Here is the explanation of the code in `main.py`:
1. We import the necessary libraries, including `boto3` for interacting with AWS services and `ClientError` for handling exceptions.
```python
import boto3
from botocore.exceptions import ClientError
```

2. We create a client for the Amazon Bedrock service using `boto3`. Region is optional if you have no set any default region in your AWS configuration, but it is required if you want to specify a different region.
```python
bedrock_client = boto3.client('bedrock-runtime', region_name='us-east-1')
```

3. Create a variable selecting the model you want to interact with. In this case, we are using `amazon-nova-pro`. You can find the exact model ID in the Amazon Bedrock documentation or console. The model ID is a string that uniquely identifies the model you want to use. It typically follows the format `provider.model-name:version`. For example, for Amazon Nova Pro, the model ID is `amazon.nova-pro-v1:0`.
```python
model_id = "amazon.nova-pro-v1:0"
```

4. We define the user message that we want to send to the model. In this case, we are asking the model to describe what is Amazon Bedrom in simple terms.

```python
user_message = "Describe Amazon Bedrock in simple terms."

conversation = [
    {
        "role": "user",
        "content": [{"text": user_message}],
    }
]
```

5. We use the `converse` method of the `bedrock_client` to send the conversation to the model and receive a response. The `converse` method takes the model ID, the conversation, and an optional inference configuration that can include parameters such as `maxTokens`, `temperature`, and `topP` to control the response generation.

Save the response from the model in a variable and print it out.
```python
    response = bedrock_client.converse(
        modelId=model_id,
        messages=conversation,
        inferenceConfig={
          "maxTokens": 512,
          "temperature": 0.7,
          "topP": 0.9,
        }
    )
    print(response)
```

The response from the `converse` method will contain the model's reply in a structured format. You can extract the text response from the model and print it out. The exact structure of the response may vary depending on the model and the API version, so you should refer to the Amazon Bedrock documentation for details on how to parse the response correctly.

Without formatting, the response will look something like this (in a more readable format):

```json
{
    "ResponseMetadata": {
        "RequestId": "97befaff-20cb-4364-b095-5fcaf02e281c",
        "HTTPStatusCode": 200,
        "HTTPHeaders": {
            "date": "Sat, 25 Apr 2026 13:34:30 GMT",
            "content-type": "application/json",
            "content-length": "1080",
            "connection": "keep-alive",
            "x-amzn-requestid": "97befaff-20cb-4364-b095-5fcaf02e281c"
        },
        "RetryAttempts": 0
    },
    "output": {
        "message": {
            "role": "assistant",
            "content": [
                {
                    "text": "Sure! Amazon Bedrock is a service provided by Amazon Web Services (AWS) that helps developers build and deploy machine learning (ML) models more easily. \n\nHere’s a simple breakdown:\n\n1. **Unified Access**: Bedrock gives you one place to access different ML models and tools from various providers, including Amazon’s own models.\n\n2. **Ease of Use**: It simplifies the process of building ML applications. You don’t need to be an expert in ML to get started.\n\n3. **Integration**: Bedrock works well with other AWS services, making it easier to incorporate ML into your existing applications.\n\n4. **Security and Privacy**: It ensures that your data and models are secure and private.\n\nIn essence, Amazon Bedrock is like a toolkit that makes it simpler for developers to use powerful ML technologies without needing to handle all the complex details themselves."
                }
            ]
        }
    },
    "stopReason": "end_turn",
    "usage": {
        "inputTokens": 8,
        "outputTokens": 178,
        "totalTokens": 186
    },
    "metrics": {
        "latencyMs": 1217
    }
}
```

The main part of the response is under the `output` key, where you can find the model's reply in the `content` field. In this example, the model provides a simple explanation of what Amazon Bedrock is.

To parse the response and extract the model's reply, you can use the following code:

```python
model_response = response['output']['message']['content'][0]['text']
print("Model response:", model_response)
```
This will print the model's response in a more readable format.
```
Model response: Sure! Amazon Bedrock is a service provided by Amazon Web Services (AWS) that helps developers build and deploy machine learning (ML) models more easily.

Here’s a simple breakdown:

1. **Unified Experience**: Bedrock offers a single place for developers to access different ML models and tools. This means you don’t have to jump between various services to find what you need.

2. **Model Access**: It gives you access to a variety of pre-trained ML models. These models can be used for different tasks like understanding language, recognizing images, and more.

3. **Customization**: You can fine-tune these pre-trained models to better suit your specific needs. This means you can make the models work better for your particular application.

4. **Deployment**: Bedrock helps you easily deploy these models so they can start working in your applications. This includes handling the infrastructure needed to run the models efficiently.

5. **Integration**: It works well with other AWS services, making it easier to incorporate ML into your existing systems and workflows.

In short, Amazon Bedrock aims to make building and using machine learning models simpler and more integrated for developers.
```