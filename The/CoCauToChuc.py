import tkinter as tk
from tkinter import ttk
from GUI_Route import *

class CoCau():
    def __init__(self):
        import matplotlib.pyplot as plt

        # Define the tree structure
        tree = {'A': ['B', 'C'],
                'B': ['D', 'E'],
                'C': ['F', 'G'],
                'D': ['H'],
                'E': [],
                'F': [],
                'G': [],
                'H': []}

        # Define the plot parameters
        fig, ax = plt.subplots(figsize=(10, 10))
        ax.set_xlim([-0.1, 1.1])
        ax.set_ylim([-0.1, 1.1])
        ax.axis('off')

        # Define the coordinates of each node
        coord = {'A': (0.5, 1),
                 'B': (0.2, 0.8),
                 'C': (0.8, 0.8),
                 'D': (0.1, 0.6),
                 'E': (0.3, 0.6),
                 'F': (0.7, 0.6),
                 'G': (0.9, 0.6),
                 'H': (0.15, 0.4)}

        # Draw the edges and nodes
        for node in tree:
            for child in tree[node]:
                ax.plot([coord[node][0], coord[child][0]], [coord[node][1], coord[child][1]], color='black')
            ax.text(coord[node][0], coord[node][1], node, ha='center', va='center', fontsize=20, fontweight='bold',
                    color='white', bbox=dict(facecolor='gray', edgecolor='black', boxstyle='round'))

        # Show the plot
        plt.show()







