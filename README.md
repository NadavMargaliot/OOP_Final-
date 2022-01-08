# Pokemon, a game to remember

![pokemons](https://user-images.githubusercontent.com/84914845/148651629-1ba5abe1-79d8-409b-8858-1b243016e7b2.jpeg)

## Description
In this project we used the infrastructure of a directed weighted graph.

We have developed a game where a group of agents have to catch Pokemons, following the path of the graph depending on the edge direction.
Each edge is weighted, and each agent has a path planned for him so that he can catch as many Pokemons as possible in the shortest amount of time in order to achieve the highest score possible.

There are 0-16 levels, each with a different amount of agents, Pokemons and a given time.
Every Pokemon that is caught creates a new Pokemon in a random location on the graph.

In this project we received data from a server (jar file) and according to that the game is played.
The information of the game is represented as a JSON file.

The implementetion of the game is made out of two parts:
* Building the graph's data structurs and algorithms.
* Use the graph data structure and algorithms to implement the "POKEMON" game.

You can find all the information about the classes and algorithms of the directed weighted graph in here https://github.com/adiel1892/Ex3_Directed_Graph_Algo

## Classes 
### game
In this class we allocate the agent to the pokemon and basiclly controling the game.
* dist_node_to_node - find distance between two nodes.
* dist_pok_to_node - find distance between pokemon to node.
* find_src_dest_pok - find src and dest for the pokemon by given a position.
* update_pokemons_agents - updating the pokemons and the agents from the server.
* update - initializing the game by the information from the server.
* find_node - find node by given a position.
* find_node_by_edge - find node by given a position on the edge.
* allocate_agents - allocate a agent to a pokemon.
* time_and_shortest - calculate the travel time of the agent , and returns the shortest path.
* CMD - sends the agent to the pokemon.
* addAgents - add the right number of agents to each case.

### GUI
In this class we creating the gui for the game.
* scale
* drawNode
* drawEdges
* drawPokemons
* drawAgents
* draw - draw everything.

### Ex4
In this class we are running the project by connecting the server to the port, game and gui. 

## our algorithms for catching pokemons
We used a greedy algorithm which searching the "best" agent and the "best pokemon pair.
A best pair is a pair that the travel time between each other is the fastest.
A travel time is declared by the agent speed devided by the distance between the agent and the pokemon.
So, we finding the best pair and sending the agent to the pokemon.



