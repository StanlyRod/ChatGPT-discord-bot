
import os
import requests
import discord

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
                'model': 'gpt-4o',
                'messages': [{'role': 'user', 'content': prompt}],
                'max_tokens': 600
        }

        
        response = requests.post(url, headers=headers, json=data)
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

    
    
#=================================================================
    

intents = discord.Intents.default()
intents.message_content = True

client = discord.Client(intents=intents)


#show loggin message
@client.event
async def on_ready():
        print('We have logged in as {0.user}'.format(client))


@client.event
async def on_message(message):
    if message.author == client.user:
        return
    
    # Check if the message content starts with ">"
    if message.content.startswith('>'):

        # Extract the sentence by removing the leading ">" character
        sentence = message.content[1:]

        try:
                
            # Generate a response using the ChatGPT language model
            answer = ChatGPT(sentence)

            # Send the generated response to the Discord channel
            await message.channel.send(answer)

        except requests.HTTPError as e:

            if e.response.status_code == 400:
                await message.channel.send("Error: The user prompt exceeds the maximum tokens allowed.")
            else:
                await message.channel.send(f"An HTTP error occurred: {e.response.status_code}")

        except discord.errors.HTTPException as e:
            await message.channel.send(f"Discord HTTP Exception the response exceed 2000 characters try again with a different prompt: {e}")

        except Exception as e:
            await message.channel.send(f"An unexpected error occurred: {e}")

    else:
        await message.channel.send("Every prompt need to start with a greater than sign '>'. Try again")


token = os.environ["DISCORDBOTKEY"]

client.run(token)
