# Problem Set 2: Line Segment Intersection

## Setup

1. From the terminal, clone your repository with the command

    `git clone your_repository_link`

    where `repository_link` is likely of the form ```https://github.com/HamiltonCollege/ps02-sweep-username```.

2. `cd` into the directory created (of the form ps02-sweep-*username*), and replace or update *sweep.py* with your functions from the assignment.

3. From the repository directory, run the timing code with 

    `python3 sweep_timer.py`

    then type in one of the two experiment options

    `same vary`

    which will run a subset of the algorithms so that you can evaluate the running time.

## Evaluating growth rates

**Experiment**: `same`

In this experiment a single table is printed, one line at a time. On each line of the experimental output, the number of input segments *n* doubles, and the number of intersections *I* is equal to *n*. Evaluate the growth rate of your algorithm by looking at how the running time grows with the number of segments and intersections:

- For *O(n log n + I)* running time, you should see the running time slightly more than double as *n* doubles.

**Experiment**: `vary`

In this experiment, multiple tables are printed, one line at a time. On each line of the experimental output, different values of *n* and *I* are printed. Within each table, *n* is fixed and *I* doubles (starting at *n*, reaching *n^2/4*). Between tables, *n* doubles. For this experiment:

- For running time *O(n log n + I)*, as *I* doubles, you should see the running time approximate double.

## Submitting

You only need to submit the file *sweep.py*. The easiest way is to upload it to GitHub by opening your repository in a browser (you can find it by navigating to github.com and clicking the link on the left-hand side); then click the *Upload files* button, and drag *sweep.py* to the browser window to update it.

Otherwise, from your repository directory on your machine, use `git` commands to submit your code with: 

`git add sweep.py`

`git commit -m "commit message goes here"`

`git push origin master`
