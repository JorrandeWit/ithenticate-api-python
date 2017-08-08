import os

file_dir = os.path.dirname(__file__)
templates_dir = os.path.join(file_dir, 'templates')


def get_xml_as_string(template_name):
    _file = open(os.path.join(templates_dir, template_name), 'r')
    _str = _file.read()
    _file.close()
    return _str.replace('\n', '')
