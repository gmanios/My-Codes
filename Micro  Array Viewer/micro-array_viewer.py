import tkinter as tk
from tkinter import filedialog
from plotly.graph_objs import *
from matplotlib.widgets import TextBox
from tkinter import *
import matplotlib.pyplot as plt
import matplotlib.lines as lines
import numpy as np
import pylustrator
import pandas as pd
from scipy.spatial.distance import pdist, squareform
import os
import seaborn as sns
pd.options.plotting.backend = "plotly"
from pylab import *
import plotly.graph_objects as go
from sklearn.cluster import KMeans
import scipy.cluster.hierarchy as sch
def Run():
  filename=Import_File()

  for f1 in filename:

    df= pd.read_csv(f1, sep="\t", skiprows=[0],header=None, low_memory=False)
    list=df.to_dict('list')
    genes = df.iloc[:, 0]
    expressions=df.loc[:, df.columns != 0]
    new=pd.DataFrame(expressions)
    new.index=genes

    all_express=df.loc[:, df.columns != 0]
    ei=expressions.index
    ec=expressions.columns
    name = os.path.basename(f1)
    expressions=np.array(expressions)
    genes=np.array(genes)
    df.index = df.index -1
    df.columns = df.columns - 1
    df.index=genes
    new=new.T
    new2=new.T


    expressions2=new2.values
    dictionary=dict(zip(new2.index,expressions2))

    expressions=pd.DataFrame(expressions)





    import plotly.express as px

    import plotly.graph_objects as go

    fig = go.Figure(data=go.Heatmap(
       z=df,
       x= np.array(df.columns),
       y= np.array(df.index),xgap=2,ygap=32,colorscale='RdYlGn'))
    fig['layout']['yaxis']['autorange'] = "reversed"
    fig['layout'].update(width=2000, height=2000, autosize=False)


    fig.update_xaxes(side="top" )
    fig.update_layout(paper_bgcolor="#2a2e2c",font_color="white",template="plotly_dark",title='Results from file   '+name)
    fig.show()
    import seaborn as sns

    sns.set(style="ticks", context="talk")
    plt.style.use("dark_background")
    sns.distplot(np.array(expressions), kde_kws={"shade": True})


    sns.set_style("white")
    genes=pd.DataFrame(genes,columns=['Genes'])
    expressions.index=np.array(genes)


    expressions=np.array(expressions)

    genes = np.array(genes)

    repeat=np.repeat(genes, len(expressions.flat) / len(genes))
    fig = px.scatter_3d(expressions, x=repeat, y=expressions.flat, z=np.linspace(0,1,len(expressions.flat)),
                        color=expressions.flat, color_continuous_scale='RdYlGn', title='3D Scatter plot ', opacity=0.7,template="plotly_dark")


    fig.update_layout(paper_bgcolor="#2a2e2c", font_color="white")
    fig.show()

    import fastcluster
    x = fastcluster.linkage(new,method='single', metric='euclidean',preserve_input=True)
    x2 = fastcluster.linkage(new, method='average', metric='euclidean')
    x3 = fastcluster.linkage(new, method='complete', metric='euclidean')


    import seaborn as sns




    x4 = sns.clustermap(new, method='single', cmap='RdYlGn')
    plt.title('Single linkage')
    x5 = sns.clustermap(new,method='average', cmap='RdYlGn')

    plt.title('Average linkage')

    x6 = sns.clustermap(new,method='complete', cmap='RdYlGn')

    plt.title('Complete linkage')

    plt.show()





def Run2():
 filename = Import_File()

 for f1 in filename:
    from bioinfokit import analys, visuz
    # load dataset as pandas dataframe
    df = pd.read_csv(f1, sep="\t")

    visuz.gene_exp.volcano(df=df, lfc='logFC', pv='P.Value', show=True, lfc_thr=2, pv_thr=0.01,
                           color=("#00239CFF", "grey", "#E10600FF"), plotlegend=True, legendpos='upper right',
                           legendanchor=(1.46, 1))


def Run3():
    filename = Import_File()

    for f1 in filename:
        from pyvis.network import Network
        import pandas as pd

        net = Network(height="1000px", width="100%", bgcolor="#222222", font_color="white")

        # set the physics layout of the network
        net.barnes_hut()
        data = pd.read_csv(f1,sep='\t')

        sources = data['Source']
        targets = data['Target']
        weights = data['Weight']

        edge_data = zip(sources, targets, weights)

        for e in edge_data:
            src = e[0]
            dst = e[1]
            w = e[2]

            net.add_node(src, src, title=src)
            net.add_node(dst, dst, title=dst)
            net.add_edge(src, dst, value=w)

        neighbor_map = net.get_adj_list()

        # add neighbor data to node hover data
        for node in net.nodes:
            node["title"] += " Neighbors:<br>" + "<br>".join(neighbor_map[node["id"]])
            node["value"] = len(neighbor_map[node["id"]])

        net.show("Network_data.html")



def Import_File(event=None):
    file_list=[]
    filename = filedialog.askopenfilenames()

    file_list.append(filename)



    return filename





def gui():
    # GUI
    root = tk.Tk()
    root.geometry("380x300")

    root.title("Simple micro - array Viewer tool  @ 2020 G.Manios")

    photo = PhotoImage(file=r"ma.png")
    photo2 = PhotoImage(file=r"small_v.png")
    photo3 = PhotoImage(file=r"net_work.png")

    photoimage2 = photo.subsample(1, 1)
    photoimage3 = photo2.subsample(1, 1)
    photoimage4 = photo3.subsample(1, 1)

    button1 = tk.Button(root, height=100, width=385, text=' Select micro-array data and view them ! ', command=Run,
                        image=photoimage2,
                        compound=LEFT).pack(side=TOP)
    button2 = tk.Button(root, height=100, width=385, text=' Insert data for volcano plot', command=Run2,
                        image=photoimage3,

                        compound=LEFT).pack(side=TOP)
    button3 = tk.Button(root, height=100, width=385, text=' Insert network data', command=Run3,
                        image=photoimage4, compound=LEFT).pack(side=TOP)




    root.mainloop()

gui()



