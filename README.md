# Burnt Pancake Search Problem
repo: https://github.com/CarltonTB/BurntPancakeSearchProblem  
Python version: 3.6  

Implementations of breadth-first search and A* search to get solutions to the burnt pancake problem.  
States are represented in the form 1b2b3b4w where the number is the pancake size, e.g. 4 is the largest and   
1 is the smallest. w means white side up and b means burnt side up, and the goal state is 1w2w3w4w.  

A* search example ( “-a” indicates to do A* search):  
 
Input:
1b2b3b4w-a               

Output (possible):  
1b|2b3b4w g=0, h=3  
1w2b|3b4w g=1, h=3  
2w|1b3b4w g=3, h=3  
2b1b|3b4w g=4, h=3  
1w2w3b|4w g=6, h=3  
3w|2b1b4w g=9, h=3  
3b2b1b|4w g=10, h=3  
1w2w3w4w g=13, h=0  

BFS example (“-f” indicates to do BFS):  

Input:  
4b3b2b1b-f  

Output:  
4b3b2b1b|  
1w2w3w4w  


Implemented using Python3. to run it, pass search problems as arguments:  
python3 burnt_pancake_problem.py 1b2b3b4w-a  

or simply run the script and you will be prompted to enter a search problem:    
python3 burnt_pancake_problem.py  
Enter a search problem in the form '1b2b3b4w-a' where -a means A* search and -f means BFS  
1b2b3b4w-a  

To run tests:  
python3 burnt_pancake_tests.py  
python3 search_tree_tests.py  