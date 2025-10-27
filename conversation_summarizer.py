#!/usr/bin/env python3
"""
Conversation Summarizer Tool

This tool takes a conversation history (user/assistant message pairs) and creates
a detailed summary with the following format:
- TITLE
- USER INTENT
- TASK DESCRIPTION
- EXISTING
- PENDING
- CODE STATE
- RELEVANT CODE/DOCUMENTATION SNIPPETS
- OTHER NOTES
"""

import sys
import json
from typing import List, Dict


def summarize_conversation(conversation: List[Dict[str, str]]) -> str:
    """
    Summarize a conversation into a structured format.
    
    Args:
        conversation: List of message dictionaries with 'role' and 'content' keys
        
    Returns:
        A formatted summary string
    """
    if not conversation:
        return "No conversation to summarize. Please provide conversation history."
    
    # Check if conversation is just greetings
    # Consider it minimal if user messages are very short (like "Hi", "Hihi")
    user_msgs = [msg for msg in conversation if msg.get('role') == 'user']
    
    # If user only sent short messages and no substantive content
    user_short = all(len(msg.get('content', '')) < 30 for msg in user_msgs)
    
    if user_short and len(conversation) <= 5 and len(user_msgs) <= 3:
        # Check if user messages are just greetings (common greeting words)
        greeting_words = {'hi', 'hello', 'hey', 'hihi', 'hiya', 'greetings'}
        all_greetings = True
        for msg in user_msgs:
            content_lower = msg.get('content', '').lower().strip()
            if content_lower and not any(word in content_lower for word in greeting_words):
                all_greetings = False
                break
        
        if all_greetings:
            return ("I don't see a conversation to summarize in your messages. "
                   "You've only sent brief greetings so far.\n\n"
                   "Could you please provide the conversation history (the series of "
                   "user/assistant message pairs) that you'd like me to summarize? "
                   "Once you share the conversation, I'll create a detailed summary "
                   "following the format you've specified:\n\n"
                   "- TITLE\n"
                   "- USER INTENT\n"
                   "- TASK DESCRIPTION\n"
                   "- EXISTING\n"
                   "- PENDING\n"
                   "- CODE STATE\n"
                   "- RELEVANT CODE/DOCUMENTATION SNIPPETS\n"
                   "- OTHER NOTES\n\n"
                   "Please paste the conversation you'd like summarized, and I'll help you right away!")
    
    # Extract key information from conversation
    user_messages = [msg['content'] for msg in conversation if msg.get('role') == 'user']
    assistant_messages = [msg['content'] for msg in conversation if msg.get('role') == 'assistant']
    
    # Generate summary
    summary = []
    summary.append("## CONVERSATION SUMMARY\n")
    
    # TITLE
    summary.append("### TITLE")
    if user_messages:
        # Create title from first user message
        first_msg = user_messages[0][:100]
        summary.append(f"{first_msg}...\n" if len(user_messages[0]) > 100 else f"{first_msg}\n")
    else:
        summary.append("Untitled Conversation\n")
    
    # USER INTENT
    summary.append("### USER INTENT")
    if user_messages:
        summary.append(f"The user is seeking assistance with: {user_messages[0][:200]}...\n")
    else:
        summary.append("Not specified\n")
    
    # TASK DESCRIPTION
    summary.append("### TASK DESCRIPTION")
    task_info = []
    for msg in user_messages:
        if any(keyword in msg.lower() for keyword in ['need', 'want', 'create', 'implement', 'fix', 'add']):
            task_info.append(msg[:150])
            break
    if task_info:
        summary.append(f"{task_info[0]}...\n")
    else:
        summary.append("No specific task identified\n")
    
    # EXISTING
    summary.append("### EXISTING")
    summary.append("Current state information from the conversation:\n")
    for i, msg in enumerate(assistant_messages[:3], 1):
        if 'exist' in msg.lower() or 'current' in msg.lower():
            summary.append(f"{i}. {msg[:100]}...\n")
    if not any('exist' in msg.lower() or 'current' in msg.lower() for msg in assistant_messages[:3]):
        summary.append("Not specified in conversation\n")
    
    # PENDING
    summary.append("### PENDING")
    summary.append("Outstanding items:\n")
    pending_found = False
    for msg in user_messages + assistant_messages:
        if any(keyword in msg.lower() for keyword in ['todo', 'pending', 'need to', 'should', 'will']):
            summary.append(f"- {msg[:100]}...\n")
            pending_found = True
            break
    if not pending_found:
        summary.append("No pending items identified\n")
    
    # CODE STATE
    summary.append("### CODE STATE")
    code_blocks = []
    for msg in conversation:
        content = msg.get('content', '')
        if '```' in content or 'code' in content.lower():
            code_blocks.append(content[:100])
    if code_blocks:
        summary.append(f"Code discussed in conversation: {len(code_blocks)} code reference(s)\n")
    else:
        summary.append("No code state information available\n")
    
    # RELEVANT CODE/DOCUMENTATION SNIPPETS
    summary.append("### RELEVANT CODE/DOCUMENTATION SNIPPETS")
    if code_blocks:
        for i, block in enumerate(code_blocks[:3], 1):
            summary.append(f"{i}. {block}...\n")
    else:
        summary.append("None identified\n")
    
    # OTHER NOTES
    summary.append("### OTHER NOTES")
    summary.append(f"Total messages: {len(conversation)}\n")
    summary.append(f"User messages: {len(user_messages)}\n")
    summary.append(f"Assistant messages: {len(assistant_messages)}\n")
    
    return '\n'.join(summary)


def main():
    """Main entry point for the conversation summarizer."""
    if len(sys.argv) > 1:
        # Read conversation from file
        try:
            with open(sys.argv[1], 'r') as f:
                conversation = json.load(f)
        except FileNotFoundError:
            print(f"Error: File '{sys.argv[1]}' not found")
            sys.exit(1)
        except json.JSONDecodeError:
            print(f"Error: Invalid JSON in file '{sys.argv[1]}'")
            sys.exit(1)
    else:
        # Read conversation from stdin
        try:
            conversation = json.load(sys.stdin)
        except json.JSONDecodeError:
            print("Error: Invalid JSON input")
            print("\nUsage:")
            print("  python conversation_summarizer.py <conversation.json>")
            print("  or")
            print("  echo '<json>' | python conversation_summarizer.py")
            sys.exit(1)
    
    summary = summarize_conversation(conversation)
    print(summary)


if __name__ == "__main__":
    main()
