"""
@created: Tien Anh Nguyen
@date: 2021-Mar-01
@description:
    +) In this example, we learn how to load and extract DICOM slices by using
        glob, os and matplotlib modules.
    +) os and glob are built-in modules of Python.
    +) matplotlib is third party library
    +) the folder (directory) contains multiple files, only one of them is DICOM
        data.
        +) using glob module to recognize DICOM data file.
        +) using SimpleITK module to read NRRD file.
"""
import os
import glob

import matplotlib.pyplot as plt
import SimpleITK as sitk

def load_data(dcm_dir):
    """
    @description:
        +) use module os.path.basename to get the file name and the extension
           of nrrd file
        +) there are 2 nrrd files, theh first one is the image file and the 
           last one is the mask file
    """
    nrrd_files = glob.glob(os.path.join(dcm_dir, '*.nrrd'))
    assert len(nrrd_files) > 0
    for nrrd_file in nrrd_files:
        file_name = os.path.basename(nrrd_file)
        if 'segmentation' not in file_name.lower():
            return nrrd_file
    return None

def extract_dcm_slice(nrrd_file, slice_index):
    """
    The dcm_image contains multiple slice, we just select one slice for 
    extraction
    """
    dcm_image = sitk.ReadImage(nrrd_file)
    dcm_arr = sitk.GetArrayFromImage(dcm_image)
    plt.imshow(dcm_arr[slice_index, :, :], cmap=plt.cm.gray)
    plt.savefig(str(slice_index) + '.png')

if __name__ == '__main__':
    """
    try to extract slice 23 of DICOM files
    """
    dcm_dir = '../../data/dicoms/7162170/25-7162170/SUB'
    patients_data = {}
    patients_data['7162170'] = {}
    nrrd_file = load_data(dcm_dir)
    slice_index = 23
    extract_dcm_slice(nrrd_file, slice_index)

