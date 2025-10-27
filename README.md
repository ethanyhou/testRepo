# testRepo

## Conversation Summarizer Tool

A tool that takes conversation history (user/assistant message pairs) and creates detailed summaries with a structured format.

### Features

The summarizer produces summaries with the following sections:
- **TITLE**: Brief title derived from the conversation
- **USER INTENT**: What the user is seeking assistance with
- **TASK DESCRIPTION**: Specific tasks identified in the conversation
- **EXISTING**: Current state information
- **PENDING**: Outstanding items that need attention
- **CODE STATE**: Information about code discussed
- **RELEVANT CODE/DOCUMENTATION SNIPPETS**: Code references from the conversation
- **OTHER NOTES**: Additional metadata about the conversation

### Usage

```bash
# Run with a conversation file
python conversation_summarizer.py example_conversations/minimal.json

# Or pipe JSON input
echo '[{"role":"user","content":"Hi"},{"role":"assistant","content":"Hello!"}]' | python conversation_summarizer.py
```

### Input Format

The tool expects a JSON array of message objects with the following structure:

```json
[
  {
    "role": "user",
    "content": "Your message here"
  },
  {
    "role": "assistant",
    "content": "Assistant response here"
  }
]
```

### Examples

See the `example_conversations/` directory for sample inputs:
- `minimal.json`: A short greeting conversation
- `full.json`: A detailed technical conversation about OAuth2 implementation

### Special Handling

When the conversation contains only brief greetings (like "Hi" and "Hihi"), the tool provides helpful guidance:

```
I don't see a conversation to summarize in your messages. You've only sent brief greetings so far.

Could you please provide the conversation history (the series of user/assistant message pairs) 
that you'd like me to summarize? Once you share the conversation, I'll create a detailed summary 
following the format you've specified:

- TITLE
- USER INTENT
- TASK DESCRIPTION
- EXISTING
- PENDING
- CODE STATE
- RELEVANT CODE/DOCUMENTATION SNIPPETS
- OTHER NOTES

Please paste the conversation you'd like summarized, and I'll help you right away!
```