'''
Sample script to test ad-hoc scanning by table drive.
This accepts a number with optional decimal part [0-9]+(\.[0-9]+)?

NOTE: suitable for optional matches
'''

def getchar(text,pos):
	""" returns char category at position `pos` of `text`,
	or None if out of bounds """
	
	if pos<0 or pos>=len(text): return None
	
	c = text[pos]
	
	# **Σημείο #3**: Προαιρετικά, προσθέστε τις δικές σας ομαδοποιήσεις
	if c == '0':
		return 'DIGIT == 0'
	if c == '1':
		return 'DIGIT == 1'
	if c == '2':
		return 'DIGIT == 2'
	if c == '3':
		return 'DIGIT == 3'
	if c == '4':
		return 'DIGIT == 4'
	if c == '5':
		return 'DIGIT == 5'
	if c >= '6' and c <= '9':
		return 'DIGIT >= 6 and DIGIT <= 9'
	
	if c == 'G':
		return 'INPUT is G'
	
	if c == 'K':
		return 'INPUT is K'
	if c == 'T':
		return 'INPUT is T'
	
	if c == 'M':
		return 'INPUT is M'
	if c == 'P':
		return 'INPUT is P'
	if c == 'S':
		return 'INPUT is S'

	return c	# anything else
	


def scan(text,transitions,accepts):
	""" scans `text` while transitions exist in
	'transitions'. After that, if in a state belonging to
	`accepts`, it returns the corresponding token, else ERROR_TOKEN.
	"""
	
	# initial state
	pos = 0
	state = 's0'
	# memory for last seen accepting states
	last_token = None
	last_pos = None
	
	
	while True:
		
		c = getchar(text,pos)	# get next char (category)
		
		if state in transitions and c in transitions[state]:
			state = transitions[state][c]	# set new state
			pos += 1	# advance to next char
			
			# remember if current state is accepting
			if state in accepts:
				last_token = accepts[state]
				last_pos = pos
			
		else:	# no transition found

			if last_token is not None:	# if an accepting state already met
				return last_token,last_pos
			
			# else, no accepting state met yet
			return 'ERROR_TOKEN',pos
			
# **Σημείο #1**: Αντικαταστήστε με το δικό σας λεξικό μεταβάσεων
transitions = { 's0': {'DIGIT == 0': 's1', 'DIGIT == 1': 's1', 'DIGIT == 2': 's1', 'DIGIT == 3': 's2'},
				's1': {'DIGIT == 0': 's3', 'DIGIT == 1': 's3', 'DIGIT == 2': 's3', 'DIGIT == 3': 's3', 'DIGIT == 4': 's3', 'DIGIT == 5': 's3', 'DIGIT >= 6 and DIGIT <= 9': 's3'},
				's2': {'DIGIT == 0': 's3', 'DIGIT == 1': 's3', 'DIGIT == 2': 's3', 'DIGIT == 3': 's3', 'DIGIT == 4': 's3', 'DIGIT == 5': 's3'},
				's3': {'DIGIT == 0': 's4'},
				's4': {'DIGIT == 0': 's5', 'DIGIT == 1': 's5', 'DIGIT == 2': 's5', 'DIGIT == 3': 's5', 'DIGIT == 4': 's5', 'DIGIT == 5': 's5', 'DIGIT >= 6 and DIGIT <= 9': 's5'},
				's5': {'DIGIT == 0': 's6', 'DIGIT == 1': 's6', 'DIGIT == 2': 's6', 'DIGIT == 3': 's6', 'DIGIT == 4': 's6', 'DIGIT == 5': 's6', 'DIGIT >= 6 and DIGIT <= 9': 's6'},
				's6': {'INPUT is G': 's7', 'INPUT is K': 's10', 'INPUT is M': 's12'},
				's7': {'DIGIT == 0': 's8', 'DIGIT == 1': 's8', 'DIGIT == 2': 's8', 'DIGIT == 3': 's8', 'DIGIT == 4': 's8', 'DIGIT == 5': 's8', 'DIGIT >= 6 and DIGIT <= 9': 's8'},
				's8': {'DIGIT == 0': 's9', 'DIGIT == 1': 's9', 'DIGIT == 2': 's9', 'DIGIT == 3': 's9', 'DIGIT == 4': 's9', 'DIGIT == 5': 's9', 'DIGIT >= 6 and DIGIT <= 9': 's9'},
				's9': {'INPUT is K': 's10', 'INPUT is M': 's12'},
				's10': {'INPUT is T': 's11'},
				's12': {'INPUT is P': 's13'},
				's13': {'INPUT is S': 's11'}
				} 

# **Σημείο #2**: Αντικαταστήστε με το δικό σας λεξικό καταστάσεων αποδοχής
accepts = {'s11': 'WIND_TOKEN'}


# get a string from input
text = input('give some input>')

# scan text until no more input
while text:		# i.e. len(text)>0
	# get next token and position after last char recognized
	token,pos = scan(text,transitions,accepts)
	if token=='ERROR_TOKEN':
		print('unrecognized input at position',pos,'of',text)
		break
	print("token:",token,"text:",text[:pos])
	# new text for next scan
	text = text[pos:]
	
