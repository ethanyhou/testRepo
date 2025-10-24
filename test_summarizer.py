#!/usr/bin/env python3
"""
Simple tests for the conversation summarizer.
"""

from conversation_summarizer import ConversationSummarizer


def test_empty_conversation():
    """Test summarizing an empty conversation."""
    summarizer = ConversationSummarizer()
    summary = summarizer.summarize()
    
    assert summary['title'] == 'Empty Conversation'
    assert 'No conversation provided' in summary['user_intent']
    print("✓ Empty conversation test passed")


def test_greeting_only():
    """Test summarizing a conversation with just a greeting."""
    summarizer = ConversationSummarizer()
    summarizer.add_message('user', 'Hi')
    summary = summarizer.summarize()
    
    assert summary['title'] == 'Initial Conversation Request'
    assert 'initiating a conversation' in summary['user_intent']
    print("✓ Greeting only test passed")


def test_multiple_messages():
    """Test summarizing a conversation with multiple messages."""
    summarizer = ConversationSummarizer()
    summarizer.add_message('user', 'Can you help me with Python?')
    summarizer.add_message('assistant', 'Of course! What do you need help with?')
    summarizer.add_message('user', 'I need to create a data processing script.')
    summary = summarizer.summarize()
    
    assert summary['title'] == 'Conversation Summary'
    assert 'Python' in summary['user_intent'] or 'Python' in summary['task_description']
    print("✓ Multiple messages test passed")


def test_format_summary():
    """Test that formatting produces valid output."""
    summarizer = ConversationSummarizer()
    summarizer.add_message('user', 'Hello')
    summary = summarizer.summarize()
    formatted = summarizer.format_summary(summary)
    
    assert '# CONVERSATION SUMMARY' in formatted
    assert '## TITLE' in formatted
    assert '## USER INTENT' in formatted
    print("✓ Format summary test passed")


def test_load_from_dict():
    """Test loading conversation from a dictionary."""
    summarizer = ConversationSummarizer()
    conversation = [
        {'role': 'user', 'content': 'Test message'},
        {'role': 'assistant', 'content': 'Test response'}
    ]
    summarizer.load_from_dict(conversation)
    
    assert len(summarizer.conversation) == 2
    assert summarizer.conversation[0]['role'] == 'user'
    print("✓ Load from dict test passed")


def run_all_tests():
    """Run all tests."""
    print("Running conversation summarizer tests...\n")
    
    test_empty_conversation()
    test_greeting_only()
    test_multiple_messages()
    test_format_summary()
    test_load_from_dict()
    
    print("\n✅ All tests passed!")


if __name__ == '__main__':
    run_all_tests()
