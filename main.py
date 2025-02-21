from langchain_openai import ChatOpenAI
from browser_use import Agent, Browser
from dotenv import load_dotenv
import asyncio
import os

# Load environment variables from .env file
load_dotenv()

# Retrieve the OpenAI API key from environment variables
api_key = os.getenv("OPENAI_API_KEY")
if not api_key:
    raise ValueError("OpenAI API key not found. Please set it in the .env file.")

# Define the task with explicit instructions
task = """ 
1️⃣ Open https://shop.nextdev.gr/wp-admin  
2️⃣ Login with **username:** admin and **password:** TsavosGeo1987@  
3️⃣ Go to Προιοντα
4️⃣ Change price for product ID: 7523 price 99€, ID: 7518 price 130€
"""

# Initialize the browser
browser = Browser()

# Initialize the controller (if required)
controller = None  # You should instantiate a controller if necessary

# Initialize the agent with the task
agent = Agent(
    task=task,
    llm=ChatOpenAI(model="gpt-4", api_key=api_key, temperature=0.7),  # Check model name
    browser=browser,
    controller=controller,  # Make sure the controller is passed if needed
    use_vision=True,  # Set use_vision as per your requirements
)

# Define the main function to run the agent once and close the browser
async def main():
    print("🚀 Agent Started. Executing task...")

    try:
        response = await agent.run()
        print("📝 Agent Response:", response)
    except Exception as e:
        print("⚠️ An error occurred:", str(e))
    finally:
        print("❌ Closing browser...")
        await browser.close()

# Run the main function
if __name__ == '__main__':
    asyncio.run(main())
