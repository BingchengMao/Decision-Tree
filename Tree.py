import numpy as np
import math
import pickle as pk

def calcShannonEnt(data_set):
	num_samples = len(data_set)
	label_count = {}
	for fea_vec in data_set:
		current_label = fea_vec[-1]
		if(current_label not in label_count.keys()):
			label_count[current_label] = 0
		label_count[current_label]+=1
	shannon_ent = 0.0
	for key in label_count.keys():
		prob = label_count[key]/num_samples
		shannon_ent -=prob*math.log(prob, 2)
	return shannon_ent

def createDataSet():
	data_set = [[1,1,'yes'],
	[1,1,'yes'],
	[1,0,'no'],
	[0,1,'no'],
	[0,1,'no']]
	labels = ['no surfacing', 'flippers']
	return data_set,labels

def splitDataSet(data_set, axis, value):
	ret_data = []
	for fea_vec in data_set:
		if(fea_vec[axis] == value):
			reduced_fea_vec = fea_vec[:axis]
			reduced_fea_vec.extend(fea_vec[axis+1:])
			ret_data.append(reduced_fea_vec)
	return ret_data

def chooseBestFeaToSplit(data_set):
	num_features = len(data_set[0])-1
	best_fea = -1
	num_data = len(data_set)
	base_shannon = calcShannonEnt(data_set)
	best_shannon = 0.0
	for i in range(num_features):
		fea_list = [sample[i] for sample in data_set]
		unique_fea_list = set(fea_list)
		tmp_shannon = 0.0
		for uniq_fea in unique_fea_list:
			sub_data_set = splitDataSet(data_set, i, uniq_fea)
			sub_num_data = len(sub_data_set)
			#print(calcShannonEnt(data_set))
			tmp_shannon+=sub_num_data/num_data*calcShannonEnt(sub_data_set)
		new_shannon = base_shannon - tmp_shannon
		#print(tmp_shannon, end = '  ')
		#print(i)
		if(new_shannon>best_shannon):
			best_shannon = new_shannon
			best_fea = i
	return best_fea

def majorityCnt(class_list):
	class_count = {}
	for vote in class_list:
		if(vote not in class_count.keys()):
			class_count[vote] = 0
		class_count[vote] +=1
	class_key = list(class_count.keys())
	class_value = list(class_count.values())
	idx = class_value.index(max(class_value))
	return class_key[idx]

def createTree(data_set, labels):
	class_list = [sample[-1] for sample in data_set]
	if(class_list.count(class_list[0]) == len(data_set)):
		return class_list[0]
	if(len(data_set[0]) == 1):
		return majorityCnt(class_list)
	best_fea = chooseBestFeaToSplit(data_set)
	best_fea_label = labels[best_fea]
	#print(best_fea_label)
	my_tree = {best_fea_label:{}}
	del(labels[best_fea])
	fea_value = [sample[best_fea] for sample in data_set]
	uniq_fea_value = set(fea_value)
	for value in uniq_fea_value:
		sub_labels = labels[:]
		my_tree[best_fea_label][value] = createTree(splitDataSet(data_set, best_fea, value),sub_labels)
	return my_tree

def classify_with_tree(my_tree, test_labels, test_set):
	first_value = list(my_tree.keys())[0]
	second_value = my_tree[first_value]
	test_value = test_set[test_labels.index(first_value)]
	for key in second_value.keys():
		if(test_value == key):
			if(type(second_value[key]).__name__ == 'dict'):
				return classify_with_tree(second_value[key], test_labels, test_set)
			else:
				return second_value[key]

def storeTree(input_tree, file_name):
	fw = open(file_name, 'w')
	pk.dump(input_tree, fw)
	fw.close()

def grabTree(file_name):
	fr = open(file_name)
	return pk.load(fr)


'''
my_data,labels = createDataSet()

print(calcShannonEnt(my_data))
print(splitDataSet(my_data, 0, 1))
print(chooseBestFeaToSplit(my_data))

my_tree = createTree(my_data,labels)
my_data,labels = createDataSet()
print(classify_with_tree(my_tree, labels, [1,0]))
'''
import plotTree
fr = open('lenses.txt')
lenses = [inst.strip().split('\t') for inst in fr.readlines()]
#print(lenses)
lense_labels = ['age','prescript', 'astigmatic', 'tearrate']
lense_tree = createTree(lenses, lense_labels)
print(lense_tree)
