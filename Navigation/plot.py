from stable_baselines3.common import results_plotter
import os
if __name__ == "__main__":
    results_plotter.plot_results([os.getcwd()+'/buffer_data/4000rewards.csv'],4000,'step',"1",(8,2))