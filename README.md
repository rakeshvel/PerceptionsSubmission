# PerceptionsSubmission

# Methodology

* I first prepped the image by filtering the red color.
  * I converted the image to HSV because it can identify the red in the cones better.
  * Then with a mask and threshold I was able to filter the red color on the screen to only the relevant portion in the cones.
* Along with that, I applied a Gaussian Blue to smooth the image.
* I then made two lines for the cones.
  * This was done by filtering the identified red pixels into two sets, one for the left line and one for the right.
* Finally the image was saved and uploaded.

# What did I try and why I think it didn't work

One of the biggest things I tried but didn't work was clustering. Now, I am not sure if my clustering was broken or whether the rest of my code was broken and causing me issues, but I abandoned that idea and went with a simple left/right of image split while i debugged the rest of my file. But since the basic splitting idea was working, I didn't try to figure out clustering again and kept the rudimentary fix I made. I also tried several other ideas for smoothing and thresholding, such as truncate and triangle, but I found binary produced the best results.

# What libraries are used

* OpenCV for obvious reasons
* NumPy for use as paramater in HSV
