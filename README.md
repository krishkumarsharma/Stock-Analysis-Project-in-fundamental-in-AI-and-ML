 System for Stock Trend Analysis

📌 Project Synopsis

Python and external financial APIs were used in the construction of this stock trend analysis system, which was created to comprehend how actual stock analysis tools operate. The project's main objectives are to retrieve stock data, examine price patterns, and produce basic buy/sell insights. In order to make the logic easy to comprehend and appropriate for academic settings, I made an effort to keep it straightforward.

The System's Features

The fundamental elements of stock analysis are included in the system:

View Stock Information

shows crucial stock information like:

Current cost Starting cost The highest cost The lowest cost Analysis of Trends determines if the stock is in: Rising trend 📈 A downward trend 📉

Calculating the Moving Average determines the 10-day moving average aids in comprehending short-term price trends

Purchase/Sell Recommendation makes a comparison-based action suggestion: Purchase if the price is higher than average. Sell 🔴 if the price is below average. Visualisation of Graphs shows a monthly trend graph. makes use of colour-coded lines: Green → Growing trend Red → A declining trend For clarity, basic markers and signals are added. 🛠 Technologies Used

Python 3: Fundamental programming • Requests: API management • Pandas: Data processing • Matplotlib: Visualisation of graphs • External API: Data from the stock market The project is lightweight and simple to use because it makes use of simple tools.

How to Manage the Software Verify that Python is installed. Install the necessary libraries: Pandas matplotlib and pip install requests Launch the application: Project.py in Python When prompted, enter the stock symbol:

For instance:

AAPL INFY.NS
📁 Project Organization Stock-Analysis-Project/project.py, README.md, and (optional) report file Data Management JSON-formatted stock data is retrieved from the API. Among the extracted values are: Closing cost Time and date Pandas is used to process data. For visualisation, monthly averages are computed. 🌟 Why I Constructed This Project

I created this project to gain an understanding of the internal workings of stock analysis tools. As I worked on this, I discovered:

How to use APIs to retrieve data in real time How to handle and purify data How to use simple logic to analyse trends How to use graphs to visualise data How to integrate several ideas into a single project 💡 Upcoming Improvements

A few enhancements that may be added in the future:

Advanced metrics (MACD, RSI) Improved machine learning prediction models Tracking stocks in real time Web-based interface, or GUI System for tracking portfolios

Take note:

This project is solely intended for educational purposes. It doesn't offer sound financial guidance.

👤 Author

VIT Bhopal University student Krish Kumar
