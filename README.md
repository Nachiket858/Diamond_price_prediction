# Diamond Price Prediction

This project predicts the price of diamonds based on their features such as carat, cut, color, clarity, depth, table, and dimensions (length, width, height). The application uses a trained machine learning model served through a Flask web application.

---

## Features
- Input form for diamond features
- Real-time price prediction
- Scalable and easy-to-deploy Flask application

---

## Project Structure
```
project/
│
├── app.py                     # Main Flask application
├── templates/
│   └── index.html             # HTML file for the input form
├── src/
│   ├── __init__.py            # Initialization file for the src module
│   └── pipelines/
│       ├── __init__.py        # Initialization file for the pipelines module
│       └── prediction_pipeline.py # Custom_data and PredictPipeline classes
├── artifacts/
│   ├── model.pkl              # Trained machine learning model
│   └── scaler.pkl             # Scaler for feature preprocessing
└── README.md                  # Project documentation
```

---

## Requirements

Install the required packages using pip:

```bash
pip install -r requirements.txt
```

### Example `requirements.txt`:
```
Flask
pandas
numpy
scikit-learn
```

---

## How to Run the Project

1. Clone the repository:

```bash
git clone <repository-url>
```

2. Navigate to the project directory:

```bash
cd project
```

3. Start the Flask application:

```bash
python app.py
```

4. Open your web browser and visit:

```
http://127.0.0.1:5000/
```

---

## Input Features

### Required Fields:
- **Carat**: The weight of the diamond (e.g., 0.5).
- **Cut**: The quality of the cut (e.g., Fair, Good, Very Good, Premium, Ideal).
- **Color**: The color grade of the diamond (e.g., D, E, F, G, H, I, J).
- **Clarity**: The clarity grade (e.g., I1, SI2, SI1, VS2, VS1, VVS2, VVS1, IF).
- **Depth**: Total depth percentage (e.g., 61.5).
- **Table**: Table width percentage (e.g., 55).
- **Length (x)**: Length in mm (e.g., 4.0).
- **Width (y)**: Width in mm (e.g., 4.5).
- **Height (z)**: Height in mm (e.g., 2.7).

---

## Implementation Details

### Flask Application
- **Routes**:
  - `/`: Renders the input form (`index.html`).
  - `/predict`: Handles the form submission, processes input data, and returns the predicted price.

### Machine Learning Pipeline
- **Custom_data**: Converts input data into a DataFrame.
- **PredictPipeline**: Loads the trained model and scaler, scales the input data, and predicts the diamond price.

---

## Example Prediction Workflow
1. Enter the diamond features in the input form.
2. Submit the form.
3. Receive the predicted price of the diamond.

---

## Screenshots
### Input Form:
(Screenshot of the input form)

### Prediction Output:
(Screenshot of the prediction result)

---

## Future Enhancements
- Improve the user interface.
- Add visualizations for feature importance.
- Deploy the app on cloud platforms like AWS, GCP, or Heroku.

---

## License
This project is licensed under the MIT License. See the LICENSE file for details.

