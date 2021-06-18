# Python code to convert standard POS form 
# to standard SOP form 

# Function to calculate no. of variables 
# used in POS expression 
def count_no_alphabets(POS): 
	i = 0
	no_var = 0

	# As expression is standard so total no. 
	# of alphabets will be equal 
	# to alphabets before first '.' character 
	while (POS[i]!='.'): 

		# checking if character is alphabet		 
		if (POS[i].isalpha()):	 
			no_var+= 1
		i+= 1
	return no_var 

# Function to calculate the max terms in integers 
def Cal_Max_terms(Max_terms, POS): 
	a = "" 
	i = 0
	while (i<len(POS)): 
		if (POS[i]=='.'): 

			# converting binary to decimal				 
			b = int(a, 2) 

			# insertion of each min term(integer) into the list				 
			Max_terms.append(b) 

			# empty the string		 
			a =""						 
			i+= 1
			
		elif(POS[i].isalpha()): 

			# checking whether variable is complemented or not 
			if(i + 1 != len(POS) and POS[i + 1]=="'"): 

				# concatenating the string with '0' 
				a += '1' 

				# incrementing by 2 because 1 for alphabet and 
				# another for "'"						
				i += 2							
			else: 

				# concatenating the string with '1' 
				a += '0'						
				i += 1
		else: 
			i+= 1

	# insertion of last min term(integer) into the list	 
	Max_terms.append(int(a, 2))		 

# Function to calculate the min terms in binary then 
# calculate SOP form of POS 
def Cal_Min_terms(Max_terms, no_var, start_alphabet): 

	# declaration of the list 
	Min_terms =[] 

	# calculation of total no. of terms that can be 
	# formed by no_var variables				 
	max = 2**no_var				 
	for i in range(0, max): 

		# checking whether the term is not 
		# present in the max terms 
		if (Max_terms.count(i)== 0): 

			# converting integer to binary and then 
			# taking the value from 2nd index as 1st 
			# two index contains '0b' 
			b = bin(i)[2:] 

			# loop used for inserting 0's before the 
			# binary value so that its length will be 
			# equal to no. of variables present in 
			# each product term		 
			while(len(b)!= no_var): 
				b ='0'+b 

			# appending the max terms(integer) in the list 
			Min_terms.append(b)	 

	SOP = "" 

	# loop till there are min terms						 
	for i in Min_terms: 

		# acquire the starting variable came from 
		# main function in every product term			 
		value = start_alphabet 

		# loop till there are 0's or 1's in each min term	 
		for j in i: 

			# checking for complement variable to be used				 
			if (j =='0'): 

				# concatenating value, ' and + in string POS				 
				SOP = SOP + value+"'"

			# checking for uncomplement variable to be used	 
			else: 

				# concatenating value and + in string POS					 
				SOP = SOP + value 

			# increment the alphabet by 1	 
			value = chr(ord(value)+1) 

		# appending the SOP string by '+" after 
		# every product term				 
		SOP = SOP+ "+"

	# for discarding the extra '+' in the last				 
	SOP = SOP[:-1]						 
	return SOP 

# main function 
def main(): 
	
	# input1 
	POS_expr ="(A'+C).(A'+C'+D).(A'+B+C).(B + C'+D').(C+D)"
	Max_terms = [] 
	
	no_var = count_no_alphabets(POS_expr) 
	Cal_Max_terms(Max_terms, POS_expr) 
	SOP_expr = Cal_Min_terms(Max_terms, no_var, POS_expr[1]) 
	
	print("Standard SOP form of " + POS_expr + " ==> " + SOP_expr) 

	# input2 
	POS_expr ="(A + B).(A'+B')"
	Max_terms = [] 
	
	no_var = count_no_alphabets(POS_expr) 
	Cal_Max_terms(Max_terms, POS_expr) 
	SOP_expr = Cal_Min_terms(Max_terms, no_var, POS_expr[1]) 
	
	print ("Standard SOP form of " + POS_expr + " ==> " + SOP_expr) 

# Driver code 
if __name__=="__main__": 
	main() 
