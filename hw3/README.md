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
![lg_normal](https://github.com/jphulse/ezr/blob/24Aug14/hw3/hw3_lg_rqsh.png)
![lg_divided](https://github.com/jphulse/ezr/blob/24Aug14/hw3/hw3_lg_divided_rqsh.png)
## Low-dimensional Data
![sm_normal](https://github.com/jphulse/ezr/blob/24Aug14/hw3/hw3_sm_rqsh.png)
![sm_divided](https://github.com/jphulse/ezr/blob/24Aug14/hw3/hw3_sm_divided_rqsh.png)
