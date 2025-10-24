# Eclipse GitHub Copilot Plugin

An Eclipse IDE plugin that integrates GitHub Copilot AI-powered code completion and suggestions directly into your Eclipse development environment.

## Overview

This plugin brings the power of GitHub Copilot to Eclipse IDE, providing intelligent code completions, suggestions, and AI-assisted coding capabilities. Leveraging OpenAI's advanced language models, it helps developers write code faster and with greater confidence.

## Features

- **Intelligent Code Completion**: Get AI-powered code suggestions as you type
- **Context-Aware Suggestions**: Receive recommendations based on your current code context and patterns
- **Multi-Language Support**: Works with Java, Python, JavaScript, and other popular programming languages
- **Inline Documentation**: Generate code comments and documentation automatically
- **Code Generation**: Create boilerplate code, functions, and classes from natural language descriptions
- **Eclipse Integration**: Seamlessly integrates with Eclipse's native editor and tooling
- **Customizable Settings**: Configure suggestion behavior, shortcuts, and preferences

## Prerequisites

Before installing the Eclipse GitHub Copilot Plugin, ensure you have:

- **Eclipse IDE**: Version 2021-06 (4.20) or later
  - Eclipse IDE for Java Developers
  - Eclipse IDE for Enterprise Java and Web Developers
  - Or any Eclipse IDE distribution with JDT support
- **Java**: JDK 11 or later
- **GitHub Copilot Subscription**: An active GitHub Copilot subscription (Individual, Business, or Enterprise)
- **Internet Connection**: Required for AI model communication

## Installation

### Option 1: Eclipse Marketplace (Recommended)

1. Open Eclipse IDE
2. Go to **Help** → **Eclipse Marketplace**
3. Search for "GitHub Copilot"
4. Click **Install** on the Eclipse GitHub Copilot Plugin
5. Follow the installation wizard and accept the license agreement
6. Restart Eclipse when prompted

### Option 2: Update Site Installation

1. Open Eclipse IDE
2. Go to **Help** → **Install New Software**
3. Click **Add** to add a new repository
4. Enter the following details:
   - Name: `GitHub Copilot Plugin`
   - Location: `[Update Site URL]`
5. Select the plugin from the available software list
6. Click **Next** and follow the installation wizard
7. Restart Eclipse when prompted

### Option 3: Manual Installation

1. Download the plugin JAR file from the [Releases](../../releases) page
2. Copy the JAR file to your Eclipse `plugins` directory
3. Restart Eclipse with the `-clean` flag: `eclipse -clean`

## Configuration

### Initial Setup

1. After installation, restart Eclipse
2. Go to **Window** → **Preferences** → **GitHub Copilot**
3. Click **Sign in to GitHub**
4. Authenticate with your GitHub account in the browser
5. Grant the necessary permissions for GitHub Copilot access
6. Return to Eclipse - you should now see "Authenticated" status

### Settings

Configure the plugin behavior through Eclipse preferences:

**Window** → **Preferences** → **GitHub Copilot**

Available settings:
- **Enable/Disable Suggestions**: Toggle Copilot suggestions on/off
- **Suggestion Trigger**: Configure when suggestions appear (automatic, manual, or on-demand)
- **Keybindings**: Customize keyboard shortcuts
  - Accept suggestion: `Tab` (default)
  - Next suggestion: `Alt + ]`
  - Previous suggestion: `Alt + [`
  - Dismiss suggestion: `Esc`
- **Language Support**: Select which file types should have Copilot enabled
- **Proxy Settings**: Configure proxy if working behind a firewall

## Usage

### Getting Started

1. Open any Java, Python, JavaScript, or supported code file
2. Start typing code - Copilot suggestions will appear in gray text
3. Press `Tab` to accept a suggestion or continue typing to ignore it
4. Use `Alt + ]` and `Alt + [` to cycle through multiple suggestions

### Example Workflows

#### Writing a Function from Comment

```java
// Function to calculate the factorial of a number
// [Copilot will suggest the complete function implementation]
```

#### Generating Unit Tests

```java
// Write a unit test for the calculateFactorial method
// [Copilot will suggest complete JUnit test code]
```

#### Creating Boilerplate Code

```java
// Create a REST controller for user management
// [Copilot will suggest controller class with CRUD endpoints]
```

