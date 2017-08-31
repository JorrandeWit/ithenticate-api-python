class Data(dict):
    def __init__(self, xml, object_name, status=None, messages=None):
        """
        Process the freakin' xml instance to a friendly dictionary!
        """
        xml_regex = ".//member[name='{object_name}']/value/array/data/value/struct"
        struct_nodes = xml.findall(xml_regex.format(object_name=object_name))

        content = {
            'data': [],
            'status': status or 200,
            'messages': messages or []
        }

        if not struct_nodes:
            # Some responses are 'simple'
            xml_regex = ".//member[name='{object_name}']"
            struct_nodes = xml.findall(xml_regex.format(object_name=object_name))
            _dict = {}

            for item in struct_nodes:
                value, key = self._value_decision_tree(item)
                _dict[key] = value

            content['data'].append(_dict)
        else:
            # Complex structures
            for struct_node in struct_nodes:
                _dict = self.break_down_struct_node(struct_node)
                content['data'].append(_dict)

        dict.__init__(self, content)

    def _value_decision_tree(self, node):
        # All properties in a single item
        key = node.find('name').text
        value_node = node.find('.//value')[0]

        # Value of node
        if value_node == 'int':
            value = int(value_node.text.strip())
        elif value_node == 'array':
            value = self.break_down_array_node(value_node)
        elif value_node == 'struct':
            value = self.break_down_struct_node(value_node)
        elif value_node == 'string':
            value = value_node.text.strip()
        else:
            # dateTime.iso8601 or something exotic
            value = value_node.text
        return value, key

    def break_down_array_node(self, node):
        """
        Dummy: To be implemented to be able to return nested array structs.
               Now, the node will return an empty string.
        """
        return node

    def break_down_struct_node(self, struct):
        # All items returned
        node_items = struct.findall('member')
        _dict = {}

        for item in node_items:
            value, key = self._value_decision_tree(item)
            _dict[key] = value
        return _dict
