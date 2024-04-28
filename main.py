from memory_profiler import profile

@profile
def process_strs(reps=10**6):
	str1 = 'python'*reps
	str2 = 'programmer'*reps
	str3 = str1 + str2
	del str2
	return str3

process_strs(reps=10**7)
