# Vba-Chr-Converter

A Python tool that converts strings into VBA Chr() sequences, useful for obfuscation or embedding text in VBA macros. Includes a decoder to revert Chr() sequences back to plain text.

## Example:

_String to be convert:_
This is a test string for VBA Chr() conversion

_Encoded VBA Chr() sequence:_
Chr(84) & Chr(104) & Chr(105) & Chr(115) & Chr(32) & Chr(105) & Chr(115) & Chr(32) & Chr(97) & Chr(32) & Chr(116) & Chr(101) & Chr(115) & Chr(116) & Chr(32) & Chr(115) & Chr(116) & Chr(114) & Chr(105) & Chr(110) & Chr(103) & Chr(32) & Chr(102) & \_
Chr(111) & Chr(114) & Chr(32) & Chr(86) & Chr(66) & Chr(65) & Chr(32) & Chr(67) & Chr(104) & Chr(114) & Chr(40) & Chr(41) & Chr(32) & Chr(99) & Chr(111) & Chr(110) & Chr(118) & Chr(101) & Chr(114) & Chr(115) & Chr(105) & Chr(111) & Chr(110)
