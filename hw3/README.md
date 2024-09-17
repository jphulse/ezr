# INSTALLATION, Running, & General Notes
Here is how to install and run my code:
* Boot up the GitHub codesoace on the 24Aug14 branch (this is the only place where I ran or wrote code so there is no gurantee it will work as expected anywhere else)
* Ensure that you have set the variable python3 correctly as per the instructions on the course website within the codespace
* In the hw3 directory, there is a script called run.sh, all you need to do is run this script, you may need to enable executable permissions "chmod +x run.sh"
* That file will queue and run all the jobs needed for this test in the background so you can do other things while it runs (takes approximately 15-30 min)
* If you do not wish to wait that long you can run just the python code with the command "python3 hw3.py [INSERT_INPUT_FILES_AND_PATHS]
* You may queue up as many files as you please for this, note that for all tests to execute during normal execution at least two files will need to be run on the same job
* Within the code for hw3.py I have placed several additional test cases via assert statements and two test methods, these are run during normal execution (as they were a great help in debuggiung) and do not need to be called separately, they test all cases indicated in the instructions and a few extras where I had issues
* Additionally, the code will automatically redirect standard out so do not mess with that, all that needs to be done is run the shell script, all output will be placed as appropriate into the appropriate folders within the out/ folder, lg for large (6 or more x cols), and sm for small, this was to easily facilitate the use of rqsh when viewing between large and small dimensionality data

# Results
## High-dimensional Data
### Brief breakdown of normal table for high dimensionality
![lg_normal](https://github.com/jphulse/ezr/blob/24Aug14/hw3/hw3_lg_rqsh.png)
  In the table above there are sveral interesting features that I would like to point out.  The first, and I believe most interesting feature is the Rank statistic for the smart and dumb treatments, both of these achieve rank 0 88% of the time (smart) and 66% of the time (dumb).  While this does make smart a decisive victor over the random selection, it does beg the interesting question of whether the accuracy penalty is worth dealing with for the speed increase in certain scenarios where accuracy may not be as crucial as speed at all times.  The second table indicates the number of evals required to reach each rank, and as you can see from the table the random and active learner are not crazy-far off of each other in this category either, especially when you start to take in mind the + or - factor that is at play here.  The DELTAS I believe are a little less relevant in this experiment, but again both treatments are relatively close in ranks 1 and 2 which I think is the big takeaway here, which is surprising as we are dealing with high dimensionality.  
  
### Brief breakdown of divided table for high dimensionality
![lg_divided](https://github.com/jphulse/ezr/blob/24Aug14/hw3/hw3_lg_divided_rqsh.png)
  In the table above I have taken the same input used in the previous table and formatted it differently to more clearly break down the different sizes as different categories so they could be evaluated individually for a more complete study.  The only category I will be breaking down is the RANK section, as the EVAL section here doesn't tell us much, and the DELTA tells us the same things we found out in the above table.  The RANK, however reveals some interesting details, firstly the active learner is almost always better on high-dimensional data regardless of the size used over the random selection.  This is not particularly surprising to me, although what is surprising is how close these are with the class of smart/40 and dumb/50 actually both having the same percentage.  I also think that it is interesting to note the fact that for the random choice the percentage value strinctly increases with N, whereas the active learner does not see a monotonic increase, and actually decreases with 20 being the second highest based on RANK 0 percentage.  Just an interesting observation, I can't really say anything too definitive other than that it appears that the active learner may actually be harmed by gaining more information before it hits a certain point and starts to increase again as it refines it's model.

## Low-dimensional Data
### Brief breakdown of normal table for low dimensionality
![sm_normal](https://github.com/jphulse/ezr/blob/24Aug14/hw3/hw3_sm_rqsh.png)
### Brief breakdown of divided table for low dimensionality
![sm_divided](https://github.com/jphulse/ezr/blob/24Aug14/hw3/hw3_sm_divided_rqsh.png)
