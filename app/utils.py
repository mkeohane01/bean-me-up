from openai import OpenAI
from dotenv import load_dotenv
import os

# Load .env file
load_dotenv()
try:
    client = OpenAI(api_key= os.getenv('OPENAI_API_KEY'))
except:
    print("Error: Please set your OpenAI API key in the .env file.")
    client = OpenAI(api_key= input("Please enter your OpenAI API key: "))


def get_last_message(thread_ID):
    '''
    This function returns the most recent message in the thread.
    '''
    messages = client.beta.threads.messages.list(thread_ID)
    return messages.data[0].content[0].text.value

def create_new_thread(start_message):
    '''
    This function creates a new thread object.
    '''
    thread = client.beta.threads.create()
    client.beta.threads.messages.create(
        thread.id,
        role='assistant',
        content=start_message
    )
    return thread

def create_assistant(name, instructions, model='gpt-4o', tools=None):
    '''
    This function creates an assistant object.
    '''
    assistant = client.beta.assistants.create(
        name=name,
        model=model,
        instructions=instructions,
        tools=tools
    )
    return assistant.id

def run_thread(query, thread_ID, assistant_ID):
    '''
    This function runs the messages in a thread.
    '''
    client.beta.threads.messages.create(
        thread_ID,
        role='user',
        content=query
    )
    client.beta.threads.runs.create_and_poll(
        thread_id=thread_ID,
        assistant_id=assistant_ID
    )
    return None

if __name__ == "__main__":
    pass