# 🚗 Smart Chassis Vibration Analysis System

### Wipro Automotive Course — Module 4 Project

A Python-based software simulation for monitoring, analyzing, and classifying vehicle chassis vibration patterns using simulated acceleration data.

---

## 📌 Project Overview

The **Smart Chassis Vibration Analysis System** is a software simulation designed to demonstrate how vibration monitoring can help identify abnormal vibration patterns in a vehicle's chassis.

The system generates simulated acceleration measurements along three axes (X, Y, and Z), calculates vibration magnitude, and compares the results against configurable thresholds.

Based on the detected vibration intensity, the system classifies the condition into three categories:

- 🟢 **Normal:** Vibration remains below the caution threshold.
- 🟠 **Caution:** Vibration reaches the caution threshold.
- 🔴 **Warning:** Vibration reaches or exceeds the warning threshold.

The application provides an interactive dashboard built using Streamlit, allowing users to visualize vibration patterns, analyze measurements, and download generated data for further analysis.

> **Note:** This project is a software simulation. The generated measurements and thresholds are illustrative and are not validated automotive safety limits. High vibration alone does not confirm structural damage or chassis cracks.

---

## 🎯 Project Objectives

The primary objectives of this project are:

1. Understand the relationship between chassis structures and vehicle vibrations.
2. Simulate three-axis acceleration measurements.
3. Calculate vibration magnitude from acceleration readings.
4. Analyze vibration intensity using statistical measurements.
5. Classify vibration levels using configurable thresholds.
6. Display vibration measurements through interactive graphs.
7. Demonstrate how abnormal vibration patterns can trigger warnings.
8. Export generated vibration data for further analysis.

---

## 🚀 Key Features

### 1. Vibration Simulation
Generates illustrative acceleration measurements along the X, Y, and Z axes.

### 2. Multiple Vibration Scenarios
The application supports four scenarios:

| Scenario | Description |
|---|---|
| Normal Road | Simulates low-level vibration |
| Moderate Vibration | Simulates increased vibration intensity |
| High Vibration Event | Simulates a period of elevated vibration |
| Sudden Impact | Simulates a short-duration vibration spike |

### 3. Configurable Simulation Settings
Users can adjust:

- Sampling rate (Hz)
- Simulation duration (seconds)
- Vibration scenario
- Caution threshold (m/s²)
- Warning threshold (m/s²)

### 4. Vibration Analysis
Calculates:

- Peak vibration magnitude
- Root Mean Square (RMS) magnitude
- Mean vibration magnitude
- Total number of samples collected

### 5. Interactive Dashboard
Displays:

- System status
- Acceleration graphs for all three axes
- Vibration magnitude graph
- Configurable threshold lines
- Sample vibration data

### 6. CSV Data Export
Allows users to download the complete simulated dataset in CSV format for further analysis.

---

## 🛠️ Technologies Used

| Technology | Purpose |
|---|---|
| Python | Core programming language |
| Streamlit | Interactive web dashboard |
| NumPy | Numerical computations and simulated data generation |
| Pandas | Data handling and CSV export |
| Plotly | Interactive data visualization |

---

## 📂 Project Structure

```text
smart_chassis_vibration_simulator/
│
├── app.py
│   └── Main application and dashboard
│
├── requirements.txt
│   └── Required Python libraries
│
├── README.md
│   └── Project documentation
│
└── Generated Data
    └── Downloadable CSV vibration datasets
```

---

## ⚙️ System Architecture

The system follows a simulation-based vibration monitoring workflow.

```text
          START
            |
            v
    Select Simulation Settings
            |
            v
    Generate Acceleration Data
       (X, Y, Z Axes)
            |
            v
    Calculate Vibration Magnitude
            |
            v
    Compute Statistical Metrics
      (Peak, RMS, Mean)
            |
            v
    Compare Against Thresholds
            |
            v
      Classify Vibration
            |
      +-----+------+
      |     |      |
      v     v      v
   NORMAL CAUTION WARNING
      |     |      |
      +-----+------+
            |
            v
     Display Dashboard
            |
            v
      Export Data as CSV
            |
            v
           END
```

