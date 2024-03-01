# <span style="color:#FF8200">NBA Shooting Visualization Tool </span>

#### Created by Price LeNoir for COSC494 (Spring 2024) taught by Dr. James Plank

## <span style="color:#8C4A1D"> About the Project </span>

The NBA Shooting Visualization Tool (NSV) provides insights into a player's shooting performance throughout designated NBA seasons. This project utilizes data sourced from `nba_api`, which is an API Client for [NBA.com](https://www.nba.com/). The repository can be found [here](https://github.com/swar/nba_api/tree/master). NSV represents each shot taken by the player, delineating successful attempts with green dots and misses with red dots. This project employs `jgraph` for visualization. [Jgraph](https://web.eecs.utk.edu/~jplank/plank/jgraph/jgraph.html), created by Dr. James Plank in 1992, is a versatile program that generates postscript files from graph descriptions. Alongside visualizing shot distribution, NSV provides statistics such as field goal percentage and 3-point field goal percentage.



## <span style="color:#8C4A1D"> Installing NSV </span>

This repository assumes `convert` is installed. If it is not, run the following command:
```bash
brew install imagemagick
```

#### 1. Install `jgraph`
The tar file is available at [Dr. Plank's website](https://web.eecs.utk.edu/~jplank/plank/jgraph/jgraph.html). Once extracted, you will need to use the makefile within the `/jgraph` directory to compile the executable. It is best to move this executable to your `$PATH`.

#### 2. Install dependencies
This project uses the `nba_api` library which requires `Python 3.7+`.
```bash
pip3 install nba_api
```

#### 3. Use Makefile
After installiing `convert`, `jgraph`, and the `nba_api` package, NSV is ready for use. The makefile within this repo will output several examples to a `/shotcharts` directory. The examples are displayed in the section below.

#### 4. Using NSV
```bash
sh nsv.sh <Firstname> <Lastname> <Startseason> <Endseason>
```

## <span style="color:#8C4A1D">  Examples </span>
There is no better use of this tool than to observe the greatness of Stephen Curry during his unanimous MVP season. Let's take a look:
```bash
sh nsv.sh Stephen Curry 2015 2016
```
![Image1](/shotcharts/Stephen_Curry_2015-2016.jpg)

It's very easy to differentiate between play styles just by visualizing the shooting volume differences between Curry and Michael Jordan during his final championship season. The majority of MJ's buckets came from inside the 3-point line.
```bash
sh nsv.sh Michael Jordan 1997 1998
```
![Image2](/shotcharts/Michael_Jordan_1997-1998.jpg)

Now, let's check out the shooting distribution for Charles Barkley. It is obvious that his 3-point shooting is about as pure as his golf swing. 
```bash
sh nsv.sh Charles Barkley 1998 1999
```
![Image3](/shotcharts/Charles_Barkley_1998-1999.jpg)

There's a significant difference between Barkley and Kyle Korver who shot almost exclusively 3-pointers during his lone all-star season with the Atlanta Hawks.
```bash
sh nsv.sh Kyle Korver 2014 2015
```
![Image4](/shotcharts/Kyle_Korver_2014-2015.jpg)

Finally, NSV also has the capability to visulize shooting over the course of multiple seasons. Let's use the Tennessee Volunteer legend, Grant Williams, as an example. The majority of William's career points have come from within the paint or behind the 3-point-arc.
```bash
sh nsv.sh Grant Williams 2019 2024
```
![Image5](/shotcharts/Grant_Williams_2019-2024.jpg)