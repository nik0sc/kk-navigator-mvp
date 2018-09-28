# kk-navigator-mvp
MVP for the kkh navigator

## school digram overview
each level of each building follow the schematic of this:

[!SUTD_map](https://github.com/nik0sc/kk-navigator-mvp/blob/master/SUTD_map.jpg)

have 2 buildings, blk1 and blk2 for now

each building have 5 floor.

and each floor have a layout look like this.

### naming, the following names are correct names for start and destination
```
## elevators
1.2elevator # elevator on building 1, level 2
2.3elevator # elevator on building 2, level 3
## corners
1.2corner1  # corner 1 on building 1, level 2
2.4corner6  # corner 6 on building 2, level 6
## classrooms, each level have same number of classrooms and their position is also the same
1.201       # clsromm1 on building 1, level 2
2.510       # clsroom10 on building 2, level 5
```
### interconnections
```
## interconnection between each elevator on the same blk
1.2elevator connects 1.3elevator is connected(we assume 1.2 is the lowest floor)
1.3elevator connects 1.4elevator and 1.2elevator is connected.

## interconnection between blks
## there is only 2 inter blk connections
1. between 1.3elevator and 2.3elevator
2. between 1.5elevator and 2.5elevator
```
## run the program
[!example](https://github.com/nik0sc/kk-navigator-mvp/blob/master/example.png)
## acknowledgements:
using [dijkstras algorithm](https://github.com/mburst/dijkstras-algorithm) to find shortest path;
