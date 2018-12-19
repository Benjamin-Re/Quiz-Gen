# Import Regex module
import re
# Open infile, save content in var
infile = open('.\\questions.txt')
infileContent = infile.readlines()

# Format infileContent
qRegex = re.compile(r'''(
	\d		# Index
	\s+		# Separator
	\		# q
	\s+		# Separator
	\		# a
	\s+		# Separator
	\		# b
	\		# c	
	\s+		# Separator
	\		# d
	\s+		# Separator
	\		# ans
	\s+		# Separator
	\		# id
)''', re.VERBOSE)


# Open outfile, write content in outfile
outfile = open('.\\outfile.txt', 'w')
for lines in infileContent:
	outfile.write(lines)
# Close both files
infile.close()
outfile.close()