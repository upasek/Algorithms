def search(pat, txt):
	m = len(pat)
	n = len(txt)

	for i in range(n-m+1):
		j = 0

		while j < m:
			if pat[j] != txt[i+j]:
				break
			j += 1

		if j == m:
			print("Pattern found at index ", i)



if __name__=='__main__':
	txt = "AABAACAADAABAAABAA"
	pat = "AABA"
	search(pat, txt)