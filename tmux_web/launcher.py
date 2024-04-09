# launcher.py
import subprocess
import os

def launch_streamlit():
    print("Launching Streamlit app...")
    dir_path = os.path.dirname(os.path.realpath(__file__))
    app_path = os.path.join(dir_path, 'app.py')
    command = f"streamlit run {app_path}"
    subprocess.run(command, shell=True)