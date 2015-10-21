import json

fileIns = open('installed_module', 'r')
installed = fileIns.read()

# read the needed technologies
dependancies = json.load(open("dependencies.json"))
dp = dependancies['dependencies']   # shortening
dpToStr = ''.join(dp)

if dpToStr in installed:
	print ('All done.')
else: 
	allPacks = json.load(open('all_packages.json'))
	selected = allPacks[dpToStr]
	print('In order to install {0}, we need {1} and {2}.'.format(dpToStr, selected[0], selected[1]))
	for i in range (0, len(selected)):
		if selected[i] not in installed:
			print ('Installing {}.'.format(selected[i]))
		else:
			print ('{} is already installed.'.format(selected[i]))
		selected2 = allPacks[selected[i]]
		print ('In order to install {0}, we need {1}'.format(selected[i],selected2[0]))

		if selected2[0] not in installed:
			print ('Installing {}.'.format(selected2[0]))
		else:
			print ('{} is already installed.'.format(selected2[0]))

		# for j in range (0, len(selected2)):
		# 	selected31 = allPacks[selected2[j]]


fileIns.close()