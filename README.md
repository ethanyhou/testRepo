# Eclipse GitHub Copilot Plugin

An Eclipse IDE plugin that integrates GitHub Copilot functionality, providing AI-powered code suggestions and completions directly within the Eclipse development environment.

## Overview

This plugin brings the power of GitHub Copilot to Eclipse IDE, enabling developers to:
- Get AI-powered code suggestions as you type
- Generate code from natural language comments
- Receive context-aware completions based on your codebase
- Improve productivity with intelligent code assistance

## Prerequisites

Before installing this plugin, ensure you have:

- **Eclipse IDE** (version 2021-06 or later recommended)
  - Eclipse IDE for Java Developers
  - Eclipse IDE for Enterprise Java and Web Developers
  - Or any Eclipse distribution with plugin support
- **Java Development Kit (JDK)** 11 or higher
- **Active GitHub Copilot subscription**
  - Individual, Business, or Enterprise plan
  - Verify your subscription at [github.com/settings/copilot](https://github.com/settings/copilot)
- **Internet connection** for Copilot API communication

## Installation

### From Eclipse Marketplace (Recommended)

1. Open Eclipse IDE
2. Go to `Help` > `Eclipse Marketplace...`
3. Search for "GitHub Copilot"
4. Click `Install` on the GitHub Copilot Plugin
5. Follow the installation wizard and accept the license agreements
6. Restart Eclipse when prompted

### From Update Site

1. Open Eclipse IDE
2. Go to `Help` > `Install New Software...`
3. Click `Add...` to add a new repository
4. Enter the following details:
   - **Name:** GitHub Copilot Plugin
   - **Location:** `https://your-update-site-url.com/updates`
5. Select the GitHub Copilot feature
6. Click `Next` and follow the installation wizard
7. Restart Eclipse when prompted

### Manual Installation

1. Download the latest plugin JAR from the [Releases](../../releases) page
2. Copy the JAR file to your Eclipse `dropins` folder:
   - Windows: `C:\Eclipse\dropins\`
   - macOS: `/Applications/Eclipse.app/Contents/Eclipse/dropins/`
   - Linux: `/opt/eclipse/dropins/` or `~/eclipse/dropins/`
3. Restart Eclipse

## Configuration

### Initial Setup

1. After installation, go to `Window` > `Preferences` (macOS: `Eclipse` > `Preferences`)
2. Navigate to `GitHub Copilot`
3. Click `Sign in to GitHub`
4. Complete the authentication flow in your browser
5. Return to Eclipse and verify the connection status

### Settings

Configure the plugin behavior in the preferences panel:

- **Enable/Disable Copilot:** Toggle AI suggestions on/off
- **Suggestion Delay:** Adjust the delay before suggestions appear (default: 100ms)
- **Auto-trigger:** Enable automatic suggestions while typing
- **Language Support:** Configure which file types trigger Copilot
- **Telemetry:** Opt-in or opt-out of usage data collection

## Usage

### Getting Code Suggestions

1. Open any supported file (Java, Python, JavaScript, etc.)
2. Start typing code or comments
3. Copilot suggestions will appear inline as you type
4. Press `Tab` to accept a suggestion
5. Press `Esc` to dismiss a suggestion
6. Use `Alt+]` to view alternative suggestions (navigate with `Alt+[` and `Alt+]`)

### Writing Code from Comments

1. Write a descriptive comment explaining what you want to accomplish:
   ```java
   // Function to calculate the factorial of a number recursively
   ```
2. Press `Enter` to start a new line
3. Copilot will suggest the implementation
4. Review and accept the suggestion with `Tab`

### Keyboard Shortcuts

| Action | Shortcut (Windows/Linux) | Shortcut (macOS) |
|--------|--------------------------|------------------|
| Accept suggestion | `Tab` | `Tab` |
| Dismiss suggestion | `Esc` | `Esc` |
| Next suggestion | `Alt+]` | `Option+]` |
| Previous suggestion | `Alt+[` | `Option+[` |
| Trigger suggestion manually | `Ctrl+Enter` | `Cmd+Enter` |
| Toggle Copilot | `Ctrl+Shift+A` | `Cmd+Shift+A` |

## Development Setup

### Building from Source

#### Prerequisites for Development

- **Eclipse IDE for RCP and RAP Developers**
- **Maven** 3.6+ (for Tycho builds)
- **Git**
- **JDK** 11 or higher

#### Clone the Repository

```bash
git clone https://github.com/your-username/eclipse-copilot-plugin.git
cd eclipse-copilot-plugin
```

#### Import into Eclipse

1. Open Eclipse IDE for RCP and RAP Developers
2. Go to `File` > `Import...` > `Existing Projects into Workspace`
3. Select the cloned repository directory
4. Import all projects
5. Wait for workspace to build

#### Build with Maven

```bash
mvn clean verify
```

The built plugin will be available in the `target` directory.

#### Running in Development Mode

1. Right-click on the plugin project
2. Select `Run As` > `Eclipse Application`
3. A new Eclipse instance will launch with the plugin installed
4. Test your changes in this runtime workspace

### Project Structure

```
eclipse-copilot-plugin/
├── bundles/
│   ├── com.github.copilot.eclipse.core/      # Core plugin functionality
│   ├── com.github.copilot.eclipse.ui/        # UI components
│   └── com.github.copilot.eclipse.lsp/       # Language Server Protocol integration
├── features/
│   └── com.github.copilot.eclipse.feature/   # Feature definition
├── releng/
│   ├── com.github.copilot.eclipse.target/    # Target platform
│   └── com.github.copilot.eclipse.updatesite/ # Update site configuration
├── tests/
│   └── com.github.copilot.eclipse.tests/     # Unit and integration tests
├── pom.xml                                     # Parent POM
└── README.md
```

### Running Tests

```bash
# Run all tests
mvn clean verify

# Run specific test bundle
cd tests/com.github.copilot.eclipse.tests
mvn clean verify

# Run with coverage
mvn clean verify -Pcoverage
```

## Contributing

We welcome contributions! Please follow these guidelines:

### Getting Started

1. Fork the repository
2. Create a feature branch: `git checkout -b feature/your-feature-name`
3. Make your changes following the coding standards
4. Write or update tests for your changes
5. Ensure all tests pass: `mvn clean verify`
6. Commit your changes: `git commit -m "Add your feature"`
7. Push to your fork: `git push origin feature/your-feature-name`
8. Open a Pull Request

### Coding Standards

- Follow the [Eclipse Code Style Guidelines](https://wiki.eclipse.org/Coding_Conventions)
- Use meaningful variable and method names
- Add JavaDoc comments for public APIs
- Keep methods focused and concise
- Write unit tests for new functionality
- Ensure code passes all quality checks

### Pull Request Guidelines

- Provide a clear description of the changes
- Reference any related issues
- Include screenshots for UI changes
- Ensure CI/CD checks pass
- Request review from maintainers
- Be responsive to feedback

### Code of Conduct

Please be respectful and constructive in all interactions. We are committed to providing a welcoming and inclusive environment for all contributors.

## Troubleshooting

### Common Issues

#### Plugin Not Appearing After Installation

- Verify Eclipse version compatibility (2021-06+)
- Check Eclipse error log: `Window` > `Show View` > `Error Log`
- Try restarting Eclipse with `-clean` flag: `eclipse -clean`

#### Authentication Issues

- Ensure you have an active GitHub Copilot subscription
- Clear cached credentials: `Window` > `Preferences` > `GitHub Copilot` > `Sign Out`
- Sign in again and complete the authentication flow

#### Suggestions Not Appearing

- Check if Copilot is enabled in preferences
- Verify internet connectivity
- Check the editor file type is supported
- Review Eclipse error log for exceptions

#### Performance Issues

- Increase suggestion delay in preferences
- Disable Copilot for large files (configure file size limit)
- Check available system memory
- Consider increasing Eclipse heap size in `eclipse.ini`

### Getting Help

- **Issues:** [GitHub Issues](../../issues)
- **Discussions:** [GitHub Discussions](../../discussions)
- **Documentation:** [Wiki](../../wiki)
- **Eclipse Forums:** [Eclipse Community Forums](https://www.eclipse.org/forums/)

## License

This project is licensed under the Eclipse Public License 2.0 (EPL-2.0) - see the [LICENSE](LICENSE) file for details.

The Eclipse Public License is a flexible open source license that allows this plugin to be used in both open source and commercial products.

## Acknowledgments

- GitHub Copilot team for the AI technology
- Eclipse Foundation for the plugin framework
- All contributors who help improve this plugin

## Additional Resources

- [GitHub Copilot Documentation](https://docs.github.com/en/copilot)
- [Eclipse Plugin Development Guide](https://www.eclipse.org/articles/article.php?file=Article-PDE-does-plugins/index.html)
- [Eclipse API Reference](https://help.eclipse.org/latest/index.jsp)
- [Language Server Protocol](https://microsoft.github.io/language-server-protocol/)

## Changelog

See [CHANGELOG.md](CHANGELOG.md) for a detailed history of changes.

## Version

Current Version: 1.0.0

---

**Note:** This plugin is not officially affiliated with GitHub or Microsoft. It is an independent implementation that integrates with the GitHub Copilot API.