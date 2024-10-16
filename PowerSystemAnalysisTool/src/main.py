import pandas as pd
import os

# Defining paths to the CSV files in the data folder
classdata_path = os.path.join('data', 'classData.csv')
detect_dataset_path= os.path.join('data', 'detect_dataset.csv')


classdata = pd.read_csv(classdata_path)
detect_data = pd.read_csv(detect_dataset_path)

print("Class Data Head:\n", classdata.head())
print("Detection Data Head:\n", detect_data.head())

# Extracting inputs and outputs for both datasets
class_input_data = classdata[['Ia', 'Ib','Ic', 'Va', 'Vb', 'Vc']]
class_output_data = classdata[['G', 'C', 'B', 'A']]
detect_input_data = detect_data[['Ia', 'Ib', 'Ic','Va', 'Vb', 'Vc']]
detect_output_data = detect_data['Output (S)'] # 0 -> no fault, 1 -> fault present

def interpret_class_fault(row):
    fault_mapping = {
        (0, 0, 0, 0): "No fault",
        (1, 0, 0, 1): "LG Fault (Phase A and Ground)",
        (0, 0, 1, 1): "LL Fault (Phase A and Phase B)",
        (1, 0, 1, 1): "LLG Fault (Phase A, B and Ground)",
        (0, 1, 1, 1): "LLL Fault (All three Phases)",
        (1, 1, 1, 1): "LLLG (Three Phase Symmetrical Fault)"
        }
    
    return fault_mapping.get(tuple(row), "Unkown Fault")

classdata['Fault Type'] = class_output_data.apply(interpret_class_fault, axis= 1)

def interpret_detect_fault(value):
    return "No Fault" if value == 0  else "Fault Present"

detect_data['Fault Status'] = detect_output_data.apply(interpret_detect_fault)

with open('power_system_data.txt', 'w') as f:
    #Write Header
    f.write("Power System Analysis Data\n")
    f.write("=" * 40 + "\n\n")

    # Class Data Section

    f.write("Classdata - Fault Classification:\n")
    f.write("Inputs (Ia, Ib, Ic, Va, Vb, Vc) and Fault types: \n")

    for index, row in classdata.iterrows():
        inputs = list(row[['Ia', 'Ib', 'Ic', 'Va', 'Vb', 'Vc']].values)
        fault_type = row['Fault Type']
        f.write(f"Row {index + 1}: Inputs: {inputs}, Fault Type : {fault_type}\n")
    
    f.write("\n" + "=" *40 + "\n\n")
    
    # Detect Dataset Section
    f.write("Detect Dataset - Fault Detection:\n")
    f.write("Inputs (Ia, Ib, Ic, Va, Vb, Vc) and Fault Status:\n")

    for index, row in detect_data.iterrows():
        inputs = list(row[['Ia', 'Ib', 'Ic', 'Va', 'Vb', 'Vc']].values)
        fault_status = row['Fault Status']
        f.write(f"Row{index + 1}: Inputs: {inputs}, Fault Status: {fault_status}\n")

print("Data successfully written to power_system_data.txt!")





