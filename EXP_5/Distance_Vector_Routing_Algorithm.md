## Experiment 5

#  Distance Vector Routing Algorithm

### AIM

Write a python program to implement and simulate algorithm for distance vector routing protocol

### ALGORITHM


1. Start
2. Initialise the number of routers and their names
3. Define the a cost matrix(graph) with direct link costs
4. Copy the cost matrix into the distance table
5. Initialise a next hop table for routing
6. Repeat until no updates occur
    1. For each Router i
        1. For each destination j
            1. For each neighbour k
                1. if cost via k is less than current cost
                2. update `distance[i][j]` and `next_hop[i][j]`
7. After convergence, print the routing table for each router 
    
    `Destination    Cost    next_hop`

8. Stop


### RESULT

The output was obtained successfully