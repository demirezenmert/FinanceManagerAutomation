


# Finance Manager Automation

Automate the categorization and updating of financial transactions in Google Sheets.

![GitHub License](https://img.shields.io/badge/license-MIT-blue.svg)

## Table of Contents

- [Introduction](#introduction)
- [Features](#features)
- [Getting Started](#getting-started)
  - [Prerequisites](#prerequisites)
  - [Installation](#installation)
- [Usage](#usage)
- [Contributing](#contributing)
- [License](#license)

## Introduction

The Finance Manager Automation is a Python script that automates the process of categorizing financial transactions and updating Google Sheets. It reads a CSV file containing financial transaction data, categorizes each transaction, and updates the corresponding Google Sheets worksheet based on the transaction's month.

## Features

- Automatically categorizes financial transactions.
- Updates Google Sheets with categorized transactions.
- Supports various transaction categories, such as monthly payments, subscriptions, groceries, and more.

## Getting Started

### Prerequisites

Before you begin, ensure you have met the following requirements:

- Python 3.x installed on your system.
- Google Sheets API credentials (JSON file) to access the Google Sheets document.

### Installation

1. Clone the repository:

   ```shell
   git clone https://github.com/demirezenmert/FinanceManagerAutomation.git
   ```

2. Install the required Python libraries:
    gspread library to update a Google Sheets document

   ```shell
   pip install gspread
   ```

3. Place your CSV files in the project directory. The script currently supports files named like `fake_bank_transactions.csv`.

4. Place your Google Sheets API credentials JSON file in the project directory.

5. To access spreadsheets via Google Sheets API
https://docs.gspread.org/en/latest/oauth2.html#enable-api-access-for-a-project

## Usage

1. Run the script by executing the following command:

   ```shell
   python finance_manager.py
   ```

2. The script will read the CSV file, categorize each transaction, and update the Google Sheets document named "Finances" with the categorized transactions.

## Contributing

Contributions are welcome! To contribute to the Finance Manager Automation project, follow these steps:

1. Fork the repository.
2. Create a new branch for your feature or bug fix.
3. Make your changes and test them thoroughly.
4. Create a pull request with a clear description of your changes.

Please ensure your code follows PEP 8 style guidelines and includes appropriate documentation and comments.
---
![alt text](https://github.com/demirezenmert/FinanceManagerAutomation/blob/master/Example.png)

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

---

