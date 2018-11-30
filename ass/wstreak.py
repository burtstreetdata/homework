def season()
	seasondata=open('c:/tmp/gl2018/gl2018.txt')
	seasonlines=seasondata.readlines()
	season_cub_games=1
	season_cub_runs=0
	season_enemy_runs_away=0
	season_enemy_runs_home=0
	cubs_wins=0
	cubs_losses=0
	cubscoreaway=0
	cubscorehome=0
	wstreak=0
	ls=0
	for line in seasonlines:
		fields = line.split(',')
		if 'CHN' in str(fields[3]):
			cubscoreaway= int(fields[9])+cubscoreaway
			season_enemy_runs_away+=int(fields [10])
			if int(fields[9])>int(fields[10]):
				cubs_wins+=1
				wstreak+=1
			   
			else:
				cubs_losses+=1
				if (wstreak>ls):
					ls=wstreak
				wstreak=0
				
			
		if 'CHN' in str(fields[6]):
			cubscorehome= int (fields [10])+cubscorehome
			season_enemy_runs_home+=int(fields[9])
			season_cub_games+=1
			if int(fields[10])>int(fields[9]):
				cubs_wins+=1
				wstreak+=1
				
			else:
				cubs_losses+=1
				if (wstreak>ls):
					ls=wstreak
				wstreak=0
	print (ls)    
	print (cubs_wins)
	print (cubs_losses)
	print (cubscoreaway)
	print (season_enemy_runs_away)
	print (cubscorehome)
	print (season_enemy_runs_home)
	
season()