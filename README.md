# pokesearch
My AP Computer Science Principles project

A python program that displays storage bin images of Pokemon from the Generation III games (I pulled most of the images from [pokeemerald](https://github.com/pret/pokeemerald)). The program works by using full 24 bit RGB ANSI escape codes to display the images in the terminal, image data is obtained by using Pillow to read the .png files then each pixel is printed as two spaces with the background color as determined by the current pixel.

The main branch is an archive of the code as I had submited it, while the redux branch is for any changes I think to make to it

## Dependencies

The only dependency is Pillow, which is easily installed by running

```python
pip install Pillow
```
