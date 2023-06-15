# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.
import geometry.volume_phantom
import geometry.geometry_pi
import dcm.dcm_generator
from lxml import etree
import sys


def verify_xml(xml_path: str, xsd_path: str) -> bool:
    xml_doc = etree.parse(xml_path)
    xsd_doc = etree.parse(xsd_path)
    xml_schema = etree.XMLSchema(xsd_doc)
    return xml_schema.validate(xml_doc)


def process_volume(cfg_path: str, dcm_template: str, dcm_output: str):
    if not verify_xml(cfg_path, 'geometry/volume_phantom.xsd'):
        print("Config file does not comply with xsd.")
        return
    vol_gen = geometry.geometry_pi.VolumeGenerator()
    vol_gen.from_xml(cfg_path)
    dcm.dcm_generator.write_volume_to_dcm(vol_gen.process_volume(), dcm_template, dcm_output)


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    """
    argv[0]: config file path
    argv[1]: dicom template file path
    argv[2]: output dicom directory
    """
    if not len(sys.argv) == 3:
        print("Does not have three arguments, use default.")
        process_volume('geometry/sample.xml', 'cfg/ct_image.dcm', 'test')
    else:
        process_volume(sys.argv[0], sys.argv[1], sys.argv[2])

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
