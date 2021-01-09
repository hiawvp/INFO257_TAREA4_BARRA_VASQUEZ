import os
from os.path import isdir, join, exists

labels = {
    0 : 'Art Nouveau o Modernismo',
    1 : 'Barroco',
    2 : 'Expresionismo',
    3 : 'Impresionismo',
    4 : 'Neoclasicismo',
    5 : 'Posimpresionismoo',
    6 : 'Realismo',
    7 : 'Romanticismo',
    8 : 'Surrealismo',
    9 : 'Symbolism'
}

def organizar_datasets():
    root = os.path.abspath('')
    print(root)
    wikiart = join(root, 'wikiart')
    
    data_folder = join(root, 'data')
    if (not exists(data_folder)):
        os.mkdir(data_folder)
        print(f"carpeta {'data'} creada en {root}")

    for dset in ['train', 'test']:
        folder = join(data_folder, dset)

        if (not exists(folder)):
            os.mkdir(folder)
            print(f"carpeta {dset} creada en {root}")

        with open(f'wikiart/{dset}.txt', 'r', encoding='utf-8') as file:
            #carpetas 0..9
            for i in range(len(labels)):
                category_folder = join(folder, str(i))
                if (not exists(category_folder)):
                    os.mkdir(category_folder)
                    print(f"carpeta {str(i)} creada en {folder}")
            #mover cada imagen a su carpeta-categoria
            for i, line in enumerate(file):
                [name, label] = line.replace('\n', '').split(' ')
                ext = name.split('.')[-1]
                output_name = join(folder, label, str(i).zfill(4) + '.' + ext)
                try:
                    os.rename(join(wikiart, name), output_name)
                except FileNotFoundError:
                    print(f"no se pudo mover {name}")
                    break
