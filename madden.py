import pandas as pd 
from division import teams
#Create a program that display Madden data according to next options
#1. Overall Rating, number of players that the user want to display.
#2. By team, ordered acording with age or weigth or position or 

madden = pd.read_csv("madden21.csv", index_col='Full Name')

print('----------------------------------\n')
print('1. Display players by Overall Rating')
print('2. Display the players by team\n')

option = int(input('Option:\t'))

while option > 3 or option < 1:
	print('Option not available')
	option = int(input('Option:\t'))
	break
else:
	if option == 1:
		players = int(input('How many players you want to display:\t'))
		data = madden[['Overall Rating','Position',' Total Salary ','Age']]

		print('\n\n\n')
		print(data.iloc[0:players].sort_values('Overall Rating', ascending= False))
	else:
		#teams 
		AFC_nrth = ['Bengals','Browns','Ravens','Steelers']
		AFC_sth = ['Colts','Jaguars','Texans','Titans']
		AFC_st = ['Bills','Dolphins','Jets','Patriots']
		AFC_wst = ['Broncos','Chargers','Chiefs','Raiders']

		NFC_nrth = ['Bears','Lions','Packers','Vikings']
		NFC_sth = ['Bucaneers','Falcons','Saints','Panthers']
		NFC_st = ['Cowboys','Eagles','Giants','Redskins']
		NFC_wst = ['Cardinals','Rams','Seahwaks','49ers']
		
		print('Conference')
		print('1.AFC')
		print('2.NFC')

		conference = int(input('Conference:\t'))
		print('\n')

		if conference == 1:
			print('1. AFC north')
			print('2. AFC south')
			print('3. AFC west')
			print('4. AFC east')
			division = int(input('Division:\t'))
			print('\n')

			if division == 1:#The user inputs the Division 
				teams(AFC_nrth)
				team = int(input('Team:\t'))

				if team == 1:#Acording to the input we find the team on the list of teams
					team = AFC_nrth[0] 
					data = madden[['Position','Overall Rating','Age','Years Pro','Height','Weight']]
					x = data.loc[madden['Team'] == team]
					print(x.iloc[0:51].sort_values('Overall Rating', ascending= False))


				elif team == 2:
					team = AFC_nrth[1]
					data = madden[['Position','Overall Rating','Age','Years Pro','Height','Weight']]
					x = data.loc[madden['Team'] == team]
					print(x.iloc[0:51].sort_values('Overall Rating', ascending= False))

				elif team == 3:
					team = AFC_nrth[2]
					data = madden[['Position','Overall Rating','Age','Years Pro','Height','Weight']]
					x = data.loc[madden['Team'] == team]
					print(x.iloc[0:51].sort_values('Overall Rating', ascending= False))


				else:
					teams = AFC_nrth[3]
					data = madden[['Position','Overall Rating','Age','Years Pro','Height','Weight']]
					x = data.loc[madden['Team'] == team]
					print(x.iloc[0:51].sort_values('Overall Rating', ascending= False))


			elif division == 2:
				teams(AFC_sth)
				team = int(input('Team:\t'))

				if team == 1:
					team = AFC_sth[0]
					data = madden[['Position','Overall Rating','Age','Years Pro','Height','Weight']]
					x = data.loc[madden['Team'] == team]
					print(x.iloc[0:51].sort_values('Overall Rating', ascending= False))


				elif team == 2:
					team = AFC_sth[1]
					data = madden[['Position','Overall Rating','Age','Years Pro','Height','Weight']]
					x = data.loc[madden['Team'] == team]
					print(x.iloc[0:51].sort_values('Overall Rating', ascending= False))

				elif team == 3:
					team = AFC_sth[2]
					data = madden[['Position','Overall Rating','Age','Years Pro','Height','Weight']]
					x = data.loc[madden['Team'] == team]
					print(x.iloc[0:51].sort_values('Overall Rating', ascending= False))

				else:
					team = AFC_sth[3]
					data = madden[['Position','Overall Rating','Age','Years Pro','Height','Weight']]
					x = data.loc[madden['Team'] == team]
					print(x.iloc[0:51].sort_values('Overall Rating', ascending= False))


			elif division == 3:
				teams(AFC_wst)
				team = int(input('Team:\t'))

				if team == 1:
					team = AFC_wst[0]
					data = madden[['Position','Overall Rating','Age','Years Pro','Height','Weight']]
					x = data.loc[madden['Team'] == team]
					print(x.iloc[0:51].sort_values('Overall Rating', ascending= False))


				elif team == 2:
					team = AFC_wst[1]
					data = madden[['Position','Overall Rating','Age','Years Pro','Height','Weight']]
					x = data.loc[madden['Team'] == team]
					print(x.iloc[0:51].sort_values('Overall Rating', ascending= False))


				elif team == 3:
					team = AFC_wst[2]
					data = madden[['Position','Overall Rating','Age','Years Pro','Height','Weight']]
					x = data.loc[madden['Team'] == team]
					print(x.iloc[0:51].sort_values('Overall Rating', ascending= False))


				else:
					team = AFC_wst[3]
					data = madden[['Position','Overall Rating','Age','Years Pro','Height','Weight']]
					x = data.loc[madden['Team'] == team]
					print(x.iloc[0:51].sort_values('Overall Rating', ascending= False))


			else:
				teams(AFC_st)
				team = int(input('Team:\t'))

				if team == 1:
					team = AFC_st[0]
					data = madden[['Position','Overall Rating','Age','Years Pro','Height','Weight']]
					x = data.loc[madden['Team'] == team]
					print(x.iloc[0:51].sort_values('Overall Rating', ascending= False))

				elif team == 2:
					team = AFC_st[1]
					data = madden[['Position','Overall Rating','Age','Years Pro','Height','Weight']]
					x = data.loc[madden['Team'] == team]
					print(x.iloc[0:51].sort_values('Overall Rating', ascending= False))


				elif team == 3:
					team = AFC_st[2]
					data = madden[['Full Name','Position','Overall Rating','Age','Years Pro','Height','Weight']]
					x = data.loc[madden['Team'] == team]
					print(x.iloc[0:51].sort_values('Overall Rating', ascending= False))


				else:
					team = AFC_st[3]
					data = madden[['Position','Overall Rating','Age','Years Pro','Height','Weight']]
					x = data.loc[madden['Team'] == team]
					print(x.iloc[0:51].sort_values('Overall Rating', ascending= False))


		else:
			print('1. NFC north')
			print('2. NFC south')
			print('3. NFC west')
			print('4. NFC east')
			division = int(input('Division:\t'))
			print('\n')

			if division == 1:
				teams(NFC_nrth)
				team = int(input('Team:\t'))

				if team == 1:
					team = NFC_nrth[0]
					data = madden[['Position','Overall Rating','Age','Years Pro','Height','Weight']]
					x = data.loc[madden['Team'] == team]
					print(x.iloc[0:51].sort_values('Overall Rating', ascending= False))

					
				elif team == 2:
					team = NFC_nrth[1]
					data = madden[['Position','Overall Rating','Age','Years Pro','Height','Weight']]
					x = data.loc[madden['Team'] == team]
					print(x.iloc[0:51].sort_values('Overall Rating', ascending= False))


				elif team == 3:
					team = NFC_nrth[2]
					data = madden[['Position','Overall Rating','Age','Years Pro','Height','Weight']]
					x = data.loc[madden['Team'] == team]
					print(x.iloc[0:51].sort_values('Overall Rating', ascending= False))


				else:
					team = NFC_nrth[3]
					data = madden[['Position','Overall Rating','Age','Years Pro','Height','Weight']]
					x = data.loc[madden['Team'] == team]
					print(x.iloc[0:51].sort_values('Overall Rating', ascending= False))


			elif division == 2:
				teams(NFC_sth)
				team = int(input('Team:\t'))

				if team == 1:
					team = NFC_sth[0]
					data = madden[['Position','Overall Rating','Age','Years Pro','Height','Weight']]
					x = data.loc[madden['Team'] == team]
					print(x.iloc[0:51].sort_values('Overall Rating', ascending= False))

				elif team == 2:
					team = NFC_sth[1]
					data = madden[['Position','Overall Rating','Age','Years Pro','Height','Weight']]
					x = data.loc[madden['Team'] == team]
					print(x.iloc[0:51].sort_values('Overall Rating', ascending= False))


				elif team == 3:
					team = NFC_sth[2]
					data = madden[['Position','Overall Rating','Age','Years Pro','Height','Weight']]
					x = data.loc[madden['Team'] == team]
					print(x.iloc[0:51].sort_values('Overall Rating', ascending= False))


				else:
					team = NFC_sth[3]
					data = madden[['Full Name','Position','Overall Rating','Age','Years Pro','Height','Weight']]
					x = data.loc[madden['Team'] == team]
					print(x.iloc[0:51].sort_values('Overall Rating', ascending= False))

			elif division == 3:
				teams(NFC_wst)
				team = int(input('Team:\t'))

				if team == 1:
					team = NFC_wst[0]
					data = madden[['Position','Overall Rating','Age','Years Pro','Height','Weight']]
					x = data.loc[madden['Team'] == team]
					print(x.iloc[0:51].sort_values('Overall Rating', ascending= False))


				elif team == 2:
					team = NFC_wst[1]
					data = madden[['Position','Overall Rating','Age','Years Pro','Height','Weight']]
					x = data.loc[madden['Team'] == team]
					print(x.iloc[0:51].sort_values('Overall Rating', ascending= False))


				elif team == 3:
					team = NFC_wst[2]
					data = madden[['Position','Overall Rating','Age','Years Pro','Height','Weight']]
					x = data.loc[madden['Team'] == team]
					print(x.iloc[0:51].sort_values('Overall Rating', ascending= False))


				else:
					team = NFC_wst[3]
					data = madden[['Position','Overall Rating','Age','Years Pro','Height','Weight']]
					x = data.loc[madden['Team'] == team]
					print(x.iloc[0:51].sort_values('Overall Rating', ascending= False))

			else:
				teams(NFC_st)	
				team = int(input('Team:\t'))

				if team == 1:
					team = NFC_st[0]
					data = madden[['Position','Overall Rating','Age','Years Pro','Height','Weight']]
					x = data.loc[madden['Team'] == team]
					print(x.iloc[0:51].sort_values('Overall Rating', ascending= False))


				elif team == 2:
					team = NFC_st[1]
					data = madden[['Position','Overall Rating','Age','Years Pro','Height','Weight']]
					x = data.loc[madden['Team'] == team]
					print(x.iloc[0:51].sort_values('Overall Rating', ascending= False))


				elif team == 3:
					team = NFC_st[2]
					data = madden[['Position','Overall Rating','Age','Years Pro','Height','Weight']]
					x = data.loc[madden['Team'] == team]
					print(x.iloc[0:51].sort_values('Overall Rating', ascending= False))


				else:
					team = NFC_st[3]
					data = madden[['Position','Overall Rating','Age','Years Pro','Height','Weight']]
					x = data.loc[madden['Team'] == team]
					print(x.iloc[0:51].sort_values('Overall Rating', ascending= False))







