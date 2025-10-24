# Calculator Project

A simple and intuitive calculator application designed to perform basic arithmetic operations with ease. This project provides a clean, user-friendly interface for everyday calculations.

## 📋 Table of Contents

- [Features](#features)
- [Getting Started](#getting-started)
- [Usage](#usage)
- [Installation](#installation)
- [Project Structure](#project-structure)
- [Technologies](#technologies)
- [Contributing](#contributing)
- [License](#license)

## ✨ Features

- **Basic Arithmetic Operations**: Addition, subtraction, multiplication, and division
- **Clear and Reset**: Clear current input or reset the entire calculation
- **Decimal Support**: Perform calculations with decimal numbers
- **Error Handling**: Graceful handling of invalid operations (e.g., division by zero)
- **Keyboard Support**: Use your keyboard for faster input
- **Responsive Design**: Works seamlessly on desktop and mobile devices

## 🚀 Getting Started

### Prerequisites

Before you begin, ensure you have the following installed:
- A modern web browser (Chrome, Firefox, Safari, or Edge)
- [Optional] Node.js (v14 or higher) if running locally with a development server

### Installation

1. **Clone the repository**
   ```bash
   git clone https://github.com/ethanyhou/testRepo.git
   cd testRepo
   ```

2. **Open in browser**
   
   For a simple HTML/CSS/JS calculator, you can directly open the `index.html` file in your browser:
   ```bash
   open index.html
   ```

   Or, if using a development server:
   ```bash
   # Using Python
   python -m http.server 8000
   
   # Using Node.js with http-server
   npx http-server
   ```

   Then navigate to `http://localhost:8000` in your browser.

## 💻 Usage

### Basic Operations

1. **Addition**: Click numbers and then the `+` button, followed by more numbers and `=`
   - Example: `5 + 3 = 8`

2. **Subtraction**: Click numbers, then `-`, more numbers, and `=`
   - Example: `10 - 4 = 6`

3. **Multiplication**: Click numbers, then `×` or `*`, more numbers, and `=`
   - Example: `7 × 6 = 42`

4. **Division**: Click numbers, then `÷` or `/`, more numbers, and `=`
   - Example: `20 ÷ 4 = 5`

### Keyboard Shortcuts

- **Numbers**: `0-9` keys
- **Operations**: `+`, `-`, `*`, `/`
- **Equals**: `Enter` or `=`
- **Clear**: `Escape` or `C`
- **Decimal**: `.`

### Special Features

- **Clear (C)**: Clears the current input
- **All Clear (AC)**: Resets the calculator to initial state
- **Backspace**: Removes the last entered digit

## 📁 Project Structure

```
testRepo/
│
├── index.html          # Main HTML file
├── css/
│   └── styles.css      # Styling for the calculator
├── js/
│   └── calculator.js   # Calculator logic and functionality
├── assets/
│   └── icons/          # Icons and images (if any)
├── README.md           # This file
└── LICENSE             # License information
```

## 🛠️ Technologies

This calculator is built with:

- **HTML5**: Structure and layout
- **CSS3**: Styling and responsive design
- **JavaScript (ES6+)**: Calculator logic and interactivity

### Future Enhancements

Potential features for future versions:
- Scientific calculator mode
- History of calculations
- Theme customization (light/dark mode)
- Memory functions (M+, M-, MR, MC)
- Advanced operations (square root, power, percentage)

## 🤝 Contributing

Contributions are welcome! Here's how you can help:

1. **Fork the repository**
2. **Create a feature branch**
   ```bash
   git checkout -b feature/AmazingFeature
   ```
3. **Commit your changes**
   ```bash
   git commit -m 'Add some AmazingFeature'
   ```
4. **Push to the branch**
   ```bash
   git push origin feature/AmazingFeature
   ```
5. **Open a Pull Request**

### Guidelines

- Write clear, concise commit messages
- Follow the existing code style
- Add comments for complex logic
- Test your changes thoroughly
- Update documentation as needed

## 📝 License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## 👥 Authors

- **Ethan Hou** - [@ethanyhou](https://github.com/ethanyhou)

## 🙏 Acknowledgments

- Inspired by classic calculator designs
- Built as a learning project to demonstrate fundamental web development concepts
- Thanks to the open-source community for inspiration and best practices

## 📞 Contact

For questions, suggestions, or issues:
- Open an issue in this repository
- Reach out via GitHub: [@ethanyhou](https://github.com/ethanyhou)

---

**Happy Calculating! 🔢**