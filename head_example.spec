#head is a command line program that takes two arguments, a filename, and a number of lines. The program print the number of lines provided form the file to the console. If no number is provided 10 is used.
#head <filename> [numlines]

#filename
Validity of filename:
  Contains invalid characters.
  Is a valid filename.

#numlines
Properties of the integer:
  Negative. [error]
  Zero. [single]
  Non-Zero. [property nonzero]
  int max. [single]
  10. [single]

#content
Size of the file contents:
  Less than numlines. [if nonzero]
  Greater than numlines. [if nonzero]
  Equal to numlines. [if nonzero]
