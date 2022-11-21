from PIL import Image
import pillow_heif
from os import walk

def heic_function(path, file_array, output_path):

    for i in range (len(file_array)):
        heif_file = pillow_heif.read_heif(path+"/"+file_array[i])
        #heif_file = pillow_heif.read_heif("../Sample/IMG_7788.HEIC")
        image = Image.frombytes(
            heif_file.mode,
            heif_file.size,
            heif_file.data,
            "raw",

        )

        image.save (output_path+"/"+file_array[i][0:-5]+".png", format("png"))



path = "./Pasta_heic"
output_path = "./Pasta_arquivos_convertidos"

path = path.replace("\\", "/")
output_path = output_path.replace("\\", "/")

filenames = next(walk(path+"/"), (None, None, []))[2]  # [] if no file

heic_function(path, filenames, output_path)

f = open("Acabou.txt", "w")