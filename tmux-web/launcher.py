# launcher.py
import subprocess
import os

def launch_streamlit():
    app_path = os.path.join(os.getcwd(), 'app.py')
    command = f"streamlit run {app_path}"
    subprocess.run(command, shell=True)
