from photoshop import Session
import os

photoshopTemplateName = "C:/Users/Stijn Rombouts/Documents/GitHub/OC-christmas-theme2/Source/psd/Template.psd"
photoshopTemplatePath = os.path.join(os.getcwd(), photoshopTemplateName)
print(photoshopTemplatePath)
sourcePath = "C:/Users/Stijn Rombouts/Documents/GitHub/OC-christmas-theme2/Source/png"
print(sourcePath)
pictureFileNames = ['AppleRecv.png', 'AppleTM.png', 'BigSur.png', 'Catalina.png',  'ExtAppleRecv.png', 'ExtAppleTM.png', 'ExtHardDrive.png', 'HardDrive.png', 'HighSierra.png', 'Mojave.png', 'Monterey.png', 'ResetNVRAM.png','Shell.png', 'Tool.png', 'Ventura.png', 'Windows10.png', 'Windows11.png']
snowPile1FileNames = ["HighSierra.png", "Mojave.png", "Catalina.png", "BigSur.png", "Monterey.png", "Ventura.png", "AppleRecv.png", "ExtAppleRecv.png"]
snowPile2FileNames = ["Shell.png", "Tool.png"]
snowPile3FileNames = ["ExtAppleTM.png", "ExtHardDrive.png", "HardDrive.png", "AppleTM.png"]
snowPile4FileNames = ["ResetNVRAM.png"]
snowPile5FileNames = ["Windows10.png", "Windows11.png"]
with Session(photoshopTemplatePath, action="open") as ps:
    for pictureFileName in pictureFileNames:
        currentPicturePath = os.path.join(sourcePath, pictureFileName)
        print(currentPicturePath)
        # Reszie to 256x256
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
   
        # save png file
        ps.app.activeDocument.saveAs(f"C:/Users/Stijn Rombouts/Documents/GitHub/OC-chrismas-theme2/Export/{pictureFileName}", ps.PNGSaveOptions())

ps.app.activeDocument.close(ps.SaveOptions.DoNotSaveChanges)
