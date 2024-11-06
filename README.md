# McVersionManager
A program for managing multiple versions of Minecraft Bedrock Edition.

Minecraft Bedrock Edition currently lacks a built-in way to install multiple versions for some reason, despite being added to the Minecraft Launcher not long ago, so I created a program for that myself.

# Disclaimer
McVersionManager was neither created by nor endorsed by Mojang Studios or Microsoft. It was created by BrightSky OSSDO.

McVersionManager also does not help you pirate Minecraft. You must have Minecraft Bedrock Edition (any version) already installed on your computer for it to work.

# Why would anyone want to downgrade Minecraft Bedrock Edition?
For the exact same reasons why they would want to downgrade Minecraft Java Edition. Maybe there's a removed feature that they want to use. Maybe there's a server that doesn't support modern versions. Maybe they prefer how the textures and villages looked before 2019. Maybe they miss the emptiness of oceans before the Aquatic Update. Maybe there's a game-breaking bug in the current version and the only way to avoid it is downgrading. Or maybe they lived the best part of their life during a certain Minecraft version, and they want to relive those good times.

I personally enjoy playing old Minecraft maps from 2014-2017. Something that sets the majority of adventure maps from that era apart from maps of the modern day is that they often used signs for storytelling rather than chat messages. With the introduction of double-sided signs in version 1.20 of Minecraft, I've noticed that all signs in old adventure maps are completely blank. And version 1.18 changed terrain generation and world height, so many of these maps also have corrupted terrain. These two factors make old adventure maps practically unplayable in the latest Minecraft version. But with McVersionManager, you can downgrade to the version in which the map was created, and play it exactly the way it was intended.

# The reason why I created McVersionManager
People have already created several tools for downgrading Minecraft Bedrock Edition, some of which I've used before, but they all have a few flaws. Examples include the Seed Picker being completely blank, and the Minecraft Marketplace not loading properly. These two things are literally the biggest incentives for me to play older versions of Minecraft Bedrock Edition, so it's a shame that they don't work. In fact, my favorite part of old Minecraft was the cool seeds that the Seed Picker provided before the world generation update. My favorites were Cliffside Village, Snow Day, and Stronghold Village.

But in McVersionManager, you can use both the Marketplace and the Seed Picker in older Minecraft versions.

Another flaw in many of these tools is the fact that they only let you downgrade to no earlier than version 0.14. But they taunt you by showing nonfunctional download buttons for 0.13. And anything below 0.13, there isn't even a button to download. But McVersionManager has all the Minecraft Bedrock Edition releases, both new and old. The only versions it currently lacks are the preview versions, but these will likely be added in the future.

# How to use McVersionManager
When you open McVersionManager, there will be 3 tabs: Versions, Imported, and Installed. The Versions tab contains a table of all Minecraft versions that you have **not** installed. There will be a download button next to each version which, when clicked, will download and install that version. It does this by fetching the desired version's package file from Microsoft's servers. If the desired version is not available on Microsoft's servers (like if it's a REALLY old version that predates Microsoft's acquisition of Minecraft), McVersionManager will fetch the desired version from archive.org. The package will then be installed and launchable by going to the Installed tab.

In the Options menu, you can specify whether or not to delete package files after installing to save disk space. By default, this is enabled.

If you want to install a Minecraft version that isn't listed in McVersionManager, you'll need to import your own package file. Click the File menu, and select "Import package". This will open a dialog where you can browse to a Windows app package (`.appx` or `.msix`), an Android app package (`.apk` or `.xapk`), or an iOS AppStore package (`.ipa`). After finding your package file in the dialog, you can click Open, and McVersionManager should immediately start installing the package. If the package is not a valid Minecraft version, you'll see an error message. However, if it is valid, it will install and appear in the Installed tab. It will also appear in the Imported tab.

You can uninstall all Minecraft versions by selecting "Uninstall all versions" in the Options menu. Be very careful with this, as all your worlds will get deleted in the process.

# Build Instructions
You can build McVersionManager using PyInstaller:

1. Download this repository to your computer.
2. Install PyQt5 using this command: `pip install PyQt5`
3. Open Windows Command Prompt and navigate to the root of the repository.
4. Create the executable by running this command: `pyinstaller --onefile --windowed source\McVersionManager.py`
5. It should create and place `McVersionManager.exe` in the `dist` folder. I honestly don't know why it's called "dist", I guess the developers of PyInstaller are just weird.

Alternatively, you can download a premade executable from the Releases page.

# License
McVersionManager is released under the MIT license.
