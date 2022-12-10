```sh
mkdir ../piano-midi.de
cd scrapy
python3 -m pip install scrapy==2.7.1
scrapy crawl amt
echo >../../piano-midi.de/COPYRIGHT "\
The MIDI, audio(MP3, OGG) and video files of Bernd Krueger are licensed under the cc-by-sa Germany License (http://creativecommons.org/licenses/by-sa/3.0/de/deed.en). 
This means, that you can use and adapt the files, as long as you attribute to the copyright holder

Name: Bernd Krueger 
Source: http://www.piano-midi.de

The distribution or public playback of the files is only allowed under identical license conditions. 

The scores are open source."
```
