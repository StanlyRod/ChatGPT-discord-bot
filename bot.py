
import os
import requests
import discord

def ChatGPT(prompt):

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



#=================================================================
try:

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

            # Generate a response using the ChatGPT language model
            answer = ChatGPT(sentence)

            # Send the generated response to the Discord channel
            await message.channel.send(answer)


    token = os.environ["DISCORDBOTKEY"]
    
    client.run(token)


except Exception as e:
    print(f"ERROR => {str(e)}")
    
finally:
    client.run(token)
