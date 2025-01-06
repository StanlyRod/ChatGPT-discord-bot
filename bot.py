import os
import sys
import discord
import gptobject as go
import httpx
import asyncio

#get openai api key and Discord bot token key from the environmental variables
try:
    openaikey = os.environ["OPENAIKEY"]
    discordbotkey = os.environ["DISCORDBOTKEY"]
except KeyError as e:
    print(f"Error: The environment variable '{e}' is not set correctly, please set it right and try again.")
    sys.exit()


# openai endpoint
endpoint = 'https://api.openai.com/v1/chat/completions'

# openai model
model = "gpt-4o"

#response tokens
max_tokens = 600


intents = discord.Intents.default()
intents.message_content = True
client = discord.Client(intents=intents)


# On bot ready
@client.event
async def on_ready():
    print(f"Bot has logged in as {client.user}")


# Handling messages
@client.event
async def on_message(message):
    if message.author == client.user:
        return

    # Check if the message starts with ">"
    if message.content.startswith('>'):

        # Extract the sentence by removing the leading ">" character
        sentence = message.content[1:]
        try:
            # Call the async chatgpt function
            answer = await go.chatgptAsync(sentence, endpoint, model, max_tokens, openaikey)

            # Send the response in chunks
            for msg in answer:
                await message.channel.send(msg)
                #wait for 300 milliseconds
                await asyncio.sleep(0.3)

        except httpx.HTTPStatusError as e:
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


async def main():
    try:
        await client.start(discordbotkey)
    except discord.errors.PrivilegedIntentsRequired as e:
        print(f"Error: Privileged intents are required. {e}")
        sys.exit(1)
    except discord.errors.LoginFailure as e:
        print(f"Login failed: {e}")
        sys.exit(1)


if __name__ == "__main__":
    asyncio.run(main())
