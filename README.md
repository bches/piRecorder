# Welcome to piRecorder!

piRecorder makes use of the PiTFT screen on the Raspberry Pi
to play and record audit through ALSA.

USAGE: ./record -d \<directory\> -f \<filename\>

Records to \<directory\>/\<filename.wav\>

If no \<directory\> is given, default is: .\/recordings

If no \<filename\> is given, default is: test

Recording can be paused/resumed by pressing space or enter

Buttons on the side of the PiTFT screen have the following mapping:
<ol>
	<li>Button 1: PLAY</li>
	<li>Button 2: RECORD</li>
	<li>Button 3: STOP</li>
	<li>Button 4: EXIT</li>
 </ol>
