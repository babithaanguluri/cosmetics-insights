========================================================================
COSMETICS INSIGHTS: ANALYTICS & SKINCARE RECOMMENDATION ENGINE
========================================================================

Cosmetics Insights is a data-driven web application that combines market analytics and personalized skincare product recommendations. The application provides interactive Tableau visualizations of skincare market trends alongside a dynamic recommendation system powered by a Flask backend and a cosmetics dataset.

A comprehensive Markdown version of this documentation has also been created at the root of the project as README.md.

------------------------------------------------------------------------
FEATURES
------------------------------------------------------------------------
* Personalized Recommendations: Get immediate product suggestions based on your skin type (Combination, Dry, Normal, Oily, Sensitive).
* Interactive Dashboards: Integrated Tableau dashboards and stories displaying product distribution, price-to-rank correlations, and brand insights.
* Dynamic Market Stats: Live statistics showing the total number of products, unique brands, and category counts directly calculated from the dataset.
* Responsive Design: A modern, premium UI customized with a sleek cosmetics theme (pink accent palette) and smooth transitions.

------------------------------------------------------------------------
TECHNOLOGY STACK
------------------------------------------------------------------------
* Backend: Python, Flask
* Data Processing: Pandas
* Frontend: HTML5, CSS3, JavaScript (ES6)
* Visualizations: Embedded Tableau Public Dashboards

------------------------------------------------------------------------
INSTALLATION & SETUP
------------------------------------------------------------------------
To run this application locally, follow these steps:

1. Prerequisite: Ensure you have Python 3 installed.
   Verify with: python --version

2. Navigate to Project Folder:
   cd "c:\Users\babit\Downloads\eBusiness"

3. Install Required Libraries:
   pip install flask pandas

   (Optional but Recommended: Use a virtual environment)
   python -m venv venv
   .\venv\Scripts\activate
   pip install flask pandas

------------------------------------------------------------------------
RUNNING THE APPLICATION
------------------------------------------------------------------------
1. Change directory to the source folder containing the backend script:
   cd eBusiness

2. Start the Flask server:
   python app.py

3. Open your browser and go to:
   http://127.0.0.1:5000
