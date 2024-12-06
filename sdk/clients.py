import requests
from typing import Dict, Optional, Any

class Client:

    def __init__(self, 
                 api_key : str, 
                 user_id : Optional[str], 
                 tenant_id : str, 
                 device_id = "simplai", 
                 base_url = "https://edge-service.simplai.ai"
                 ):
        
        """
        Initialization of Client

        api_key(string):api_key generated from the dashbaord
        user_id(string - Optional):user_id available from the dashbaord
        tenant_id(string): tenant_id available from the dashboard

        """
        self.api_key = api_key
        self.user_id = user_id
        self.tenant_id = tenant_id
        self.device_id = device_id
        self.base_url = base_url
        self.headers = {
            "PIM-SID": self.api_key,
            "X-USER-ID": self.user_id,
            "X-TENANT-ID": self.tenant_id,
            "X-DEVICE-ID": self.device_id,
            "Content-Type": "application/json",
        }
    
    def make_request(self, 
                     method: str, 
                     endpoint: str, 
                     params: Optional[Dict[str, Any]] = None, 
                     json: Optional[Dict[str, Any]] = None, 
                     data: Optional[Dict[str, Any]] = None,  # Add support for form data
                     files: Optional[Dict[str, Any]] = None  # Add support for file uploads
                     ) -> requests.Response:
        """
        Helper function to make HTTP requests.
        """
        url = f'{self.base_url}{endpoint}'

        # Send the request with appropriate arguments
        response = requests.request(
            method=method,
            url=url,
            headers=self.headers,
            params=params,
            json=json,
            data=data,  # Pass form data
            files=files  # Pass file data
        )

        response.raise_for_status()  # Raise HTTPError for bad responses (4xx or 5xx)
        return response

    