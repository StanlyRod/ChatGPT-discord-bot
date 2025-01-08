import logging
import httpx


logging.basicConfig(level=logging.ERROR)

# splits the response into segments of 2000 characters
# and returns a list of these segments.
def chop_response(response) -> list[str]:
    chopped_response = []
    for e in range(0, len(response), 2000):
        chopped_response.append(response[e:e + 2000])
    return chopped_response


# Define a function to make a request to the ChatGPT API.
# Takes a prompt (string), endpoint (string), model (string), max_tokens (int), and openaikey (string) as inputs.
async def chatgptAsync(prompt:str, endpoint:str, model:str, max_tokens:int, openaikey:str) -> list[str]:

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

        #longer timeout duration 120 seconds
        timeout = httpx.Timeout(120.0)

        #HTTP client with a specified timeout
        async with httpx.AsyncClient(timeout=timeout) as client:
            #asynchronous POST request
            response = await client.post(endpoint, headers=headers, json=data)
            
            #parse the JSON response from the POST request
            re = response.json()
            
            #check for error in the response
            if "error" in re:
                logging.error(f"Error with OpenAI API: {re['error']['message']}")
                return [f"Error with OpenAI API: {re['error']['message']}"]
            
            #get the answer from the json response
            full_response = re['choices'][0]['message']['content']

            #if response length is greater than 2000 characters then call the 'chop_response' function, 
            # if not return the full response in a list
            return chop_response(full_response) if len(full_response) > 2000 else [full_response]
            

    except httpx.HTTPStatusError as e:
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

    except httpx.RequestError as e:
        logging.error(f"A network request exception occurred: {e}")
        return [f"A network request exception occurred: {e}"]
    
    except Exception as e:
        logging.error(f"An unexpected error occurred: {e}")
        return [f"An unexpected error occurred: {e}"]


