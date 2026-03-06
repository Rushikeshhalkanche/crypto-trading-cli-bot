# Crypto Trading CLI Bot

A command-line crypto trading bot built in Python that allows users to place MARKET and LIMIT orders using the Binance API.

---

## Features

- Place MARKET orders
- Place LIMIT orders
- Input validation
- Structured logging
- CLI interface using Typer

---

## Project Structure

trading_bot/
│
├── bot/
│   ├── client.py
│   ├── orders.py
│   ├── validators.py
│   └── logging_config.py
│
├── logs/
│   └── trading.log
│
├── cli.py
├── requirements.txt
├── .env.example
└── README.md

---

## Setup Instructions

### 1 Install Python

Python 3.9 or higher is recommended.

### 2 Clone the repository

git clone https://github.com/yourusername/crypto-trading-cli-bot.git

cd crypto-trading-cli-bot

### 3 Create Virtual Environment

Windows

python -m venv venv
venv\Scripts\activate

### 4 Install dependencies

pip install -r requirements.txt

---

## Environment Variables

Create a `.env` file based on `.env.example`

Example:

BINANCE_API_KEY=your_api_key  
BINANCE_SECRET_KEY=your_secret_key

---

## How to Run

### MARKET Order

python cli.py BTCUSDT BUY MARKET 0.001

### LIMIT Order

python cli.py BTCUSDT BUY LIMIT 0.001 --price 30000

---

## Logs

All trading activity is logged in:

logs/trading.log

Example log entries include:

- MARKET order execution
- LIMIT order execution

---

## Assumptions

- Binance API credentials are stored securely in `.env`
- Quantity must be positive
- LIMIT orders require a price parameter

---

## Requirements

Python libraries used:

- python-binance
- typer
- rich
- python-dotenv

Install them using:

pip install -r requirements.txt

---

## Author

Rushikesh Halkanche
