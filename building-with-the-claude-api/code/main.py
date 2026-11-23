from chat_utils import add_user_message, add_assistant_message, chat
from chat_display import print_chat

system_prompt = """
You are a patient cience tutor.
Do not directly answer a student's questions.
Guide them to a solution step by step.
"""

# Start with an empty message list
messages = []

# Add the initial user question
add_user_message(messages, "Oi, can you help me understand how photosynthesis works?")

# Get Claude's response
answer = chat(messages)

# Add Claude's response to the conversation history
add_assistant_message(messages, answer)

# Add a follow-up question
add_user_message(messages, "Can you explain the role of chlorophyll in photosynthesis?")

# Get the follow-up response with full context
final_answer = chat(messages)
add_assistant_message(messages, final_answer)

print_chat(messages)
