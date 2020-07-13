# Convert Numbers In Text To Words By Language

## Assumptions
0. The definition of a string of a valid number is given in base.py
1. File size should not exceed available memory allowed by OS
2. The supported number does not exceed 999,999,999,999
3. At the moment only English is supported

## Design and Implementation
1. #### Scope(Boundary) of the problem
    - The input is a string of text. The text can be in any natural language. The source of intput can be read from memory, file, netowrk, etc.
    - The output is a string of numbers in words. The words can be in any natural language.
    - A valid number can be int, float, scientific notion, etc. In this version, int is supported.
    - Given target language English, the output is made up of a finite set of number words. Therefore a full enumeration
    of building words should be provided
    
2. #### Test Setup(BDD cycle)
    the test should start from passing simple common testcases. for instance 0, 1, 10, in order to make sure the project 
    can always pass the test while deleveoping further on.
    In summary, the testsuite should include
    - string of invalid numbers
    - string of unique-spelling numbers
    - string of non-unique-spelling numbers
    - string of mixed of words and numbers
    - string of text of any forms
    
3. #### Top-down approach
    At the beginning of prototyping, I started from identifying objects and defining high level interfaces. In this problem,
    A generic converter, which handles text parsing and number formatting, and a language specific converter, which handles 
    parsing of unique number string to this language have been identified. By doing so, the project is scalable horizontally
    at adding more language specific converters while vertically scallable at handling IO, formatting, more number types.
    
4. #### Core algorithm
    ```
    Given a valid number
        if type is int
            parse int by 3 digits groups
        if type is float
            parse int by 3 digits groups
            parse decimals
            concat
        if scientific
            pasrse scientific
    ```
    Given the first iteration, the implementation of integer parsing is delivered. More number types can
    be added in the following versions.

5. #### Future work
    - add network based reader to io utils, add writer to files
    - add more language specific converters
    - add converting function for floats, and scientific notations
    - extend the max number to be supported

## Instructions to Run
#### Project
1. Install this package by running bin/install.sh
2. On commmand line, you can run n2w by using below example commands.

```
$ n2w -t 'abc 123'
one hundred and twenty-three
$ n2w -f 'test/test_input.txt'
eleven
twenty-one
```

#### Test Suites
Navigate to project root and run pytest
```
$pytest
=================================== test session starts ====================================
platform darwin -- Python 3.5.0, pytest-5.4.3, py-1.9.0, pluggy-0.13.1
rootdir: /Users/justin/PycharmProjects/n2w
collected 10 items                                                                         

test/test_num2word.py ..........                                                     [100%]

==================================== 10 passed in 0.06s ====================================
```
