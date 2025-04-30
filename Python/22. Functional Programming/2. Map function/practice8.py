# Remove file extensions
# files = ['data.csv', 'report.pdf','image.jpeg']

files = ['data.csv', 'report.pdf','image.jpeg']
res = list(map(lambda s:s.split(".")[0], files))
print(res)