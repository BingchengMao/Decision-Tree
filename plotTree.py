import matplotlib.pyplot as plt
decision_node = dict(boxstyle ="sawtooth", fc ="0.8")
leaf_node = dict(boxstyle ="round4", fc ="0.8")
arrow_args = dict(arrowstyle = "<-")

def createPlot():
	fig = plt.figure(1, facecolor = 'white')
	fig.clf()
	createPlot.ax1 = plt.subplot(111,frameon = False)
	plotNode('a decision node', (0.5, 0.1), (0.1, 0.5), decision_node)
	plotNode('a leaf node', (0.8, 0.1), (0.3, 0.8), leaf_node)
	plt.show()

def plotNode(node_txt, center_pt, parent_pt, node_type):
	createPlot.ax1.annotate(node_txt, xy = parent_pt, xycoords='axes fraction',
		xytext=center_pt, textcoords='axes fraction',
		va="center", ha="center",bbox=node_type, arrowprops=arrow_args)

def getNumLeafs(my_tree):
	num_leafs = 0
	first_value = list(my_tree.keys())[0]
	second_value = my_tree[first_value]
	for key in second_value.keys():
		if (type(second_value[key]).__name__ =='dict'):
			num_leafs += getNumLeafs(second_value[key])
		else:
			num_leafs+=1
	return num_leafs

def getTreeDeepth(my_tree):
	max_deepth = 0
	first_value = list(my_tree.keys())[0]
	second_value = my_tree[first_value]
	for key in second_value.keys():
		if(type(second_value[key]).__name__ == 'dict'):
			thisDeepth = 1 + getTreeDeepth(second_value[key])
		else:
			thisDeepth = 1
		if(thisDeepth>max_deepth):
			max_deepth = thisDeepth
	return max_deepth

def retrieveTree(i):
    listOfTrees =[{'no surfacing': {0: 'no', 1: {'flippers': {0: 'no', 1: 'yes'}}}},
                  {'no surfacing': {0: 'no', 1: {'flippers': {0: {'head': {0: 'no', 1: 'yes'}}, 1: 'no'}}}}
                  ]
    return listOfTrees[i]

my_tree = retrieveTree(0)
print(getTreeDeepth(my_tree),getNumLeafs(my_tree))


#createPlot()