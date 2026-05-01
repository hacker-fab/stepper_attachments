from inference import get_model
import os

# Find the path where roboflow stores cache
# Example for Windows Users: r"C:\Users\<username>\.roboflow\cache"
model_cache_dir = "INSERT PATH TO YOUR WEIGHTS"
os.environ["MODEL_CACHE_DIR"] = model_cache_dir

# Make a Roboflow account and insert your own key here
API_KEY = "INSERT KEY"
model = get_model(
    model_id="INSERT MODEL",
    api_key=API_KEY
)

random_image = "path to random image"
results = model.infer(random_image)

# once this runs, visit your 'model_cache_dir' and run
# `cp <model_cache_dir> <destination that's out of the cache>`
# dig into the directly and look for a .onnx file -> those are your cached weights
