# JsonFlat

A command line utility written in python that flattens a json object

## Steps to run:

1) Clone the github repo
2) Install python 2/3 : ``https://www.python.org/downloads/``
2) Navigate to the JsonFlat project
3) Run as : ``cat <path_to_json_file> | python main.py``

Where `path_to_json_file` is a json file containing the json object. Example file
in the project : `test_json.json`

Example run :

``cat test_json.json | python main.py``


## Steps to run unit tests:

The project uses the built in unittest module in python for unit test coverage

`python -m unittest -v test_json_flattener`

## Notes

- *Why Python?* : Mostly for the ease of developing command line applications and 
also for the minimal setup required by the users of the utility to get it up and running

- *Why minimal documentation?* : I believe clean code is the best documentation. 
String documentation isn't maintainable in the long term and can eventually become misleading 

- *Why BFS?* : Breadth first search allows for a more scalable solution as compared to recursive Depth first search 
where the scalability is limited by the maximum recursion stack, which is 999 in case of python

- *What I would have done differently for production code?*    
-- Extract json parsing functionality and parsing command line arguments into a utils module of its own to enable re-use   
-- JsonFlattener would implement an Interface to enable easy swapping of methods (say using DFS)     
-- Improved unit test coverage for main.py
 
