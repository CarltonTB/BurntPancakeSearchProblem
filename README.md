# Burnt Pancake Search Problem
Implementations of breadth-first search and A* search to get solutions to the burnt pancake problem.

A* search example:

Input:
1b2b3b4w-a                # “-a” indicates to do A* search  

Output (possible):  
1b2b|3b4w g=0, h=3  
1b2b4b|3w g=2, h=4  
1b2b|4b3b g=3, h=4  
|1b2b3w4w g=5, h=2  
4b3b|2w1w g=9, h=4  
4b3b1b|2b g=11, h=4  
4b3b|1b2w g=12, h=4  
4b3b2b|1w g=14, h=4  
|4b3b2b1b g=15, h=4  
1w2w3w4w g=19, h=0  

BFS example:  

Input:  
4b3b2b1b-f                # “-f” indicates to do BFS  

Output:  
|4b3b2b1b  
1w2w3w4w  


Implemented using Python3. to run it, pass search problems as arguments:
python3 burnt_pancake_problem.py 1b2b3b4w-a

or simply run the script and you will be prompted to enter a search problem:
python3 burnt_pancake_problem.py
Enter a search problem in the form '1b2b3b4w-a' where -a means A* search and -f means BFS search