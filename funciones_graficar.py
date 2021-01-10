from os import listdir
import pandas as pd
from os.path import join
import numpy as np
import matplotlib.pyplot as plt
from matplotlib.ticker import MaxNLocator



categories = { "train" : ("train_accy", "train_loss"), 
               "valid" : ("valid_accy", "valid_loss")}

def data_extractor(path, category):
    data = []
    for file in sorted(listdir(path)):
        #file : run - model/label - time - tag - ej"train_loss.csv" 
        name = file.split("-")
        if (len(name)== 6):
            model = name[1] + "-" + name[2]
        else:
            model = name[1]
        if (category == (name[-1].split("."))[0]):
            values = list(pd.read_csv(join(path, file))["Value"])
            data.append((model, values))
    return data



def plot(stage, experiment, title=""):
    bottom = 1.5 if stage == "valid" else -0.1
    top = 7. if stage == "valid" else 3.
    fig, ax = plt.subplots(1, 2, figsize=(8,4), tight_layout=True)
    for i, cosa in enumerate(categories.get(stage)):
        data = data_extractor(f"pruebas/{experiment}", cosa)
        for (label, values) in data:
            epochs = np.arange(len(values)) + 1
            ax[i].plot(epochs, values, label=label)
        ax[i].legend()
        ax[i].set_xlabel('Época')
        ax[i].set_ylabel(cosa.split("_")[-1])
        ax[i].grid()
        ax[i].xaxis.set_major_locator(MaxNLocator(integer=True))
    
    if (ax[1].get_ylim()[1] > 7.):
        ax[1].set_ylim(bottom, top)
    fig.suptitle(f"{title}\n{stage}")
    plt.show()