import sys
import os
# This adds the 'src' folder to the path manually so the test can find the code
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '../src')))

from tracer import analyze_metadata

def test_analyze_metadata_success():
    # This checks if the function returns the expected string
    result = analyze_metadata("ML-Project-Alpha")
    assert result == "Metadata extracted for ML-Project-Alpha"

def test_analyze_metadata_empty():
    # This checks if the error handling works
    result = analyze_metadata("")
    assert result == "Error: No repository name provided"
