# OC Christmas Theme 2
A Christmas theme for OpenCore

<img src="Preview/Preview1.png">
<img src="Preview/Preview2.png">

## Requirements
- OpenCore 0.7.0 or newer
- Opencanopy added to OpenCore
## Installation
- Change PickerAttributes to 144 in config.plist
    ```
    <key>PickerAttributes</key>
    <integer>144</integer>
    ```
- Download the latest release and extract it
- Copy the extracted folder to `EFI/OC/Resources/Image`
- Enable the theme in config.plist
    ```
    <key>PickerMode</key>
    <string>External</string>
    <key>PickerVariant</key>
    <string>Core-i99\Christmas2</string>
    ```

## Notes
Clover already has a christmas theme for over a year, but OpenCore doesn't have one. So I decided to make one. I used the background image from CloverHackyColor's christmas theme and the Reset NVRAM icon from blackosx's OpenCanopyIcons. I based my icons from the Acidanthera GoldenGate icons from Acidanthera's OcBinaryData.
This was the first time I used Photoshop, so it might not be perfect.

## Credits
- [CloverHackyColor](https://github.com/CloverHackyColor) for the [background image](https://github.com/CloverHackyColor/CloverThemes/blob/master/christmas/background.png)
- [Blackosx](https://github.com/blackosx) for [Reset NVRAM icon](https://github.com/blackosx/OpenCanopyIcons/blob/master/Set1/Tool/ResetNVRAM.icns)
- [Acidanthera](https://github.com/acidanthera) for [Acidanthera GoldenGate icons](https://github.com/acidanthera/OcBinaryData/tree/master/Resources/Image/Acidanthera/GoldenGate)