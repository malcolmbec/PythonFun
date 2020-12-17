## Game Prompt Generator

**Author(s):** Becca Malcolm  

**Language:** Python3  

### Description

A simple prompt generator for making a game. The prompt generated takes the form of theme(s), goal(s), resource(s) and rule(s). 

- **Themes**: settings, genres, motifs and other themes to use for world-building or designing the game

- **Goals**: player objectives i.e. the purpose or focal point of the core game loop

- **Resources**: things that are managed by the player and that may affect the goal(s)

- **Rules**: mechanics or constraints for interacting with the core game loop OR designing the game i.e. how the player achieves the goal(s) OR challenges for the developer(s)

### How to Use

```
usage: game_prompt_generator [-h] [-g {1,2}] [-rs {1,2}] [-ru {1,2}]
                             [-th {1,2,3,4,5,6,7,8,9}]

Generate a game prompt.

optional arguments:
  -h, --help            show this help message and exit
  -g {1,2}, --goals {1,2}
                        the number of goals to generate
  -rs {1,2}, --resources {1,2}
                        the number of resources to generate
  -ru {1,2}, --rules {1,2}
                        the number of rules to generate
  -th {1,2,3,4,5,6,7,8,9}, --themes {1,2,3,4,5,6,7,8,9}
                        the number of themes to generate
```