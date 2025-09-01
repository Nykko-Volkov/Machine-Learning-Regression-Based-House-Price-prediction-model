# House Price Prediction App

This project is a simple machine learning regression-based web app for predicting house prices based on the size of the house (in square feet). The app is built using Streamlit and uses a pre-trained model to estimate prices.

## Features
- User-friendly slider to input house size
- Real-time price prediction
- Powered by a trained regression model
- Simple and clean UI with Streamlit

## Demo
Check out the live demo: [https://nathan-ml.streamlit.app](https://nathan-ml.streamlit.app)

## How to Run Locally
1. **Clone or download this repository.**
2. **Install dependencies:**
   ```bash
   pip install streamlit joblib
   ```
3. **Ensure you have the following files in the same directory:**
   - `hppa.py` (main app)
   - `house_price_model.pkl` (trained model)
4. **Run the app:**
   ```bash
   streamlit run hppa.py
   ```
5. **Open the provided local URL in your browser.**

## File Descriptions
- `hppa.py`: Streamlit app source code
- `house_price_model.pkl`: Pre-trained regression model
- `house_size_price.csv`: Dataset used for training (optional)
- `house.ipynb`: Jupyter notebook for model training and exploration

## Requirements
- Python 3.7+
- streamlit
- joblib

## Author
Nathan

## License
This project is for educational purposes.
