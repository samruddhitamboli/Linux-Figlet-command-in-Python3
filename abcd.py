
x=input("Enter string").upper()
s=list(x)
for j in range(1,8):
	for t in s:
		print(' ',end='' )
		if t=='A':
			if(j==1):
				print('   *   ',end='')
			elif(j==2):
				print('  * *  ',end='')
			elif(j==3):
				print(' *   * ',end='')
			elif(j==4 or j==6 or j==7):
				print('*     *',end='')
			elif(j==5):
				print('*******',end='')
			else:
				print('*     *',end='')
		elif t=='B':
			if(j==1 or j==7 or j==4):
				print('****** ',end='')
			else:
				print('*     *',end='')
		elif t=='C':
			if(j==1 or j==7):
				print(' ***** ',end='')
			elif(j==2 or j==6):
				print('*     *',end='')
			else:
				print('*      ',end='')
		elif t=='D':
			if(j==1 or j==7):
				print('****** ',end='')
			else:
				print('*     *',end='')
		elif t=='E':
			if(j==1 or j==7):
				print('*******',end='')
			elif(j==4):
				print('*****  ',end='')
			else:
				print('*      ',end='')
		elif t=='F':
			if(j==1):
				print('*******',end='')
			elif(j==4):
				print('****** ',end='')
			else:
				print("*      ",end='')
		elif t=='G':
			if(j==1 or j==7):
				print('*******',end='')
			elif(j==2 or j==6):
				print('*     *',end='')
			elif(j==3):
				print('*      ',end='')
			elif(j==4):
				print('*  ****',end='')
			else:
				print('*  *  *',end='')
		elif t=='H':
			if(j==1 or j==2 or j==3 or j==5 or j==6 or j==7):
				print('*     *',end='')
			else:
				print('*******',end='')
		elif t=='I':
			if(j==1 or j==7):
				print('*******',end='')
			else:
				print('   *   ',end='')
		elif t=='J':
			if(j==1):
				print('*******',end='')
			elif(j==2 or j==3 or j==4):
				print('   *   ',end='')
			elif(j==5 or j==6):
				print('*  *   ',end='')
			else:
				print(' ***   ',end='')
		elif t=='K':
			if(j==1 or j==7):
				print('*     *',end='')
			elif(j==2 or j==6):
				print('*   *  ',end='')
			elif(j==3 or j==5):
				print('* *    ',end='')
			else:
				print('*      ',end='')
		elif t=='L':
			if(j==1 or j==2 or j==3 or j==4 or j==5 or j==6):
				print('*      ',end='')
			else:
				print('*******',end='')
		elif t=='M':
			if(j==1):
				print(' *   * ',end='')
			elif(j==2):
				print('* * * *',end='')
			elif(j==3):
				print('*  *  *',end='')
			else:
				print('*     *',end='')
		elif t=='N':
			if j==1 or j==7:
				print('*     *',end='')
			elif j==2:
				print('**    *',end='')
			elif j==3:
				print('* *   *',end='')
			elif j==4:
				print('*  *  *',end='')
			elif j==5:
				print('*   * *',end='')
			else:
				print('*    **',end='')
		elif t=='O':
			if j==1 or j==7:
				print(' ***** ',end='')
			else:
				print('*     *',end='')
		elif t=='P':
			if j==1 or j==4:
				print('*******',end='')
			elif j==2 or j==3:
				print('*     *',end='')
			else:
				print('*      ',end='')
		elif t=='Q':
			if j==1:
				print('  ***  ',end='')
			elif j==2 or j==3:
				print('*     *',end='')
			elif j==4:
				print('*  *  *',end='')
			elif j==5:
				print('*   * *',end='')
			elif j==6:
				print('*    **',end='')
			else:
				print(' **** *',end='')
		elif t=='R':
			if j==1 or j==4:
				print('*******',end='')
			elif j==2 or j==3:
				print('*     *',end='')
			elif j==5:
				print('**     ',end='')
			elif j==6:
				print('*  *   ',end='')
			else:
				print('*     *',end='')
		elif t=='S':
			if j==1 or j==7 or j==4:
				print(' ***** ',end='')
			elif j==2 or j==6:
				print('*     *',end='')
			elif j==3:
				print('*      ',end='')
			else:
				print('      *',end='')
		elif t=='T':
			if j==1:
				print('*******',end='')
			else:
				print('   *   ',end='')
		elif t=='U':
			if j==7:
				print(' ***** ',end='')
			else:
				print('*     *',end='')
		elif t=='V':
			if j==1 or j==2 or j==3 or j==4:
				print('*     *',end='')
			elif j==5:
				print(' *   * ',end='')
			elif j==6:
				print('  * *  ',end='')
			else:
				print('   *   ',end='')
		elif t=='W':
			if(j==7):
				print(' *   * ',end='')
			elif(j==6):
				print('* * * *',end='')
			elif(j==5):
				print('*  *  *',end='')
			else:
				print('*     *',end='')
		elif t=='X':
			if j==1 or j==7:
				print('*     *',end='')
			elif j==2 or j==6:
				print(' *   * ',end='')
			elif j==3 or j==5:
				print('  * *  ',end='')
			else:
				print('   *   ',end='')
		elif t=='Y':
			if j==1:
				print('*     *',end='')
			elif j==2:
				print(' *   * ',end='')
			elif j==3:
				print('  * *  ',end='')
			else:
				print('   *   ',end='')
		elif t=='Z':
			if j==1 or j==7:
				print('*******',end='')
			elif j==2:
				print('     * ',end='')
			elif j==3:
				print('    *  ',end='')
			elif j==4:
				print('   *   ',end='')
			elif j==5:
				print('  *    ',end='')
			else:
				print(' *    ',end='')	
		else:
			print('',end='')
	print('')
	
			
