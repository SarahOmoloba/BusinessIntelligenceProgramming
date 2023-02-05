# Regular Expressions
import re
#8.18a
pattern = r'([a-z]+.){3,}[\s.,-_][a-z]+[\s.,-_][a-z]+[\s.,-_][a-z]+[\s.,-_][a-z]+'

sentence = 'mika,is.the cutest-dog'

'Match' if re.fullmatch(pattern,sentence) else 'Not a Match'

#test for length
'Match' if re.fullmatch(pattern,'mika,is.the cutest-dog') else 'Not a Match'# pass for five
'Match' if re.fullmatch(pattern,'mika,is.the cutest-dog_right') else 'Not a Match'# pass for more than five
'Match' if re.fullmatch(pattern,'mika,is.the cutest') else 'Not a Match'# fail for less than five

#test for signs
'Match' if re.fullmatch(pattern,'mika,is.the cutest-dog_right') else 'Not a Match'# pass for signs in the pattern
'Match' if re.fullmatch(pattern,'mika,is.the cutest!dog ngl') else 'Not a Match'# fail for signs not in the pattern

#8.18b

'''Valid tests'''#to see if the expression accepts those that it should

'Valid' if re.fullmatch(r'(?=.*?[A-Z])(?=.*?[a-z])(?=.*?[0-9])(?=.*?[#?!@$%<^>&*-]).{7,}', 'Pa$sw0rd') else 'Invalid' # pass
#Test to see if the password obeyed all parameters
'Valid' if re.fullmatch(r'(?=.*?[A-Z])(?=.*?[a-z])(?=.*?[0-9])(?=.*?[#?!@$%<^>&*-]).{7,}', 'Pa$sw0rd2') else 'Invalid' # pass
#Test to see if the regular expression accepts more than 8 characters
'Valid' if re.fullmatch(r'(?=.*?[A-Z])(?=.*?[a-z])(?=.*?[0-9])(?=.*?[#?!@$%<^>&*-]).{7,}', 'pa$sw0rD') else 'Invalid' # pass
#Test to see if the regular expression accepts the uppercase letter in a different position
'Valid' if re.fullmatch(r'(?=.*?[A-Z])(?=.*?[a-z])(?=.*?[0-9])(?=.*?[#?!@$%<^>&*-]).{7,}', 'Pa$(sw0rd') else 'Invalid'# pass
#Test to see if the regular expression accepts other signs not specified
'Valid' if re.fullmatch(r'(?=.*?[A-Z])(?=.*?[a-z])(?=.*?[0-9])(?=.*?[#?!@$%^&<^>-]).{7,}', 'Pa$sw0 rd') else 'Invalid'# pass
#Test to see if the regular expression accepts white space

'''Invalid tests'''#to see if the expression rejects those that it should

'Valid' if re.fullmatch(r'(?=.*?[A-Z])(?=.*?[a-z])(?=.*?[0-9])(?=.*?[#?!@$%<^>&*-]).{7,}', 'pa$sw0rd') else 'Invalid'#pass
#Test to see if the regular expression accepts input without uppercase letter
'Valid' if re.fullmatch(r'(?=.*?[A-Z])(?=.*?[a-z])(?=.*?[0-9])(?=.*?[#?!@$%<^>&*-]).{7,}', 'Passw0rd') else 'Invalid'#pass
#Test to see if the regular expression accepts input without special character
'Valid' if re.fullmatch(r'(?=.*?[A-Z])(?=.*?[a-z])(?=.*?[0-9])(?=.*?[#?!@$%<^>&*-]).{7,}', 'Pa$w0rd') else 'Invalid'#pass
#Test to see if the regular expression accepts input less than 8 characters
'Valid' if re.fullmatch(r'(?=.*?[A-Z])(?=.*?[a-z])(?=.*?[0-9])(?=.*?[#?!@$%<^>&*-]).{7,}', 'Pa$sword') else 'Invalid'#pass
#Test to see if the regular expression accepts input without digits
'Valid' if re.fullmatch(r'(?=.*?[A-Z])(?=.*?[a-z])(?=.*?[0-9])(?=.*?[#?!@$%^&<^>-]).{7,}', 'PA$SW0RD') else 'Invalid'#pass
#Test to see if the regular expression accepts input without lowercase letter



