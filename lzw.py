class TwoWayDict(dict):
    def __setitem__(self, key, value):
        # Remove any previous connections with these values
        if key in self:
            del self[key]
        if value in self:
            del self[value]
        dict.__setitem__(self, key, value)
        dict.__setitem__(self, value, key)

    def __delitem__(self, key):
        dict.__delitem__(self, self[key])
        dict.__delitem__(self, key)

    def __len__(self):
        """Returns the number of connections"""
        return dict.__len__(self) // 2

d = TwoWayDict()
count = 0
for number in range(32,127):
	d[count] = chr(number)
	count += 1

s = ""
ch = ""
output = ""
read_file = open("sample.txt","r")
sample = read_file.read()
read_file.close()
compressed_file = open("compressed.txt","w+")

for ch in sample:
	if s+ch in d.values():
		s = s + ch
	else :
		# print(d[s])
		output = output + str(d[s]) + " "
		d[count] = s + ch
		count += 1
		s = ch
# print(d[s])
output = output + str(d[s]) + " "
compressed_file.write(output)
compressed_file.close()
# print(output)