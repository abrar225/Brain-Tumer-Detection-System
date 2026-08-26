import sys

if hasattr(sys.stdout, "reconfigure"):
    sys.stdout.reconfigure(encoding="utf-8", errors="replace")

import numpy as np
import time
from tensorflow.keras.models import load_model

def examine_model():
    print("========================================")
    print("      Model Examination & Peak Test     ")
    print("========================================")
    
    try:
        print("\n[1] Loading model from models/model.h5...")
        model = load_model('models/model.h5')
        print("✅ Model loaded successfully!")

        print("\n[2] Model Architecture Summary")
        model.summary()

        print("\n[3] Model Shape Analysis")
        print(f"Input Shape Expected:  {model.input_shape}")
        print(f"Output Shape Expected: {model.output_shape}")
        
        # Testing inference speed and capability with dummy data
        img_size = model.input_shape[1]
        print(f"\n[4] Peak Capability Test: Generating dummy tensor of shape (1, {img_size}, {img_size}, 3)")
        dummy_input = np.random.rand(1, img_size, img_size, 3)
        
        print("Warming up model...")
        _ = model.predict(dummy_input, verbose=0)
        
        print("Running benchmark (100 iterations)...")
        start = time.time()
        for i in range(100):
            _ = model.predict(dummy_input, verbose=0)
        end = time.time()
        
        avg_time = ((end - start) * 1000) / 100
        print(f"✅ Peak Inference Speed: {avg_time:.2f} ms per image")
        
        predictions = model.predict(dummy_input, verbose=0)
        print(f"Sample Output Probabilities: {predictions[0]}")
        print("========================================\n")
        
    except Exception as e:
        print(f"❌ Error examining model: {e}")

if __name__ == "__main__":
    examine_model()
