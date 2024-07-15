# YTMusic_Overlay
Edge_Extension and Python code for displaying currently playing music on top of fullscreen applications

How to setup:
1. Navigate to edge://extensions/ and select Load Unpacked (Or you can directly install the extension from the dist folder .crx file)
2. select the folder named Edge_Extension that includes the background.js, content.js and manifest.js files
3. Open or refresh music.youtube.com to start transmitting song information to localserver port 5000
4. Either run overlay.exe from the dist folder or compile and run the script yourself using python in src/overlay.py
5. You will see your song update on the top left of your screen as you play music in ytmusic
6. You will need to close it from your task manager if you ran the executable.
