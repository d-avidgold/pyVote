# pyVote

I've always been fascinated by voting systems across the world, and I've recently been reading up on the mathematical properties that they can, do, and should have. As a result, I've begun work on this project, which allows for quick computation of a variety of social choice functions through python. 

This Readme file contains two specifications: one for the command line utility of the program, and another for the files it can take as input (.vot files). As of right now, the parser is not very forgiving, so I recommend reading each part carefully to avoid error messages. 

# How to Use this Program

The general argument for the program is of the form here:

> python main.py [file.vot flags*]*

Where file.vot can be any VOT file, and flags are of three flavors:

1. Single-Vote Systems
    1. No arguments: -maj, -min, -plur
    1. One argument: -dict Dictator, -mon Monarch, -quot Quota
1. Ranked-Vote Systems
    1. TODO
1. Approval Voting Systems
    1. TODO
    
# How to write, edit, and naviage .vot files

VOT files are inspired by the Across Lite puzzle files. They contain information on the title of the vote, the type (one of the three above), comments on the ballots, and then voter and candidate information. 

The most vital part of the file is below the <BALLOTS> header. In any of the three systems above, each line of the ballots area is given by a set of (comma-separated) voters, a colon, and then the preference that group shares. It is not necessary to bundle voters together, but it can make the files much much shorter, and is recommended. However, no voter can cast two ballots, and no write-ins are allowed, with either of these resulting in an error. See example2.vot for an example of single-vote systems.

# Contact info:

Please contact me if there are any questions, recommendations, comments, or general feedback.

Email: david (dot) gold (at) yale (dot) edu

# References 

