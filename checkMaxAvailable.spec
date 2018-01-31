#CheckMaxAv verifies the maximum spendable amount on a credit card.
#The output is :
#   the maximum amount of money that can be sent using the card
#   a message stating the card is inactive
#
#Different card types have different limits.

Environment:
#value available
amount available:
  negative.
  positive.
  0.

Parameters:
#name: a string with length in (0,256]
name value:
  contains whitespace. [single]
  null. [error]

name length:
  0.    [single]
  256.  [single]
  257.  [single]
  random value (0,256].

#cardNum: a sequence of 16 digits
cardNum is valid (card exists):
  yes.
  no. [error]

cardNum value:
  all 0s. [single]
  max. [single]
  random.

cardNum length:
  16 digits.
  < 16 digits. [error]
  > 16 digits. [error]

#IDcode: a sequence of max 3 digits
IDCode is valid (matches card):
  yes.
  no. [error]

IDCode value:
  000. [single]
  max. [single]
  random 3 digits.

IDCode length:
  4 digits. [error]
  < 3 digits. [error]
  3 digits.

#date: mm/yyyy
date:
  less than today. [single]
  greater than today. [single]
  greater than expiration date. [error]
  less than expiration date.

#cardType: Visa, Mastercard, Visa Electron, American express
cardType:
  Visa.
  Mastercard.
  Visa Electron.
  American express.
