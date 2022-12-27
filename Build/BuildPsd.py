from photoshop import Session
import os
import shutil
from PIL import Image

photoshop_template_location = "Source/psd"
photoshop_template_name = "Template.psd"
photoshop_template_path = os.path.join(os.getcwd(), photoshop_template_location, photoshop_template_name)
photoshop_template_apple_name = "Apple.psd"
photoshop_template_apple_path = os.path.join(os.getcwd(), photoshop_template_location, photoshop_template_apple_name)
photoshop_template_background_name = "Background.psd"
photoshop_template_background_path = os.path.join(os.getcwd(), photoshop_template_location, photoshop_template_background_name)
source_location = "Source/png"
source_path = os.path.join(os.getcwd(), source_location)
export_location = "Export"
export_png_location = "png"
export_png_1x_location = "1x"
export_png_2x_location = "2x"
export_png_orig_location = "pngOrig"
export_path = os.path.join(os.getcwd(), export_location)
export_png_path = os.path.join(export_path, export_png_location)
export_png_1x_path = os.path.join(export_png_path, export_png_1x_location)
export_png_2x_path = os.path.join(export_png_path, export_png_2x_location)
export_png_orig_path = os.path.join(export_png_path, export_png_orig_location)
png_orig_location = "Source/pngOrig"
png_orig_path = os.path.join(os.getcwd(), png_orig_location)
picture_file_names = ['AppleRecv.png', 'AppleTM.png', 'Apple11.png', 'Apple10_15.png',  'ExtAppleRecv.png', 'ExtAppleTM.png', 'ExtHardDrive.png',\
'HardDrive.png', 'Apple10_13.png', 'Apple10_14.png', 'Apple12.png', 'ResetNVRAM.png','Shell.png', 'Tool.png', 'Apple13.png', 'Windows.png', \
'Windows10.png', 'Windows11.png']

# Create export folder
if os.path.exists(export_path):
    shutil.rmtree(export_path)
os.mkdir(export_path)
os.mkdir(export_png_path)
os.mkdir(export_png_orig_path)
os.mkdir(export_png_1x_path)
os.mkdir(export_png_2x_path)

# Save Template.psd with different images as PNG
with Session(photoshop_template_path, action="open") as ps:
    for picture_file_name in picture_file_names:
        current_picture_path = os.path.join(source_path, picture_file_name)
        # Replace image on layer Picture
        ps.app.activeDocument.activeLayer = ps.app.activeDocument.layers.getByName("Picture")
        replace_contents = ps.app.stringIDToTypeID("placedLayerReplaceContents")
        desc = ps.ActionDescriptor
        idnull = ps.app.charIDToTypeID("null")
        desc.putPath(idnull, current_picture_path)
        ps.app.executeAction(replace_contents, desc)

        # Resize to 256x256
        ps.app.activeDocument.resizeImage(256, 256)
        # Save as PNG 256x256
        ps.app.activeDocument.saveAs(os.path.join(export_png_2x_path, picture_file_name), ps.PNGSaveOptions())

        # Resize to 128x128
        ps.app.activeDocument.resizeImage(128, 128)
        # Save as PNG 128x128
        ps.app.activeDocument.saveAs(os.path.join(export_png_1x_path, picture_file_name), ps.PNGSaveOptions())

    # Close document
    ps.app.activeDocument.close(ps.SaveOptions.DoNotSaveChanges)

# Save Apple.psd as Apple.png
with Session(photoshop_template_apple_path, action="open") as ps:
    # resize to 256x256
    ps.app.activeDocument.resizeImage(256, 256)
    # Save as PNG 256x256
    ps.app.activeDocument.saveAs(os.path.join(export_png_2x_path, "Apple.png"), ps.PNGSaveOptions())

    # resize to 128x128
    ps.app.activeDocument.resizeImage(128, 128)
    # Save as PNG 128x128
    ps.app.activeDocument.saveAs(os.path.join(export_png_1x_path, "Apple.png"), ps.PNGSaveOptions())

    # Close document
    ps.app.activeDocument.close(ps.SaveOptions.DoNotSaveChanges)

# Save Background.psd as Background.png
with Session(photoshop_template_background_path, action="open") as ps:
    ps.app.activeDocument.saveAs(os.path.join(export_png_1x_path, "Background.png"), ps.PNGSaveOptions())
    ps.app.activeDocument.saveAs(os.path.join(export_png_2x_path, "Background.png"), ps.PNGSaveOptions())

    # Close document
    ps.app.activeDocument.close(ps.SaveOptions.DoNotSaveChanges)

# Copy all images from pngOrig folder to export path
for image_file in os.listdir(png_orig_path):
    shutil.copy(os.path.join(png_orig_path, image_file), export_png_orig_path)

# Export pngOrig images to 1x and 2x
for image_file in os.listdir(export_png_orig_path):
    # print only the files
    current_file_path = os.path.join(export_png_orig_path, image_file)
    current_file_path1x = os.path.join(export_png_1x_path, image_file)
    current_file_path2x = os.path.join(export_png_2x_path, image_file)
    if os.path.isfile(current_file_path):
        # Save 1x image: resize image to half size
        im = Image.open(current_file_path)
        width, height = im.size
        width = int(width / 2)
        height = int(height / 2)
        im_resize = im.resize((width, height), Image.Resampling.LANCZOS)
        im_resize.save(current_file_path1x, 'PNG')

        # Save 2x image: copy image from PngDir to PngDir2x
        shutil.copy(current_file_path, current_file_path2x)
