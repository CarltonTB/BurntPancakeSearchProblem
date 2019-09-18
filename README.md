# Burnt Pancake Search Problem
Implementations of breadth-first search and A* search to get solutions to the burnt pancake problem.

A* search example:

Input:
1b2b3b4w-a                # “-a” indicates to do A* search  

Output (possible):  
1b|2b3b4w g=0, h=23
1w2b|3b4w g=1, h=22  
2w1b3b|4w g=3, h=21  
3w1w|2b4w g=6, h=19  
1b3b2b|4w g=8, h=16  
2w3w|1w4w g=11, h=14  
3b2b1w|4w g=13, h=12  
1b|2w3w4w g=16, h=9  
1w2w3w4w g=17, h=0  

BFS example:  

Input:  
4b3b2b1b-f                # “-f” indicates to do BFS  

Output:  
|4b3b2b1b  
1w2w3w4w  