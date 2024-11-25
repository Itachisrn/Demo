from rembg import remove 
from PIL import Image
import io

input_path = 'F:/Mine.jpg'
output_path = 'F:/Mi.png'

input = Image.open(input_path)
output = remove(input)
output.save(output_path)
Image = Image.open('F:/Mi.png')
Image.show()