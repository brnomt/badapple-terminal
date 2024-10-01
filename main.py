from ascii_magic import AsciiArt
import os
import pathlib
import time


directory = pathlib.Path(__file__).parent.resolve()

frames_dir = directory / 'frames' / 'png'
output_dir = directory / 'frames'

for i in os.listdir(frames_dir):
    # Verificar si el archivo es una imagen PNG
    if i.endswith('.png'):
        # Crear la ruta completa del archivo
        image_path = frames_dir / i
        output_file = output_dir / f"{i[:-4]}.txt"

    time.sleep(0.0119)
    my_art = AsciiArt.from_image(str(image_path))
    my_art.to_terminal(columns=70, monochrome=True)

    my_art.to_file(
        path=str(output_file),
        columns=70,
        monochrome=True
    )