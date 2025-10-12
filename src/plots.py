import matplotlib.pyplot as plt
import pandas as pd
import numpy as np

class Plotter1():
    def __init__(self, df):
        self.df = df

    def boxplotter(self):
        n = len(self.df)

        rows = int(np.ceil(np.sqrt(n)))
        cols = int(np.ceil(n / rows))

        fig, axes = plt.subplots(rows, cols, figsize=(15, 10))
        axes = axes.flatten()

        for idx, series in enumerate(self.df):
            numeric_values = pd.to_numeric(series, errors="coerce").dropna()
            
            if len(numeric_values) > 0:  # evitar series vacías
                axes[idx].boxplot(numeric_values.values)
                axes[idx].set_title(series.name, fontsize=8)
                axes[idx].tick_params(axis='x', which='both', bottom=False, top=False, labelbottom=False)
            else:
                axes[idx].text(0.5, 0.5, "No numeric data", ha='center', va='center')
                axes[idx].set_title(series.name, fontsize=8)
                axes[idx].axis("off")

        for j in range(idx + 1, len(axes)):
            fig.delaxes(axes[j])

        plt.tight_layout()
        plt.show()

class Plotter2():
    def __init__(self, df):
        self.df = df

    def histplotter(self):
        n = len(self.df)

        # calcular layout (cuadrado aproximado)
        rows = int(np.ceil(np.sqrt(n)))
        cols = int(np.ceil(n / rows))

        fig, axes = plt.subplots(rows, cols, figsize=(15, 10))
        axes = axes.flatten()

        for idx, series in enumerate(self.df):
            numeric_values = pd.to_numeric(series, errors="coerce").dropna()
            
            if len(numeric_values) > 0:
                axes[idx].hist(numeric_values.values, bins=20, color="skyblue", edgecolor="black")
                axes[idx].set_title(series.name, fontsize=8)
            else:
                axes[idx].text(0.5, 0.5, "No numeric data", ha='center', va='center')
                axes[idx].set_title(series.name, fontsize=8)
                axes[idx].axis("off")

        # eliminar subplots sobrantes
        for j in range(idx + 1, len(axes)):
            fig.delaxes(axes[j])

        plt.tight_layout()
        plt.show()