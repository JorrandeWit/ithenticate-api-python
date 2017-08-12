class Data(dict):
    def __init__(self, xml, object_name, status=None, messages=None):
        """
        Process the freakin' xml instance to a friendly dictionary!
        """
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
                value_node = item.find('.//value')[0]

                # Value of node
                if value_node == 'int':
                    value = int(value_node.text.strip())
                elif value_node == 'array':
                    value = self.break_down_array_node(value_node)
                else:
                    # dateTime.iso8601 or string
                    value = value_node.text.strip()
                _dict[key] = value
            content['data'].append(_dict)

        dict.__init__(self, content)

    def break_down_array_node(self, node):
        """
        Dummy: To be implemented to be able to return nested array structs.
               Now, the node will return an empty string.
        """
        return node
