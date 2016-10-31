#!/usr/bin/env python

"""
Python course EBC 2016
Day 4 - Exercise instructions
Lucas Sinclair <lucas.sinclair@me.com>

* Write a program in a file called "exercise_day4.py"
* You have until the start of the next course at 13h00 tomorrow to finish it.
* Once the program is done, upload it in your github repository "python_homework" in a directory named "day4".

The program should read the file named "lulu_mix_16.csv". This file should be placed in your "home" directory. Your program should use the OS environment variable "$HOME" to find the file.
This file is a comma separated values format. It contains information about different music tracks.

For each line in the file (excluding the header) the program should produce a new "Song" instance. It should place all the Song instances created in a list called "songs".

### Each Song object should have these attributes:

* title
we2
* artist
The artist of the song as a string.

* duration
The title of the song as an integer in seconds.

When creating new Song instances:

-> If the duration of a song is not a number, set it to 0, but issue a warning.
-> If the duration of a song is negative, raise an Exception and stop the program.

### Each Song object should have these methods:

* pretty_duration(self)
Returns a nice string describing the duration. For instance if the duration is 3611, this methods takes no input and returns "01 hours 00 minutes 11 seconds" as a string.

* play(self)
Automatically opens a webpage on your computer with a youtube search for the title.

Once your program is ready the following four lines of code should run without errors. (After you have removed the negative duration song!).
"""
#importing the os
import os
import sys
import warnings
import webbrowser
#set path

in_path = "lulu_mix_16.csv"

# Check that the pass is valid 

if not os.path.exists(in_path):
	raise exception ("No file at '%s'." % in_path)
#####################

class Song(object):
	def __init__(self, title, artist, duration):
		self.title = title
		self.artist = artist
		self.duration = duration
		try:
			self.duration = int(duration)
		except ValueError:	
			warnings.warn("warning, duration is not a number") 
			self.duration = 0
		if self.duration < 0:
			raise Exception ("Negative duration")

	def pretty_duration(self):
		secs = self.duration
		mins = secs/60
		hours = mins/60
		return "%02i hours %02i minutes %02i seconds" % (hours, mins, secs)

	def play(self):
		webbrowser.open("https://www.youtube.com/results?search_query=" + self.title



fh = open(in_path, "r")
fl = fh.next()
songs = [Song(*line.stip('\n').split(',')) for line in fh]

songs = []

for line in handle:
    try : s = Song(*line.strip('\n').split(','))
    except ValueError: pass
    songs.appen(s)

	print line
	# create a song using the line info
	# put this song in a list
	testsong = Song(line.split(",")[0],line.split(",")[1],line.split(",")[2])
	songs.append(testsong)







for s in songs: print s.artist
for s in songs: print s.pretty_duration()
print sum(s.duration for s in songs), "seconds in total"
songs[6].play()