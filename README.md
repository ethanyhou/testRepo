# Eclipse GitHub Copilot Plugin

An Eclipse plugin that integrates GitHub Copilot into the Eclipse IDE, bringing AI-powered code completion and suggestions directly to your Eclipse development environment.

## Table of Contents

- [Overview](#overview)
- [Features](#features)
- [Prerequisites](#prerequisites)
- [Installation](#installation)
- [Usage](#usage)
- [Development Setup](#development-setup)
- [Building the Plugin](#building-the-plugin)
- [Testing](#testing)
- [Contributing](#contributing)
- [License](#license)
- [Support](#support)

## Overview

The Eclipse GitHub Copilot Plugin provides seamless integration of GitHub Copilot's AI-powered code suggestions into the Eclipse IDE. This plugin enables developers to leverage Copilot's capabilities while working in their familiar Eclipse environment, enhancing productivity and code quality.

## Features

- **AI-Powered Code Completion**: Get intelligent code suggestions as you type
- **Context-Aware Suggestions**: Receive recommendations based on your current code context
- **Multi-Language Support**: Works with Java, Python, JavaScript, and other languages supported by Eclipse
- **Inline Documentation**: Generate code comments and documentation automatically
- **Code Refactoring Assistance**: Get suggestions for improving existing code
- **Eclipse Integration**: Native integration with Eclipse's editor and UI components
- **Customizable Settings**: Configure Copilot behavior to match your workflow

## Prerequisites

Before installing the Eclipse GitHub Copilot Plugin, ensure you have:

- **Eclipse IDE**: Version 2021-06 (4.20) or later
  - Eclipse IDE for Java Developers
  - Eclipse IDE for Enterprise Java and Web Developers
  - Or any Eclipse distribution with JDT (Java Development Tools)
- **Java Runtime Environment**: JRE 11 or later
- **GitHub Copilot Subscription**: An active GitHub Copilot subscription (Individual, Business, or Enterprise)
- **Internet Connection**: Required for Copilot API access

## Installation

### Installing from Eclipse Marketplace

1. Open Eclipse IDE
2. Navigate to **Help** → **Eclipse Marketplace**
3. Search for "GitHub Copilot"
4. Click **Install** next to the Eclipse GitHub Copilot Plugin
5. Follow the installation wizard and accept the license agreement
6. Restart Eclipse when prompted

### Installing from Update Site

1. Open Eclipse IDE
2. Navigate to **Help** → **Install New Software**
3. Click **Add** to add a new repository
4. Enter the following details:
   - Name: `GitHub Copilot for Eclipse`
   - Location: `https://update-site-url-here` (replace with actual update site URL)
5. Select the plugin from the list
6. Click **Next** and follow the installation wizard
7. Restart Eclipse when prompted

### Manual Installation

1. Download the plugin JAR file from the releases page
2. Copy the JAR file to your Eclipse `plugins` directory
3. Restart Eclipse
4. The plugin should be automatically detected and loaded

## Usage

### Initial Setup

1. After installation, navigate to **Window** → **Preferences** → **GitHub Copilot**
2. Click **Sign in to GitHub** and authenticate with your GitHub account
3. Verify that your GitHub Copilot subscription is active
4. Configure your preferences (optional)

### Getting Code Suggestions

1. Open any supported file in the Eclipse editor (e.g., `.java`, `.py`, `.js`)
2. Start typing your code
3. Copilot will automatically provide suggestions as you type
4. Press **Tab** to accept a suggestion or **Esc** to dismiss it
5. Use **Alt + ]** to see the next suggestion
6. Use **Alt + [** to see the previous suggestion

### Generating Code from Comments

1. Write a descriptive comment explaining what you want to accomplish
   ```java
   // Function to calculate the factorial of a number
   ```
2. Press **Enter** to create a new line
3. Copilot will suggest an implementation
4. Press **Tab** to accept the suggestion

### Keyboard Shortcuts

- **Tab**: Accept the current suggestion
- **Esc**: Dismiss the current suggestion
- **Alt + ]**: Next suggestion
- **Alt + [**: Previous suggestion
- **Alt + \**: Show all suggestions (inline)
- **Ctrl + Enter**: Open Copilot suggestions panel

## Development Setup

### Environment Setup

1. **Clone the repository**:
   ```bash
   git clone https://github.com/your-org/eclipse-copilot-plugin.git
   cd eclipse-copilot-plugin
   ```

2. **Install Eclipse PDE (Plugin Development Environment)**:
   - Download Eclipse IDE for RCP and RAP Developers, or
   - Install PDE in your existing Eclipse: **Help** → **Install New Software** → Select your Eclipse version → **Eclipse Plugin Development Tools**

3. **Import the project**:
   - Open Eclipse
   - **File** → **Import** → **Existing Projects into Workspace**
   - Select the cloned repository directory
   - Click **Finish**

### Dependencies

The plugin requires the following dependencies:

- **Eclipse Platform**: 4.20 or later
- **Eclipse JDT**: For Java development support
- **Eclipse UI**: For editor integration
- **GitHub Copilot API Client**: Included in the plugin
- **LSP4J** (Language Server Protocol for Java): For language server integration

Dependencies are managed through the `META-INF/MANIFEST.MF` and `feature.xml` files.

### Project Structure

```
eclipse-copilot-plugin/
├── plugin/                 # Main plugin project
│   ├── src/               # Source code
│   ├── META-INF/          # Plugin manifest
│   └── plugin.xml         # Plugin configuration
├── feature/               # Feature project
│   └── feature.xml        # Feature configuration
├── update-site/           # Update site project
├── tests/                 # Test projects
└── README.md             # This file
```

## Building the Plugin

### Prerequisites for Building

- **Maven**: 3.6.0 or later
- **Java JDK**: 11 or later
- **Tycho**: Maven plugin for Eclipse (included in pom.xml)

### Build Instructions

1. **Build using Maven**:
   ```bash
   mvn clean verify
   ```

2. **Build using Eclipse**:
   - Right-click on the project → **Export** → **Deployable plug-ins and fragments**
   - Select the destination directory
   - Click **Finish**

3. **Create Update Site**:
   ```bash
   mvn clean install -P build-update-site
   ```

The built plugin will be available in the `target` directory.

## Testing

### Running Unit Tests

```bash
mvn clean test
```

### Running Integration Tests

```bash
mvn clean verify -P integration-tests
```

### Manual Testing

1. Launch a runtime Eclipse instance:
   - Right-click on the plugin project → **Run As** → **Eclipse Application**
2. A new Eclipse instance will launch with the plugin installed
3. Test the plugin functionality in this runtime instance

### Writing Tests

Tests are located in the `tests/` directory. Follow the existing test patterns:

- Use JUnit 4 or 5 for unit tests
- Use SWTBot for UI tests
- Use Mockito for mocking dependencies

## Contributing

We welcome contributions to the Eclipse GitHub Copilot Plugin! Here's how you can help:

### Reporting Issues

1. Check the [issue tracker](https://github.com/your-org/eclipse-copilot-plugin/issues) for existing issues
2. Create a new issue with:
   - Clear description of the problem
   - Steps to reproduce
   - Expected vs actual behavior
   - Eclipse version and OS information
   - Plugin version

### Submitting Pull Requests

1. Fork the repository
2. Create a new branch for your feature:
   ```bash
   git checkout -b feature/your-feature-name
   ```
3. Make your changes following the coding standards
4. Add or update tests as needed
5. Ensure all tests pass:
   ```bash
   mvn clean verify
   ```
6. Commit your changes with a clear message
7. Push to your fork and submit a pull request

### Coding Standards

- Follow Eclipse Java code formatting conventions
- Use meaningful variable and method names
- Add JavaDoc comments for public APIs
- Keep methods focused and concise
- Write unit tests for new functionality
- Ensure backward compatibility when possible

### Development Guidelines

- Use Eclipse PDE best practices
- Follow OSGi bundle conventions
- Handle errors gracefully
- Log appropriate information for debugging
- Respect user privacy and data security
- Test on multiple Eclipse versions

## License

This project is licensed under the [MIT License](LICENSE) - see the LICENSE file for details.

### Third-Party Licenses

This plugin uses the following third-party components:

- **GitHub Copilot API**: Subject to GitHub Copilot Terms of Service
- **Eclipse Platform**: Eclipse Public License 2.0
- **LSP4J**: Eclipse Public License 2.0

## Support

### Getting Help

- **Documentation**: See the [Wiki](https://github.com/your-org/eclipse-copilot-plugin/wiki) for detailed documentation
- **FAQ**: Check the [Frequently Asked Questions](https://github.com/your-org/eclipse-copilot-plugin/wiki/FAQ)
- **Issues**: Report bugs or request features via [GitHub Issues](https://github.com/your-org/eclipse-copilot-plugin/issues)
- **Discussions**: Join the conversation in [GitHub Discussions](https://github.com/your-org/eclipse-copilot-plugin/discussions)

### GitHub Copilot Support

For issues related to GitHub Copilot itself (not the Eclipse integration):

- [GitHub Copilot Documentation](https://docs.github.com/en/copilot)
- [GitHub Support](https://support.github.com/)

### Security Issues

If you discover a security vulnerability, please email security@your-org.com instead of using the issue tracker.

---

**Note**: This plugin is not officially affiliated with or endorsed by GitHub or Microsoft. GitHub Copilot is a trademark of GitHub, Inc.