# Eclipse GitHub Copilot Plugin

An Eclipse IDE plugin that integrates GitHub Copilot functionality, bringing AI-powered code completion and suggestions directly into your Eclipse development environment.

## Overview

This plugin enables developers using Eclipse IDE to leverage GitHub Copilot's AI capabilities for intelligent code suggestions, autocompletion, and coding assistance. It seamlessly integrates with Eclipse's editor to provide contextual code recommendations as you type.

## Features

- **AI-Powered Code Completion**: Get intelligent code suggestions based on your current context and coding patterns
- **Multi-Language Support**: Works with various programming languages supported by Eclipse
- **Contextual Suggestions**: Receives recommendations based on your code comments, function names, and existing code
- **Inline Documentation**: Automatically suggests code comments and documentation
- **Code Generation**: Generate entire functions or code blocks from natural language descriptions
- **Test Generation**: Assistance in creating unit tests for your code
- **Seamless Eclipse Integration**: Native integration with Eclipse editor and UI

## Prerequisites

Before installing this plugin, ensure you have:

- **Eclipse IDE**: Version 2021-03 (4.19) or later
  - Eclipse IDE for Java Developers
  - Eclipse IDE for Enterprise Java and Web Developers
  - Or any Eclipse distribution with plugin installation capabilities
