import os
from typing import Any, Dict, List, Optional, Union
import pathlib

def create_table (data: Dict[str, List[Any]], caption: Optional[str]) -> Optional[str]:
	columns = data.keys()
	max_index = max([len(data[column]) for column in columns])
	if not max_index: return "not valid"

	path = str(pathlib.Path().resolve()) + "/table.txt"
	table = open(path, "w")

	table.write("\\begin{table}[h!]" + os.linesep)
	table.write("	\\centering" + os.linesep)
	table.write("	\\begin{tabular}{|%s|}" % "|".join(["c" for i in range(len(columns))]) + os.linesep)
	table.write("		\\hline" + os.linesep)
	table.write("		" + " & ".join([column for column in columns]) + "\\\\" + os.linesep)
	table.write("		\\hline" + os.linesep)
	for i in range(max_index):
		table.write("		" + " & ".join([str(data[column][i]) if i < len(data[column]) else "" for column in columns]) + "\\\\" + os.linesep)
	table.write("		\\hline" + os.linesep)
	table.write("	\\end{tabular}" + os.linesep)
	table.write("	\\caption{%s}" % (caption or "Tabla generada en python.") + os.linesep)
	table.write("	\\label{tab:pythonTab}" + os.linesep)
	table.write("\\end{table}" + os.linesep)

	table.close()
	return None


# dummy_data = {
# 	"col1": [1,2,3,4,5,6],
# 	"col2": [2,4,6,8,10,12],
# 	"col3": [3,6,9,12,15,18],
# 	"col4": [4,5,6,7],
# 	"col5": [0,0,0,0,0,0]
# }

# create_table(dummy_data)