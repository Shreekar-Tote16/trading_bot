# Binance Futures Demo Trading Bot

## Overview
A CLI-based trading bot for Binance USDT-M Futures Demo environment.

## Features
- Market and Limit order support
- BUY and SELL support
- Structured architecture
- Logging to file
- Input validation
- Error handling

## Setup

1. Create virtual environment
2. Install dependencies:
   pip install -r requirements.txt
3. Create .env file:

   BINANCE_API_KEY=your_demo_key
   BINANCE_SECRET_KEY=your_demo_secret

## Demo Futures API Endpoint
https://demo-fapi.binance.com

## Run Examples

Market Order:
python cli.py --symbol BTCUSDT --side BUY --type MARKET --quantity 0.002

Limit Order:
python cli.py --symbol BTCUSDT --side SELL --type LIMIT --quantity 0.002 --price 65000

## Logs
Logs are stored in logs/trading_bot.log

## Assumptions
- Minimum notional enforced by exchange
- Demo trading environment used

## Security Note

The `.env` file containing API credentials is intentionally excluded via `.gitignore`.
Please create your own `.env` file before running.


