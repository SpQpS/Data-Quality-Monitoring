import pandas as pd

def monitor_data_quality(file_path, threshold=3):
    # Read the CSV file into a pandas DataFrame
    df = pd.read_csv(file_path)

    # Check for anomalies in numerical columns
    anomalies = []
    for column in df.select_dtypes(include='number').columns:
        mean = df[column].mean()
        std = df[column].std()

        # Identify values outside the threshold (e.g., 3 standard deviations from the mean)
        outlier_condition = (df[column] > mean + threshold * std) | (df[column] < mean - threshold * std)
        outliers = df[outlier_condition]

        if not outliers.empty:
            anomalies.append(f"Anomalies detected in {column}: {outliers.tolist()}")

    return anomalies

if __name__ == "__main__":
    # Specify the path to your CSV file
    data_file_path = "path/to/your/data.csv"

    # Set the threshold for anomaly detection (adjust as needed)
    threshold_value = 3

    # Monitor data quality and print any anomalies found
    anomalies_found = monitor_data_quality(data_file_path, threshold_value)
    
    if anomalies_found:
        for anomaly in anomalies_found:
            print(anomaly)
        print("Data quality issues detected. Please investigate.")
    else:
        print("No data quality issues found.")
