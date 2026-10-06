import os
import sys

sys.path.insert(0, os.path.join(os.path.dirname(__file__), "..", "app"))
os.environ["AGS_API_KEY"] = "test-key"
os.environ["LITELLM_MASTER_KEY"] = "test-key"
