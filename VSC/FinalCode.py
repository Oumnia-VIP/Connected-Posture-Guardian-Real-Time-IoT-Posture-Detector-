# ai_virtual_sender.py
import joblib
import serial
import time
import warnings

# Suppress all warnings for clean output
warnings.filterwarnings("ignore")

# Load your AI model
model = joblib.load('posture_model.pkl')

ARDUINO_PORT = 'COM10'      # Your Arduino
VIRTUAL_PORT = 'COM11'      # Your Virtual Port (instead of Bluetooth)

print("🔌 Connecting to devices...")

# Connect to Arduino USB
try:
    arduino = serial.Serial(ARDUINO_PORT, 9600, timeout=1)
    time.sleep(2)
    print(f"✅ Connected to Arduino on {ARDUINO_PORT}")
except Exception as e:
    print(f"❌ Failed to connect to Arduino on {ARDUINO_PORT}: {e}")
    exit()

# Connect to Virtual Port (instead of Bluetooth)
try:
    virtual_out = serial.Serial(VIRTUAL_PORT, 9600)
    time.sleep(2)
    print(f"✅ Connected to Virtual Port on {VIRTUAL_PORT}")
except Exception as e:
    print(f"❌ Failed to connect to Virtual Port on {VIRTUAL_PORT}: {e}")
    arduino.close()
    exit()

print("🚀 SYSTEM READY!")
print("Arduino USB (COM10) → AI → Virtual (COM11) → COM12 → Node-RED")
print("Wear the sensor and try different postures!")
print("Press Ctrl+C to stop\n")

# Track last posture to avoid sending duplicates
last_posture = None

try:
    while True:
        if arduino.in_waiting > 0:
            line = arduino.readline().decode().strip()
            
            if line and ',' in line and line != "READY":
                try:
                    x, y, z = map(float, line.split(','))
                    
                    # Your 100% accurate AI!
                    posture = model.predict([[x, y, z]])[0]
                    confidence = model.predict_proba([[x, y, z]]).max()
                    
                    # Only send if posture changed (no duplicates)
                    if posture != last_posture:
                        # Send direct to Virtual Port
                        virtual_out.write(f"{posture}\n".encode())
                        print(f"📡 {posture:12} ({confidence:.1%}) → Virtual Port")
                        last_posture = posture
                    
                except Exception as e:
                    continue
        
        time.sleep(0.02)  # Small sleep to prevent CPU overload
        
except KeyboardInterrupt:
    print("\n🛑 Stopped by user")
finally:
    arduino.close()
    virtual_out.close()
    print("🔌 Disconnected from both devices")