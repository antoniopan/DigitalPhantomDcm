# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.
import geometry.volume_phantom
import geometry.geometry_pi
import dcm.dcm_generator
from lxml import etree


def print_hi(name):
    # Use a breakpoint in the code line below to debug your script.
    print(f'Hi, {name}')  # Press Ctrl+F8 to toggle the breakpoint.


def verify_xml(xml_path: str, xsd_path: str) -> bool:
    xml_doc = etree.parse(xml_path)
    xsd_doc = etree.parse(xsd_path)
    xml_schema = etree.XMLSchema(xsd_doc)
    return xml_schema.validate(xml_doc)


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    if verify_xml('geometry/sample.xml', 'geometry/volume_phantom.xsd'):
        vol_gen = geometry.geometry_pi.VolumeGenerator()
        vol_gen.from_xml('geometry/sample.xml')
        dcm.dcm_generator.write_volume_to_dcm(vol_gen.process_volume(), 'cfg/ct_image.dcm', 'test')
        # config = volume_phantom.CreateFromDocument(open('geometry/sample.xml').read())
    print_hi('PyCharm')

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
