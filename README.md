# testRepo - Conversation Summarizer Tool

A simple tool for summarizing conversations in a structured format.

## Overview

This repository provides a Python-based conversation summarizer that takes conversation data and generates structured summaries following a specific format with the following sections:

- **Title**: A brief title for the conversation
- **User Intent**: What the user is trying to accomplish
- **Task Description**: Detailed description of the task
- **Existing**: What has already been done or accomplished
- **Pending**: What still needs to be done
- **Code State**: Status of any code discussed or modified
- **Relevant Code/Documentation Snippets**: Important code or documentation references
- **Other Notes**: Additional relevant information

## Installation

No special installation required. Just ensure you have Python 3.6+ installed:

```bash
python3 --version
```

## Usage

### Command Line

To summarize a conversation from a JSON file:

```bash
python3 conversation_summarizer.py example_conversation.json
```

### Python API

You can also use the tool programmatically:

```python
from conversation_summarizer import ConversationSummarizer

# Create summarizer instance
summarizer = ConversationSummarizer()

# Add messages
summarizer.add_message('user', 'Hi')
summarizer.add_message('assistant', 'Hello! How can I help you?')
summarizer.add_message('user', 'I need help with Python')

# Generate summary
summary = summarizer.summarize()

# Print formatted summary
print(summarizer.format_summary(summary))
```

### Conversation Format

Conversations should be provided as JSON arrays with message objects containing `role` and `content` fields:

```json
[
    {
        "role": "user",
        "content": "Hi"
    },
    {
        "role": "assistant",
        "content": "Hello! How can I help you today?"
    }
]
```

## Examples

### Example 1: Simple Greeting

Input (`example_conversation.json`):
```json
[
    {
        "role": "user",
        "content": "Hi"
    }
]
```

Output:
```
# CONVERSATION SUMMARY

## TITLE
Initial Conversation Request

## USER INTENT
The user is initiating a conversation and requesting a summary, but no actual conversation content has been provided yet.

## TASK DESCRIPTION
No technical task has been described. The user has only sent a greeting and may be requesting assistance.

...
```

### Example 2: Full Conversation

See `example_full_conversation.json` for a more complete example with multiple messages and task details.

## Testing

To test the tool with the provided examples:

```bash
# Test with simple greeting
python3 conversation_summarizer.py example_conversation.json

# Test with full conversation
python3 conversation_summarizer.py example_full_conversation.json
```

## Features

- ✅ Structured summary format
- ✅ Support for multiple message types (user, assistant, system)
- ✅ Automatic intent extraction
- ✅ Task identification
- ✅ Code state tracking
- ✅ JSON file input support
- ✅ Python API for programmatic use

## Contributing

Feel free to open issues or submit pull requests to improve the tool.

## License

MIT License