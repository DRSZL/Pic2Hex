import argparse
import imageHelper

byteOffset = int(256/8)

def byteArrayToHex(byteArr):
    hex_representation = ''.join([f'{int("".join(map(str, byte)), 2):02x}' for byte in byteArr])
    
    return hex_representation
    
def hexRepresentationFromNumpyArray(numArray):
    arr = numArray.flatten()
    bytes_array = [arr[i:i+8] for i in range(0, len(arr), 8)]
        
    return byteArrayToHex(bytes_array)

def int8inBinary(binary):
    return ''.join(f'{element:02x}' for element in binary)


parser = argparse.ArgumentParser(description="simple parser for image folder path")
parser.add_argument('folder_path', type=str, help='image folder path')
args = parser.parse_args()

folder_path = args.folder_path


image_paths = imageHelper.find_images(folder_path)


for image_path in image_paths:

    image_name = image_path.split('\\')[-1]
    print(image_name)

    textFileName = f"{'image2hex_'}{image_name}.txt"

    with open(textFileName, 'w') as f:

        # load raw data and create hex for each 256 bit a hex (forwards and backwards)
        try:
            data = imageHelper.getRawImageData(image_path)
        except IOError:
            print("Error: File does not exist or cannot be read.")
            return
        
        for offset in range(len(data) - byteOffset):
            hexi1 = data[offset:offset + byteOffset]
            hexStr1 = int8inBinary(hexi1)
            f.write(hexStr1 + '\n')
            hexi2 = hexStr1[::-1]
            f.write(hexi2 + '\n')
            
        
        # scaling down to 16x16 and create hex
        numpy_array = imageHelper.image_to_binaryNumpy(image_path)
        numpy_array_inverted = imageHelper.invertBinaryArray(numpy_array)

        hex1 = hexRepresentationFromNumpyArray(numpy_array)
        hex2 = hexRepresentationFromNumpyArray(numpy_array_inverted)
        f.write(hex1 + '\n')
        f.write(hex2 + '\n')
