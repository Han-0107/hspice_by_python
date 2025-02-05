import subprocess
import os

def delete_non_python_files(folder_path):
    for filename in os.listdir(folder_path):
        file_path = os.path.join(folder_path, filename)
        
        if os.path.isfile(file_path) and not filename.endswith('.py'):
            os.remove(file_path)

delete_non_python_files('/data/yaohuihan/Research/STA_Modeling/Spice/Cirs/generated')
delete_non_python_files('/data/yaohuihan/Research/STA_Modeling/Spice/Cirs/models/waveform')
delete_non_python_files('/data/yaohuihan/Research/STA_Modeling/Spice/Cirs/simulated')
delete_non_python_files('/data/yaohuihan/Research/STA_Modeling/Spice/Cirs/results/lib')
delete_non_python_files('/data/yaohuihan/Research/STA_Modeling/Spice/Cirs/results/csv')
delete_non_python_files('/data/yaohuihan/Research/STA_Modeling/Spice/Cirs/results/pivot')
delete_non_python_files('/data/yaohuihan/Research/STA_Modeling/Spice/Libs/Dataset')
delete_non_python_files('/data/yaohuihan/Research/STA_Modeling/Spice/Libs/Dataset/train')
delete_non_python_files('/data/yaohuihan/Research/STA_Modeling/Spice/Libs/Dataset/test')



scripts = [ '/data/yaohuihan/Research/STA_Modeling/Spice/Cirs/generated/generate_hspice.py', 
            '/data/yaohuihan/Research/STA_Modeling/Spice/Cirs/simulated/run_hspice.py', 
            '/data/yaohuihan/Research/STA_Modeling/Spice/Cirs/results/post_process1.py', 
            '/data/yaohuihan/Research/STA_Modeling/Spice/Cirs/results/post_process2.py',
            '/data/yaohuihan/Research/STA_Modeling/Spice/Cirs/results/post_process3.py',
            '/data/yaohuihan/Research/STA_Modeling/Spice/Cirs/results/post_process4.py']

for script in scripts:
    try:
        subprocess.run(['python', script], check=True)
    except subprocess.CalledProcessError as e:
        break
