N = 8
output = open("ktp1.cnf","w")
for i in range(N**2):
	clause = []
	for r in range(N):
		for c in range(N):
			clause.append(i*N**2 + r*N + c + 1)

	buf = " ".join(map(str,clause))
	buf += ' 0 \n'
	output.write(buf)

for i in range(N**2):
	for r in range(N):
		for c in range(N):
			base = -(i*N**2 + r*N + c + 1)
			for m in range(r, N):
				for n in range(c, N-1):
					clause = []
					clause.append(base)
					clause.append(-(i*N**2 + m*N + n + 2))
					buf = " ".join(map(str,clause))
					buf += ' 0 \n'
					output.write(buf)

for i in range(N**2-1):
	dif = [(2, 1),(2, -1),(-2, 1),(-2, -1),(1, 2),(1, -2),(-1, 2),(-1, -2)]
	for r in range(N):
		for c in range(N):
			clause = [-(i*N**2 + r*N + c + 1)]
			for dr, dc in dif:
				nr = r + dr
				nc = c + dc
				if nr not in range(N) or nc not in range(N):
					continue
				clause.append((i+1)*N**2 + nr*N + nc + 1)

			buf = " ".join(map(str,clause))
			buf += ' 0 \n'
			output.write(buf)

for r in range(N):
	for c in range(N):
		for i1 in range(N**2-1):
			for i2 in range(i1+1, N**2):
				clause = []
				clause.append(-(i1*N**2 + r*N + c + 1))
				clause.append(-(i2*N**2 + r*N + c + 1))
				buf = " ".join(map(str,clause))
				buf += ' 0 \n'
				output.write(buf)

output.close()

