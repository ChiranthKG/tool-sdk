from tools import Tool
from clients import Client

# Initialize the Client with API credentials
api_key = "218899de-dda1-4593-8d2a-0be1ad25a97c"
user_id = "727"
tenant_id = "518"

client = Client(api_key=api_key, user_id=user_id, tenant_id=tenant_id)

# Initialize the Tool with the client
tool = Tool(client=client)

# Define inputs for `create_request`
tool_inputs = {
    "text": "What is the chemical formula of salt?"
}

try:
    # Call `create_request` and retrieve response
    create_response = tool.create_request(
        tool_id="674ab626e35cb809745799b7",  # Example tool ID
        action="START_SCREEN",
        text_input=tool_inputs["text"]
    )
    print("Response from create_request:")
    print(create_response)

    # Extract and display `conversation_id` and `message_id`
    conversation_id = create_response.get("result", {}).get("conversation_id")
    message_id = create_response.get("result", {}).get("message_id")

    if conversation_id and message_id:
        print(f"\nExtracted conversation_id: {conversation_id}")
        print(f"Extracted message_id: {message_id}")
    else:
        raise ValueError("Missing `conversation_id` or `message_id` in the response.")

except ValueError as ve:
    print(f"Error: {ve}")

except Exception as e:
    print(f"An unexpected error occurred: {e}")

# Now testing `fetch_result` method
try:
    # Manually input the `conversation_id` and `message_id`
    conversation_id = input("Enter the conversation_id: ")
    message_id = input("Enter the message_id: ")

    if not conversation_id or not message_id:
        raise ValueError("Both `conversation_id` and `message_id` must be provided.")

    # Fetch tool result using `fetch_result`
    fetch_response = tool.fetch_result(
        conversation_id=conversation_id,
        message_id=message_id
    )
    print("\nResponse from fetch_result:")
    print(fetch_response)

except ValueError as ve:
    print(f"Error: {ve}")

except Exception as e:
    print(f"An unexpected error occurred: {e}")
