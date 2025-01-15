# Calories Burnt Prediction Using XGBoost Regression  

## Overview  
This project predicts the number of calories burnt during physical activities using machine learning. The model is powered by the XGBoost regression algorithm, and a user-friendly interface is built using Streamlit to make predictions easy and accessible.  

## Features  
- **Input Data**: Includes features such as age, gender, height, weight, duration of activity, heart rate, and step count.  
- **Output**: Predicted calories burnt.  
- **Model**: XGBoost regression for precise predictions.  
- **Interactive Interface**: Streamlit app for real-time predictions.  
- **Performance Metrics**: Mean Absolute Error (MAE), Mean Squared Error (MSE), and R² score.  

## Project Structure  
```
├── data/                     # Dataset and preprocessing scripts  
├── notebooks/                # Jupyter notebooks for EDA and training  
├── src/                      # Source code for training and prediction  
│   ├── preprocess.py         # Data preprocessing utilities  
│   ├── train.py              # Model training script  
│   └── predict.py            # Prediction script  
├── app/                      # Streamlit app source code  
│   └── app.py                # Main Streamlit app file  
├── tests/                    # Unit tests for scripts  
├── requirements.txt          # Required Python packages  
├── README.md                 # Project documentation  
└── LICENSE                   # License for the project  
```  

## Getting Started  

### Prerequisites  
- Python 3.7 or higher  
- Streamlit  

### Installation  
1. Clone the repository:  
   ```bash  
   git clone https://github.com/yourusername/calories-burnt-prediction.git  
   cd calories-burnt-prediction  
   ```  

2. Install dependencies:  
   ```bash  
   pip install -r requirements.txt  
   ```  

### Usage  

#### 1. **Prepare the Dataset**  
Place your dataset in the `data/` folder and ensure the file paths in the scripts are correct.  

#### 2. **Data Preprocessing**  
Run the preprocessing script:  
```bash  
python src/preprocess.py  
```  

#### 3. **Train the Model**  
Train the XGBoost regression model:  
```bash  
python src/train.py  
```  

#### 4. **Run the Streamlit App**  
Launch the Streamlit app for real-time predictions:  
```bash  
streamlit run app/app.py  
```  

#### 5. **Make Predictions via CLI (Optional)**  
You can also make predictions through the CLI:  
```bash  
python src/predict.py --input data/test_data.csv  
```  

### Streamlit App  
The Streamlit app provides a simple interface to input the required features and instantly view predictions.  

Example screenshot of the app:  
![App Screenshot](https://drive.google.com/file/d/1rW7qCpU-UxoQstJzp8UGgRDgBlyX_B5-/view?usp=sharing)  

### Example Output  
Input via Streamlit or CLI:  
```json  
{
  "age": 25,
  "gender": "Male",
  "height_cm": 175,
  "weight_kg": 70,
  "duration_min": 30,
  "heart_rate_bpm": 120,
  "steps_count": 4000
}  
```  
Output:  
```json  
{
  "predicted_calories_burnt": 230.45
}  
```  

## Results  
- **Train/Test Split**: 80% training, 20% testing.  
- **Best R² Score**: 0.85 (example).  

## Dependencies  
- pandas  
- numpy  
- scikit-learn  
- xgboost  
- matplotlib  
- streamlit  

## Contributing  
Contributions are welcome! Please fork the repository, create a new branch, and submit a pull request.  

## License  
This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.  
