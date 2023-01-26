type Position = [number, number, number]
type Uv = [number, number]
type Vertex = [number, number, number]

export class OBJFile {
	positions: Position[] = []
	uvs: Uv[] = []
	vertices: Vertex[] = []

	constructor(path: string) {}
}
