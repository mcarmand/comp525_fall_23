COMP 525 Data Structures Fundamentals - Fall 2023

## Homework 2 Guidelines

Assigned week 6. Due by Midnight Nov 1st.

### Purpose of the homework

In this homework assignment you will:

- Design and implement **linear-efficient algorithms** that use Python 
  `str` and `list` built-in data types
- Practice **test-driven incremental development** to: 1) understand, 
  document, and test; 2) design, and 3) implement a computational solution
- Apply **version control**  that supports incremental development.

### Test-driven incremental development

#### I. Understand and document the problem

- The docstrings for the modules **linear_efficiency.py** in **src** and all 
  testing modules in **tests** must have your name and completion date. 
- All testing functions must have docstrings.
- **Version control** these development changes to reflect the 
  **documentation step**. Note that this is the very first commit of the 
  program development for this assignment. 

To understand the problem, we need to know **what** the solution (or 
**output** should be for different **input** cases. That's why we write test 
cases as testing functions in a testing module that corresponds to each 
**source function** in **src/linear_efficiency,.py** that we develop. 

For each **source function** in **src/linear_efficiency.py**:
- Create a testing module `test_xxx.py`, where `xxx` is the name of the 
  source function
- The testing module has testing functions corresponding to different test 
  cases. 
- There are as many testing functions as "happy path" and "edge" 
  test cases are documented in the source function docstring  with 
  **return** docstring items. 
- Check code analysis and style of the implementation. 
  - Fix all **PyCharm Problems**.
  - Run **pycodestyle** and **pylint** and fix all styling errors.
- **Version control** these changes to reflect the **testing development 
  step**.

#### II. Devise a plan: Write your design ONE source function at at time.

- Design the solution the source functions, ONE function at a time.
- Write the design in the **DESIGN.md** file.
- **Version control** these changes to reflect the **design development 
  step** for each source function.

After designing a source function, move on to implement it

#### III. Carry out the plan: Implement the functions, ONE at a time

- Implement the source functions, ONE at a time, guided by your design.
- Test, debug, fix, and test again its implementation.
- Check code analysis and style of the implementation. 
  - Fix all **PyCharm Problems**.
  - Run **pycodestyle** and **pylint** and fix all styling errors.
- **Version control** these changes to reflect the **implementation step**.

Repeat steps I, II, and III for each of the **src/linear_efficiency.py** 
source functions:

- `hide(sentence)`
- `reduce_adjacent(num_lst)`
- `reverse(word)`

Note that source function development is ONE function at a time. This means 
that testing, design, and implementation development steps require at 
minimim 3 commits for each source function. 

### Individual work
This assignment is exclusively individual work. If you have any questions, 
please ask me. I'll share my answers with the entire class. 

Think of this assignment as a technical "white-board" interview when you 
have to convince the technical team you are interested in joining that you 
have the problem solving and programming skills they need.

- Do not copy the implementation from the internet or have the implementation 
  generated by online services.
- Do not ask somebody else to write the implementation for you.
- Do not give your implementation to someone else.

### Make your submission

When you are done, synchronize your remote repo with the development in 
your local repo using the following `git` commands in PyCharm `git-bash` or 
`bash` terminal:

- `git remote -v` \<--- shows the remote URL, to ensure that you push to the right remote repo
- `git log`\<--- to see the all your commits
- `git push origin main` \<-- to publish your local repo to GitHub

### Evaluation

- **Documentation** : 10%
- **Testing and implementation** : 20%
- **Design** : 30%
- **Incremental development** : 20%
- **Style** : 20%:
  - Eliminate all **PyCharm Problems** signaled by PyCharm.
  - Run **pycodestyle** and **pylint** to eliminate any styling errors.
- **Bonus:** 10%
  - Develop a **timing** module to time and compare the execution run-time 
    of the source functions.