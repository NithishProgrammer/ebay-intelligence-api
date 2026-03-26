
-----

# 📦 eBay Marketplace Intelligence API

[](https://www.python.org/)
[](https://fastapi.tiangolo.com/)
[](https://opensource.org/licenses/MIT)

An **asynchronous Python API** designed to navigate the complex DOM structure of eBay to extract live auction and "Buy It Now" pricing data. This tool utilizes specialized parent-child selectors to ensure data accuracy across various eBay regions.

-----

## 🚀 Key Features

  * **🎯 Precision Selectors**: Targets the `x-price-primary` container to avoid common "active offer" or "shipping cost" text traps.
  * **🌍 Multi-Currency Support**: Smart cleaning logic for `US $`, `£`, and `EUR` formats.
  * **🛡️ Connection Stability**: Optimized `httpx` headers to prevent connection resets during high-traffic periods.

-----

## 🛠️ Installation

1.  **Clone the Repository**

    ```bash
    git clone https://github.com/NithishProgrammer/ebay-intelligence-api.git
    cd ebay-tracker-api
    ```

2.  **Install Requirements**

    ```bash
    pip install fastapi uvicorn httpx beautifulsoup4
    ```

3.  **Launch the API**

    ```bash
    python -m uvicorn main:app --reload
    ```

    *The API will be live at: `http://127.0.0.1:8000`*

-----

## 📡 API Documentation

### 1\. Initialize Tracker

**Endpoint:** `GET /s`  
**Parameters:** `url` (eBay Listing Link)  
**Action:** Dispatches the background "Helper" to start the 6-second polling loop.

### 2\. Fetch Latest Insights

**Endpoint:** `GET /show`  
**Description:** Reads the latest data from the global `notebook` variable.
**Sample Response:**

```json
{
  "Product": "Vintage Film Camera - Tested",
  "price": "$45.99",
}
```

-----

## ⚖️ Rules, Regulations & Ethical Use

> **Notice:** eBay has specific policies regarding automated access. Please use this tool responsibly:

1.  **Polling Frequency**: While this script defaults to **6 seconds**, it is recommended to increase this to **30+ seconds** for long-term monitoring to avoid IP flagging.
2.  **Public Data Only**: This tool only accesses data available to the public. It does not bypass login screens or access private user bidding history.
3.  **Robots.txt Compliance**: eBay's `robots.txt` allows certain levels of crawling; ensure your use case aligns with their "Permitted Use" guidelines.
4.  **Disclaimer**: The author (**Nithish**) provides this code "as is" and is not liable for any account restrictions or technical blocks encountered while using this tool.

-----

## 🗺️ Project Roadmap

  - [x] Primary Price Extraction
  - [x] Background Task Integration
  - [x] Currency Symbol Sanitization
  - [ ] **Next Step:** Scraping Seller Feedback ratings.
  - [ ] **Next Step:** Support for eBay Auction "Time Left" countdowns.

-----

## 📜 License

Distributed under the **MIT License**.

**Developed by [Nithish](https://github.com/NithishProgrammer) | Puducherry, India 🇮🇳**

-----

