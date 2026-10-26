# ⚡ PriceWise — Multi-Store Electronics Price Comparator & 6-Month Price Tracker

[![Python Version](https://img.shields.io/badge/python-3.10%20%7C%203.11%20%7C%203.12-blue.svg)](https://www.python.org/)
[![Framework](https://img.shields.io/badge/backend-FastAPI-009688.svg)](https://fastapi.tiangolo.com/)
[![License](https://img.shields.io/badge/license-MIT-green.svg)](LICENSE)
[![Market](https://img.shields.io/badge/market-Indian%20E--Commerce-orange.svg)](#supported-retailers)

**PriceWise** is an intelligent, full-stack price comparison and historical trend tracker built specifically for the Indian electronics market. It compares real-time prices across major retailers, identifies the single lowest price deal, calculates exact savings, and graphs 6 months of historical price movements to tell buyers whether right now is the best time to purchase.

---

## 🚀 Key Features

* **🛒 5-Retailer Multi-Store Comparison:** Simultaneously compares prices, ratings, and delivery options across:
  * 📦 **Amazon India**
  * 🛍️ **Flipkart**
  * ⚡ **Croma**
  * 🏪 **Reliance Digital**
  * 🏷️ **Tata CLiQ**
* **📈 6-Month Historical Price Graph:** Dynamic SVG price curve tracking month-by-month changes with **All-Time Low**, **Average**, and **Peak Price** analytics.
* **💡 Smart Buy Advisor:** Built-in heuristic engine providing instant purchase advice (*"🔥 All-Time Low"*, *"🟢 Good Deal"*, or *"🟡 Wait for Sale"*).
* **📱 Comprehensive Electronics Coverage:**
  * **Smartphones:** Apple iPhone 13–17 series, Google Pixel 7a–9 Pro XL, Samsung Galaxy S23–S25 Ultra / Z Fold / Z Flip, OnePlus, Nothing, Redmi.
  * **Laptops:** Apple MacBook Air/Pro (M2/M3), Dell XPS, ASUS ROG Zephyrus, Lenovo Legion, HP Victus.
  * **Audio & Wearables:** Sony WH-1000XM4/XM5, AirPods Pro 2, AirPods Max, Apple Watch Series 10 / Ultra 2, Galaxy Watch 7.
  * **Home & Kitchen Appliances:** Inverter ACs (Daikin, LG, Voltas), Refrigerators (Samsung, LG, Haier), Washing Machines (Bosch, LG), Water Purifiers (Kent, Aquaguard), Air Purifiers (Dyson, Coway), Robot Vacuums, Microwaves, Dishwashers, and Geysers.
* **🛡️ Query Validation & Error Handling:** Strictly filters non-electronic terms and provides graceful, contextual recovery suggestions.
* **🔗 Direct 1-Click Purchase Links:** Deep-links directly into retailer product pages with URL encoding.

---

## 🛠️ Architecture & Tech Stack

```text
price-comparator-app/
├── backend/
│   ├── app.py                  # FastAPI REST API & static file server
│   ├── comparator.py           # Core comparison, validation & history algorithm
│   └── electronics_database.py # Curated Indian market benchmark database
├── static/
│   └── index.html              # Responsive dark-theme frontend with SVG charts
├── run_app.py                  # One-command daemon launcher & auto-browser script
└── README.md
```

* **Backend:** Python 3.12, FastAPI, Uvicorn
* **Frontend:** Modern Vanilla JavaScript, Responsive CSS3 Grid/Flexbox, Dynamic SVG Canvas
* **API Endpoints:**
  * `GET /api/compare?q={product_name}` — Returns store rankings, lowest price, max savings, and 6-month historical data.
  * `GET /api/catalog` — Returns benchmark electronics grouped by category.

---

## ⚡ Quick Start

### 1. Clone the repository
```bash
git clone https://github.com/your-username/pricewise-comparator.git
cd pricewise-comparator
```

### 2. Install dependencies
```bash
pip install fastapi uvicorn requests beautifulsoup4
```

### 3. Run the application
```bash
python run_app.py
```
The app will automatically launch in your default browser at:  
👉 **http://127.0.0.1:5000**

---

## 📊 API Example

### Request
```http
GET /api/compare?q=iPhone%2017
```

### Response
```json
{
  "query": "iPhone 17",
  "product_title": "Apple iPhone 17 (256 GB) - Black / Silver / Pink",
  "category": "Smartphones",
  "best_store": "Flipkart",
  "lowest_price": 81999,
  "highest_price": 84900,
  "max_savings": 2901,
  "price_history": {
    "lowest_recorded": 81999,
    "highest_recorded": 88550,
    "average_price": 84520,
    "advice_badge": "🔥 All-Time Low",
    "advice_text": "Exceptional time to buy! The price is currently at its 6-month lowest recorded level."
  },
  "comparisons": [
    {
      "store": "Flipkart",
      "price": 81999,
      "mrp": 89900,
      "discount_pct": 9,
      "rating": 4.7,
      "delivery": "Free Delivery in 2 Days",
      "buy_url": "https://www.flipkart.com/search?q=iPhone+17"
    },
    {
      "store": "Amazon India",
      "price": 82900,
      "mrp": 89900,
      "discount_pct": 8,
      "rating": 4.7,
      "delivery": "Free Prime Delivery Tomorrow",
      "buy_url": "https://www.amazon.in/s?k=iPhone+17"
    }
  ]
}
```

---

## 📄 License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.
