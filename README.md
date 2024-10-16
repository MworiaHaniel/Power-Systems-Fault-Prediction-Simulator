# Fault Prediction using Machine Learning Simulator

## Overview
This project is designed to predict fault types in power systems based on input voltages and currents. Using machine learning techniques, specifically a Random Forest classifier, this simulator allows users to input real-time voltage and current readings and receive predictions on potential faults. The Machine learning model uses the Electrical Fault detection and classification dataset from Kaggle

## Features
- **User Input**: Interactive fields for inputting current (Ia, Ib, Ic) and voltage (Va, Vb, Vc) values.
- **Fault Prediction**: Predicts the type of fault based on user input using a trained machine learning model.
- **Web Interface**: Built using Streamlit for easy access and usability.

## Libraries Used
- [scikit-learn](https://scikit-learn.org/stable/) - For implementing machine learning models.
- [joblib](https://joblib.readthedocs.io/en/latest/) - For saving and loading the trained model.
- [Streamlit](https://streamlit.io/) - For building a web-based interactive simulator.
- [pandas](https://pandas.pydata.org/) - For data manipulation and analysis.
- [numpy](https://numpy.org/) - For numerical operations.

## Getting Started

### Prerequisites
- Python 3.x
- Required libraries (install via pip):

```bash
pip install pandas numpy scikit-learn streamlit joblib

//project-root
├── data/
│   ├── classData.csv
│   └── detect_dataset.csv
└── src/
    ├── fault_classifier.pkl    # Trained model
    ├── fault_prediction_app.py  # Streamlit application
    ├── main.py                 # Main application logic (if applicable)
    ├── power_system_data.txt    # Text file with power system analysis data
    └── TrainModel.py           # Script for training the machine learning model



Here's the updated README.md file reflecting the new project structure, with a data folder containing classData.csv and detect_dataset.csv, and a src folder containing fault_classifier.pkl, fault_prediction_app.py, main.py, power_system_data.txt, and TrainModel.py.

markdown
Copy code
# Fault Prediction using Machine Learning Simulator

## Overview
This project is designed to predict fault types in power systems based on input voltages and currents. Using machine learning techniques, specifically a Random Forest classifier, this simulator allows users to input real-time voltage and current readings and receive predictions on potential faults.

## Features
- **User Input**: Interactive fields for inputting current (Ia, Ib, Ic) and voltage (Va, Vb, Vc) values.
- **Fault Prediction**: Predicts the type of fault based on user input using a trained machine learning model.
- **Web Interface**: Built using Streamlit for easy access and usability.

## Libraries Used
- [scikit-learn](https://scikit-learn.org/stable/) - For implementing machine learning models.
- [joblib](https://joblib.readthedocs.io/en/latest/) - For saving and loading the trained model.
- [Streamlit](https://streamlit.io/) - For building a web-based interactive simulator.
- [pandas](https://pandas.pydata.org/) - For data manipulation and analysis.
- [numpy](https://numpy.org/) - For numerical operations.

## Getting Started

### Prerequisites
- Python 3.x
- Required libraries (install via pip):

```bash
pip install pandas numpy scikit-learn streamlit joblib
Running the Simulator
Clone this repository:

bash
Copy code
git clone <repository-url>
cd <repository-folder>
Train the machine learning model (if not already trained):

Ensure you have your dataset ready in the data folder.
Run the training script to generate the fault_classifier.pkl model:
bash
Copy code
python src/TrainModel.py  # Replace with your actual training script filename
Start the Streamlit app:

bash
Copy code
streamlit run src/fault_prediction_app.py  # Replace with your actual Streamlit app filename
Open your web browser and go to http://localhost:8501 to access the Fault Prediction Simulator.

Project Structure
bash
Copy code
/project-root
├── data/
│   ├── classData.csv
│   └── detect_dataset.csv
└── src/
    ├── fault_classifier.pkl    # Trained model
    ├── fault_prediction_app.py  # Streamlit application
    ├── main.py                 # Main application logic (if applicable)
    ├── power_system_data.txt    # Text file with power system analysis data
    └── TrainModel.py           # Script for training the machine learning model

Fault Types
The following fault types are predicted by the simulator:

0: No Fault
1: LG Fault (Phase A and Ground)
2: LL Fault (Phase A and Phase B)
3: LLG Fault (Phase A, B and Ground)
4: LLL Fault (All three Phases)


Areas for Improvement
Model Performance: Further evaluation and tuning of the machine learning model could improve prediction accuracy. Experimenting with different algorithms (e.g., Neural Networks, SVM) or hyperparameter tuning may yield better results.
Data Augmentation: The current model may benefit from more diverse training data to enhance its robustness. Collecting additional fault data under varying conditions can help in generalizing the model.
User Interface Enhancements: The Streamlit interface can be improved by adding visualizations, such as graphs or charts, to better represent the input data and prediction outcomes.
Error Handling: Implement better error handling in user inputs to ensure the application can gracefully handle invalid or out-of-range inputs.
Documentation: More detailed documentation on model training, evaluation metrics, and user guides can improve user experience and understanding of the system.