---

## 🧮 Mathematical Model

### 1. Vibration Magnitude

The vibration magnitude is calculated using the acceleration values along the three axes.

$$
A = \sqrt{a_x^2 + a_y^2 + a_z^2}
$$

Where:

- `A` = Vibration magnitude
- `a_x` = X-axis acceleration
- `a_y` = Y-axis acceleration
- `a_z` = Z-axis acceleration

The magnitude represents the combined acceleration value across the three axes.


### 2. Peak Magnitude

Peak magnitude represents the maximum vibration magnitude observed during the simulation.

$$
A_{peak} = \max(A_1, A_2, \ldots, A_n)
$$

### 3. Root Mean Square (RMS)

RMS is calculated as:

$$
A_{RMS} = \sqrt{\frac{1}{N}\sum_{i=1}^{N} A_i^2}
$$

Where:

- `N` = Total number of samples
- `Ai` = Vibration magnitude at sample `i`

### 4. Mean Magnitude

Mean magnitude is calculated as:

$$
A_{mean} = \frac{1}{N}\sum_{i=1}^{N} A_i
$$

These metrics help summarize the vibration behavior of the simulated signal.

---

## 🚦 Vibration Classification

The system compares the peak vibration magnitude against two configurable thresholds.

| Condition | Classification | System Status |
|---|---|---|
| Peak < Caution Threshold | Normal | 🟢 NORMAL |
| Caution Threshold ≤ Peak < Warning Threshold | Moderate | 🟠 CAUTION |
| Peak ≥ Warning Threshold | High | 🔴 WARNING |

### Default Thresholds

| Parameter | Default Value |
|---|---|
| Caution Threshold | 1.50 m/s² |
| Warning Threshold | 3.00 m/s² |

These values are demonstration settings and are not validated limits for real vehicles.

---

## 💻 Installation and Setup

Follow these instructions to run the project locally.

### Prerequisites

Make sure the following are installed:

- Python 3.10 or later
- pip
- Visual Studio Code (recommended)

---

### Step 1: Download the Project

Download or clone the project repository.

If using Git:

```bash
git clone <YOUR_GITHUB_REPOSITORY_URL>
```

Navigate into the project folder:

```bash
cd smart_chassis_vibration_simulator
```

Alternatively, extract the downloaded ZIP file and open the extracted folder in VS Code.

---

### Step 2: Create a Virtual Environment

On macOS or Linux:

```bash
python3 -m venv .venv
```

Activate the environment:

```bash
source .venv/bin/activate
```

On Windows:

```powershell
python -m venv .venv
.venv\Scripts\activate
```

---

### Step 3: Install Dependencies

Upgrade pip:

```bash
python -m pip install --upgrade pip
```

Install the required libraries:

```bash
pip install -r requirements.txt
```

---

### Step 4: Run the Application

Start the Streamlit application:

```bash
streamlit run app.py
```

The dashboard will open in your default browser.

If it does not open automatically, navigate to:

```text
http://localhost:8501
```

---

## 📊 How to Use the Application

### Step 1: Open the Dashboard

Run the application using:

```bash
streamlit run app.py
```

### Step 2: Configure Simulation Settings

Use the sidebar to select:

- Sampling rate
- Simulation duration
- Vibration scenario
- Caution threshold
- Warning threshold

### Step 3: Run the Simulation

Click the **Run Simulation** button.

The application generates simulated acceleration data and performs vibration analysis.

### Step 4: Analyze the Results

Review the following:

- System status
- Peak magnitude
- RMS magnitude
- Mean magnitude
- Acceleration graphs
- Vibration magnitude graph
- Event summary

### Step 5: Download the Dataset

Click the **Download complete data as CSV** button to export the generated measurements.

---

## 🧪 Testing and Validation

The application supports four test scenarios.

### Test Case 1: Normal Road

