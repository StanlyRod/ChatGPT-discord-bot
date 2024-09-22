import requests


# Define a function to make a request to the ChatGPT API.
# Takes a prompt (string), endpoint (string), model (string), max_tokens (int), and openaikey (string) as inputs.
def chatgpt(prompt:str, endpoint:str, model:str, max_tokens:int, openaikey:str):


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

        
        response = requests.post(endpoint, headers=headers, json=data)
        re = response.json()

        #get the answer from the json response
        fullResponse = re['choices'][0]['message']['content']

        return fullResponse
    
    except requests.HTTPError as e:
        errorMessage = ""

        if e.response.status_code == 400:
            errorMessage = "Bad request: The open-AI request was invalid or malformed."
        elif e.response.status_code == 401:
            errorMessage = "Unauthorized: Your open-API key is invalid or missing."
        elif e.response.status_code == 403:
            errorMessage = "Forbidden: Your open-API key does not have permission to access this resource."
        elif e.response.status_code == 404:
            errorMessage = "Not found: The requested resource was not found."
        elif e.response.status_code == 429:
            errorMessage = "Rate limit exceeded: You have exceeded your openAI-API rate limit or quota check your plan and billing details."
        elif e.response.status_code == 500:
            errorMessage = "Internal server error: An unexpected error occurred on the server. Retry your request in few minutes"
        elif e.response.status_code == 503:
            errorMessage = "Service unavailable: The server is currently unable to handle the request due to high traffic or maintenance."
        else:
            errorMessage = f"An HTTP error occurred: {e.response.status_code}"
        return errorMessage
    
    except requests.RequestException as e:
        return f"A request exception occurred: {e}"
    
    except Exception as e:
        return f"An unexpected error occurred: {e}"
