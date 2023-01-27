import ObjFile from 'obj-file-parser'
import * as fs from 'fs/promises'

const DEBUG_PATH = 'D:/github-repos/mcmap-plush-rush/objmodels/cow.obj'

async function main() {
	const fileContents = await fs.readFile(DEBUG_PATH, 'utf-8')
	const obj = new ObjFile(fileContents)
	const content = obj.parse()
	await fs.writeFile('./output.json', JSON.stringify(content, null, '\t'))
}

main()
