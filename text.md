https://github.com/idealo/image-super-resolution
[SRGAN implementation](https://github.com/eriklindernoren/PyTorch-GAN#super-resolution-gan)
https://blog.paperspace.com/image-super-resolution/

# Introduction to the problem 

Idea map LR images to HR images 

Single image Super-Resolution (SISR) aims to generate a visually pleasing high-resolution (HR) image from its degraded
low-resolution (LR) measurement

1) This problem is ill-formulated (multiple HR images could be mapped to same LR image)

A lot of SR algorithms were proposed. Including: 

[Interpolation based](https://ieeexplore.ieee.org/document/1658087)
Eg. Bicubic interpolation (extension of spline interpolation to two-dimensional grid)
[Reconstruction based](https://ieeexplore.ieee.org/document/6241428)
And learning based

# Why we skip over Interpolation methods

1) They are boring and not interesting to implement
2) They perform worse than learning based methods
3) We already implemented them 

# Why we skip over Reconstruction based methods 

1) They are pretty much learning methods

# So what about learning based methods 

We can use any ml method to interpolate image

First paper dates at 2014: [Image super-resolution using deep convolution networks]()
