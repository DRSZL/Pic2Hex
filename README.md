# Pic2Hex

Main goal of this small project is to make possible attacking vectors for bitcoin walltes.
(Maybe someone has his private key stored in an image ;) )

This program is designed to take any image as input and convert it into 256-bit hexadecimal values (private-key). 

It works by decoding the image into its constituent pixel information, then processing these data points to generate a corresponding sequence of hexadecimal values. 
This results in a unique 256-bit hex value for each image processed.

There are 3 different scenarios:

1) A given image is rescaled to an 16x16 (ones and zeros - greyscale) image. The pixel information will be stored as an binary number by reading each row
   (e.g. 1001100111001011...1111001001010100 & 0110011000110100...0000110110101011) and its inverted value. These two binary numbers will be then converted to hexadecimal values.

2) The code processes an image file to extract portions of its data, converts these to binary format.
   Within each iteration, the code extracts a slice of the raw data starting from offset and spanning byteOffset bytes. It iterates through the raw data.
   The loop starts at the beginning of data and stops before the end by a specified byteOffset.This slice, stored in hexi1, is then converted to a binary format using the function int8inBinary.

All hexadical-strings (possible private-keys) are writen to a file.
