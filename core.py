# Import necessary libraries
import discord
import openai

# Define your OpenAI GPT-3 API key
gpt3_api_key = "YOUR-OPENAI-API-KEY"

# Initialize the OpenAI GPT-3 model
openai.api_key = gpt3_api_key

# Create a Discord bot instance
intents = discord.Intents.default()
intents.typing = False
intents.presences = False
intents.message_content = True
bot = discord.Client(intents=intents)

@bot.event
async def on_ready():
    print(f'Logged in as {bot.user.name}')

@bot.event
async def on_message(message):
    if message.author == bot.user:
        return

    if message.content.startswith('!ask'):
        # Extract the question from the message
        question = message.content[5:]

        # Provide a specific and focused prompt for bug bounty questions you can change this to whatever you like just make it logical its chat gpt
        prompt = f"Bug Bounty Assistant: Explain the concept of {question} in the context of bug bounty programs. Provide real-world examples and insights related to bug hunting."

        # Use GPT-3 to generate an answer
        response = openai.Completion.create(
            engine="text-davinci-003",
            prompt=prompt,
            max_tokens=250,  # Adjust the response length as needed
        )

        answer = response.choices[0].text

        # Send the answer to the same channel
        await message.channel.send(f"Bug Bounty Hunter: {answer}")

if __name__ == "__main__":
    # Place your Discord bot token here
    bot.run("YOUR-DISCORD-BOT-TOKEN")
