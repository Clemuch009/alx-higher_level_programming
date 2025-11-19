#!/usr/bin/node

export const nbOccurences = function(list, searchElement){
	let count = 0;
	for (let item of list){
		if (item === searchElement)
		{
			count++;
		}
	}
	return count;
}
