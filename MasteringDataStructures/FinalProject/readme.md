# Overview of Color Removal
Monochromatic colors are colors where the red, green, and blue values are all the same. One popular example of monochromatic colors is grayscale. To convert an image into grayscale, you read the red, green, and blue values and compute the brightness
```
brightness = 0.3 * red + 0.6 * green + 0.1 * blue
```
You then reassign the red, green, and blue attributes to this single value. Note that you leave the alpha value unchanged. Converting an image to grayscale does not affect its transparency.  

The function mono is responsible for converting an image to monochrome, though it has two different versions depending on whether sepia is True or False. You will approach this function in two steps. First you will implement it assuming sepia is False.  

You will add the code for the True option at the second step.  

This function is fairly straightforward as you do not need to add or remove pixels from the image; you just change attributes. Therefore, it is a good warm-up for the rest of the project.  

# Add Grayscale Conversion

Implement the function mono for the case sepia is False. You do not need to add an if-statement yet. You can delay that until the next step. Read the specification for mono for how to implement this function.  

When you are done, you should try it out on the various test images. For example, the command  

```
python pictool.py mono images/Goldhill.png Goldhill2.png
```
should perform the following conversion:  

<img width="360" height="288" alt="Goldhill" src="https://github.com/user-attachments/assets/c6911a07-ad7e-4a36-9ec6-5e8ffc66ceb6" />

<img width="360" height="288" alt="Goldhill2" src="https://github.com/user-attachments/assets/b714caf5-b029-4fee-93fc-2c9d7fe22ed4" />

# Add Sepia Conversion

Sepia was a process used to increase the longevity of photographic prints. To simulate a sepia-toned photograph, you darken the green value to int(0.6 * brightness) and blue value to int(0.4 * brightness), producing a reddish-brown tone. Extend your implementation of mono to include the case when sepia is True. Use an if-statement to make sure that you do not break grayscale conversion. Your function should produce normal grayscale when sepia is False and sepia tone when it is True.
To test out sepia tone, you will need to execute pictool.py with the sepia option, adding --sepia=True to the end of the command line. For example, executing the command

```
python pictool.py mono images/Goldhill.png Goldhill3.png --sepia=True
```

Important: Because you can put anything you want in the sepia option (say --sepia=blue), we recommend that you enforce the precondition for sepia in the function with assert statements.

