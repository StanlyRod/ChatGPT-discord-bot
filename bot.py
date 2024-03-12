
import os
import requests
#import discord

def ChatGPT(prompt):


    try:
        #get ChatGPT API KEY from the environmental variable
        openaikey = os.environ["OPENAIKEY"]

        #chatgpt endpoint
        url = 'https://api.openai.com/v1/chat/completions'


        headers = {
                'Content-Type': 'application/json',
                'Authorization': f'Bearer {openaikey}'
        }
        data = {
                'model': 'gpt-3.5-turbo',
                'messages': [{'role': 'user', 'content': prompt}],
                'max_tokens': 600
        }

        
        response = requests.post(url, headers=headers, json=data)
        re = response.json()

        #get the answer from the json response
        fullResponse = re['choices'][0]['message']['content']

        return fullResponse
    
    except requests.HTTPError as e:

        if e.response.status_code == 400:
            print("Bad request: The open-AI request was invalid or malformed.")
        elif e.response.status_code == 401:
            print("Unauthorized: Your open-API key is invalid or missing.")
        elif e.response.status_code == 403:
            print("Forbidden: Your open-API key does not have permission to access this resource.")
        elif e.response.status_code == 404:
            print("Not found: The requested resource was not found.")
        elif e.response.status_code == 429:
            print("Rate limit exceeded: You have exceeded your open-API rate limit.")
        elif e.response.status_code == 500:
            print("Internal server error: An unexpected error occurred on the server.")
        elif e.response.status_code == 503:
            print("Service unavailable: The server is currently unable to handle the request due to temporary overload or maintenance.")
        else:
            print(f"An HTTP error occurred: {e.response.status_code}")
    except requests.RequestException as e:
        print(f"A request exception occurred open-AI: {e}")
    except Exception as e:
        print(f"An unexpected error occurred open-AI: {e}")





respuesta = ChatGPT("who was the first president of the united states")
print(respuesta)
    



#=================================================================
# try:

#     intents = discord.Intents.default()
#     intents.message_content = True

#     client = discord.Client(intents=intents)


#    #show loggin message
#     @client.event
#     async def on_ready():
#         print('We have logged in as {0.user}'.format(client))


#     @client.event
#     async def on_message(message):
#         if message.author == client.user:
#             return
        
#         # Check if the message content starts with ">"
#         if message.content.startswith('>'):

#             # Extract the sentence by removing the leading ">" character
#             sentence = message.content[1:]

#             # Generate a response using the ChatGPT language model
#             answer = ChatGPT(sentence)

#             # Send the generated response to the Discord channel
#             await message.channel.send(answer)


#     token = os.environ["DISCORDBOTKEY"]
    
#     client.run(token)


# except Exception as e:
#     print(f"ERROR => {str(e)}")
    
# finally:
#     client.run(token)
