import subprocess
import os 
current_dir = os.getcwd()
text_name="nOTEPAD"
text_path = os.path.join(current_dir,text_name)

subprocess.Popen(['python',text_path])