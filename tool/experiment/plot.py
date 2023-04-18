import matplotlib.pyplot as plt
import matplotlib.lines as mlines
import matplotlib.patches as mpatches
import pandas as pd

from tool.experiment.data import EnergyData


def get_perf_times(energy_data: EnergyData) -> list:
    """
    Helper method for format_ax_cpu and format_ax_ram.
    perf_times and gpu_times (see format_ax_gpu) are lists of tuples in the format (time, label, color, style), where
    - time (float, seconds) is the time relative to the start of perf/nvidia (exact times can be found in START_TIMES_FILE)
    - label (str) is a description of this time
    - color (str) is a matplotlib color, e.g. 'r','b','g'
    - style (str|tuple) is a matplotlib line style, e.g. 'dashed' or (0, (1, 10))
    """
    perf_times = [
        (energy_data.start_time_perf, "method_start", 'r', 'dashed'),
        (energy_data.end_time_perf, "method_end", 'r', 'solid'),
        (energy_data.pickle_load_time_perf, "pickle_load", 'b', 'solid'),
        (energy_data.import_time_perf, "import", 'g', 'dotted'),
        (energy_data.begin_stable_check_time_perf, "stable_check", 'y', 'dashed'),
        (energy_data.begin_temperature_check_time_perf, "temperature_check", 'c', (0, (1, 10)))
    ]
    return perf_times


def format_ax_cpu(energy_data: EnergyData, ax: plt.Axes):
    """
    Populate the given Axes object with CPU energy data needed for plotting energy consumption over time,
    including markers for the key times.
    """
    cpu_times = get_perf_times(energy_data)
    cpu_times.append(
        (energy_data.lag_end_time_cpu, "lag_end", 'm', 'dotted')
    )

    ax.set_title("CPU Energy over time")
    ax.plot(energy_data.cpu_energy["time_elapsed"], energy_data.cpu_energy["energy (J)"])
    ax_legend_handles = []
    for time, label, color, linestyle in cpu_times:
        ax.axvline(x=time, color=color, linewidth=1,linestyle=linestyle, alpha=0.7)
        ax_legend_handles.append(mlines.Line2D([], [], color=color, label=label, linestyle=linestyle))
    ax.legend(handles=ax_legend_handles, loc="upper left")

    return ax


def format_ax_ram(energy_data: EnergyData, ax: plt.Axes):
    """
    Populate the given Axes object with RAM energy data needed for plotting energy consumption over time,
    including markers for the key times.
    """
    ram_times = get_perf_times(energy_data)
    ram_times.append(
        (energy_data.lag_end_time_ram, "lag_end", 'm', 'dotted')
    )

    ax.set_title("RAM Energy over time")
    ax.plot(energy_data.ram_energy["time_elapsed"], energy_data.ram_energy["energy (J)"])
    ax_legend_handles = []
    for time, label, color, linestyle in ram_times:
        ax.axvline(x=time, color=color, linewidth=1, linestyle=linestyle, alpha=0.7)
        ax_legend_handles.append(mlines.Line2D([], [], color=color, label=label, linestyle=linestyle))
    ax.legend(handles=ax_legend_handles, loc="upper left")

    return ax


def format_ax_gpu(energy_data: EnergyData, ax: plt.Axes):
    gpu_times = [
        (energy_data.start_time_nvidia, "method_start", 'r', 'dashed'),
        (energy_data.end_time_nvidia, "method_end", 'r', 'solid'),
        (energy_data.pickle_load_time_nvidia, "pickle_load", 'b', 'solid'),
        (energy_data.import_time_nvidia, "import", 'g', 'dotted'),
        (energy_data.begin_stable_check_time_nvidia, "stable_check", 'y', 'dashed'),
        (energy_data.lag_end_time_gpu, "lag_end", 'm', 'dotted'),
        (energy_data.begin_temperature_check_time_nvidia, "temperature_check", 'c', (0, (1, 10)))
    ]

    ax.set_title("GPU Power over time")
    ax.plot(energy_data.gpu_energy["time_elapsed"], energy_data.gpu_energy["power_draw (W)"])
    ax_legend_handles = []
    for time, label, color, linestyle in gpu_times:
        ax.axvline(x=time, color=color, linewidth=1, linestyle=linestyle, alpha=0.7)
        ax_legend_handles.append(mlines.Line2D([], [], color=color, label=label, linestyle=linestyle))
    ax.legend(handles=ax_legend_handles, loc="upper left")


def plot_single_energy_with_times(energy_data: EnergyData, hardware_component: str = "gpu"):
    """
    Given an EnergyData object, create a single plot showing the energy consumption over time
    with key start/end times indicated by lines.
    The hardware_component parameter must be one of "cpu", "ram", "gpu".
    """
    fig, ax = plt.subplots()
    fig.suptitle(f"Data for {energy_data.function_name} from {energy_data.project_name}", fontsize=16)

    ax = eval(f"format_ax_{hardware_component}(energy_data, ax)")

    figure = plt.gcf() # get current figure
    figure.set_size_inches(12, 6)
    plt.savefig('energy_plot.png', dpi=200)

    plt.show()


def plot_energy_with_times(energy_data: EnergyData):
    """
    Given an EnergyData object, create a plot with 3 graphs showing the energy consumption over time
    for CPU, RAM and GPU with start/end times indicated by lines.
    Set one or more of the parameters cpu, ram, gpu to False to exclude it from the graph.
    """

    fig, [ax1, ax2, ax3] = plt.subplots(nrows=1, ncols=3)

    fig.suptitle(f"Data for {energy_data.function_name} from {energy_data.project_name}", fontsize=16)
    
    ax1 = format_ax_cpu(energy_data, ax1)
    ax2 = format_ax_ram(energy_data, ax2)
    ax3 = format_ax_gpu(energy_data, ax3)
    
    # fig.tight_layout()
    
    figure = plt.gcf() # get current figure
    figure.set_size_inches(20, 6)
    plt.savefig('energy_plot.png', dpi=200)

    plt.show()

def plot_combined(energy_data):
    """
    Concatenates the three energy dataframes from the EnergyData object into one containing only energy consumption of each hardware component
    as well as the sum of these three values over time. It does not attempt to merge the perf and nvidia-smi data
    in a way that synchronises the measurements in same rows to be at the same time.
    TODO implement that.
    """
    min_len = min([len(energy_data.gpu_energy), len(energy_data.cpu_energy), len(energy_data.ram_energy)]) - 1
    print(min_len)
    combined_df = pd.concat(
        [
        energy_data.gpu_energy.iloc[:min_len]['power_draw (W)'],
        energy_data.cpu_energy.iloc[:min_len]['energy (J)'],
        energy_data.ram_energy.iloc[:min_len]['energy (J)']
        ],
        axis=1)
    combined_df.columns = ['gpu_power', 'cpu_energy', 'ram_energy']
  
    combined_df['sum'] = combined_df.sum(axis=1)

    print("Combined plot:")
    print(combined_df)
    print("Statistics (stdv, mean):")
    print(combined_df.std())
    print(combined_df.mean())
    combined_df.plot()
    plt.show()