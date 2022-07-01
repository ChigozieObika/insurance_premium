import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
sns.set_theme(style="darkgrid")


def freq_distr_plot(df, feature, Outliers=False):
    plt.rcParams.update({'figure.figsize': (5, 3), 'figure.dpi': 100})
    sns.histplot(df[feature], bins=20, kde=True)
    plt.ylabel('count', fontsize=10, fontweight='bold')
    plt.xlabel(f'{feature}', fontsize=10, fontweight='bold')
    if Outliers:
        plt.title(f'Frequency Distribution of {feature.capitalize()} for Outliers', 
                fontsize=12, fontweight='bold')
    else:
        plt.title(f'Frequency Distribution of {feature.capitalize()}', 
                fontsize=12, fontweight='bold')
    plt.show()

def data_scatter_plot(*args, Outliers=False):
    args = list(args)
    plt.rcParams.update({'figure.figsize': (5, 3), 'figure.dpi': 100})
    if len(args)==3:
        sns.relplot(
            data=args[0], y=args[1], x=args[2] 
        )
        if Outliers:
            plt.title(f'Scatterplot of {args[1]} vs {args[2]} for Outliers', 
                    fontsize=12, fontweight='bold')
        else:
            plt.title(f'Scatterplot of {args[1]} vs {args[2]}', 
                    fontsize=12, fontweight='bold')
    if len(args)==4:
        sns.relplot(
            data=args[0], y=args[1], x=args[2], hue=args[3] 
        )
        if Outliers:
            plt.title(f'Scatterplot of {args[1]} vs {args[2]} vs {args[3]} for Outliers', 
                    fontsize=12, fontweight='bold')
        else:
            plt.title(f'Scatterplot of {args[1]} vs {args[2]} vs {args[3]}', 
                    fontsize=12, fontweight='bold')
    if len(args)==5:
        sns.relplot(
            data=args[0], y=args[1], x=args[2], hue=args[3], style=args[4] 
        )
        if Outliers:
            plt.title(f'Scatterplot of {args[1]} vs {args[2]} vs {args[3]} vs {args[4]} for Outliers', 
                    fontsize=12, fontweight='bold')
        else:
            plt.title(f'Scatterplot of {args[1]} vs {args[2]} vs {args[3]} vs {args[4]}', 
                    fontsize=12, fontweight='bold')
    plt.ylabel(f'{args[1]}', fontsize=10, fontweight='bold')
    plt.xlabel(f'{args[2]}', fontsize=10, fontweight='bold')
    plt.show()

def grouped_data(*args):
    args=list(args)
    countby=args[1]; groupby_list=args[2:]
    result= args[0].groupby(
    groupby_list)[countby].mean().round(2)
    result = pd.DataFrame(result)
    result.reset_index(inplace=True)
    result.rename(columns = {'charges':'avg_charges'},
    inplace=True)
    return result

def avg_charges_barplot(df, outliers=False):
    cols = list(df.columns)
    plt.figure(figsize=(3, 3), dpi=150)
    sns.barplot(y=cols[1], x=cols[0], 
                hue=cols[0], data=df, 
                )
    if not outliers:
        plt.title(f'Average charges vs {cols[0]}')
    else:
        plt.title(f'Average charges vs {cols[0]} for outliers')
    plt.legend(loc = 2, bbox_to_anchor = (1,1))
    plt.show()

def avg_charges_catplot(df, outliers=False):
    cols=list(df.columns)
    if len(cols)< 4:
        sns.catplot(y=cols[2], x=cols[0], hue=cols[1], 
                    data=df, kind="bar",
                    height=4, aspect=.8)
        if not outliers:
            plt.title(f'Average charges vs {cols[0]} vs {cols[1]}')
        else:
            plt.title(f'Average charges vs {cols[0]} vs {cols[1]} for outliers')
    else:
        sns.catplot(y=cols[3], x=cols[0], 
                hue=cols[1], col=cols[2], data=df,
                kind='bar', height=4, aspect=.8
                )
    plt.show()