### PyLam , Georgios Manios 2019
from tkinter import*
from tkinter import scrolledtext

def get_all_combinations(parent): # Finds all possible combinations of alleles a parent can pass on to their offspring, assuming independen assortment.
	if len(parent) == 1:
		return [parent[0][0], parent[0][1]]
	else:
		genlist = []
		for x in get_all_combinations(parent[1:]):
			genlist.append(parent[0][0] + x)
			genlist.append(parent[0][1] + x)
		return genlist

def make_row(genotype, allele):
	row = []
	for a in genotype:
		row.append(a + allele)
	return row


def make_table(parent1, parent2):
	table = []
	for a in parent1:
		table.append(make_row(parent2, a))
	return table


def print_table(table, c1, c2): # formats and prints Punnett square
	latextable = []
	divlength = (len(c1[0])*2+4)*2**(len(c1[0]))
	print('')
	print('', end=' ')
	for a in c2:
		print(' '*(len(c1[0])+3) + a + '', end=' ')
		latextable.append('& ' + a + ' ')
	print('\n' + ' '*(len(c1[0])+1) + '-'*(divlength))
	latextable.append('\\\ \n\\hline\n')

	for i, row in enumerate(table):
		print(c1[table.index(row)], end=' ')
		latextable.append(c1[table.index(row)] + ' & ')
		print('|', end=' ')
		for j, cell in enumerate(row):
			print(cell + ' | ', end=' ')
			if j != len(row)-1:
				latextable.append(cell + ' & ')
			else:
				latextable.append(cell + ' ')
		print('\n' + ' '*(len(c1[0])+1) + '-'*(divlength))
		if i != len(table)-1:
			latextable.append('\\\ \n')
	return latextable



def main(p1_genotype,p2_genotype):

	c1 = get_all_combinations(p1_genotype)
	c2 = get_all_combinations(p2_genotype)
	a = make_table(c1, c2)
	latextable = print_table(a, c1, c2)

	file = open("mendel.txt", "w")
	file.write(str(make_table(c1,c2)))
	file.write(str(print_table(a,c1,c2)))
	file.close()

def print_genotype_frequencies(table): # calculates frequencies for each genotype present in table
	freqtable = []
	freqtable.append('\n')
	calculated = []
	genotypes = [a for b in table for a in b]
	for k, x in enumerate(genotypes):
		count = 0
		for y in genotypes:
			if sorted(x) == sorted(y):
				count += 1
		if sorted(x) not in calculated:
			print("The frequency of the " + x + " genotype is " + str(float(count)/float((len(genotypes)))*100) + "%.")
			freqtable.append(x + ' & ' + str(float(count)/float((len(genotypes)))*100) + '\\% \\\ \\hline \n')
		calculated.append(sorted(x))
	return freqtable

def main():
    p1 = entry.get().split(' ')
    global latextable,freqtable
    p2 = entry2.get().split(' ')
    c1 = get_all_combinations(p1)
    c2 = get_all_combinations(p2)
    a = make_table(c1, c2)
    latextable = print_table(a, c1, c2)
    #txt.insert(INSERT, latextable)
    freqtable = print_genotype_frequencies(a)
    txt.insert(INSERT, freqtable)

def delete_button():
    txt.delete(1.0,END)


def nothing():
    print("\n")

window=Tk()
window.configure(background="gray28")
window.title("MENDEL GENOTYPES-ΓΕΩΡΓΙΟΣ Α.ΜΑΝΙΟΣ @2019")
window.geometry('700x250')
txt = scrolledtext.ScrolledText(window,width=40,height=10,bg="khaki")# text area
txt.grid(column=7,row=0)#text area position
entry = Entry(window , width=20,bg="royalblue")
entry.grid(column=1,row = 1 ) #10
entry2 = Entry(window , width=20,bg="salmon")
entry2.grid(column=2,row =1) # 20
label1 = Label(text="Give the genotypes\nyou want below",bg="gold3")
label1.grid(column=1,row=0)
label2 = Label(text="Results ")
label2.grid(column=6,row=0)
#label3 = Label(text="Genotype 2 ")
#label3.grid(column=2,row=0)
button1 = Button(window,text="Click for results ",command=main,bg="limegreen")
button1.grid(column=1, row=3)
button2 = Button(window,text="Delete",command=delete_button,bg="red")
button2.grid(column=7, row=1)
button3=Button(window,text="Genotype 2 ",command=nothing,bg="gold3")
button3.grid(column=2,row=2)
button4=Button(window,text="Genotype 1 ",command=nothing,bg="gold3")
button4.grid(column=1,row=2)
window.mainloop()
