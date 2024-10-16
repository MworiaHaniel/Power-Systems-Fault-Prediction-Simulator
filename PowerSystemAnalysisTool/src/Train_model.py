import re
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import accuracy_score, classification_report, confusion_matrix
import joblib
import logging

# Setting up logging
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

def load_data_from_txt(file_path):
    inputs = []
    fault_types = []

    try:

        with open(file_path, 'r') as file:
            content =  file.readlines()

        logging.info(f"File '{file_path}' successfully loaded. checking content")

        if not content:
            logging.error("The file is empty. Please check the file content.")
            return pd.DataFrame, []
        

        # Skip header lines
        class_data_section = False
        for line in content:
            line = line.strip()
            if "Classdata" in line:
                class_data_section = True
                continue
            if "Detect Dataset" in line:
                class_data_section =  False

            if class_data_section and line:
                # extracts inputs and fault type
                match = re.search(r'Inputs:\s*\[(.*?)\],\s*Fault Type\s*:\s*(.+)', line)
                if match:
                    inputs_data = list(map(float, match.group(1).split(',')))
                    fault_type = match.group(2)
                    inputs.append(inputs_data)
                    fault_types.append(fault_type)

        logging.info(f"Extracted {len(inputs)} input samples.")

        if not inputs:
            logging.error("No input samples extracted. Check the file format  and content")

        return pd.DataFrame(inputs, columns=['Ia', 'Ib', 'Ic', 'Va', 'Vb', 'Vc']), fault_types
    

    except FileNotFoundError as e:
        logging.error(f"File not found: {file_path}")
        return pd.DataFrame, []
    
    except Exception as e:
        logging.error(f"An error occured: {e}")
        raise
                    
# Features -> X and Target Labels ->y
X, y = load_data_from_txt('power_system_data.txt')

if X.empty or not y:
    logging.error("No data available for training. Exiting the program")

else:
    y = pd.Series(y).astype('category').cat.codes # converting to numeric codes

    # 30% of the data will be used for testing and 70% will be used for training
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.3, random_state=42)
    model = RandomForestClassifier(random_state = 42)
    model.fit(X_train, y_train) # trains the Random  Forest Model using the training data

    # Evaluate the Model
    y_pred = model.predict(X_test)
    accuracy = accuracy_score(y_test, y_pred)
    logging.info(f"Model Accuracy: {accuracy * 100:.2f}%")

    # Display a classification report and confusion matrix
    print("\nClassification Report:")
    print(classification_report(y_test, y_pred))
    print("Confusion Matrix")
    print(confusion_matrix(y_test, y_pred))

    joblib.dump(model, 'fault_classifier.pkl')
    logging.info("Model saved as 'fault_classifier.pkl'")






