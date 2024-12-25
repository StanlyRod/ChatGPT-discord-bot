# Discord ChatGPT Bot
A simple Discord bot powered with ChatGPT.

This repository contains a Python-based Discord bot that integrates with OpenAI's ChatGPT API to provide AI-driven responses to user prompts. The bot listens for messages in a Discord channel that start with the > character and returns a response generated by the ChatGPT model.

### Features

- Responds to user prompts in Discord channels using OpenAI's GPT-4 model.
- Handles errors gracefully, including OpenAI API errors and Discord message length limits.
- Provides detailed error messages for common issues like exceeding token limits or rate limits.
- Easy integration with environmental variables for secure API key management.

### Requirements

- Python 3.8 or higher 
- Discord bot token
- OpenAI API key


### Create a New Discord Application and get bot token key

1. Go to the Discord Developer Portal. https://discord.com/developers/applications?form=MG0AV3 
- or follow this instructions https://discordpy.readthedocs.io/en/stable/discord.html
2. Click on the "New Application" button.
3. Give your application a name and click "Create".
  
![bot name](https://github.com/user-attachments/assets/e743af70-aae4-4b6b-aaf1-c24dac1e69f3)

4. In the "Bot" tab, assign administrator permissions to the bot and obtain its token key.

![bot permissions](https://github.com/user-attachments/assets/ce82746e-c872-4d22-90ca-4ddc9d2cb4b4)

![get bot token ](https://github.com/user-attachments/assets/3809cef5-cc90-424c-87d4-abbc899d5ebe)

### Note
> ⚠️ **When a bot is given Administrator permissions in Discord, it gains access to almost all actions within the server.**

5 In the OAuth tab, enable the "bot" checkbox and select the "administrator" checkbox under bot permissions.

![oauth permissions](https://github.com/user-attachments/assets/6e67e188-02f5-4bd4-8b28-7eb734c30c09)

6 In the OAuth tab, copy the generated url.
You will use the URL to invite the bot to a Discord server.

1. Copy the Generated URL:

- From the OAuth2 section in the Discord Developer Portal, copy the URL that you generated by selecting the required permissions.
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



### Create a Bot User

1. In your new application's settings, go to the "Bot" tab.

2. Click "Add Bot" and confirm.

3. Note down the token shown on this page, as you will need it later.

### Installation

1 Clone the Repository
```bash
git clone https://github.com/your-username/discord-chatgpt-bot.git
cd discord-chatgpt-bot
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
- Set the OPENAIKEY and DISCORDBOTKEY environment variables in your system.

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

5 Run the bot
```bash
python bot.py
```
