# How long does it take for a computor to solve A-Puzzle-A-Day for every day in 2024?

**A-Puzzle-A-Day** is an adictive puzzle by [DragonFjord](https://www.dragonfjord.com/) where one tries to tile a calendar with certain pentris pieces revealing only the today's day and month. 
It be challanging for a beginner to solve some of the days.

### The answer is...
**1026.9 seconds** on M1 Max using a rather naive implementation available here.

### Usage
Generate an answer for a specific day using the month and the day as the arguments
```
python generate_single.py 12 29
```

Here is the example output:
```
Answer for December 29

LZTTTT..
LZZZT...
LLLZOOJ.
CCBBOOJ.
CBBBOOJ.
CCQQQJJ.
.QQ.....
........
```

## Generalization

The code generalizes to any shape-based puzzles on grids of 8x8 or smaler.

### City puzzle

The script for solving a city puzzle is a demostration of such an adaptation. 

## Where can I get this puzzle?
Here is the list of **A-Puzzle-A-Day** original puzzles (not an affiliate link, they are just good):
 - https://www.dragonfjord.com/product/a-puzzle-a-day-acrylic/
 - https://www.dragonfjord.com/product/a-puzzle-a-day/
 - https://www.dragonfjord.com/product/a-puzzle-a-day-deluxe/
 - https://www.dragonfjord.com/product/apad-legendary-boxed/

## Alternative solutions
After finishing this readme I discovered **a lot** of [alternative solutions](https://github.com/search?q=A-Puzzle-A-Day&type=repositories).

If you want to do a comparison benchmark, I will gladly accept a PR with results. 

## Special thanks
Special thanks to Polina for brainstorming the solution ideas and to [Anna](https://github.com/kvashchuka) for showing me this cool puzzle. 
   
