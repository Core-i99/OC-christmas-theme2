import os
import subprocess

# Locations
export_location = "Export"
export_png_location = "png"
export_png_1x_location = "1x"
export_png_2x_location = "2x"
export_png_orig_location = "pngOrig"
export_icns_location = "icns/Core-i99/Christmas2"
tools_location = "Source/Tools"

# Paths
export_path = os.path.join(os.getcwd(), export_location)
export_png_path = os.path.join(export_path, export_png_location)
export_png_1x_path = os.path.join(export_png_path, export_png_1x_location)
export_png_2x_path = os.path.join(export_png_path, export_png_2x_location)
export_png_orig_path = os.path.join(export_png_path, export_png_orig_location)
export_icns_path = os.path.join(export_path, export_icns_location)
tools_path = os.path.join(os.getcwd(), tools_location)

# Create directories
if not os.path.exists(export_icns_path):
    os.makedirs(export_icns_path)

# Convert PNG to ICNS
for image_file in os.listdir(export_png_1x_path):
    icnspackpath = os.path.join(tools_path, "icnspack.exe")
    icns_file_path = os.path.join(export_icns_path, image_file.replace(".png", ".icns"))
    icns_file_1x_path = os.path.join(export_png_1x_path, image_file)
    icns_file_2x_path = os.path.join(export_png_2x_path, image_file)
    subprocess.call([icnspackpath, icns_file_path, icns_file_1x_path, icns_file_2x_path])