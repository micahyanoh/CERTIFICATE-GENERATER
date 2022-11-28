from importlib.resources import path
import os
def create_folders():
    try:
        os.makedirs('generated-certificate-data')
        os.makedirs('generated-certificate-data/images')
        os.makedirs('generated-certificate-data/pdf')
    except:
        pass

create_folders()