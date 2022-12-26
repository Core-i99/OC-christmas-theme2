from photoshop import Session
import os
import shutil
import subprocess

photoshopTemplateLocation = "Source/psd"
photoshopTemplateName = "Template.psd"
photoshopTemplatePath = os.path.join(os.getcwd(), photoshopTemplateLocation, photoshopTemplateName)
photoshopTemplateAppleName = "Apple.psd"
photoshopTemplateApplePath = os.path.join(os.getcwd(), photoshopTemplateLocation, photoshopTemplateAppleName)
photoshopTemplateBackgroundName = "Background.psd"
photoshopTemplateBackgroundPath = os.path.join(os.getcwd(), photoshopTemplateLocation, photoshopTemplateBackgroundName)
sourceLocation = "Source/png"
sourcePath = os.path.join(os.getcwd(), sourceLocation)
exportLocation = "Export"
exportPngLocation = "png"
exportIcnsLocation = "icns"
exportPath = os.path.join(os.getcwd(), exportLocation)
exportPngPath = os.path.join(exportPath, exportPngLocation)
exportIcnsPath = os.path.join(exportPath, exportIcnsLocation)
pngOrigLocation = "Source/pngOrig"
pngOrigPath = os.path.join(os.getcwd(), pngOrigLocation)
toolsLocation = "Source/Tools"
toolsPath = os.path.join(os.getcwd(), toolsLocation)
pictureFileNames = ['AppleRecv.png', 'AppleTM.png', 'Apple11.png', 'Apple10_15.png',  'ExtAppleRecv.png', 'ExtAppleTM.png', 'ExtHardDrive.png', 'HardDrive.png', 'Apple10_13.png', 'Apple10_14.png', 'Apple12.png', 'ResetNVRAM.png','Shell.png', 'Tool.png', 'Apple13.png', 'Windows.png', 'Windows10.png', 'Windows11.png']
snowPile1FileNames = ["Apple10_13.png", "Apple10_14.png", "Apple10_15.png", "Apple11.png", "Apple12.png", "Apple13.png", "AppleRecv.png", "ExtAppleRecv.png"]
snowPile2FileNames = ["Shell.png", "Tool.png"]
snowPile3FileNames = ["ExtAppleTM.png", "ExtHardDrive.png", "HardDrive.png", "AppleTM.png"]
snowPile4FileNames = ["ResetNVRAM.png"]
snowPile5FileNames = ["Windows.png", "Windows10.png", "Windows11.png"]

# Create export folder
if os.path.exists(exportPath):
    shutil.rmtree(exportPath)
os.mkdir(exportPath)
os.mkdir(exportPngPath)
os.mkdir(exportIcnsPath)

# Save Template.psd with different images as PNG
with Session(photoshopTemplatePath, action="open") as ps:
    for pictureFileName in pictureFileNames:
        currentPicturePath = os.path.join(sourcePath, pictureFileName)
        # Resize to 256x256
        ps.app.activeDocument.resizeImage(256, 256)
        # Replace image on layer Picture
        ps.app.activeDocument.activeLayer = ps.app.activeDocument.layers.getByName("Picture")
        replace_contents = ps.app.stringIDToTypeID("placedLayerReplaceContents")
        desc = ps.ActionDescriptor
        idnull = ps.app.charIDToTypeID("null")
        desc.putPath(idnull, currentPicturePath)
        ps.app.executeAction(replace_contents, desc)
        # Set visibility of layers
        SnowPile1Layer = ps.app.activeDocument.layers.getByName("Snowpile1")
        SnowPile2Layer = ps.app.activeDocument.layers.getByName("Snowpile2")
        SnowPile3Layer = ps.app.activeDocument.layers.getByName("Snowpile3")
        SnowPile4Layer = ps.app.activeDocument.layers.getByName("Snowpile4")
        SnowPile5Layer = ps.app.activeDocument.layers.getByName("Snowpile5")
        if pictureFileName in snowPile1FileNames:
            SnowPile1Layer.visible = True
            SnowPile2Layer.visible = False
            SnowPile3Layer.visible = False
            SnowPile4Layer.visible = False
            SnowPile5Layer.visible = False
        elif pictureFileName in snowPile2FileNames:
            SnowPile1Layer.visible = False
            SnowPile2Layer.visible = True
            SnowPile3Layer.visible = False
            SnowPile4Layer.visible = False
            SnowPile5Layer.visible = False
        elif pictureFileName in snowPile3FileNames:
            SnowPile1Layer.visible = False
            SnowPile2Layer.visible = False
            SnowPile3Layer.visible = True
            SnowPile4Layer.visible = False
            SnowPile5Layer.visible = False
        elif pictureFileName in snowPile4FileNames:
            SnowPile1Layer.visible = False
            SnowPile2Layer.visible = False
            SnowPile3Layer.visible = False
            SnowPile4Layer.visible = True
            SnowPile5Layer.visible = False
        elif pictureFileName in snowPile5FileNames:
            SnowPile1Layer.visible = False
            SnowPile2Layer.visible = False
            SnowPile3Layer.visible = False
            SnowPile4Layer.visible = False
            SnowPile5Layer.visible = True
        else:
            SnowPile1Layer.visible = False
            SnowPile2Layer.visible = False
            SnowPile3Layer.visible = False
            SnowPile4Layer.visible = False
            SnowPile5Layer.visible = False

        # Save as PNG
        ps.app.activeDocument.saveAs(os.path.join(exportPngPath, pictureFileName), ps.PNGSaveOptions())

    # Close document
    ps.app.activeDocument.close(ps.SaveOptions.DoNotSaveChanges)

# Save Apple.psd as Apple.png
with Session(photoshopTemplateApplePath, action="open") as ps:
    # resize to 256x256
    ps.app.activeDocument.resizeImage(256, 256)

    # Save as PNG
    ps.app.activeDocument.saveAs(os.path.join(exportPngPath, "Apple.png"), ps.PNGSaveOptions())

    # Close document
    ps.app.activeDocument.close(ps.SaveOptions.DoNotSaveChanges)

# Save Background.psd as Background.png
with Session(photoshopTemplateBackgroundPath, action="open") as ps:
    # resize to 3840x2160
    ps.app.activeDocument.resizeImage(3840, 2160)

    # Save as PNG
    ps.app.activeDocument.saveAs(os.path.join(exportPngPath, "Background.png"), ps.PNGSaveOptions())

    # Close document
    ps.app.activeDocument.close(ps.SaveOptions.DoNotSaveChanges)

# Copy all images from pngOrig folder to export path
for imageFile in os.listdir(pngOrigPath):
    shutil.copy(os.path.join(pngOrigPath, imageFile), exportPngPath)

# Convert PNG to ICNS
for imageFile in os.listdir(exportPngPath):
    # call subprocess to run icnspack.exe
    icnsPackPath = os.path.join(toolsPath, "icnspack.exe")
    icnsFilePath = os.path.join(exportIcnsPath, imageFile.replace(".png", ".icns"))
    pngFilePath = os.path.join(exportPngPath, imageFile)
    subprocess.call([icnsPackPath, icnsFilePath, pngFilePath, pngFilePath])