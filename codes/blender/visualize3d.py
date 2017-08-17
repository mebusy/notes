import ut
import csv
import urllib.request
###################
# Reading in Data #
###################

# Read iris.csv from file repository
url_str = 'http://blender.chrisconlan.com/iris.csv'
iris_csv = urllib.request.urlopen(url_str)
iris_ob = csv.reader(iris_csv.read().decode('utf-8').splitlines())

# Store header as list, and data as list of lists
iris_header = []
iris_data = []

for v in iris_ob:
    if not iris_header:
        iris_header = v 
    else:
        v = [float(v[0]), float(v[1]), float(v[2]), float(v[3]), str(v[4])]
        iris_data.append(v)

# Columns:
# 'Sepal.Length', 'Sepal.Width',
# 'Petal.Length', 'Petal.Width', 'Species'

# Visualize 3 dimensions
# Sepal.Length, Sepal.Width, and 'Petal.Length'

# Clear scene
ut.delete_all()

# Place data
for i in range(0, len(iris_data)): 
    ut.create.sphere('row-' + str(i))

v = iris_data[i]
ut.act.scale((0.25, 0.25, 0.25))
ut.act.location((v[0], v[1], v[2]))


