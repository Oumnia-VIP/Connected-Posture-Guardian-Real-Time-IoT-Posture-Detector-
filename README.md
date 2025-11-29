# Connected Posture Guardian: Real-Time-IoT-Posture-Detector

An affordable IoT solution for real-time student posture monitoring with AI-powered classification.

# Overview
Connected Posture Guardian is a real-time IoT system designed to help students maintain proper posture during extended study sessions. Using affordable hardware combined with machine learning, the system detects posture changes in under 2 seconds and provides immediate feedback through a web dashboard and mobile app.

# Key Statistics
- 100% classification accuracy on test data
- 98%+ accuracy in real-world conditions
- <2 seconds latency from sensor movement to alert
- $0 budget friendly - built with affordable components

# Features
Real-Time Posture Detection : Continuous monitoring with sub-2-second latency
AI-Powered Classification : Random Forest model trained on 800+ posture samples
Multi-Platform Interface : Web dashboard (Node-RED) and mobile app (MQTT)
Affordable Hardware : Arduino-based system accessible to students
Intuitive Alerts : Color-coded feedback (green/yellow/red) and non-intrusive notifications
Historical Analytics : Track posture trends and study habits over time

# Problem Statement
University students face significant challenges:

💻 85% report neck or back pain during exam periods
📚 6-12 hours/day average study time
💰 Limited budget for ergonomic solutions
🎒 Poor posture leads to fatigue, reduced concentration, and lower grades

# System Architecture

Hardware Stack
- Arduino Microcontroller : Reads and processes sensor data
- PmodACL Accelerometer : Measures X, Y, Z acceleration
- Bluetooth Module : Wireless communication to processing layer
- Polling Interval : 0.1 seconds for responsive detection

Software Stack
- Python : AI engine and data processing
- Node-RED : Dashboard and visualization
- MQTT : Real-time communication protocol
- Random Forest : Machine learning classification

# Posture Classification
The system detects four posture states:

Good Posture:
X: -0.98 to -1.00 (strong negative)
Y: -0.02 to +0.01 (near zero)
Z: 0.18 to 0.24 (low - sensor horizontal)
Pattern: Strong negative X, low Z

Slouching:
X: -0.21 to -0.23 (moderate negative)
Y: 0.00 to +0.01 (near zero)
Z: 0.91 to 0.93 (high - sensor vertical)
Pattern: Moderate negative X, high Z

Lean Right:
X: -0.62 to -0.83 (moderate negative)
Y: -0.37 to -0.60 (strong negative)
Z: 0.33 to 0.62 (medium)
Pattern: Strong negative Y

Lean Left:
X: -0.62 to -0.81 (moderate negative)
Y: +0.49 to +0.73 (strong positive)
Z: 0.24 to 0.36 (low-medium)
Pattern: Strong positive Y


🤖 Machine Learning Model
# Algorithm: Random Forest Classifier

Trees: 100 decision trees
Max Depth: 10
Min Samples Split: 2
Cross-Validation: 5-fold
Train-Test Split: 80/20
Training Data: 800 samples across all posture types

Why Random Forest?
✅ Handles non-linear body movement patterns
✅ Resistant to overfitting
✅ Fast inference for real-time capability
✅ Works well with small tabular datasets
✅ Provides confidence scores for each prediction

🔧 Installation & Setup
# Prerequisites

Arduino IDE
Python 3.8+
Node.js and Node-RED
MQTT Broker (HiveMQ or Mosquitto)

# Hardware Setup

Connect PmodACL accelerometer to Arduino via I2C : Sensor measures X,Y,Z acceleration
Arduino reads and sends via USB every 0.1s
Configure Bluetooth module for wireless communication: Bluetooth send the posture to Node red 



# Configuration

Update MQTT broker address in Python AI engine
Configure Node-RED with broker credentials
Set COM port mappings (Python: COM11, Node-RED: COM12)

# Run the code on arduino ide to collecte data in real time then once the mesures are sent to model we run the code on VSC where the model will apply the classifcation and the FinalCode will showcase the type of the posture and send it via bluethooth to Node-Red where we can see the results on the dashboard then the MQTT will send it to the MQTT.FX app .


👥 Contributors

Omnia BOUMADJOU
Ghita LABZAR
