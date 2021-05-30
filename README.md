# Genshin Impact Autoplay Music
A game auxiliary script that allows you to autoplay music in Genshin Impact via a game prop called Windsong Lyre. Aim for fun XD.

![Screenshot](https://github.com/FancleX/Genshin-Impact-Autoplay/blob/main/Images/WindsongLyre.png)

***
## Features
* The script has been converted to executable file that is friendly to use.
* The program is compatible with different music, as long as the music file is in the requested format.
* Settings are able to be adjusted by users. Such as key delay.
* Not required IDE and enviroment.
***
## Requirements
* Genshin Impact
* Prop: "Windsong Lyre" which you can get from a pasted activity. If you have, it should be under Gadge. See the below picture.

![Screenshot](https://github.com/FancleX/Genshin-Impact-Autoplay/blob/main/Images/Location.png)

***
## Introduction
### Principle
* Simulates keyboard presses (library: PyAutoGUI) by recognizing musical scores.
### Format of musical score
![Screenshot](https://github.com/FancleX/Genshin-Impact-Autoplay/blob/main/Images/Score_c.png)

* The musical score consists of three elements, letter, parentheses, and space. These three charge for different functions. The program will ask you to change these settings at the beginning to gain a better performance of a play.

![Screenshot](https://github.com/FancleX/Genshin-Impact-Autoplay/blob/main/Images/Explaination.PNG)

***
## Getting Started
1. Click "Code" button to download a zip file.
2. After upzipping, go to src folder and find "Genshin Impact Autoplay.exe" file. Please ensure if songs and the exe file are at the same path, you can directly input the file's name to start. Otherwise, you will see a '...' button by the side, which is used to import file from your local documents.

![Screenshot](Example\Explain1.png)

3. Run "Genshin Impact", once you enter the game, equip with the prop and back to the main interface.
4. Press key "Z" to start Windsong Lyre and back to your Desktop. 
5. Right click the Genshin Impact Autoply.exe file, left click "Run as adminstrator". Wait for few seconds, you will get the UI displayed.
6. Here provides with two musics. One is Canon, and the other one is Opening of Lie in April. For example, type "Canon.txt" to the entry bar and choose how to start it. If you want run with default setting then click the left button. Please ensure name input valid, otherwise you will receieve a error notification.

	![Screenshot](Example\subwindow.png)
	![Screenshot](Example\error.png)

7. The defalt setting is apt and suitable to play Canon, if you expect to play others, please press the right side button to change the settings. Optimized settings for Lie in April OP are shown below, which is still not good. But you should create a better one.

	![Screenshot](Example\setting.png)

8. At the last, you are free to press Run to start. Once seeing the status indication starting to print countdown, you have three seconds to go back to Genshin Impact and move your hands away from your keyboard. Then, the autoplay starts.

***
## Snippets show
Canon:

[![](https://res.cloudinary.com/marcomontalbano/image/upload/v1621880532/video_to_markdown/images/youtube--pgvWKjzbRHw-c05b58ac6eb4c4700831b2b3070cd403.jpg)](https://youtu.be/pgvWKjzbRHw "")

OP of Lie in April:

[![](https://res.cloudinary.com/marcomontalbano/image/upload/v1621880818/video_to_markdown/images/youtube--5GQwYB2WExo-c05b58ac6eb4c4700831b2b3070cd403.jpg)](https://youtu.be/5GQwYB2WExo "")
***
## Disclaimer
* The program just uses for fun will not engage in any commercial purpose and offensive way. 
* Do not use any musical score has copyright.
***
## Known Issues
* The game prop has a limited range of only three octaves, so some tones can't be produced.
* The real music plays faster and slower depending on the chapter, and the program can only simulate resting notes between keystrokes. It can only be used to a certain extent to change the tempo or speed of playing.
***
## Reference
Musical score sources:
* http://www.5you.com/news/466818-2.html
* https://www.ququyou.com/yuanshen/113590.html
