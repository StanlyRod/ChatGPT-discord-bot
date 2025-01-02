import requests
import logging

logging.basicConfig(level=logging.ERROR)

# splits the input string 'response' into segments of 2000 characters each 
# and returns a list of these segments.
def chop_response(response) -> list[str]:
    chopped_response = []
    for e in range(0, len(response), 2000):
        chopped_response.append(response[e:e + 2000])
    return chopped_response


# Define a function to make a request to the ChatGPT API.
# Takes a prompt (string), endpoint (string), model (string), max_tokens (int), and openaikey (string) as inputs.
def chatgpt(prompt:str, endpoint:str, model:str, max_tokens:int, openaikey:str) -> list[str]:


    try:

        headers = {
                'Content-Type': 'application/json',
                'Authorization': f'Bearer {openaikey}'
        }
        data = {
                'model': model,
                'messages': [{'role': 'user', 'content': prompt}],
                'max_tokens': max_tokens
        }

        #send http POST request to OPENAI Api
        response = requests.post(endpoint, headers=headers, json=data)
        # Parse the JSON response returned by the server
        re = response.json()
        
        #empty list
        chunk_response = []

        #if error found in openai api response then return error message
        if "error" in re:
           chunk_response.append(f"Error with OPENAI Api: {re['error']['message']}")
           return chunk_response

        #get the answer from the json response
        full_response = re['choices'][0]['message']['content']
        
        # Check if the length of the full response is less than 2000 characters
        if len(full_response) <= 2000:

            # If true, add the full response to the chunk_response list
            chunk_response.append(full_response)

            # Return the list containing the single full response
            return chunk_response
        
        else:
            # If the full response is greater than 2000 characters,
            # call the function 'chop_response' to split the response
            response_in_parts = chop_response(full_response)
            # Return the list
            return response_in_parts
    
    except requests.HTTPError as e:
        errorMessage = []

        if e.response.status_code == 400:
            errorMessage.append("Bad request: The open-AI request was invalid or malformed.")
        elif e.response.status_code == 401:
            errorMessage.append("Unauthorized: Your open-API key is invalid or missing.")
        elif e.response.status_code == 403:
            errorMessage.append("Forbidden: Your open-API key does not have permission to access this resource.")
        elif e.response.status_code == 404:
            errorMessage.append("Not found: The requested resource was not found.")
        elif e.response.status_code == 429:
            errorMessage.append("Rate limit exceeded: You have exceeded your openAI-API rate limit or quota check your plan and billing details.")
        elif e.response.status_code == 500:
            errorMessage.append("Internal server error: An unexpected error occurred on the server. Retry your request in few minutes")
        elif e.response.status_code == 503:
            errorMessage.append("Service unavailable: The server is currently unable to handle the request due to high traffic or maintenance.")
        else:
           errorMessage.append(f"An HTTP error occurred: {e.response.status_code}")
        return errorMessage
    
    except requests.RequestException as e:
        logging.error(f"A request exception occurred: {e}")
        return [f"A request exception occurred: {e}"]
    
    except Exception as e:
        logging.error(f"A request exception occurred: {e}")
        return [f"An unexpected error occurred: {e}"]

