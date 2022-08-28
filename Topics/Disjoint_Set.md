# Disjoint Set

## Disjoint Sets and Operations

Disjoint Sets:
   - Non directed and non connected graph with one or multiple components
   - Each component is represented as a set.
   - Every two sets are not having anythin in common. - disjoint  

Operations
   1. Find: Find out any element or vertex belongs to which set
   2. Union: Add an edge between two vertices belong to different set, then perform the union between two sets
    
Example:

    s1 = {1, 2, 3, 4}     1 - 2 - 3 - 4
    s2 = {5, 6, 7, 8}     5 - 6 - 7 - 8
    s1 ∩ s2 = Ø
    
    Add edge (4, 6)       1 - 2 - 3 - 4 - 5 - 6 - 7 - 8
    s3 = s1 ∪ s2 
       = {1, 2, 3, 4, 5, 6, 7, 8}

    Add edge (1, 5)         1 - 2 - 3 - 4
    -> same set             |           |        
    -> there is a circle    5 - 6 - 7 - 8                    
                                    

   

## Graphical Representation

        7
     1 --- 3
    1|     |2
     |     |
     2 --- 4
    6|  5
     |  9
     5 --- 7
    3|     |4
     |     |
     6 --- 8
        8
    
Start: consider each elemen/vertex as a set

    1 2 3 4 5 6 7 8   
    u = {{1}, {2}, {3}, {4}, {5}, {6}, {7}, {8}}
    
Perform Union for edges 1 - 4: 

For each edge, one node as parent, one as child.

root ->  representive of the set

    (1, 2) (3, 4) (5, 6) (7, 8)
       1      3      5      7
       |      |      |      | 
       2      4      6      8
    s1 = {1, 2}, s2 = {3, 4}, s3 = {5, 6}, s4 = {7, 8}

Perform Union for edge 5: 

Find parent for vertices 2 and 4, and connect two parents - one as parent and the other as child.

    Find parents: (2, 4) -> (1, 3)
    Connect:
          1
         / \
        2   3
             \
              4
    s5 = {1, 2, 3, 4}, s3 = {5, 6}, s4 = {7, 8}

Perform Union for edge 6:

    (2, 5) -> (1, 5)
           1
         / | \
        2  3  5
            \  \
             4  6
    s5 = {1, 2, 3, 4, 5, 6}, s4 = {7, 8}

Perform Union for edge 7: 

Parents belong to the same set -> has circle

    (1, 3) -> (1, 1)

Perform Union for edge 8: 

    (6, 8) -> (1, 7)
             1
           / | \
         /  / \  \
        2  3   5  7
            \   \  \
             4   6  8
    s6 = {1, 2, 3, 4, 5, 6, 7, 8}

Perform Union for edge 9: 

Parents belong to the same set -> has circle

    (5, 7) -> (1, 1)
                
## Array Representation

Start:

Define a ```Parent``` array for eight vertices, each is initialized as -1, which means each vertex is in its own center.

    Parent: [-1, -1, -1, -1, -1, -1, -1, -1]
             1   2   3   4   5   6   7   8

Edge (1, 2):

Find parent: ```O(1)``` -> (1, 2)
Union two parents: 1 as parent, 2 as child 

    Parent[1] := Parent[1] + Parent[2] // how many nodes in the set
    Parent[2] := 1

    Parent: [-2, 1, -1, -1, -1, -1, -1, -1]
             1   2   3   4   5   6   7   8

Edge (3, 4), (5, 6), (7, 8)

    (3, 4) -> (3, 4)
    Parent: [-2, 1, -2,  3, -1, -1, -1, -1]
             1   2   3   4   5   6   7   8
    
    (5, 6) -> (5, 6)
    Parent: [-2, 1, -2,  3, -2,  5, -1, -1]
             1   2   3   4   5   6   7   8

    (7, 8) -> (7, 8)
    Parent: [-2, 1, -2,  3, -2,  5, -2,  7]
             1   2   3   4   5   6   7   8

Edge (2, 4)

    (2, 4) -> (1, 3) -> (-2, -2)
    Parent: [-4, 1,  1,  3, -2,  5, -2,  7]
             1   2   3   4   5   6   7   8

Edge (2, 5)

    (2, 5) -> (1, 5) -> (-4, -2) -> 1 as parent
    Parent: [-6, 1,  1,  3,  1 ,  5, -2,  7]
             1   2   3   4   5    6   7   8

Edge (1, 3)

    (1, 3) -> (1, 1) -> same parent -> has circle

Edge (6, 8)

    (6, 8) -> (1, 7) -> (-6, -2) -> 1 as parent
    Parent: [-8, 1,  1,  3,  1 ,  5,  1,  7]
             1   2   3   4   5    6   7   8

Edge (5, 7)

    (5, 7) -> (1, 1) -> same parent -> has circle

## Weighted Union & Collapsing Find

Weighted union:
- Weight: how many elements in the set
- Make the set with higher weights as parent
- To make the Uion set as balanced as possible
- Worst time for ```makeset```, ```find``` and ```union```: ```O(logn)```
  
Collapsing Find:
- Tranverse the whole tree, and directly link a node to the direct parent of the set.
- Time complexity with both weighted union and collapsing find: $O(\alpha_n)$, $\alpha_n$ is the inverse Ackerman function, which grows extraordinarily slowly. So this factor is 4 or less for any n that can actually be written in the physical universe. This makes disjoint-set operations practically amortized constant time.

             1
           / | \
         /  / \  \
        2  3   5  7
            \   \  \
             4   6  8

Find(2): 2 -> 1 two steps
Find(3): 3 -> 1 two steps
Find(4): 4 -> 3 -> 1 three steps

    Find(6)
               1
           / / | \  \
         /  /  |  \  \
        2  3   5   7  6
            \       \
             4       8
    Find(8)
              1
         / / / \ \ \
        2 3 5  7 6 8
             \     
              4      

## Applications
1. Detecting a Cycle: union two elements with the same parent 
2. Connected component of undirected graph: build set with find and union functions, count # of sets/roots
3. Merge connected component: find every node, merge two nodes if they have the same parent

## Questions

[200. Number of Islands](../src/200.number-of-islands.py)

[323. Number of Connected Components in an Undirected Graph](../src/323.number-of-connected-components-in-an-undirected-graph.py)

[684. Redundant Connection](../src/684.redundant-connection.py)

[721. Accounts Merge](../src/721.accounts-merge.py)


## Resources
1. https://www.youtube.com/watch?v=wU6udHRIkcc
2. https://en.wikipedia.org/wiki/Disjoint-set_data_structure#Time_complexity
3. https://leetcode.com/explore/featured/card/graph/618/disjoint-set/3881/
