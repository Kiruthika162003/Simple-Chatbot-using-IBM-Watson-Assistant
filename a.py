#using python
# Import necessary modules
import json
from ibm_watson import AssistantV1
from ibm_cloud_sdk_core.authenticators import IAMAuthenticator

# Set up authentication using your IBM Cloud API key
apikey = "YOUR_API_KEY"
authenticator = IAMAuthenticator(apikey)

# Create an instance of the AssistantV1 class
url = "YOUR_WATSON_ASSISTANT_URL"
assistant = AssistantV1(
    version="2019-02-28",
    authenticator=authenticator
)
assistant.set_service_url(url)

# Create a session with the chatbot
session_response = assistant.create_session(
    assistant_id="YOUR_ASSISTANT_ID"
).get_result()

session_id = session_response["session_id"]

# Send a message to the chatbot and get the response
response = assistant.message(
    assistant_id="YOUR_ASSISTANT_ID",
    session_id=session_id,
    input={
        'message_type': 'text',
        'text': 'Hello'
    }
).get_result()

response_text = response["output"]["generic"][0]["text"]
print("Chatbot: " + response_text)

# Close the session to release resources (optional)
assistant.delete_session(
    assistant_id="YOUR_ASSISTANT_ID",
    session_id=session_id
)
