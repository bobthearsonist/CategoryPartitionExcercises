#Capitalize OPT <filename>

#Parameters
#Filename
Validity of filename:
  Valid.
  Invalid. [error]

#OPT -l,-e,-s,-x
Parameters:
  l.      [property l]
  e.      [property e]
  s.      [property s]
  x.      [property x]
  empty.  [property empty]

#[<string of delimiters>]
Delimiters:
  empty. [if s]
  specified.[if s] [property specifiedDelimiters]

#Environment
#File Content
File contains:
  Empty.
  New lines.
  Exclamations.
  Delimiters. [if specifiedDelimiters]
  Upper case meeting rules.
  Uppercase not meeting rules.
  All uppercase.
  All lowercase.
  Whitespace.
  No whitespace.
