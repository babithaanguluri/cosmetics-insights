import os
import re
from flask import Flask, render_template, request, jsonify
import pandas as pd

app = Flask(__name__, template_folder='.', static_folder='assets')

# Load the dataset
CSV_PATH = os.path.join(os.path.dirname(__file__), 'cosmetics.csv')
df = pd.read_csv(CSV_PATH)

def clean_brand_name(name):
    if not isinstance(name, str):
        return name
    return name.strip()

df['Brand'] = df['Brand'].apply(clean_brand_name)

@app.route('/')
def home():
    # Calculate statistics
    total_products = len(df)
    unique_brands_count = df['Brand'].nunique()
    unique_categories = df['Label'].nunique()
    skin_types_count = 5 # Combination, Dry, Normal, Oily, Sensitive
    
    # Extract brand list words split by space (matching user's mockup list of 184 brands)
    brand_words = set()
    for brand in df['Brand'].unique():
        words = brand.split()
        for w in words:
            clean_word = w.upper().strip(',.()\"')
            if clean_word:
                brand_words.add(clean_word)
            
    sorted_brands = sorted(list(brand_words))
    
    return render_template('index.html', 
                           total_products=f"{total_products:,}",
                           unique_brands_count=unique_brands_count,
                           unique_categories=unique_categories,
                           skin_types_count=skin_types_count,
                           brands=sorted_brands)

@app.route('/recommend', methods=['POST'])
def recommend():
    data = request.get_json() or {}
    skin_type = data.get('skin_type', 'Combination').strip().capitalize()
    
    valid_skin_types = ['Combination', 'Dry', 'Normal', 'Oily', 'Sensitive']
    if skin_type not in valid_skin_types:
        return jsonify({'error': 'Invalid skin type'}), 400
        
    # Filter products suitable for the selected skin type
    filtered_df = df[df[skin_type] == 1].copy()
    
    # Sort by Rank (descending) then by Price (ascending) to get top rated/best value products
    recommended = filtered_df.sort_values(by=['Rank', 'Price'], ascending=[False, True])
    
    # Get top 6 products
    top_recommendations = recommended.head(6).to_dict(orient='records')
    
    # Sanitize NaNs
    for prod in top_recommendations:
        for k, v in prod.items():
            if pd.isna(v):
                prod[k] = None
                
    return jsonify({
        'skin_type': skin_type,
        'recommendations': top_recommendations
    })

if __name__ == '__main__':
    app.run(debug=True, port=5000)
