# launcher.py
import subprocess
import os

def launch_streamlit():
    print("Launching Streamlit app...")
    app_path = './app.py'
    command = f"streamlit run {app_path}"
    subprocess.run(command, shell=True)
