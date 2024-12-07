# Gold Price Comparison Tool

![Gold Price Comparison](docs/images/gold_price_comparison_banner.png)

## Table of Contents

- [Introduction](#introduction)
- [Features](#features)
- [Prerequisites](#prerequisites)
- [Installation](#installation)
- [Usage](#usage)
- [Screenshots](#screenshots)
- [Contributing](#contributing)
- [License](#license)
- [Acknowledgments](#acknowledgments)

## Introduction

The **Gold Price Comparison Tool** is a Python application that allows global gold traders to compare the price of gold in Thailand with the price in their local country. By inputting your local currency, exchange rate, and the price of gold in your locale, you can make informed trading decisions based on accurate and personalized data.

## Features

- **User-friendly Interface**: A simple and intuitive graphical interface built with PySide6 (Qt for Python).
- **Currency Conversion**: Converts Thailand's gold price to your local currency using the provided exchange rate.
- **Gold Price Comparison**: Compares gold prices per gram or ounce in both countries.
- **Personalized Input**: Accepts inputs for local currency symbol, exchange rate, local gold price, and Thailand gold price.
- **Validation**: Ensures that all inputs are valid and provides error messages for invalid data.
- **Result Display**: Clearly shows which country offers a better gold price and the price difference.

## Prerequisites

- **Python 3.6 or later**
- **PySide6 library** for creating the graphical user interface.

## Installation

### 1. Clone the Repository

Clone this repository to your local machine:

```bash
git clone https://github.com/yourusername/GoldPriceComparison.git
cd GoldPriceComparison
```

Replace `yourusername` with your GitHub username if you forked the repository.

### 2. Create a Virtual Environment (Optional but Recommended)

Create a virtual environment to manage dependencies:

```bash
python -m venv venv
```

Activate the virtual environment:

- On Windows:

  ```bash
  venv\Scripts\activate
  ```

- On macOS/Linux:

  ```bash
  source venv/bin/activate
  ```

### 3. Install Dependencies

Install the required Python packages using `pip`:

```bash
pip install -r requirements.txt
```

If you didn't create a virtual environment, ensure that you have `PySide6` installed:

```bash
pip install PySide6
```

## Usage

### Running the Application

Run the `main.py` script to start the application:

```bash
python main.py
```

### Application Workflow

1. **Launch the Application**: A window titled **"Gold Price Comparison"** will appear.

2. **Input Your Data**:

   - **Local Currency Symbol**: Enter the symbol or abbreviation of your local currency (e.g., USD, EUR, GBP).
   - **Exchange Rate**: Provide the exchange rate from your local currency to Thai Baht (THB per 1 unit of your currency).
   - **Gold Price in Local Country**: Enter the current price of gold in your country per ounce.
   - **Gold Price in Thailand**: Enter the gold price in Thailand per Gold Baht in THB.
   - **Investment Amount**: (If available) Enter the amount you plan to invest in your local currency.

3. **Calculate**: Click the **"Calculate"** button.

4. **View Results**:

   - The application will display:
     - Gold prices in both countries converted to the same unit (per ounce or gram) and currency.
     - A comparison indicating which country offers a better price.
     - The price difference per unit.

### Example

- **Local Currency Symbol**: USD
- **Exchange Rate (USD to THB)**: 33.00
- **Gold Price in Local Country (USD/ounce)**: 1,800.00
- **Gold Price in Thailand (THB/Gold Baht)**: 42,600

**Expected Output**:

```
Gold Price Comparison:
Your Local Country: 1,800.00 USD/ounce
Thailand: 1,915.87 USD/ounce
Your local country offers a better gold price.
Price difference: 115.87 USD/ounce
```

## Screenshots

### Main Interface

![Main Interface](docs/images/main_interface.png)

### Input Example

![Input Example](docs/images/input_example.png)

### Result Display

![Result Display](docs/images/result_display.png)

*(Note: Images are for illustrative purposes. Actual application may vary.)*

## Contributing

Contributions are welcome! Please follow these steps:

1. **Fork the Repository**: Click the "Fork" button at the top-right of this page.

2. **Clone Your Fork**:

   ```bash
   git clone https://github.com/yourusername/GoldPriceComparison.git
   cd GoldPriceComparison
   ```

3. **Create a Branch**:

   ```bash
   git checkout -b feature/YourFeatureName
   ```

4. **Make Your Changes**: Implement your feature or bug fix.

5. **Commit Changes**:

   ```bash
   git commit -am "Add feature XYZ"
   ```

6. **Push to Your Fork**:

   ```bash
   git push origin feature/YourFeatureName
   ```

7. **Create a Pull Request**: Go to the original repository and create a pull request from your fork.

## License

This project is licensed under the **MIT License**.

See the [LICENSE](LICENSE) file for details.

## Acknowledgments

- **PySide6**: For providing the Python bindings for the Qt application framework.
- **Qt**: The framework makes it possible to develop cross-platform applications.
- **Contributors**: Thanks to everyone who has contributed to this project.

---

If you have any questions or need further assistance, please feel free to open an issue or contact the maintainer.

# Documentation

## Project Structure

```
GoldPriceComparison/
├── main.py          # The main Python script to run the application
├── main.qml         # The QML file defining the UI layout
├── requirements.txt # List of Python dependencies
├── LICENSE          # License file
├── README.md        # This readme file
└── docs/
    └── images/
        ├── gold_price_comparison_banner.png
        ├── input_example.png
        ├── main_interface.png
        └── result_display.png
```

## Code Overview

### main.py

This script contains the backend logic of the application, including:

- **MainBackend Class**: Handles the calculation logic and communicates with the QML UI.
- **Functions**:
  - `parse_european_number()`: Parses numbers formatted in European style (e.g., "1.234,56").
  - `format_european_number()`: Formats float numbers into European style strings.
  - `calculateResults()`: Performs the gold price comparison calculation.

### main.qml

Defines the user interface using QML, including:

- Input fields for:
  - Local currency symbol
  - Exchange rate
  - Local gold price
  - Thailand gold price
- Buttons for "Calculate" and "Exit"
- A text area to display results or error messages

## Development Notes

### Internationalization

- **Number Formatting**: The application uses European number formatting (e.g., commas for decimals, periods for thousands).
- **Localization**: If expanding to support multiple languages, consider implementing QML's internationalization features.

### Extensibility

- **Additional Currencies**: The application can be extended to include automatic exchange rate fetching from APIs.
- **Historical Data**: Implement features to analyze historical gold prices.
- **Graphical Charts**: Use QML charts to visually represent price comparisons over time.

## Troubleshooting

- **PySide6 Installation Issues**: If you encounter problems installing `PySide6`, ensure that you are using a compatible Python version (Python 3.6 or later).

- **Application Doesn't Start**: Check that both `main.py` and `main.qml` are in the same directory, and that you're running the script from that directory.

- **Error Messages**: If you receive validation error messages, double-check your inputs to ensure they are correct and in the proper format.

## References

- **PySide6 Documentation**: [https://doc.qt.io/qtforpython/](https://doc.qt.io/qtforpython/)
- **Qt QML Documentation**: [https://doc.qt.io/qt-5/qmlapplications.html](https://doc.qt.io/qt-5/qmlapplications.html)

## Contact

For support or to report issues, please open an issue in the GitHub repository or contact the maintainer at [your.email@example.com](mailto:your.email@example.com).

---

Thank you for using the Gold Price Comparison Tool! Your feedback and contributions are always appreciated.
