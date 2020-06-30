import queue


class JsonEntry:
    def __init__(self, key, value):
        self.key = key
        self.value = value


class JsonFlattener:
    """
    Breadth First Search Approach:

    Initially all entries from the dictionary are inserted into a queue. Every time an entry is processed from the queue,
    if the entry is a terminal entry (i.e does not have a populated dict as its value), its added to the flattened result.
    if not, then further entries are generated from the nested dict value and processing is continued until the queue is empty

    """
    def __init__(self):
        pass

    def flatten(self, json_dict):
        if json_dict is None:
            return None
        entry_queue = queue.Queue()
        flat_json_dict = dict()

        for key, value in json_dict.items():
            entry_queue.put(JsonEntry(key=key, value=value))

        while not entry_queue.empty():
            json_entry = entry_queue.get()
            if self._is_terminal(json_entry):
                self._add_to_flattened_dict(json_entry, flat_json_dict)
            else:
                self._add_nested_entries(json_entry, entry_queue)

        return flat_json_dict

    @staticmethod
    def _is_terminal(json_entry):
        return (type(json_entry.value) is not dict) or (len(json_entry.value) is 0)

    @staticmethod
    def _add_to_flattened_dict(json_entry, flat_json_dict):
        flattened_key = json_entry.key
        value = json_entry.value
        flat_json_dict[flattened_key] = value

    @staticmethod
    def _add_nested_entries(json_entry, entry_queue):
        cur_flattened_key = json_entry.key
        cur_value = json_entry.value

        for nested_key, nested_value in cur_value.items():
            next_flattened_key = str(cur_flattened_key) + '.' + nested_key
            entry_queue.put(JsonEntry(next_flattened_key, nested_value))
