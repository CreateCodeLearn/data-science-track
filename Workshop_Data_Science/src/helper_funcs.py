'''
Helper functions for data science workshop
'''

import os
import numpy as np
import pandas as pd


def cuteplot(gpd_df, crs="Mollweide", title=None, kdp=False, map_extend=(-27, 45, 33, 73.5), bw=0.2):
    '''
    Function to leverage the cartopy library to plot geographical data
    '''
    import matplotlib.pyplot as plt
    import cartopy.crs as ccrs
    import cartopy.feature as cfeature
    import seaborn as sns

    # map projections
    proj = {"PlateCarree": ("+proj=eqc +lat_ts=0 +lat_0=0 +lon_0=0 +x_0=0 +y_0=0 +ellps=WGS84 +datum=WGS84 +units=m +no_defs",
                            ccrs.PlateCarree()),
            "Mollweide": ("+proj=moll +lon_0=0 +x_0=0 +y_0=0 +ellps=WGS84 +datum=WGS84 +units=m +no_defs",
                          ccrs.Mollweide()),
            "Robinson": ("+proj=robin +lon_0=0 +x_0=0 +y_0=0 +ellps=WGS84 +datum=WGS84 +units=m +no_defs",
                         ccrs.Robinson()),
            "UTM32N": ("+proj=utm +zone=32 +ellps=intl +units=m +no_defs",
                       ccrs.EuroPP()),
            "Orthographic": ("+proj=ortho", ccrs.Orthographic())
            }

    # plot figure
    fig = plt.figure()
    ax = plt.axes(projection=proj.get(crs)[1])
    # add features
    ax.coastlines(resolution='50m')
    ax.stock_img()
    countries = cfeature.NaturalEarthFeature(category='cultural',
                                             name='admin_0_boundary_lines_land',
                                             scale='50m',
                                             facecolor='none',
                                             edgecolor="black")
    ax.add_feature(countries)

    # extend
    ax.set_extent(map_extend)
    # plot geopandas data frame
    if crs != "PlateCarree":
        gpd_df = gpd_df.to_crs(proj.get(crs)[0])

    if kdp:
        kdp_germany = sns.kdeplot(gpd_df['Target Longitude'],
                                  gpd_df['Target Latitude'],  # y-axis
                                  cmap="viridis",
                                  shade=True,
                                  shade_lowest=False,
                                  bw=bw,
                                  transform = ccrs.PlateCarree()
                                  )
        kdp_germany.plot()
    else:
        gpd_df.plot(ax=ax, marker='o', color='red',
             markersize=5, alpha=0.01)
    # add gridlines
    ax.gridlines()

    if title is not None:
        ax.set_title(title, size=16)
    plt.tight_layout()

def plot_confusion_matrix(cm, classes,
                          normalize=False,
                          title='Confusion matrix'):
    """
    This function prints and plots the confusion matrix.
    Normalization can be applied by setting `normalize=True`.
    """
    import itertools
    import matplotlib.pyplot as plt

    if normalize:
        cm = cm.astype('float') / cm.sum(axis=1)[:, np.newaxis]
        print("Normalized confusion matrix")
    else:
        print('Confusion matrix, without normalization')

    cmap = plt.cm.Blues
    plt.imshow(cm, interpolation='nearest', cmap=cmap)
    plt.title(title)
    plt.colorbar()
    tick_marks = np.arange(len(classes))
    plt.xticks(tick_marks, classes, rotation=45)
    plt.yticks(tick_marks, classes)

    fmt = '.2f' if normalize else 'd'
    thresh = cm.max() / 2.
    for i, j in itertools.product(range(cm.shape[0]), range(cm.shape[1])):
        plt.text(j, i, format(cm[i, j], fmt),
                 horizontalalignment="center",
                 color="white" if cm[i, j] > thresh else "black")

    plt.tight_layout()
    plt.ylabel('True label')
    plt.xlabel('Predicted label')