# realtime_test.py
import joblib
import serial
import time
import serial.tools.list_ports

# Find Arduino port
def find_arduino_port():
    ports = list(serial.tools.list_ports.comports())
    for p in ports:
        if 'Arduino' in p.description or 'USB' in p.description:
            return p.device
    return None

# Load AI model
print("🧠 Loading AI model...")
model = joblib.load('posture_model.pkl')
print(f"✅ Model loaded! Can detect: {list(model.classes_)}")

# Find and connect to Arduino
arduino_port = find_arduino_port()
if not arduino_port:
    print("❌ Arduino not found! Check USB connection.")
    print("Available ports:")
    ports = list(serial.tools.list_ports.comports())
    for p in ports:
        print(f"  - {p.device}: {p.description}")
    exit()

print(f"🔌 Connecting to Arduino on {arduino_port}...")
ser = serial.Serial(arduino_port, 9600, timeout=1)
time.sleep(2)  # Wait for connection

print("\n🎯 REAL-TIME POSTURE DETECTION ACTIVE!")
print("========================================")
print("Wear the sensor and try these postures:")
print("  - Sit straight → GOOD POSTURE")
print("  - Lean forward → SLOUCHING") 
print("  - Lean left    → LEAN LEFT")
print("  - Lean right   → LEAN RIGHT")
print("========================================")
print("Press Ctrl+C to stop\n")

# Posture emojis
emojis = {
    'good_posture': '✅',
    'slouching': '⚠️',
    'lean_left': '⬅️',
    'lean_right': '➡️'
}

try:
    while True:
        if ser.in_waiting > 0:
            line = ser.readline().decode('utf-8').strip()
            
            if line and ',' in line and 'READY' not in line:
                try:
                    # Parse sensor data
                    x, y, z = map(float, line.split(','))
                    
                    # AI prediction
                    posture = model.predict([[x, y, z]])[0]
                    confidence = model.predict_proba([[x, y, z]]).max()
                    
                    # Confidence color
                    if confidence > 0.9:
                        conf_color = "🟢"
                    elif confidence > 0.7:
                        conf_color = "🟡" 
                    else:
                        conf_color = "🔴"
                    
                    # Display result
                    print(f"{emojis.get(posture, '❓')} {posture:12} | {conf_color} {confidence:5.1%} | XYZ: [{x:7.3f}, {y:7.3f}, {z:7.3f}]")
                    
                except ValueError:
                    continue  # Skip bad data
                
        time.sleep(0.1)
        
except KeyboardInterrupt:
    print("\n🛑 Stopped by user")
finally:
    ser.close()
    print("🔌 Arduino disconnected")