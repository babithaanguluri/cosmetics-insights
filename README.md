# Cosmetics Insights: Analytics & Skincare Recommendation Engine

Cosmetics Insights is a data-driven web application that combines market analytics and personalized skincare product recommendations. The application provides interactive Tableau visualizations of skincare market trends alongside a dynamic recommendation system powered by a Flask backend and a cosmetics dataset.

---

## 🚀 Features

- **Personalized Recommendations**: Get immediate product suggestions based on your skin type (Combination, Dry, Normal, Oily, Sensitive).
- **Interactive Dashboards**: Integrated Tableau dashboards and stories displaying product distribution, price-to-rank correlations, and brand insights.
- **Dynamic Market Stats**: Live statistics showing the total number of products, unique brands, and category counts directly calculated from the dataset.
- **Beautiful, Responsive Design**: A modern, premium UI customized with a sleek cosmetics theme (pink accent palette) and smooth transitions.

---

## 🛠️ Technology Stack

- **Backend**: Python, Flask
- **Data Processing**: Pandas
- **Frontend**: HTML5, CSS3 (Vanilla + Bootstrap 5), JavaScript (ES6)
- **Visualizations**: Embedded Tableau Public Dashboards
- **Design Template**: Based on the elegant eBusiness corporate template

---

## 📁 Project Directory Structure

```text
eBusiness/
├── .gitignore                  # Git untracked pattern file
├── README.md                   # Project documentation (this file)
└── eBusiness/                  # Flask Application Source Directory
    ├── app.py                  # Main Flask server & recommendation logic
    ├── cosmetics.csv           # Product dataset (1,400+ entries)
    ├── index.html              # Core application frontend
    ├── portfolio-details.html  # Portfolio detail pages
    ├── service-details.html    # Service details page
    ├── starter-page.html       # Template helper page
    ├── assets/                 # CSS, JS, Images, and Vendor dependencies
    └── forms/                  # Helper contact forms
```

---

## ⚙️ Installation & Setup

To run this application locally, follow these steps:

### 1. Prerequisite
Ensure you have Python 3 installed on your machine. You can verify this by running:
```bash
python --version
```

### 2. Clone/Navigate to Project Folder
Navigate to the directory:
```bash
cd "c:\Users\babit\Downloads\eBusiness"
```

### 3. Install Required Libraries
Install the Python dependencies (`flask` and `pandas`):
```bash
pip install flask pandas
```

*Optional but Recommended:* Use a virtual environment:
```bash
python -m venv venv
.\venv\Scripts\activate
pip install flask pandas
```

---

## 🏃 Running the Application

1. Change directory to the source folder containing the backend script:
   ```bash
   cd eBusiness
   ```
2. Start the Flask server:
   ```bash
   python app.py
   ```
3. Open your browser and go to:
   [**http://127.0.0.1:5000**](http://127.0.0.1:5000)

---

## 📊 Recommendation Algorithm

The recommendation engine:
1. Filters the dataset to isolate products flagged for the selected skin type (`Combination`, `Dry`, `Normal`, `Oily`, or `Sensitive`).
2. Sorts the filtered subset dynamically:
   - Primarily by **Rank** (descending order, to find top-rated items).
   - Secondarily by **Price** (ascending order, to ensure value-for-money options appear first).
3. Serves the top 6 product matches as JSON to render seamlessly on the web interface.
