# Stock Market Analysis Pipeline

## Overview
This project implements an end-to-end data pipeline for analyzing stock market data, with a focus on cloud provider companies. The pipeline downloads historical stock data, processes it, calculates technical indicators, performs various analyses, and generates visualizations.

## Project Structure
```
stock-analysis-project/
│
├── data/                      # Data directory
│   ├── raw/                   # Raw data from API
│   ├── processed/             # Cleaned and structured data
│   └── analyzed/              # Data with calculated indicators
│
├── notebooks/                 # Jupyter notebooks for exploration
│
├── scripts/                   # Python scripts
│   ├── download_data.py       # Downloads stock data from Yahoo Finance
│   ├── process_data.py        # Cleans and restructures the data
│   ├── analyze_data.py        # Calculates technical indicators and metrics
│   ├── visualize_data.py      # Creates visualizations and charts
│   └── main.py                # Orchestrates the entire pipeline
│
├── results/                   # Output of analyses
│   ├── figures/               # Generated charts and visualizations
│   └── reports/               # Analysis reports
│
├── utils/                     # Utility functions
│   ├── __init__.py
│   ├── api_helpers.py         # Helper functions for API calls
│   └── indicators.py          # Functions for technical indicators
│
├── requirements.txt           # Project dependencies
├── README.md                  # This file
└── .gitignore                 # Git ignore file
```

## Features
- **Data Collection**: Downloads historical stock data for major cloud providers using Yahoo Finance API
- **Data Processing**: Cleans, restructures, and prepares the data for analysis
- **Technical Analysis**: Calculates key indicators including:
  - Simple Moving Averages (SMA)
  - Exponential Moving Averages (EMA)
  - Relative Strength Index (RSI)
  - Moving Average Convergence Divergence (MACD)
- **Performance Metrics**: Calculates returns over different time periods, volatility, and maximum drawdown
- **Correlation Analysis**: Analyzes relationships between different stocks
- **Trend Identification**: Identifies market trends based on technical indicators
- **Visualization**: Generates charts and graphs to visualize the analysis

## Installation

### Prerequisites
- Python 3.8 or higher
- pip (Python package installer)

### Setup
1. Clone the repository:
   ```bash
   git clone https://github.com/yourusername/stock-analysis-project.git
   cd stock-analysis-project
   ```

2. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```

## Usage

### Running the Complete Pipeline
To run the entire pipeline from data download to visualization:

```bash
python scripts/main.py
```

### Running Individual Components

1. **Download Data**:
   ```bash
   python scripts/download_data.py
   ```

2. **Process Data**:
   ```bash
   python scripts/process_data.py
   ```

3. **Analyze Data**:
   ```bash
   python scripts/analyze_data.py
   ```

4. **Visualize Data**:
   ```bash
   python scripts/visualize_data.py
   ```

## Sample Analysis

The analysis pipeline generates several insights:

1. **Technical Indicators**: Moving averages, RSI, and MACD for each stock
2. **Performance Comparison**: Returns over 1-month, 3-month, and 6-month periods
3. **Correlation Matrix**: How different cloud provider stocks move in relation to each other
4. **Trend Analysis**: Identification of uptrends, downtrends, and sideways movements

## Customization

You can customize the analysis by modifying parameters in the scripts:

- Change the list of tickers in `download_data.py` to analyze different companies
- Adjust the time periods for moving averages in `analyze_data.py`
- Modify the visualization styles in `visualize_data.py`

## Dependencies

Major dependencies include:
- pandas: Data manipulation and analysis
- numpy: Numerical computing
- yfinance: Yahoo Finance API wrapper
- matplotlib/seaborn: Data visualization

For a complete list, see `requirements.txt`.

## Future Improvements

Potential enhancements for the project:
- Add more advanced technical indicators
- Implement predictive modeling
- Create interactive dashboards for visualization
- Add backtesting for trading strategies
- Incorporate fundamental analysis data

## License
This project is licensed under the MIT License - see the LICENSE file for details.

## Acknowledgments
- Yahoo Finance for providing the stock market data
- The open-source community for the libraries used in this project