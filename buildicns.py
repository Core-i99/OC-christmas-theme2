import os
import subprocess

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

for imageFile in os.listdir(exportPngPath):
    # call subprocess to run icnspack
    icnsPackPath = os.path.join(toolsPath, "icnspack")
    icnsFilePath = os.path.join(exportIcnsPath, imageFile.replace(".png", ".icns"))
    pngFilePath = os.path.join(exportPngPath, imageFile)
    subprocess.Popen(['sh', icnsPackPath, icnsFilePath, pngFilePath, pngFilePath])
