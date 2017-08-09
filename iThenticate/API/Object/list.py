class List(dict):
    def __init__(self, xml, object_name, status=None, messages=None):
        xml_regex = ".//member[name='{object_name}']/value/array/data/value/struct"
        nodes = xml.findall(xml_regex.format(object_name='folders'))
        content = {
            'data': [],
            'status': status or 200,
            'messages': messages or []
        }
        for node in nodes:
            # All items returned
            node_items = node.findall('member')
            _dict = {}
            for item in node_items:
                # All properties in a single item
                key = item.find('name').text
                value = item.find('.//value')[0].text
                _dict[key] = value
            content['data'].append(_dict)

        dict.__init__(self, content)
