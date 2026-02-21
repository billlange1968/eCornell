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

# Overview of Image Flipping

Image flipping is slightly different than changing colors. In image flipping you need to swap the pixel values between two locations. For example, in a horizontal flip, the top-left pixel becomes the top-right pixel and vice versa. While you could swap each of the red, green, blue, and alpha values individually, there is no problem with swapping the entire RGB objects and leaving the contents of the objects unchanged.  

The function flip is responsible for flipping an image, though it has two different versions depending on whether vertical is True or False. You will approach this function in two steps. First you will implement it assuming vertical is False.  

You will add the code for the True option at the second step.

# Add Horizontal Flipping

Implement the function flip for the case vertical is False. You do not need to add an if-statement yet. You can delay that until the next step. Read the specification for flip for how to implement this function.  

When you are done, you should try it out on the various test images. For example, the command

```
python pictool.py flip images/Goldhill.png Goldhill4.png
```
should perform the following conversion:  

<img width="360" height="288" alt="Goldhill" src="https://github.com/user-attachments/assets/512d7c5c-bbe8-4ce0-9dfe-23706c7e8e33" />
<img width="360" height="288" alt="Goldhill4" src="https://github.com/user-attachments/assets/916c39ec-7dea-4949-94be-1fb709bc5144" />

Important: It is very easy to get this function "off-by-one". That is why we recommend testing it on debug.py first. This image is small enough that you can follow any print statements that you add for debugging.

# Add Vertical Flipping

Extend your implementation of the function flip to include the case vertical is True. Use an if-statement to make sure that you do not break horizontal flipping. Your function should flip horizontally when vertical is False and vertically when it is True. 

To test out vertical flipping, you will need to execute pictool.py with the vertical option, adding --vertical=True to the end of the command line. For example, executing the command  

```
python pictool.py flip images/Goldhill.png Goldhill5.png --vertical=True
```
should perform the following conversion:  


Important: Because you can put anything you want in the vertical option (say --vertical=blue), we recommend that you enforce the precondition for vertical in the function with assert statements.

# Overview of Image Rotation

Rotation is harder than the other two forms of process. That is because rotation changes the dimensions of the image. An image that is 10 pixels by 20 pixels becomes 20 pixels by 10 pixels. The problem is similar to computing the transpose of a matrix that was shown in the module Programming with Nested Lists.  

This is easy if we want to make a copy of an image. We just create an accumulator for the new image and add the pixels one at a time, just like any 2D table. However, all of our functions want us to modify the table argument. The best way to do this is to cheat.  

First, we create a rotated copy using an accumulator variable. Then, we erase all of the rows of the original image using the clear list method. While this will erase all the image contents, the top-level list object is still there. We then append all of the rows of the copy to the old (empty) image, filling it back up. If you think about how these objects are represented in memory, you can see that this will successfully modify the image argument.
To rotate images, you will implement two functions: transpose and rotate. The function transpose will do all the hard work, while rotate will use this function as a helper.

# Add Image Transposition

The function transpose does not have any parameters other than image. Implement this function as specified. It is very similar to the function of the same name shown in the videos for the module Programming with Nested Lists. Download this function from the Canvas page if you need a hint.  

This function will look like it rotates the image, but it’s slightly different. It actually rotates and flips. You should test it out on the less symmetrical images. For example, the command  

```
python pictool.py transpose images/Japan.png Japan2.png
```

should perform the following conversion:  


