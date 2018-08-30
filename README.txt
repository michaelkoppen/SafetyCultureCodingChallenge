Running Instructions:
	- Right click fridgeSensors.py and open with python.exe.
	or
	- Open fridgeSensors.py with an IDE such as pyCharm and run within it.
	

Testing Instructions:
	- Right click fridgeSensors.py and open with python.exe.
	or
	- Open fridgeSensorsTest.py with an IDE such as pyCharm and run within it.
	- Doing either of these will run three tests proving that the calculateAverages, calculateMedians, and calculateModes functions to produce accurate results.


Assumptions:
	- It was assumed that the fridge temperatures will always be floats or integers and will therefore not need handling for errors such as ValueErrors.
	- It was assumed that the sum method was allowed to be used for this challenge when calculating averages.
	- It was assumed that fridge a's average was correct even though the calculateAverages function returned a value of 3.77 and the challenge displayed a value of 3.78. This was assumed because the calculateAverages function was tested against the imported mean() method and was correct. My result is also only off by 0.01 compared to the challenge's.


Important decisions and trade-offs:
	- Original temperature data was simply stored as a JSON array locally in the program rather than in a seperate file.
	- Printed output JSON array with each element on a new line as this format was shown on the task sheet.
	- Dictionaries were used to store temperatures, averages, medians and modes in order for each set of values to be easily identifiable with their respected fridge's id. This also allows the four dictionaries to be used independently in the future if they are ever needed.
	- When testing the program, mode threw an exception when more than one value was common. I therefore had to manually enter the expected output in the assert for my own calulateMode function.
