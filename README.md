
📈 Live Cryptocurrency Dashboard
================================
Demo Video
----------

A demo video showcasing how the dashboard works is available here:

https://github.com/user-attachments/assets/0324c455-dc5c-4f79-a43c-718fd993c1c7

The video demonstrates how to:

*   View live data for cryptocurrencies.
    
*   Interact with the dashboard's features, such as viewing the top 5 cryptocurrencies and price change insights.
    
*   Export the data to an Excel file.

Overview
--------

This project provides a real-time cryptocurrency dashboard, fetching live data from the CoinGecko API for the top 50 cryptocurrencies by market capitalization. The dashboard displays live prices, market data, and insightful analysis of the top 5 cryptocurrencies, average price, highest and lowest price change over the last 24 hours. The dashboard refreshes periodically, and the data can be exported to an Excel file for further analysis.

Features
--------

*   **Live Cryptocurrency Data**: Fetches live data for the top 50 cryptocurrencies by market capitalization.
    
*   **Top 5 Cryptocurrencies by Market Cap**: Displays the top 5 cryptocurrencies with the highest market capitalization.
    
*   **Average Price**: Displays the average price of all top 50 cryptocurrencies.
    
*   **Price Change Analysis**: Shows the highest and lowest price change percentages in the last 24 hours.
    
*   **Data Export**: Automatically saves the latest data to an Excel file (Crypto\_Live\_Data.xlsx) after each refresh.
    
*   **Customizable Refresh Rate**: Adjust the refresh rate of the data from 30 seconds to 10 minutes.
    

Requirements
------------

To run this project, you need to have the following Python libraries installed:

*   requests
    
*   pandas
    
*   streamlit
    
*   openpyxl (for exporting to Excel)
    

You can install the required libraries using the following command:
 ```bash
 pip install requests pandas streamlit openpyxl   `
```

How to Run
----------

1.  **Clone the Repository** or create a new Python file.
    
2. **Run the command to install dependencies**
      ```bash
      pip install requests pandas streamlit openpyxl
      ```
4.  **Create a Python file (e.g., main.py)** and paste the provided code into the file.
    
5.  **To run the code**
    ```bash
      streamlit run main.py
    ```
7.  Open the web page shown in your terminal (typically http://localhost:8501) to view the dashboard.
    

Code Overview
-------------

### Fetch Cryptocurrency Data

The fetch\_crypto\_data() function fetches live cryptocurrency data from the CoinGecko API and returns it as a Pandas DataFrame.

### Analyze Data

The analyze\_data() function performs analysis on the cryptocurrency data, including:

*   Top 5 cryptocurrencies by market capitalization.
    
*   Average cryptocurrency price.
    
*   Highest and lowest price changes over the last 24 hours.
    

### Streamlit Dashboard

*   The Streamlit dashboard displays live cryptocurrency data in a clean and interactive layout.
    
*   The dashboard includes a sidebar for adjusting the refresh rate and provides a downloadable Excel file (Crypto\_Live\_Data.xlsx).
    
*   The main area of the dashboard displays the live cryptocurrency table, insights on the top 5, the average price, and the highest/lowest price change in the last 24 hours.
    

Customization
-------------

*   **Refresh Rate**: You can adjust the refresh rate of the data between 30 seconds and 10 minutes through the sidebar.
    
*   **Data Export**: The dashboard automatically saves the latest data into an Excel file after each refresh.

    
Troubleshooting
---------------

*   **If the data is not displaying**: Ensure that the required libraries are installed, and check for any issues with the API or internet connectivity.
    
*   **If the refresh rate is not working**: Make sure the time.sleep() function is not being interrupted or blocked by any other processes.
    


