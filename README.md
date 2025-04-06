# Simple-Spacewar-Game
Hello, thanks a lot for checking out this repository. It would be a great pleasure for me if someone reviews the code and suggest some beneficial improvements. PLease feel free to do any necessary modifications to make the game more efficient and enjoyable. 

## Overview:
This is a simple prototype of the classic Spacewar game which was created in the 1960s. Even though this one is a bit different, it is based on the same idea. In theory, there should be a rocket which the player can control. There are invaders moving in random directions. The player gets a point for shooting each of the invaders. While doing so, the player also has avoid collision with any of those invaders as well as the outer boundary.

## Game Controls:
1)  Left Arrow Key: To rotate anticlockwise
2)  Right Arrow Key: To rotate clockwise
3)  Upward Arrow Key: To move forward
4)  Spacebar key: To shoot

## Libraries and Tools used:
This entire game has been built using python programming language. 
The libraries used are:
1) pygame
2) random
3) math
4) sys

The pygame library is the main component of the game. It provides the features and tools necessary to build a game. The lines of code are significantly reduced used the methods provided by the library. Math library is imported to perform some trigonometric calculations which are involved in the direction of rocket and invaders. Sys library is used to smoothly terminate the game once it is over. Random library is imported to generate the random numbers so as to randomize the initial positions of the invaders. 

## Problems I faced during the programming of this game:
There were a lots and lots of problems and errors I faced during writing the code. The following are some of them:
1) Firstly, I faced some doubts while developing a mathematical logic for rotating the rocket. Fortunately enough, I managed to develop that even though it is not at all perfect and efficient.
2) Secondly, I faced some problems working with images. The problem was that the image quality deteriorated after rotating. That's why I had to draw the inbuilt pygame shapes instead.
3) Also the, collision function of the rocket not perfectly executed. Sometimes it terminates the game even when the rocket has not really collided with the invaders or the boundaries. While many of the times, the collision was not detected even when the rocket seemingly collided with them.


## Conclusion:
The main objective of building this game is to test my own programming skills. Currently I am a student who is still learning how to code. Any kind of suggestions and feedbacks would be highly appreciable.