| Parameter | Value |
|---|---|
| Test Case ID | TC-01 |
| Scenario | Normal Road |
| Expected Status | NORMAL |
| Expected Behavior | Vibration remains below the caution threshold |

**Observation:** The system classifies the simulated vibration as normal when the peak magnitude is below the caution threshold.

### Test Case 2: Moderate Vibration

| Parameter | Value |
|---|---|
| Test Case ID | TC-02 |
| Scenario | Moderate Vibration |
| Expected Status | CAUTION or WARNING |
| Expected Behavior | Increased vibration is detected |

**Observation:** The system classifies the vibration according to the peak magnitude and the configured thresholds.

### Test Case 3: High Vibration Event

| Parameter | Value |
|---|---|
| Test Case ID | TC-03 |
| Scenario | High Vibration Event |
| Expected Status | WARNING |
| Expected Behavior | Elevated vibration triggers a warning |

**Observation:** The system displays a warning when the peak magnitude reaches or exceeds the warning threshold.

### Test Case 4: Sudden Impact

| Parameter | Value |
|---|---|
| Test Case ID | TC-04 |
| Scenario | Sudden Impact |
| Expected Status | WARNING |
| Expected Behavior | A sudden vibration spike is detected |

**Observation:** The system identifies the simulated impact based on the peak magnitude.

---

## 📋 Test Results Summary

Record the actual results after running each scenario.

| Test Case | Scenario | Expected Result | Actual Result |
|---|---|---|---|
| TC-01 | Normal Road | Normal | To be recorded |
| TC-02 | Moderate Vibration | Caution/Warning | To be recorded |
| TC-03 | High Vibration Event | Warning | To be recorded |
| TC-04 | Sudden Impact | Warning | To be recorded |

> The actual values may vary between simulation runs because the acceleration data is generated randomly.

---

## 🔗 SCREENSHOTS 📸

### NORMAL ROAD

<img width="1440" height="900" alt="Screenshot 2026-09-27 at 6 35 49 PM" src="https://github.com/user-attachments/assets/befa37bd-2cd0-43e9-96df-71f2947b8531" />
<img width="1440" height="900" alt="Screenshot 2026-09-27 at 6 35 56 PM" src="https://github.com/user-attachments/assets/335f410c-95c4-4ea1-a537-4cb4791f527c" />
<img width="1440" height="900" alt="Screenshot 2026-09-27 at 6 36 03 PM" src="https://github.com/user-attachments/assets/490ff963-1d4b-45a0-86bd-aa9d1e7bed02" />
<img width="1440" height="900" alt="Screenshot 2026-09-27 at 6 36 10 PM" src="https://github.com/user-attachments/assets/1b874613-6a6d-40c2-ade9-7485943e009c" />
<img width="1440" height="900" alt="Screenshot 2026-09-27 at 6 36 17 PM" src="https://github.com/user-attachments/assets/b1f086da-1a92-489b-9bdb-3662942cc1c4" />

### MODERATE VIBRATION

<img width="1440" height="900" alt="Screenshot 2026-09-27 at 6 37 06 PM" src="https://github.com/user-attachments/assets/b0dac16e-15e8-409d-bd12-e4493cd632e5" />
<img width="1440" height="900" alt="Screenshot 2026-09-27 at 6 37 12 PM" src="https://github.com/user-attachments/assets/0bd8ba17-f7ec-4f9e-90e7-3af534bc6d33" />
<img width="1440" height="900" alt="Screenshot 2026-09-27 at 6 37 19 PM" src="https://github.com/user-attachments/assets/3c256b9e-6197-49b2-b3fc-e90a275f5a1f" />
<img width="1440" height="900" alt="Screenshot 2026-09-27 at 6 37 27 PM" src="https://github.com/user-attachments/assets/b5a7b701-22f7-4d61-9766-f7f087f69e32" />
<img width="1440" height="900" alt="Screenshot 2026-09-27 at 6 37 34 PM" src="https://github.com/user-attachments/assets/36963787-7c91-43d6-b17f-a8e464655a8c" />

### HIGH VIBRATION EVENT

