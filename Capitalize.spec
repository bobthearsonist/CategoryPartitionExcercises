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
  empty.

#[<string of delimiters>]
Delimiters:
  empty. [if s]
  specified.[if s] [property specifiedDelimiters]

#Environment
#File length
File length is:
  Empty. [property empty]
  Not empty.

#File Content
File contains:
  New lines. [if !empty]
  Exclamations. [if !empty]
  Delimiters. [if !empty][if specifiedDelimiters]
  Upper case meeting rules.[if !empty]
  Uppercase not meeting rules.[if !empty]
  All uppercase.[if !empty]
  All lowercase.[if !empty]
  Whitespace.[if !empty]
  No whitespace.[if !empty]
