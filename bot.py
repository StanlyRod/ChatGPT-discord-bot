import os
import sys
import requests
import discord
import gptobject as go



# Get ChatGPT API KEY from the environmental variable
try:
    openaikey = os.environ["OPENAIKEY"]
except KeyError as kee:
    print(f"Error: The environment variable 'OPENAIKEY' is not set. Please set it and try again. {kee}")
    sys.exit()

#Get Discord bot token key from the environmental variable
try:
    discordbotkey = os.environ["DISCORDBOTKEY"]
except KeyError as ke:
    print(f"Error: The environment variable 'DISCORDBOTKEY' is not set. Please set it and try again. {ke}")
    sys.exit()


# openai endpoint
endpoint = 'https://api.openai.com/v1/chat/completions'

# openai model
model = "gpt-4o"

#response tokens
max_tokens = 600



def discord_action():

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
                answer = go.chatgpt(sentence, endpoint, model, max_tokens, openaikey)

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

    try:
        client.run(discordbotkey)
    except discord.errors.LoginFailure as e:
        print(f"Login failed: {e}")
        print("Please check the Discord bot token. Ensure it's valid and correctly set in the environment variables.")
        sys.exit(1)




def main():
    discord_action()
    


    
if __name__ == "__main__":
    main()