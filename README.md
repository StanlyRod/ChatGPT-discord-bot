# Discord ChatGPT Bot
A simple Discord bot powered with ChatGPT.

This repository contains a Python-based Discord bot that integrates with OpenAI's ChatGPT API to provide AI-driven responses to user prompts. The bot listens for messages in a Discord channel that start with the > character and returns a response generated by the ChatGPT model.

### Features

- Responds to user prompts in Discord channels using OpenAI's GPT-4 model.
- Handles errors gracefully, including OpenAI API errors and Discord message length limits.
- Provides detailed error messages for common issues like exceeding token limits or rate limits.
- Easy integration with environmental variables for secure API key management.

### Requirements

- Python 3.13 or higher 
- Discord bot token
- OpenAI API key

### Note
- > ⚠️ **Check your Python version: Run python --version to check the version of Python you're using.**
- > ⚠️ **If using Python 3.13 or above: You'll need to find an alternative library for audio manipulation.**
- > ⚠️ **If using Python 3.11 or 3.12: You can still use audioop, but consider migrating to an alternative library.**
- > ⚠️ **Install audioop-lts: For projects like discord.py that require audioop on newer Python versions, you can install the audioop-lts package:**
```bash
pip install audioop-lts
```

### Create a New Discord Application and get bot token key

1. Go to the Discord Developer Portal. https://discord.com/developers/applications?form=MG0AV3 
- or follow this instructions https://discordpy.readthedocs.io/en/stable/discord.html
2. Click on the "New Application" button.
3. Give your application a name and click "Create".
  
![bot name](https://github.com/user-attachments/assets/e743af70-aae4-4b6b-aaf1-c24dac1e69f3)

4. In the "Bot" tab, assign administrator permissions to the bot and obtain its token key.

![bot permissions](https://github.com/user-attachments/assets/ce82746e-c872-4d22-90ca-4ddc9d2cb4b4)

![get bot token ](https://github.com/user-attachments/assets/3809cef5-cc90-424c-87d4-abbc899d5ebe)

5. Enable all the Privileged Gateway Intents under the "Bot" tab.

![privileged intents](https://github.com/user-attachments/assets/99d75ae0-b041-401b-bc2b-0ba1fcea8f14)

### Note
> ⚠️ **When a bot is given Administrator permissions in Discord, it gains access to almost all actions within the server.**

6. In the OAuth tab, enable the "bot" checkbox and select the "administrator" checkbox under bot permissions.

![oauth permissions](https://github.com/user-attachments/assets/6e67e188-02f5-4bd4-8b28-7eb734c30c09)

7. In the OAuth tab, copy the generated url.

You will use the URL to invite the bot to a Discord server.

1. Copy the Generated URL:

- From the OAuth2 section in the Discord Developer Portal, copy the URL that you generated by selecting the required permissions.

![copy url](https://github.com/user-attachments/assets/67da3486-845f-4caf-b354-fbda39feeb9d)


2. Open the URL in a Browser:

- Paste the URL into your browser's address bar and press Enter.
3. Select the Server:

- You will be redirected to a Discord page asking you to select a server to add the bot to.
- From the dropdown menu, choose the server where you want to invite the bot.
- Note: You must have Manage Server permissions in the server to invite a bot.
4. Authorize the Bot:

- Click the Authorize button to grant the bot the permissions specified in the URL.
- If required, complete the CAPTCHA to verify.
5. Check the Bot's Status:

- Open the Discord server you added the bot to.
- Check the member list to ensure the bot is now a member of the server.
- The bot should appear offline until its code is running and it is connected to Discord.


### Installation

1 Clone the Repository
```bash
git clone https://github.com/StanlyRod/ChatGPT-discord-bot.git
cd ChatGPT-discord-bot
```

2 Set Up a Virtual Environment (Optional but Recommended)
```bash
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
```

3 Install Required Libraries
```bash
pip install -r requirements.txt
```

4 Set Environment Variables
- Set the OPENAIKEY and DISCORDBOTKEY environment variables in your system and restart your computer.

Linux/Mac:
```bash
export OPENAIKEY="your-openai-api-key"
export DISCORDBOTKEY="your-discord-bot-key"
```
Windows (Command Prompt):
```cmd
set OPENAIKEY=your-openai-api-key
set DISCORDBOTKEY=your-discord-bot-key
```
Windows (PowerShell):
```powershell
$env:OPENAIKEY="your-openai-api-key"
$env:DISCORDBOTKEY="your-discord-bot-key"
```

### Usage

1. Create a python virtual environment, activate the virtual environment, install all the required dependencies and clone the repository.

![Screenshot 2024-12-27 141142](https://github.com/user-attachments/assets/9333ba3a-0094-447f-a0f8-7d496c5f4ca1)

2. Run the bot

```bash
python bot.py
```
![Screenshot 2024-12-27 142403](https://github.com/user-attachments/assets/546aa95e-b21c-4e69-a2b7-b28493be80e2)


### Note
> ⚠️ **Use greater than symbol '>'**
3. Make sure to use the greater than symbol '>' before any prompt,
if the bot sees a prompt without the > prefix, it responds with a reminder:
"Every prompt needs to start with a greater than sign '>'.
Try again." This helps users quickly understand how to interact with the bot effectively.

![Screenshot 2024-12-27 142958](https://github.com/user-attachments/assets/f28fb175-7506-45e0-b9e1-7e6cc7983d4b)

### Note
> ⚠️ **When using the Discord API to send messages to a channel, it is crucial to be specific in your prompt and token usage to avoid exceeding Discord's 2,000-character limit per message.
> This limit includes all text, emojis, and formatting (e.g., Markdown or embeds). If the ChatGPT API response exceeds 2,000 characters, the bot will raise a discord.errors.HTTPException and send the following message to the Discord channel:

"Discord HTTP Exception: The response exceeds 2,000 characters. Try again with a shorter prompt."**

![Screenshot 2024-12-27 171249](https://github.com/user-attachments/assets/33552f8e-7e29-4b4c-bee6-9d4daaf89700)

## Docker


![dockericon](https://github.com/user-attachments/assets/d6205559-bdb9-4f42-9608-3a1f91c212a1)

