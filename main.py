import pyperclip
import re

# creating a regex for phone numbers and e-mail patterns
# phone regex
phone_regex = re.compile(r'''
(
((\d\d\d)|(\(\d\d\d))?      # area code, which is optional
(\s|-)                      # first separator
\d\d\d                      # first 3 digits
-                           # second separator
\d\d\d\d                    # last 4 digits
(((ext(\.)?\s)|x)           # extension word-part, which is optional
 (\d{2,5}))?                # extension number-part, which is also optional
)
''', re.VERBOSE)


# e-mail regex
email_regex = re.compile(r'''
[a-zA-Z0-9_.+]+             # name part of the e-mail address
@                           # @ symbol
[a-zA-Z0-9_.+]+             # domain name part
''', re.VERBOSE)

# getting the text of the clipboard
text = pyperclip.paste()

extracted_phone = phone_regex.findall(text)
extracted_email = email_regex.findall(text)

# creating a new list with only the complete phone numbers, discarding sub-groups created by the regex
all_phone_numbers = []
for phone_number in extracted_phone:
    all_phone_numbers.append(phone_number[0])


# saving the extracted phone numbers and e-mails in a variable and formatting my output
results = '\n'.join(all_phone_numbers) + '\n\n\n' + '\n'.join(extracted_email)

# transfering the results to the copy function (CTRL + C) to be pasted anywhere you want.
pyperclip.copy(results)


# If you want to just test this software, you can remove the comment on the line below and see the output that was transfered to your clipboard.
# print(results)