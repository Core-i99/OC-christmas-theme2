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

# call subprocess to run icnspack
icnsPackPath = os.path.join(toolsPath, "icnspack")
icnsFilePath = os.path.join(exportIcnsPath, "Apple.icns")
pngFilePath = os.path.join(exportPngPath, "Apple.png")
print("icnsPackPath: " + icnsPackPath)
print("icnsFilePath: " + icnsFilePath)
print("pngFilePath: " + pngFilePath)
# subprocess on single line
command = f"{icnsPackPath} {icnsFilePath} {pngFilePath} {pngFilePath}"
print("command: " + command)
subprocess.call(command, shell=True)