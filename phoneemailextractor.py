#! python3
# phoneemailextractor.py

# class ideas
# text grabber
# finder
# result producer

import re, pyperclip
# import time


# phone finder
class Phone_Regex:
	"""Contains a method of the regular expression pattern match to execute to
	find phone numbers."""

	def phone_regex_method(self):
		"""
		Creates a function of the regular expression pattern match to execute to
		find phone numbers.
		:return: phone_regex
		"""
		phone_regex = re.compile(r'''(
		(\d{3}|\(\d{3}\))?     	       # area code
		(\s|-|\.)?			   	       # separator
		(\d{3}	)			   	       # first 3 digits
		(\s|-|\.)			   	       # separator
		(\d{4})				   	       # last 4 digits
		(\s*(ext|x|ext.)\s*\d{1,5})?   # extension
		)''', re.VERBOSE)

		return phone_regex

class Email_Regex:
	"""
	Creates a function of the regular expression pattern match to execute to
	find emails.
	:return: email_regex
	"""
	def email_regex_method(self):
		email_regex = re.compile(r'''(
		[a-zA-Z0-9._%+-]+              # username
		@                              # @ symbol
		[a-zA-Z0-9.-]+                 # domain name
		(\.[a-zA-Z]{2,4})              # dot something
		)''', re.VERBOSE)

		return email_regex

class Text_Grabber:
	"""Takes text from clipboard and assigns it to variable 'text'."""

	def from_clipboard(self):
		text = str(pyperclip.paste())

		return text

	# def from_file(self, text_file):
	# 	with open(text_file) as fo:
	# 		regex_str = fo.read()


# find matches
class Finder:
	"""Applies phone and email regex's to find phone numbers and emails
	within the copied text or from the provided text file (text file incompl)."""

	def finder_method(self, phone_regex, email_regex, text):

		matches = []
		for groups in phone_regex.findall(text):
			phone_num = '-'.join([groups[1], groups[3], groups[5]])
			if len(groups) >= 6:
				phone_num += groups[6]
			matches.append(phone_num)
		for groups in email_regex.findall(text):
			matches.append(groups[0])

		return matches


class Producer:
	"""Output the found phone numbers and emails to clipboard, to terminal,
	and/or to text file (text file incompl.)"""

	def check_for_matches(self, matches):
		"""If matches exist, then call one or both copy functions."""
		if matches:
			return matches
		else:
			print('No phone numbers or email addresses found.')

	def copy_print_matches(self, verified_matches):
		joined_matches = '\n'.join(verified_matches)
		pyperclip.copy(joined_matches)
		print('Found phone numbers/emails! Copied to clipboard.')
		return print(joined_matches)

	# def copy_save_matches(self, matches):
	# 	filename = "matches_" + time.strftime("%m%d-%H%M%S") + ".txt"
	#
	# 	joined_matches = '\n'.join(matches)
	# 	pyperclip.copy(joined_matches)
	#
	# 	f = open(filename, "w+")
	# 	f.write(pyperclip.paste())
	# 	f.close()
	#
	# 	return print(f"Matches saved to {filename}")

# get text
# send text to phone and email regex
# find matches
# produce matches
if __name__ == '__main__':
	new_grabber = Text_Grabber()
	text = new_grabber.from_clipboard()

	new_phone_re = Phone_Regex()
	phone_regex = new_phone_re.phone_regex_method()

	new_email_re = Email_Regex()
	email_regex = new_email_re.email_regex_method()

	new_finder = Finder()
	matches = new_finder.finder_method(phone_regex, email_regex, text)

	new_producer = Producer()
	verified_matches = new_producer.check_for_matches(matches)
	if verified_matches is not None:
		new_producer.copy_print_matches(verified_matches)