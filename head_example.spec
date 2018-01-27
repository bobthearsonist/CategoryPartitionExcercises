#head is a command line program that takes two arguments, a filename, and a number of lines. The program print the number of lines provided form the file to the console. If no number is provided 10 is used.
#head <filename> [numlines]

#filename
Validity of filename:
  Contains invalid characters. [error] [property valid]
  Is a valid filename.

#numlines
Properties of the integer:
  Negative. [error]
  Zero. [property zero]
  int max. [single]
  9.
  10.
  11.

#content
Size of the file contents:
  Less than numlines. [if !zero]
  Greater than numlines.
  Equal to numlines.
