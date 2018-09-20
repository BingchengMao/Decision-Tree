import matplotlib.pyplot as plt
decision_node = dict(boxstyle ="sawtooth", fc ="0.8")
leaf_node = dict(boxstyle ="round4", fc ="0.8")
arrow_args = dict(arrowstyle = "<-")



def createPlot(in_tree):
	fig = plt.figure(1, facecolor = 'white')
	fig.clf()
	axprops = dict(xticks=[], yticks=[])
	createPlot.ax1 = plt.subplot(111,frameon = False, **axprops)
	plotTree.totalW = float(getNumLeafs(in_tree))
	plotTree.totalD = float(getTreeDeepth(in_tree))
	plotTree.x0ff = -0.5/plotTree.totalW
	plotTree.y0ff = 1.0
	plotTree(in_tree, (0.5, 1.0), '')
	#plotNode('a decision node', (0.5, 0.1), (0.1, 0.5), decision_node)
	#plotNode('a leaf node', (0.8, 0.1), (0.3, 0.8), leaf_node)
	plt.show()

def plotMidText(cntr_pt, parent_pt, txt_string):
	x_mid = (parent_pt[0]-cntr_pt[0])/2.0+cntr_pt[0]
	y_mid = (parent_pt[1]-cntr_pt[1])/2.0+cntr_pt[1]
	createPlot.ax1.text(x_mid, y_mid, txt_string)



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

def plotTree(my_tree, parent_pt, node_txt):
	num_leafs = getNumLeafs(my_tree)
	depth = getTreeDeepth(my_tree)
	first_str = list(my_tree.keys())[0]
	cntr_pt = (plotTree.x0ff + (1.0+ num_leafs)/2.0/plotTree.totalW,plotTree.y0ff)
	plotMidText(cntr_pt, parent_pt, node_txt)
	plotNode(first_str, cntr_pt, parent_pt, decision_node)
	second_dict = my_tree[first_str]
	plotTree.y0ff = plotTree.y0ff - 1.0/plotTree.totalD
	for key in second_dict.keys():
		if type(second_dict[key]).__name__ == 'dict':
			plotTree(second_dict[key], cntr_pt, str(key))
		else:
			plotTree.x0ff = plotTree.x0ff + 1.0/plotTree.totalW
			plotNode(second_dict[key], (plotTree.x0ff, plotTree.y0ff),cntr_pt, leaf_node)
			plotMidText((plotTree.x0ff, plotTree.y0ff),cntr_pt, str(key))
	plotTree.y0ff = (plotTree.y0ff)+1.0/plotTree.totalD

		

def retrieveTree(i):
    listOfTrees =[{'no surfacing': {0: 'no', 1: {'flippers': {0: 'no', 1: 'yes'}}}},
                  {'no surfacing': {0: 'no', 1: {'flippers': {0: {'head': {0: 'no', 1: 'yes'}}, 1: 'no'}}}}
                  ]
    return listOfTrees[i]
'''
my_tree = retrieveTree(0)
print(getTreeDeepth(my_tree),getNumLeafs(my_tree))

createPlot(my_tree)
'''