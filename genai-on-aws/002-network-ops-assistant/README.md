# Bedrock Agent that serves as a Network Operations Assistant for AWS Cloud Network services.

In this project, we will build a Bedrock Agent that serves as a Network Operations Assistant for AWS Cloud Network services. The agent will be able to answer questions and provide guidance on various AWS Cloud Network services such as Amazon VPC, AWS Transit Gateway, AWS Direct Connect, and more.

This will be a continuation of the previous project where we built a [basic Bedrock Agent](../001-basic-bedrock/). We will give the agent some "persona" and ask it to think and behave in a certain way to make it more helpful and engaging.

This can be achieved by providing the agent with a system prompt. Just like `messages` provide input to the agent from the user's point of video, a `system` prompt is a type of prompt that provides instructions or context to the model about the task it should perform, or the persona it should adopt during the conversation.

Most of the code will be similar to the previous project as below:

```python
import boto3
from botocore.exceptions import ClientError

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
```

Now, to make the agent more helpful and engaging, we will create a system prompt that provides instructions to the model about its persona and behavior to act like a helpful and engaging Network Operations Assistant for AWS Cloud Network services. The system prompt will provide context about the agent's knowledge and how it should respond to user queries.

```python
system_prompts = [{"text": "You are a helpful and engaging Network Operations Assistant for AWS Cloud Network services. You have deep knowledge of AWS Cloud Network services such as Amazon VPC, AWS Transit Gateway, AWS Direct Connect, AWS VPNs and more. You can answer questions and provide guidance on these services in a clear and concise manner. You can also provide examples and best practices to help users understand how to use these services effectively. If provided with any errors or logs, you can analyze them and provide troubleshooting steps to resolve the issues."}]
```

Finally, we will send the conversation to the model along with the system prompt and receive a response. The `converse` method of the `bedrock_client` allows us to include both the user messages and the system prompts in the request.

```python
response = bedrock_client.converse(
    modelId=model_id,
    messages=conversation,
    system=system_prompts,
    inferenceConfig={
      "maxTokens": 512,
      "temperature": 0.7,
      "topP": 0.9,
    }
)

model_response = response['output']['message']['content'][0]['text']
print("Model response:", model_response)
```

The response we get from the model will take all of the inputs we provided and generate a response as seen below.

```
### Secondary CIDR Blocks

You can associate multiple CIDR blocks with a single VPC. Here are the details:

- **Maximum Number of Secondary CIDR Blocks:** You can associate up to 256 secondary IPv4 CIDR blocks with a single VPC.
- **CIDR Block Size for Secondaries:** Each secondary CIDR block can range from a /16 to a /28.

### Example

Let's say you create a VPC with a primary CIDR block of `10.0.0.0/16`. You can then associate secondary CIDR blocks like `10.1.0.0/16`, `10.2.0.0/16`, and so on, up to a total of 256 secondary CIDR blocks.

### Best Practices

1. **Plan Your CIDR Blocks:** Make sure to plan your CIDR blocks carefully to avoid overlap and to ensure you have enough IP addresses for your needs.
2. **Use CIDR Blocks Efficiently:** Try to use the smallest CIDR block that meets your requirements to conserve IP address space.
3. **Monitor Usage:** Keep an eye on your VPC's IP address usage to ensure you don't run out of available addresses.

If you have any specific scenarios or need further clarification, feel free to ask!
```

As we can  see from the response, the agent has a personality of being helpful and technical but the answer about Maximum Number of Secondary CIDR Blocks is not exactly right. We will continue to experiment and improve on our agent becoming more accurate in further iterations.


Even though this script serves our purpose, we can further enhance it by adding error handling and logging to manage any exceptions that may occur during the API call. This will make our agent more robust and reliable.

The modified python script [main2.py](main2.py) with error handling and logging is available in the same folder. You can run it to see how it works.