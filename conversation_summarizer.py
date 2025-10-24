#!/usr/bin/env python3
"""
Conversation Summarizer Tool

This tool provides functionality to summarize conversations following a structured format.
"""

import json
import sys
from typing import List, Dict, Optional


class ConversationSummarizer:
    """
    A tool to summarize conversations with a structured format.
    """
    
    def __init__(self):
        self.conversation = []
    
    def add_message(self, role: str, content: str):
        """
        Add a message to the conversation.
        
        Args:
            role: The role of the speaker (e.g., 'user', 'assistant', 'system')
            content: The content of the message
        """
        self.conversation.append({
            'role': role,
            'content': content
        })
    
    def load_from_dict(self, conversation: List[Dict[str, str]]):
        """
        Load conversation from a list of message dictionaries.
        
        Args:
            conversation: List of message dictionaries with 'role' and 'content' keys
        """
        self.conversation = conversation
    
    def summarize(self) -> Dict[str, str]:
        """
        Generate a structured summary of the conversation.
        
        Returns:
            A dictionary containing the summary with keys:
            - title
            - user_intent
            - task_description
            - existing
            - pending
            - code_state
            - relevant_snippets
            - notes
        """
        if not self.conversation:
            return {
                'title': 'Empty Conversation',
                'user_intent': 'No conversation provided',
                'task_description': 'No task described',
                'existing': '- No prior work mentioned',
                'pending': '- Conversation content needs to be provided',
                'code_state': 'No code discussed',
                'relevant_snippets': 'None available',
                'notes': 'The conversation is empty.'
            }
        
        # Analyze conversation
        user_messages = [msg for msg in self.conversation if msg['role'] == 'user']
        assistant_messages = [msg for msg in self.conversation if msg['role'] == 'assistant']
        
        # Extract key information
        first_user_message = user_messages[0]['content'] if user_messages else ''
        
        # Determine if it's a greeting or actual content
        is_greeting = first_user_message.strip().lower() in ['hi', 'hello', 'hey', 'greetings']
        
        if is_greeting and len(user_messages) == 1:
            return {
                'title': 'Initial Conversation Request',
                'user_intent': 'The user is initiating a conversation and requesting a summary, but no actual conversation content has been provided yet.',
                'task_description': 'No technical task has been described. The user has only sent a greeting and may be requesting assistance.',
                'existing': '- No prior work or accomplishments mentioned\n- No files referenced\n- No code discussed',
                'pending': '- The user needs to provide the actual conversation content or task description\n- Once provided, a detailed summary can be created following the specified format',
                'code_state': 'No files have been discussed or modified.',
                'relevant_snippets': 'None available - no conversation content was provided.',
                'notes': 'The user appears to have initiated contact but has not yet provided specific task details or conversation content to summarize.'
            }
        
        # For non-greeting conversations, provide basic analysis
        return {
            'title': 'Conversation Summary',
            'user_intent': self._extract_intent(user_messages),
            'task_description': self._extract_task(user_messages),
            'existing': self._extract_existing(self.conversation),
            'pending': self._extract_pending(self.conversation),
            'code_state': self._extract_code_state(self.conversation),
            'relevant_snippets': self._extract_snippets(self.conversation),
            'notes': self._extract_notes(self.conversation)
        }
    
    def _extract_intent(self, user_messages: List[Dict[str, str]]) -> str:
        """Extract user intent from messages."""
        if not user_messages:
            return 'No clear intent identified'
        
        # Simple heuristic: look at first substantial message
        for msg in user_messages:
            content = msg['content'].strip()
            if len(content) > 10:  # More than just a greeting
                return f"User is requesting: {content[:200]}..."
        
        return 'User intent unclear from brief messages'
    
    def _extract_task(self, user_messages: List[Dict[str, str]]) -> str:
        """Extract task description."""
        tasks = []
        for msg in user_messages:
            content = msg['content'].lower()
            if any(keyword in content for keyword in ['please', 'can you', 'need', 'want', 'help', 'create', 'fix', 'update']):
                tasks.append(msg['content'][:200])
        
        return '\n'.join(tasks) if tasks else 'No specific task described'
    
    def _extract_existing(self, conversation: List[Dict[str, str]]) -> str:
        """Extract information about existing work."""
        existing = []
        for msg in conversation:
            content = msg['content'].lower()
            if any(keyword in content for keyword in ['already', 'existing', 'current', 'have']):
                existing.append(f"- {msg['content'][:100]}")
        
        return '\n'.join(existing) if existing else '- No prior work mentioned'
    
    def _extract_pending(self, conversation: List[Dict[str, str]]) -> str:
        """Extract pending items."""
        pending = []
        for msg in conversation:
            content = msg['content'].lower()
            if any(keyword in content for keyword in ['need to', 'should', 'must', 'pending', 'todo', 'will']):
                pending.append(f"- {msg['content'][:100]}")
        
        return '\n'.join(pending) if pending else '- No pending items identified'
    
    def _extract_code_state(self, conversation: List[Dict[str, str]]) -> str:
        """Extract code state information."""
        code_mentions = []
        for msg in conversation:
            content = msg['content']
            if any(keyword in content.lower() for keyword in ['code', 'file', 'function', 'class', 'script']):
                code_mentions.append(msg['content'][:100])
        
        return '\n'.join(code_mentions) if code_mentions else 'No code discussed'
    
    def _extract_snippets(self, conversation: List[Dict[str, str]]) -> str:
        """Extract relevant code snippets."""
        snippets = []
        for msg in conversation:
            content = msg['content']
            # Look for code blocks
            if '```' in content or 'def ' in content or 'class ' in content:
                snippets.append(content[:200])
        
        return '\n'.join(snippets) if snippets else 'None available'
    
    def _extract_notes(self, conversation: List[Dict[str, str]]) -> str:
        """Extract additional notes."""
        return f'Conversation contains {len(conversation)} messages with {len([m for m in conversation if m["role"] == "user"])} user messages.'
    
    def format_summary(self, summary: Dict[str, str]) -> str:
        """
        Format the summary dictionary into a readable text format.
        
        Args:
            summary: The summary dictionary
            
        Returns:
            Formatted summary text
        """
        formatted = f"""# CONVERSATION SUMMARY

## TITLE
{summary['title']}

## USER INTENT
{summary['user_intent']}

## TASK DESCRIPTION
{summary['task_description']}

## EXISTING
{summary['existing']}

## PENDING
{summary['pending']}

## CODE STATE
{summary['code_state']}

## RELEVANT CODE/DOCUMENTATION SNIPPETS
{summary['relevant_snippets']}

## OTHER NOTES
{summary['notes']}
"""
        return formatted


def main():
    """Main function for CLI usage."""
    if len(sys.argv) < 2:
        print("Usage: python conversation_summarizer.py <conversation_file.json>")
        print("\nOr use interactively:")
        print("  from conversation_summarizer import ConversationSummarizer")
        print("  summarizer = ConversationSummarizer()")
        print("  summarizer.add_message('user', 'Hello')")
        print("  summary = summarizer.summarize()")
        print("  print(summarizer.format_summary(summary))")
        sys.exit(1)
    
    # Load conversation from JSON file
    with open(sys.argv[1], 'r') as f:
        conversation_data = json.load(f)
    
    summarizer = ConversationSummarizer()
    summarizer.load_from_dict(conversation_data)
    
    summary = summarizer.summarize()
    print(summarizer.format_summary(summary))


if __name__ == '__main__':
    main()
