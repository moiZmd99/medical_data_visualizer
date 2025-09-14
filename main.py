from medical_data_visualizer import draw_cat_plot, draw_heat_map
import matplotlib.pyplot as plt

def main():
    cat_fig = draw_cat_plot()
    cat_fig.suptitle("Categorical Plot of Medical Data", fontsize=16)
    plt.show()

    heat_fig = draw_heat_map()
    plt.title("Correlation Heatmap of Medical Data", fontsize=16)
    plt.show()

if __name__ == "__main__":
    main()
