class Data(dict):
    def __init__(self, xml, status=None, messages=None):
        """
        Process the freakin' xml instance to a friendly dictionary!
        """

        content = {
            'data': None,
            'status': status or 200,
            'messages': messages or []
        }

        struct_nodes = xml.findall('./')
        data = self._breakdown_tree(struct_nodes)
        content['data'] = data

        dict.__init__(self, content)

    def _breakdown_tree(self, nodes):
        # All properties in a single item
        _data = {}
        for node in nodes:
            value_node = node.find('value')

            if not value_node:
                # Recursively find data as this is not a data node
                return self._breakdown_tree(node.findall('./'))
            else:
                key = node.find('name')
                value_node = value_node[0]

            # Value of node
            if value_node.tag == 'int':
                value = int(value_node.text.strip())
            elif value_node.tag in ['array', 'struct', 'data', 'param']:
                value = self._breakdown_tree(value_node.findall('./'))
            # elif value_node.tag == 'struct':
            #     value = self.break_down_struct_node(value_node)
            elif value_node.tag == 'string':
                try:
                    value = value_node.text.strip()
                except AttributeError:
                    # Maliciously constructed data is detected in the responses for the string nodes
                    value = value_node.text
            else:
                # dateTime.iso8601 or something exotic
                value = value_node.text

            try:
                if key.text in ['api_status', 'status', 'messages', 'sid']:
                    # Exclude this, it'll just be duplicate in the response dictionary
                    continue
                _data[key.text] = value
            except AttributeError:
                # Root element is list as its node won't have a name
                _data = [value]
        return _data
