# pokesearch
My AP Computer Science Principles project

A python program that displays storage bin images of Pokemon from the Generation III games (I pulled most of the images from [pokeemerald](https://github.com/pret/pokeemerald)). The program works by using full 24 bit RGB ANSI escape codes to display the 32x32 images in the terminal, image data is obtained by using Pillow to read the .png files then each pixel is printed as two spaces with the background color as determined by the current pixel.

## Dependancies

The only dependancy is Pillow, which is easily installed by running

```python
pip install Pillow
```
