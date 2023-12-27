# Flipkart Product Comparison App and price drop alert

### Project Overview:

This project aims to scrape mobile phone data from Flipkart and provide insights into the best-rated, storage, battery, and overall best mobile phones within a specific budget. The data is extracted using web scraping techniques, and the results are displayed based on various criteria.
The dropAlert.py script is designed to track the price drop of a specific product on Flipkart and send an email notification to the user when the product's price falls below a specified target price.
![Capture1](https://github.com/AmanKumar2626/Flipkart-Smartphone-comparison-and-price-drop-alert/assets/92772172/a9677ea7-85fb-4a0e-ad0d-d26977f8c4df)
![Capture2](https://github.com/AmanKumar2626/Flipkart-Smartphone-comparison-and-price-drop-alert/assets/92772172/31f8a8c4-44d6-476c-ac8f-1a7333af2c6a)


### Features:

1. Web Scraping:
   - Utilizes Selenium and BeautifulSoup for web scraping Flipkart to gather information on mobile phones.
   - Navigates through pages of search results to collect data on multiple mobile phones.

2. Data Collection:
   - Gathers information such as mobile name, price, storage, screen size, camera details, battery capacity, and processor.
   - Handles potential pop-ups, such as OTP overlays, for smooth execution.

3. Analysis and Insights:
   - Identifies the most highly rated mobile phones based on user ratings.
   - Determines the mobile phones with the best storage capacity among the highly rated ones.
   - Finds the mobile phones with the best battery performance among the selected phones.
   - Presents the overall best mobile phones considering multiple factors, including ratings and prices.
  
4. Email Notification:

   - Sends an email notification using the smtplib library when the current price drops below the target price.
   - The email includes details such as the product name, current price, target price, Flipkart URL, and a personalized message.

5. Automated Tracking:

   - Continuously checks the product's price at regular intervals (every 24 hours).
   - Runs indefinitely until the current price falls below the user's specified target price.

### How to Use:

1. Dependencies:
   - Install the required Python libraries using the following:
     ```bash
     pip install pandas beautifulsoup4 selenium requests
     ```

2. WebDriver:
   - Download the appropriate WebDriver for Chrome from [here](https://sites.google.com/chromium.org/driver/).
   - Update the `path` variable in the script with the path to the downloaded WebDriver.

3. Email Configuration:

   - Configure your email credentials on dropAlert.py file (sender's email ID and password) in the send_email function.
     
4. Run the Script:
   - Execute the script by running the Python file containing the gui.py code.
     python gui.py
   - It will open a gui interface of two tabs, In first tab Product price drop alert interface will appear where you have to enter user name, Flipkart link, Product Name, Wish price and Email.
     ![Capture1](https://github.com/AmanKumar2626/Flipkart-Smartphone-comparison-and-price-drop-alert/assets/92772172/50233727-063a-4b90-9828-ce72072195bc)
     The script will check the product's price regularly and notify you via email if the price drops below your specified target.
     

   - In Second Tab price comparison of smartphones interface will appear where you just need to enter your budget.
     ![Capture2](https://github.com/AmanKumar2626/Flipkart-Smartphone-comparison-and-price-drop-alert/assets/92772172/761d41a3-a503-4b54-a8de-2bf8b7ffc288)

     The script will open a Chrome browser, scrape data from Flipkart, and display insights on the best mobile phones.
     

5. View Results:
   - The script will print details of the most highly rated mobile phones, the best storage phones, best battery phones, and overall best mobile phones.
   - The results will include mobile name, ratings, storage, camera details, screen size, battery capacity, processor, and prices.
   - And you can track your smartphone price with your budget so if it in less then your budget price it will give you email notification.

Note:
- The script may need adjustments based on Flipkart's website changes, and users are encouraged to review and modify the code accordingly.

### Additional Information:

- The project uses Python, Selenium, BeautifulSoup, and Pandas for web scraping, data extraction, and analysis.
- Make sure to comply with Flipkart's terms of service and policies while using web scraping techniques on their website.
- The code includes error handling for potential issues like pop-ups, making it robust for varied situations.

### Disclaimer: This project is for educational purposes only, and users are responsible for adhering to the terms of service of any website they interact with using web scraping.
