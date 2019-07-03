# selfie-smash

This game exists in the following remote repository: https://github.com/richiebubbs/selfie-smash

To begin, fork the repository and then clone or download the repository to your computer's desktop.  You can navigate to the app from the command line as follows:

```sh
cd ~/Desktop/selfie-smash
```
Note: all further instructions assume you are running this app from the repository's root directory...

# Requirements

* Anaconda 3.7

* Python 3.7

* Pip


# Set-Up

This game makes use of the pygame package.  You will need to create a virtual environment and then activate the virtual environment through the command line, as follows:

```sh
conda create -n game-env python=3.7 #first time only
conda activate game-env
```

From the command line install the required package:

```sh
pip install pygame
```

To run the game from the command line:

```sh
python selfie-smash
```

Please note, the game already has an image you can use to play, but it is more fun if you use your own image.  To do so, take your favorite selfie and save it in the root directory of the repository.  You must call the image "selfie" and it must be in jpg format.  (Future Scope: I would like to find a way to have the user simply save it to the desktop and it could be in any format, but I wasn't able to get there this time around.)

# Playing the Game

The game play is very simple.  When you run the app you will get an intro screen in the pygame window that displays the title and has a button for "Play" and a button for "Quit" click the button for "Play" (Hopefully this works, sometimes it took me multiple clicks, but I am still working on debugging that.)

You will see the image of the selfie in the bottom of the game display (note: my selfie came out sideways, so I wrote a line of code to rotate it.  However, when my wife tried with her own selfie, it did not need to be rotated, so hopefully this isn't an issue.)

Move the image to the left and right with the left and right arrow keys.  Try to avoid getting hit by the obstacles which will fall from the top of the game display.  Be careful, the more obstacles you dodge, the faster they will go and the larger they become!

Keep going until you get smashed.  When you do you will see a message saying "You got Smashed!" and a prompt to play again or quit.

# Attributions
I am new to coding games, so I received a *lot* of help from the internet with this, mostly from this really great site: <br>
[Python Game Development Tutorial](https://pythonprogramming.net/game-development-tutorials/) <br> and this screencast: 
[Screencast](https://youtu.be/P-UuVITG7Vg?list=PLQVvvaa0QuDdLkP8MrOXLe_rKuf6r80KO)

and also from the following websites:

[pygame](https://www.pygame.org/)

[Loading Images in Pygame](https://stackoverflow.com/questions/20160477/loading-images-in-pygame)

[Transforming Images in pygame](https://www.pygame.org/docs/ref/transform.html)

[Fonts in pygame](https://stackoverflow.com/questions/38001898/what-fonts-can-i-use-with-pygame-font-font)

[Help from Professor Rosetti!! (thanks!!)](https://github.com/s2t2/a-ppb-python-game)