<img width="1440" height="900" alt="Screenshot 2026-09-27 at 6 38 22 PM" src="https://github.com/user-attachments/assets/d62979e2-2886-461d-967f-66626838cf81" />
<img width="1440" height="900" alt="Screenshot 2026-09-27 at 6 38 29 PM" src="https://github.com/user-attachments/assets/49c1a2df-da16-4528-9530-1dfe0aff315c" />
<img width="1440" height="900" alt="Screenshot 2026-09-27 at 6 38 36 PM" src="https://github.com/user-attachments/assets/e4b3909e-4fb2-49e7-ac94-dc1895e70dd7" />
<img width="1440" height="900" alt="Screenshot 2026-09-27 at 6 38 46 PM" src="https://github.com/user-attachments/assets/ce73dd31-3eca-4feb-8bb1-dde4ced23303" />

### SUDDEN IMPACT

<img width="1440" height="900" alt="Screenshot 2026-09-27 at 6 39 40 PM" src="https://github.com/user-attachments/assets/128a54f5-1a58-43e4-9e06-43a5ab071d81" />
<img width="1440" height="900" alt="Screenshot 2026-09-27 at 6 39 47 PM" src="https://github.com/user-attachments/assets/371de8f3-7106-4a87-a7fa-ff4f8d9720f0" />
<img width="1440" height="900" alt="Screenshot 2026-09-27 at 6 39 54 PM" src="https://github.com/user-attachments/assets/c0cc67ea-105f-4b2e-98c8-d61fc4fcd516" />
<img width="1440" height="900" alt="Screenshot 2026-09-27 at 6 39 59 PM" src="https://github.com/user-attachments/assets/4f6a15ad-06d0-406f-84bb-ec3f8db2a571" />

---

## ⚠️ Limitations

The current implementation has the following limitations:

1. The application uses simulated acceleration data rather than measurements from a real vehicle.
2. The vibration thresholds are illustrative and are not validated automotive safety limits.
3. The system does not directly detect chassis cracks or confirm structural damage.
4. The application does not use a physical accelerometer or microcontroller.
5. The current implementation does not perform frequency-domain analysis.
6. The simulation does not account for all real-world vehicle operating conditions.

Actual structural health monitoring would require calibrated sensors, vehicle-specific testing, validated thresholds, and engineering assessment.

---

## 🔮 Future Scope

The project can be extended with the following improvements:

### 1. Hardware Integration
Connect an accelerometer such as the MPU6050 to an ESP32 to collect physical vibration measurements.

### 2. Real-Time Monitoring
Develop a system that receives and analyzes live sensor data.

### 3. Frequency-Domain Analysis
Implement Fast Fourier Transform (FFT) to study vibration frequency components.

### 4. Historical Data Analysis
Store vibration measurements and compare results across multiple test sessions.

### 5. Advanced Signal Processing
Introduce filtering and signal-processing techniques to improve the analysis of measured vibration signals.

### 6. Machine Learning
Explore machine-learning methods for identifying vibration patterns after collecting and validating suitable datasets.

### 7. Vehicle-Specific Calibration
Establish thresholds using controlled experiments and reference measurements for a specific vehicle and operating condition.

---

## 🏁 Conclusion

The **Smart Chassis Vibration Analysis System** demonstrates how a software-based simulation can be used to monitor and analyze vehicle chassis vibration patterns.

By generating three-axis acceleration data, calculating vibration magnitude, and comparing the results against configurable thresholds, the application classifies vibration conditions into normal, caution, and warning categories.

The interactive Streamlit dashboard provides graphical visualization, statistical measurements, and CSV data export.

The project connects automotive chassis engineering with vibration monitoring and demonstrates a conceptual approach to identifying abnormal vibration behavior.

Although the current implementation is limited to simulated data, it provides a foundation for future development involving real sensors, signal processing, and validated automotive monitoring methods.

---

## 👩‍💻 Author

**Trisha Basak**

B.Tech — Computer Science and Engineering

**Project:** Smart Chassis Vibration Analysis System

---
