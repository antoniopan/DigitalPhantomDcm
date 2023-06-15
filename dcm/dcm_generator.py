import pydicom
import pydicom.uid
import copy
import os
import numpy as np
from volume import volume3d


def write_volume_to_dcm(vol: volume3d.Volume3D, sample_file_path: str, output_dir: str):
    if not os.path.exists(output_dir):
        os.mkdir(output_dir)

    ds = pydicom.dcmread(sample_file_path)
    ds.PatientName = "Test^Patient^Name"
    ds.PatientID = "123456"
    ds.InstanceUID = pydicom.uid.generate_uid()

    ds.PixelSpacing = [vol.x_spacing, vol.y_spacing]
    ds.Columns = vol.x_dim
    ds.Rows = vol.y_dim
    temp = copy.deepcopy(vol.x_orientation.v)
    ds.ImageOrientationPatient = temp.extend(vol.y_orientation.v)
    vol_origin = vol.origin()
    for i in range(vol.z_dim):
        ds.ImagePositionPatient = [vol_origin.x, vol_origin.y, vol_origin.z]
        ds.InstanceNumber = i
        ds.PixelData = np.ascontiguousarray(np.transpose(vol.pixel_data[:, :, i]))
        prefix = ''
        if i < 10:
            prefix = '000'
        elif i < 100:
            prefix = '00'
        elif i < 1000:
            prefix = '0'
        save_path = '%s/%s%d.dcm' % (output_dir, prefix, i)
        ds.save_as(save_path)
        vol_origin.move(vol.z_spacing * vol.y_orientation.z_unit_vector())
    return
