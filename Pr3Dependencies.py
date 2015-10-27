import json

fileIns = open('installed_module', 'r')
installed = fileIns.read()

# read the needed technologies
dependancies = json.load(open("dependencies.json"))
dpToStr = ''.join(dependancies['dependencies'] )
update_file = open('installed_module', 'a')						
allPacks = json.load(open('all_packages.json'))
selected = allPacks[dpToStr]

def traverse_allpacks(selected):
	for alll in selected:
		if alll in installed:
			print ('{0} is allready installed'.format(alll.capitalize()))
		else:
			
			print ('Installing: {0}....'.format(alll))
			update_tech = update_file.writelines('\n{0}'.format(alll))
			for i in range (0, len(allPacks[alll])):
				
				if allPacks[alll][i] in installed:
					print('In order to install {0}, we need {1}.'.format(alll, allPacks[alll][i]), end = ' ')
				else:
					print('In order to install {0}, we need {1}'.format(alll, allPacks[alll][i]))
			if allPacks[alll] :		
				selected = allPacks[alll]
				traverse_allpacks(selected)

if dpToStr in installed:
	print ('Maa\'man you are fully set to start the project.  All techs are already under your belt!')
else: 
	print ('Installing {0}'.format(dpToStr))
	print('In order to install {0}, we need:'.format(dpToStr) , end = ' ') 
	for i in (0, len(selected)-1):
		print (selected[i], end = ' ')
		if len(selected) > 0 and i < len(selected)-1 : 
			print ('and', end = ' ')
	print()

traverse_allpacks(selected)

update_file.close()
fileIns.close()