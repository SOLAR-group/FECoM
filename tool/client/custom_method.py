
import sys
from tool.client.client_config import EXPERIMENT_DIR
from tool.server.local_execution import before_execution as before_execution_INSERTED_INTO_SCRIPT
from tool.server.local_execution import after_execution as after_execution_INSERTED_INTO_SCRIPT

experiment_number = sys.argv[1]
experiment_project = sys.argv[2]

EXPERIMENT_FILE_PATH = EXPERIMENT_DIR /'local-execution'/ experiment_project / f'experiment-{experiment_number}.json'

