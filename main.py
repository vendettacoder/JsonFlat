import json
import sys

from json_flattener import JsonFlattener


def main():
    try:
        json_dict = read_json_file(sys.stdin)
    except ValueError as error:
        print("Error in loading json file : \n{0}".format(error))
        sys.exit()

    flat_dict = JsonFlattener().flatten(json_dict)
    print(json.dumps(flat_dict, indent=4, sort_keys=True))


def read_json_file(json_file):
    json_dict = json.load(json_file)
    return json_dict


if __name__ == "__main__":
    main()
