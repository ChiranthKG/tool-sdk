from clients import Client
from typing import Dict, Any
import requests

class Tool:
    def __init__(self, client: Client):
        """
        Initialize the Tool class.

        client (Client): An instance of the Client class for API communication.
        """
        self.client = client

    def create_request(self, 
                       tool_id: str, 
                       action: str, 
                       text_input: str, 
                       language_code: str = "EN",
                       source: str = "APP", 
                       endpoint: str = "/interact/api/ve1/intract/tool/conversation") -> Dict[str, Any]:
        """
        Initiates a conversation with the AI tool.

        Parameters:
            tool_id (str): The ID of the tool.
            action (str): The action to be performed.
            text_input (str): The input text from the user.
            language_code (str): The language code for the conversation (default: "EN").
            source (str): The source of the conversation (default: "APP").

        Returns:
            Dict[str, Any]: The JSON response from the server containing the conversation ID and message ID.
        """
        if not text_input:
            raise ValueError("The 'text_input' parameter is required and cannot be empty.")
        
        # Adjusted payload structure to match the required format
        payload = {
            "tool_id": tool_id,
            "language_code": language_code,
            "source": source,
            "action": action,
            "inputs": {
                        "text": text_input
                    }
        }
        print("Payload being sent:")
        print(payload)

        try:
            response = self.client.make_request(
                method="POST",
                endpoint=endpoint,
                json=payload
            )
            return response.json()
        
        except requests.HTTPError as e:
            print(f"HTTP error: {e.response.status_code} - {e.response.text}")
            raise

        except Exception as e:
            print(f"An unexpected error has occurred: {str(e)}")
            raise

    def fetch_result(self, 
                     conversation_id: str, 
                     message_id: str, 
                     endpoint: str = "/interact/api/v1/intract/conversation/fetchDetails") -> requests.Response:
        """
        Fetches the result of a conversation using the conversation ID and message ID.

        Parameters:
            conversation_id (str): The ID of the conversation.
            message_id (str): The ID of the message.
            endpoint (str): API endpoint to fetch the result (default provided).

        Returns:
            str: The response message from the tool.
        """
        params = {
            "cId": conversation_id,
            "mId": message_id
        }

        try:
            response = self.client.make_request(
                method="GET",
                endpoint=endpoint,
                params=params
            )
            return response.text
        
        except requests.HTTPError as e:
            print(f"HTTP error: {e.response.status_code} - {e.response.text}")
            raise

        except Exception as e:
            print(f"An unexpected error has occurred: {str(e)}")
            raise
