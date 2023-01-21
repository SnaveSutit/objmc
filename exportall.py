import subprocess
import shutil

DEFAULT_OFFSET = [-0.0001, -0.51, 0.1928]

files = [
	# {
	# 	'name': 'empty',
	# 	'output': 'empty',
	# 	'texture': 'D:/github-repos/mcmap-plush-rush/resources/assets/minecraft/textures/block/empty.png',
	# 	'offset': [0, 0, 0],
	# 	'scale': 1.0
	# },
	{
		'name': 'main_dinning_hall',
		'output': 'main_dinning_hall_se',
		'texture': 'D:/github-repos/mcmap-plush-rush/resources/assets/minecraft/textures/block/fnaf_1/party_table_end.png',
		'offset': [0, 0, 0],
		'scale': 1.0
	},
	# {
	# 	'name': 'main_dinning_hall',
	# 	'output': 'main_dinning_hall_sw',
	# 	'texture': 'D:/github-repos/mcmap-plush-rush/resources/assets/minecraft/textures/block/fnaf_1/party_table_end.png',
	# 	'offset': [18, 0, 0],
	# 	'scale': 1.0
	# },
	# {
	# 	'name': 'main_dinning_hall',
	# 	'output': 'main_dinning_hall_nw',
	# 	'texture': 'D:/github-repos/mcmap-plush-rush/resources/assets/minecraft/textures/block/fnaf_1/party_table_end.png',
	# 	'offset': [18, 0, 24],
	# 	'scale': 1.0
	# },
	# {
	# 	'name': 'main_dinning_hall',
	# 	'output': 'main_dinning_hall_ne',
	# 	'texture': 'D:/github-repos/mcmap-plush-rush/resources/assets/minecraft/textures/block/fnaf_1/party_table_end.png',
	# 	'offset': [0, 0, 24],
	# 	'scale': 1.0
	# }
]

for file in files:
	offset = [
		DEFAULT_OFFSET[0] + file['offset'][0],
		DEFAULT_OFFSET[1] + file['offset'][1],
		DEFAULT_OFFSET[2] + file['offset'][2]
	]
	subprocess.call(
		f'python objmc.py --objs "D:/github-repos/mcmap-plush-rush/objmodels/{file["name"]}.obj" --texs "{file["texture"]}" --frames 0 --out "{file["output"]}.json" "block/objmc/{file["output"]}.png" --offset {offset[0]} {offset[1]} {offset[2]} --scale {file["scale"]} --duration 20 --easing 3 --colorbehavior ttt --autorotate 0'
	)
	shutil.copy(f'./{file["output"]}.png', 'D:/github-repos/mcmap-plush-rush/resources/assets/minecraft/textures/block/objmc/')
	shutil.copy(f'./{file["output"]}.json', 'D:/github-repos/mcmap-plush-rush/resources/assets/minecraft/models/block/objmc/')