### Best Practices

- Write clear, descriptive comments to guide Copilot suggestions
- Review and test all AI-generated code before committing
- Use Copilot as an assistant, not a replacement for understanding code
- Break down complex tasks into smaller, manageable pieces
- Provide context through meaningful variable names and function signatures

## Troubleshooting

### Common Issues

**Issue**: Copilot suggestions not appearing
- **Solution**: Check your authentication status in preferences
- Verify your GitHub Copilot subscription is active
- Ensure the file type is enabled in Copilot settings
- Try restarting Eclipse

**Issue**: Authentication fails
- **Solution**: Clear cached credentials and sign in again
- Check your internet connection
- Verify GitHub service status at [githubstatus.com](https://www.githubstatus.com)

**Issue**: Slow suggestions or timeouts
- **Solution**: Check your network connection
- Configure proxy settings if behind a firewall
- Verify Eclipse has sufficient memory allocated (increase in eclipse.ini)

**Issue**: Plugin conflicts
- **Solution**: Update all plugins to latest versions
- Check for conflicting keybindings in **Window** → **Preferences** → **General** → **Keys**

### Logs and Diagnostics

View plugin logs for troubleshooting:
1. Go to **Window** → **Show View** → **Error Log**
2. Look for entries related to "GitHub Copilot" or "Copilot Plugin"
3. Share relevant log entries when reporting issues

## Development

### Building from Source

```bash
# Clone the repository
git clone https://github.com/ethanyhou/testRepo.git
cd testRepo

# Build with Maven
mvn clean install

# The built plugin will be in target/plugins/
```

### Development Environment Setup

1. Install Eclipse IDE for RCP and RAP Developers
2. Import the project as an existing Maven project
3. Set target platform to match Eclipse version
4. Run as Eclipse Application for testing

### Project Structure

```
testRepo/
├── plugins/              # Plugin source code
├── features/             # Feature definitions
├── tests/                # Unit and integration tests
├── target/               # Build output
└── README.md            # This file
```

## Contributing

We welcome contributions! Please follow these guidelines:

1. **Fork the repository** and create a feature branch
2. **Write tests** for new features or bug fixes
3. **Follow code style**: Use Eclipse formatter settings (included in project)
4. **Update documentation** as needed
5. **Submit a pull request** with a clear description of changes

### Code of Conduct

- Be respectful and inclusive
- Provide constructive feedback
- Focus on what is best for the community

### Reporting Issues

Found a bug or have a feature request? Please:
1. Check existing issues to avoid duplicates
2. Use issue templates when available
3. Provide detailed reproduction steps
4. Include Eclipse version, Java version, and OS information

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## Privacy and Data

GitHub Copilot processes code snippets to provide suggestions. Please review:
- [GitHub Copilot Privacy Statement](https://docs.github.com/en/site-policy/privacy-policies/github-copilot-privacy-statement)
- [GitHub Copilot Terms](https://github.com/features/copilot/terms)

This plugin does not collect or store any personal data beyond what is necessary for GitHub Copilot functionality.

## Support

### Documentation

- [GitHub Copilot Official Documentation](https://docs.github.com/en/copilot)
- [Eclipse Plugin Development Guide](https://www.eclipse.org/articles/)

### Getting Help

- **Issues**: Report bugs or request features via [GitHub Issues](../../issues)
- **Discussions**: Ask questions in [GitHub Discussions](../../discussions)
- **Wiki**: Check the [project wiki](../../wiki) for guides and FAQs

### Contact

- **Project Maintainer**: [Your Name/Team]
- **Email**: [contact@example.com]
- **GitHub**: [@ethanyhou](https://github.com/ethanyhou)

## Acknowledgments

- Thanks to GitHub and OpenAI for the Copilot technology
- Eclipse Foundation for the IDE platform
- All contributors who help improve this plugin

## Roadmap

- [ ] Enhanced multi-language support
- [ ] Copilot Chat integration
- [ ] Customizable suggestion templates
- [ ] Offline mode with cached suggestions
- [ ] Team collaboration features
- [ ] Plugin marketplace improvements

---

**Note**: This is a third-party plugin and is not officially affiliated with GitHub or Microsoft. GitHub Copilot is a trademark of GitHub, Inc.