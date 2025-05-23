import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
from matplotlib import cm
import plotly.graph_objects as go
from scipy.special import zeta
import tkinter as tk
from tkinter import ttk
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg

def calculate_zeta_grid(sigma_min, sigma_max, t_min, t_max, points=50):
    sigma = np.linspace(sigma_min, sigma_max, points)
    t = np.linspace(t_min, t_max, points)
    sigma_grid, t_grid = np.meshgrid(sigma, t)
    s_grid = sigma_grid + 1j * t_grid
    

    zeta_values = np.zeros_like(s_grid, dtype=complex)
    for i in range(points):
        for j in range(points):
            try:
                zeta_values[i, j] = zeta(s_grid[i, j])
            except:
                zeta_values[i, j] = float('nan') + 1j * float('nan')

    magnitude = np.abs(zeta_values)
    phase = np.angle(zeta_values)
    
    return sigma_grid, t_grid, zeta_values, magnitude, phase

def calculate_single_zeta(sigma, t):
    s = complex(sigma, t)
    try:
        result = zeta(s)
        return result, np.abs(result), np.angle(result)
    except:
        return None, None, None

class RiemannZetaApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Riemann Zeta Function Visualizer")
        self.root.geometry("1200x800")
        

        self.control_frame = ttk.Frame(root, padding="10")
        self.control_frame.pack(side=tk.TOP, fill=tk.X)
        
        self.plot_frame = ttk.Frame(root)
        self.plot_frame.pack(side=tk.BOTTOM, fill=tk.BOTH, expand=True)
        

        ttk.Label(self.control_frame, text="ζ(s) calculate (s = σ + it için)").grid(column=0, row=0, columnspan=4)
        
        ttk.Label(self.control_frame, text="σ value:").grid(column=0, row=1)
        self.sigma_var = tk.DoubleVar(value=0.5)
        self.sigma_entry = ttk.Entry(self.control_frame, textvariable=self.sigma_var, width=10)
        self.sigma_entry.grid(column=1, row=1)
        
        ttk.Label(self.control_frame, text="t value:").grid(column=2, row=1)
        self.t_var = tk.DoubleVar(value=14.0)
        self.t_entry = ttk.Entry(self.control_frame, textvariable=self.t_var, width=10)
        self.t_entry.grid(column=3, row=1)
        
        self.calc_button = ttk.Button(self.control_frame, text="calculate", command=self.calculate_point)
        self.calc_button.grid(column=4, row=1)
        
        self.result_var = tk.StringVar()
        self.result_label = ttk.Label(self.control_frame, textvariable=self.result_var)
        self.result_label.grid(column=0, row=2, columnspan=5)
        
  
        ttk.Separator(self.control_frame, orient=tk.HORIZONTAL).grid(column=0, row=3, columnspan=5, sticky="ew", pady=10)
        ttk.Label(self.control_frame, text="3D Surface Plot Range").grid(column=0, row=4, columnspan=4)
        
        ttk.Label(self.control_frame, text="σ min:").grid(column=0, row=5)
        self.sigma_min_var = tk.DoubleVar(value=-2)
        ttk.Entry(self.control_frame, textvariable=self.sigma_min_var, width=5).grid(column=1, row=5)
        
        ttk.Label(self.control_frame, text="σ max:").grid(column=2, row=5)
        self.sigma_max_var = tk.DoubleVar(value=2)
        ttk.Entry(self.control_frame, textvariable=self.sigma_max_var, width=5).grid(column=3, row=5)
        
        ttk.Label(self.control_frame, text="t min:").grid(column=0, row=6)
        self.t_min_var = tk.DoubleVar(value=-20)
        ttk.Entry(self.control_frame, textvariable=self.t_min_var, width=5).grid(column=1, row=6)
        
        ttk.Label(self.control_frame, text="t max:").grid(column=2, row=6)
        self.t_max_var = tk.DoubleVar(value=20)
        ttk.Entry(self.control_frame, textvariable=self.t_max_var, width=5).grid(column=3, row=6)
        
        ttk.Label(self.control_frame, text="Number of points:").grid(column=0, row=7)
        self.points_var = tk.IntVar(value=30)
        ttk.Entry(self.control_frame, textvariable=self.points_var, width=5).grid(column=1, row=7)
        
        self.plot_button = ttk.Button(self.control_frame, text="Create 3D Graphics", command=self.generate_plot)
        self.plot_button.grid(column=4, row=6)
        

        self.canvas_frame = ttk.Frame(self.plot_frame)
        self.canvas_frame.pack(fill=tk.BOTH, expand=True)
        
        self.fig = plt.figure(figsize=(10, 8))
        self.canvas = FigureCanvasTkAgg(self.fig, master=self.canvas_frame)
        self.canvas.get_tk_widget().pack(fill=tk.BOTH, expand=True)
        

        self.ax = self.fig.add_subplot(111)
        self.ax.text(0.5, 0.5, "Riemann Zeta Function Visualizer\n\nEnter values ​​and click Calculate or Create Graph button", 
                     ha='center', va='center', fontsize=12)
        self.ax.axis('off')
        self.canvas.draw()
        
    def calculate_point(self):
        sigma = self.sigma_var.get()
        t = self.t_var.get()
        
        z, mag, phase = calculate_single_zeta(sigma, t)
        if z is not None:
            result_text = f"ζ({sigma}+{t}i) = {z.real:.6f} + {z.imag:.6f}i\n"
            result_text += f"Büyüklük: |ζ({sigma}+{t}i)| = {mag:.6f}\n"
            result_text += f"Faz: Arg(ζ({sigma}+{t}i)) = {phase:.6f} radyan"
            self.result_var.set(result_text)
        else:
            self.result_var.set("An error occurred while calculating the zeta function value")
    
    def generate_plot(self):
        sigma_min = self.sigma_min_var.get()
        sigma_max = self.sigma_max_var.get()
        t_min = self.t_min_var.get()
        t_max = self.t_max_var.get()
        points = self.points_var.get()
        

        self.fig.clear()

        sigma_grid, t_grid, zeta_values, magnitude, phase = calculate_zeta_grid(
            sigma_min, sigma_max, t_min, t_max, points
        )
        

        ax1 = self.fig.add_subplot(121, projection='3d')
        surf1 = ax1.plot_surface(sigma_grid, t_grid, magnitude, cmap=cm.viridis, 
                           linewidth=0, antialiased=True)
        ax1.set_xlabel('σ (Reel kısım)')
        ax1.set_ylabel('t (Sanal kısım)')
        ax1.set_zlabel('|ζ(s)|')
        ax1.set_title('Büyüklük |ζ(s)|')
        
        ax2 = self.fig.add_subplot(122, projection='3d')
        surf2 = ax2.plot_surface(sigma_grid, t_grid, phase, cmap=cm.hsv, 
                           linewidth=0, antialiased=True)
        ax2.set_xlabel('σ (Reel kısım)')
        ax2.set_ylabel('t (Sanal kısım)')
        ax2.set_zlabel('Arg(ζ(s))')
        ax2.set_title('Faz Arg(ζ(s))')
        
        self.fig.tight_layout()
        self.canvas.draw()

# Ana giriş noktası
def main():
    root = tk.Tk()
    app = RiemannZetaApp(root)
    root.mainloop()

if __name__ == "__main__":
    main()
