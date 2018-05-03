class Data(dict):
    def __init__(self, xml, status=None, messages=None):
        """Process the xml instance into a friendly dictionary."""

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
            if node.tag == 'member':
                # Dictionary item
                key = node.find('name').text
                value_node = node.find('value')[0]

                if value_node.tag == 'int':
                    value = int(value_node.text.strip())
                elif value_node.tag in ['array', 'struct', 'data', 'param']:
                    value = self._breakdown_tree(value_node.findall('./'))
                elif value_node.tag == 'string':
                    try:
                        value = value_node.text.strip()
                    except AttributeError:
                        # Maliciously constructed data is detected in the responses for the string nodes
                        value = value_node.text
                else:
                    # dateTime.iso8601 or something exotic
                    value = value_node.text

                _data[key] = value
            elif node.tag == 'value':
                # Nodes are list items
                if not isinstance(_data, list):
                    _data = []
                _data.append(self._breakdown_tree(node.findall('./')))
            else:
                # Recursively find data as this is not a data node
                return self._breakdown_tree(node.findall('./'))
        return _data