- **Java Development Kit (JDK)**: JDK 11 or later
- **GitHub Copilot Subscription**: An active GitHub Copilot subscription
  - Individual, Business, or Enterprise plan
  - You can sign up at [github.com/features/copilot](https://github.com/features/copilot)
- **GitHub Account**: A GitHub account linked to your Copilot subscription
- **Internet Connection**: Required for communicating with GitHub Copilot services

## Installation

### Install from Eclipse Marketplace

1. Open Eclipse IDE
2. Go to **Help** → **Eclipse Marketplace**
3. Search for "GitHub Copilot"
4. Click **Install** on the Eclipse GitHub Copilot Plugin
5. Follow the installation wizard prompts
6. Restart Eclipse when prompted

### Install from Update Site

1. Open Eclipse IDE
2. Go to **Help** → **Install New Software**
3. Click **Add** to add a new update site
4. Enter the following details:
   - Name: `GitHub Copilot for Eclipse`
   - Location: `[Update Site URL]`
5. Select the GitHub Copilot Plugin from the available software list
6. Click **Next** and follow the installation wizard
7. Accept the license agreement
8. Restart Eclipse when prompted

### Manual Installation

1. Download the plugin JAR file from the releases page
2. Copy the JAR file to your Eclipse `plugins` directory
3. Restart Eclipse with the `-clean` flag:
   ```bash
   eclipse -clean
   ```

## Configuration

### Initial Setup

1. After installation, go to **Window** → **Preferences** (or **Eclipse** → **Preferences** on macOS)
2. Navigate to **GitHub Copilot**
3. Click **Sign in to GitHub**
4. Follow the authentication flow in your web browser
5. Authorize the Eclipse GitHub Copilot Plugin
6. Return to Eclipse to confirm successful authentication

### Settings

Configure plugin behavior under **Window** → **Preferences** → **GitHub Copilot**:

- **Enable/Disable Copilot**: Toggle GitHub Copilot on or off
- **Suggestion Delay**: Adjust the delay before suggestions appear (in milliseconds)
- **Auto-trigger**: Enable or disable automatic suggestion triggering
- **Language Preferences**: Configure language-specific settings
- **Telemetry**: Opt in or out of usage data collection

## Usage

### Basic Usage

1. **Start Coding**: Open any source file in Eclipse
2. **Receive Suggestions**: As you type, GitHub Copilot will provide suggestions
3. **Accept Suggestions**: 
   - Press `Tab` to accept the current suggestion
   - Press `Esc` to dismiss suggestions
4. **Cycle Through Suggestions**: Use `Alt+]` (next) or `Alt+[` (previous) to cycle through alternative suggestions

### Advanced Features

#### Generate Code from Comments

1. Write a descriptive comment explaining what you want to code:
   ```java
   // Function to calculate the fibonacci sequence up to n terms
   ```
2. Press `Enter` and wait for Copilot to suggest the implementation
3. Review and accept the suggestion

#### Generate Unit Tests

1. Place your cursor in a test file
2. Write a comment describing the test:
   ```java
   // Test that the user authentication fails with invalid credentials
   ```
3. Accept Copilot's suggested test implementation

### Keyboard Shortcuts

| Action | Windows/Linux | macOS |
|--------|---------------|-------|
| Accept suggestion | `Tab` | `Tab` |
| Dismiss suggestion | `Esc` | `Esc` |
| Next suggestion | `Alt+]` | `Option+]` |
| Previous suggestion | `Alt+[` | `Option+[` |
| Trigger suggestion manually | `Alt+\` | `Option+\` |
| Open Copilot panel | `Ctrl+Shift+A` | `Cmd+Shift+A` |

### Status Bar

The GitHub Copilot status indicator in the Eclipse status bar shows:
- ✓ Green: Copilot is active and connected
- ⚠ Yellow: Copilot is active but experiencing issues
- ✗ Red: Copilot is disabled or not authenticated

## Development Setup

### Prerequisites for Development

- Eclipse IDE for Eclipse Committers (2021-03 or later)
- Eclipse Plugin Development Environment (PDE)
- JDK 11 or later
- Maven 3.6+ or Tycho build tools
- Git

### Building from Source

1. **Clone the Repository**:
   ```bash
   git clone https://github.com/[your-org]/eclipse-github-copilot.git
   cd eclipse-github-copilot
   ```

2. **Import into Eclipse**:
   - Open Eclipse IDE for Eclipse Committers
   - Go to **File** → **Import** → **Existing Projects into Workspace**
   - Select the cloned repository directory
   - Import all projects

3. **Set Target Platform**:
   - Open the target definition file (`.target` file)
   - Click **Set as Target Platform**
   - Wait for dependencies to resolve

4. **Build the Project**:
   - Right-click on the project
   - Select **Run As** → **Maven build**
   - Or build from command line:
     ```bash
     mvn clean install
     ```

### Running in Development Mode

1. Right-click on the plugin project
2. Select **Run As** → **Eclipse Application**
3. A new Eclipse instance will launch with the plugin installed
4. Test your changes in this runtime instance

### Project Structure

```
eclipse-github-copilot/
├── plugin/                 # Main plugin code
│   ├── src/               # Java source files
│   ├── META-INF/          # Plugin metadata
│   └── plugin.xml         # Plugin configuration
├── feature/               # Eclipse feature definition
├── update-site/           # Update site project
├── tests/                 # Unit and integration tests
├── docs/                  # Documentation
├── .github/               # GitHub Actions workflows
└── pom.xml               # Maven POM file
```

## Troubleshooting

### Plugin Not Showing Suggestions

1. **Check Authentication**:
   - Go to **Window** → **Preferences** → **GitHub Copilot**
   - Verify you're signed in
   - Try signing out and signing back in

2. **Verify Copilot Status**:
   - Check the status bar for the Copilot indicator
   - Ensure it shows as active (green)

3. **Check Internet Connection**:
   - Copilot requires an active internet connection
   - Verify your network settings and proxy configuration

### Suggestions Are Slow

1. **Adjust Suggestion Delay**:
   - Go to **Preferences** → **GitHub Copilot**
   - Reduce the suggestion delay setting

2. **Check Network Latency**:
   - High network latency can slow down suggestions
   - Consider your network connection quality

### Plugin Not Loading

1. **Verify Eclipse Version**:
   - Ensure you're using Eclipse 2021-03 or later
   - Update Eclipse if necessary

2. **Check Plugin Installation**:
   - Go to **Help** → **About Eclipse** → **Installation Details**
   - Verify the GitHub Copilot Plugin is listed

3. **Clean Workspace**:
   ```bash
   eclipse -clean
   ```

### Authentication Issues

1. **Clear Authentication Cache**:
   - Go to **Preferences** → **GitHub Copilot**
   - Click **Sign Out** then **Sign In** again

2. **Check Copilot Subscription**:
   - Verify your GitHub Copilot subscription is active at [github.com/settings/copilot](https://github.com/settings/copilot)

3. **Browser Authentication**:
   - Ensure your default browser is configured correctly
   - Try a different browser for authentication if issues persist

## Contributing

We welcome contributions from the community! Here's how you can help:

### Reporting Issues

1. Check existing issues to avoid duplicates
2. Create a new issue with:
   - Clear, descriptive title
   - Steps to reproduce the problem
   - Expected vs actual behavior
   - Eclipse version and OS information
   - Plugin version
   - Relevant logs from Eclipse Error Log view

### Submitting Pull Requests

1. **Fork the Repository**
2. **Create a Feature Branch**:
   ```bash
   git checkout -b feature/your-feature-name
   ```
3. **Make Your Changes**:
   - Follow the existing code style
   - Add tests for new functionality
   - Update documentation as needed
4. **Commit Your Changes**:
   ```bash
   git commit -m "Add feature: description of your changes"
   ```
5. **Push to Your Fork**:
   ```bash
   git push origin feature/your-feature-name
   ```
6. **Create a Pull Request**:
   - Provide a clear description of your changes
   - Reference any related issues
   - Ensure all tests pass

### Development Guidelines

- Follow Eclipse plugin development best practices
- Write unit tests for new features
- Maintain backward compatibility when possible
- Update documentation for user-facing changes
- Use meaningful commit messages
- Keep pull requests focused on a single feature or fix

### Code Style

- Follow standard Java coding conventions
- Use 4 spaces for indentation (no tabs)
- Maximum line length: 120 characters
- Use meaningful variable and method names
- Add JavaDoc comments for public APIs

## License

This project is licensed under the [MIT License](LICENSE) - see the LICENSE file for details.

## Acknowledgments

- GitHub Copilot team for the AI technology
- Eclipse Foundation for the plugin framework
- All contributors who have helped improve this plugin

## Support

- **Documentation**: See the [Wiki](https://github.com/[your-org]/eclipse-github-copilot/wiki) for detailed guides
- **Issues**: Report bugs and request features via [GitHub Issues](https://github.com/[your-org]/eclipse-github-copilot/issues)
- **Discussions**: Join the conversation in [GitHub Discussions](https://github.com/[your-org]/eclipse-github-copilot/discussions)
- **Stack Overflow**: Tag questions with `eclipse-copilot`

## Changelog

See [CHANGELOG.md](CHANGELOG.md) for a list of changes in each version.

## Privacy and Telemetry

This plugin communicates with GitHub's servers to provide Copilot suggestions. Please review:
- [GitHub Copilot Privacy Statement](https://docs.github.com/en/site-policy/privacy-policies/github-copilot-privacy-statement)
- Plugin telemetry settings in **Preferences** → **GitHub Copilot**

## Related Projects

- [GitHub Copilot for Visual Studio Code](https://marketplace.visualstudio.com/items?itemName=GitHub.copilot)
- [GitHub Copilot for JetBrains IDEs](https://plugins.jetbrains.com/plugin/17718-github-copilot)
- [GitHub Copilot for Visual Studio](https://visualstudio.microsoft.com/github-copilot/)

---

**Note**: This is an unofficial Eclipse plugin for GitHub Copilot. For official GitHub Copilot support, please visit [github.com/features/copilot](https://github.com/features/copilot).