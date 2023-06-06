"""
An Experiment contains the logic needed to run one kind of experiment for one specific project on the server.

"""

import subprocess, os
from abc import ABC, abstractmethod
from pathlib import Path
from enum import Enum

# TODO adopt project-level experiments for local execution
# from tool.measurement.send_request import send_request_with_func_details as send_request
# from tool.measurement.function_details import FunctionDetails, build_function_details


class ExperimentKinds(Enum):
    METHOD_LEVEL = "method-level"
    PROJECT_LEVEL = "project-level"
    DATA_SIZE = "data-size"


def format_full_output_dir(output_dir: Path, experiment_kind: str, project: str):
    """
    returns the path output_dir/experiment_kind/project
    """
    return output_dir / experiment_kind / project


def format_output_file(output_dir: Path, experiment_number: int):
    return output_dir / f"experiment-{experiment_number}.json"


# base class that any Experiment subclass must implement
# if there is shared code between experiments we can add it here as a method
class Experiment(ABC):
    def __init__(self, experiment_kind: ExperimentKinds, project: str, output_dir: Path):
        """
        args:
        - experiment_kind specifies the kind of experiment (e.g. ExperimentKinds.METHOD_LEVEL)
        - project is a string in the form "category/project_name"
        - output_dir should most likely be set to patching_config.EXPERIMENT_DIR
        """
        self.experiment_kind = experiment_kind
        self.number = None
        self.project = project
        self.__output_dir = format_full_output_dir(output_dir, experiment_kind.value, project)
    
    # the output files are always in the same format, so this general formatter should work for any Experiment
    @property
    def output_file(self) -> Path:
        if self.number is None:
            raise ValueError("Experiment number is None, but is expected to be a positive integer.")
        return format_output_file(self.__output_dir, self.number)
    
    # this method must update self.number to be equal to exp_number
    @abstractmethod
    def run(self, exp_number: int):
        pass


class PatchedExperiment(Experiment):
    def __init__(self, experiment_kind: ExperimentKinds, project: str, experiment_dir: Path, code_dir: Path):
        """
        See Experiment for more info on args.
        code_dir should most likely be set to patching_config.CODE_DIR
        """
        
        # only method-level or project-level experiments are PatchedExperiments
        assert (experiment_kind == ExperimentKinds.METHOD_LEVEL) or (experiment_kind == ExperimentKinds.PROJECT_LEVEL)
        
        super().__init__(experiment_kind, project, experiment_dir)
        self.__code_file = code_dir / f"{self.project}_{experiment_kind}.py"

    def run(self, exp_number):
        self.number = exp_number
        with subprocess.Popen(['python', self.__code_file, str(self.number), str(self.project)], stdout=subprocess.PIPE, stderr=subprocess.PIPE, bufsize=1, universal_newlines=True) as p:
            for line in p.stdout:
                print(line, end='')
            for line in p.stderr:
                print(line, end='')  # Print error output to console
        return


class DataSizeExperiment(Experiment):
    # TODO make it clear that n_runs is the theoretical number of runs, which is smaller when start_at > 1
    # TODO adopt to local execution
    def __init__(self, project: str, experiment_dir: Path, n_runs: int, function_details, vary_args: list, start_at: int = 1):
        # raise NotImplementedError("This experiment has not been tested yet")
        """
        args:
            - n_runs (int): the total number of runs per experiment
            - function_details (FunctionDetails): a fully configured FunctionDetails object, containig all details necessary for executing a function on the server
            - vary_size_of (list[str]): a list the args of a FunctionDetails object, which are numpy arrays and the size of which should be varied.
            - start_at (int) (optional): if specified, this should be a number between 1 and n_runs, and the run() method will start at this number instead of at 1.
        """
        super().__init__(ExperimentKinds.DATA_SIZE, project, experiment_dir)
        assert start_at > 0 and start_at <= n_runs
        self.n_runs = n_runs
        self.start_at = start_at
        self.function_details = function_details
        self.vary_args = vary_args
    
    def run(self, exp_number):
        self.number = exp_number

        # start with run 1, such that the fraction is never 0
        for run in range(self.start_at, self.n_runs+1):
            fraction = run / self.n_runs
            print(f"Begin run [{run}] with data size {fraction} of original")

            self.function_details.args = self.vary_arg_sizes(fraction)
            # TODO adopt to local execution
            # send_request(
            #     function_details = self.function_details,
            #     experiment_file_path= self.output_file
            # )

    def vary_arg_sizes(self, fraction: float) -> list:
        """
        fraction must be between 0 and 1!
        E.g. if an arg in vary_args has shape (100,10,10) and fraction=0.5, return an array of shape (50,10,10).
        So this method only scales the first dimension of the array by the given fraction.
        """
        return [arg[:int(arg.shape[0]*fraction)] for arg in self.vary_args]