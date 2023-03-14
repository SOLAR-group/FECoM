import dill
import requests
from config import URL, DEBUG
from function_details import FunctionDetails
import sys
sys.path.insert(0,'..')
import os
import traceback
import time

import json
import concurrent.futures


def store_response(response):
    if DEBUG:
        print(f"Result: {response}")

    try:
        if os.path.exists('/home/saurabh/code-energy-consumption/client_agent/methodcall-energy-dataset.json'):
            with open('/home/saurabh/code-energy-consumption/client_agent/methodcall-energy-dataset.json', 'r+') as f:
                file_content = f.read()
                if file_content.strip():
                    existing_data = json.loads(file_content)
                else:
                    existing_data = []
        else:
            existing_data = []
            with open('/home/saurabh/code-energy-consumption/client_agent/methodcall-energy-dataset.json', 'w+') as f:
                f.write(json.dumps(existing_data))
    except Exception as e:
        print(f"Error opening file: {e}")
        return

    if response:
        try:
            data = json.loads(response)
            existing_data.append(data)
            print("Data loaded from response")
            with open('/home/saurabh/code-energy-consumption/client_agent/methodcall-energy-dataset.json', 'w+') as f:
                print("Type of existing data", type(existing_data))
                json_data = json.dumps(existing_data) # Convert to JSON string
                print("Type of json data", type(json_data))
                f.write(json_data)
                print("Data written to file")
        except json.decoder.JSONDecodeError as e:
            print(f"Error decoding JSON: {e}")
        except Exception as e:
            print(f"Error writing JSON to file: {e}")
            print(traceback.format_exc())
    else:
        print("Response content is empty")





# for testing purposes
# TODO how can we best pass the username and password to this function? Write a wrapper?
def send_request(imports: str, function_to_run: str, function_args: list = None, function_kwargs: dict = None, max_wait_secs: int = 0, wait_after_run_secs: int = 0, return_result: bool = False, method_object = None, custom_class: str = None, username: str = "tim9220", password: str = "qQ32XALjF9JqFh!vF3xY"):
    """
        Send a request to execute any function to the server and return specified data.
        If return_result=False, the returned object is JSON of the following format:
        function_to_run: {
            "energy_data": {
                "cpu": df_cpu_json,
                "ram": df_ram_json,
                "gpu": df_gpu_json
            },
            "times": {
                "start_time_server": start_time_server,
                "end_time_server": end_time_server,
                "start_time_perf": start_time_perf, 
                "end_time_perf": end_time_perf,
                "start_time_nvidia": start_time_nvidia_normalised,
                "end_time_nvidia": end_time_nvidia_normalised,
            },
            "input_sizes" {
                "args_size": args_size_bit,
                "kwargs_size": kwargs_size_bit,
                "object_size": object_size_bit
            }
        }
    }
    """
    try:
        
        # (1) Construct a FunctionDetails object containg all the function data & settings for the server
        function_details = FunctionDetails(
            imports,
            function_to_run,
            function_args,
            function_kwargs,
            max_wait_secs,
            wait_after_run_secs,
            return_result,
            method_object,
            custom_class,
            method_object.__module__ if custom_class is not None else None
        )

        if DEBUG:
            print(f"Sending {function_to_run} request to {URL}")
            print("######SIZES######")
            print(f"Data size of function_args: {len(dill.dumps(function_args))}")
            print(f"Data size of function_kwargs: {len(dill.dumps(function_kwargs))}")
            print(f"Data size of method_object: {len(dill.dumps(method_object))}")

        # (2) Serialise data with dill 
        run_data = dill.dumps(function_details)

        # (3) Send the request to the server and wait for the response
        # verify = False because the server uses a self-signed certificate
        # TODO this setting throws a warning, we need to set verify to the trusted certificate path instead.
        # But this didn't work for a self-signed certificate, since a certificate authority (CA) bundle is required
        while True:
            run_resp = requests.post(URL, data=run_data, auth=(username, password), verify=False, headers={'Content-Type': 'application/octet-stream'})
            
            if DEBUG:
                print("RECEIVED RESPONSE")
            # (4) Check whether the server could execute the method successfully
            # if the HTTP status code is 500, the server could not reach a stable state.
            # TODO: now, we simply raise an error and save the energy data. Should we send a new request instead?
            if run_resp.status_code == 500:
                deserialised_response = dill.loads(run_resp.content)
                error_file = "timeout_energy_data.json"
                with open(error_file, 'w') as f:
                    json.dump(deserialised_response["energy_data"], f)
                time.sleep(30)
                continue  # retry the request
                # raise TimeoutError(str(deserialised_response["error"]) + "\nYou can find the energy data in ./" + error_file)
            # catch unauthorized error if authentication fails
            elif run_resp.status_code == 401:
                raise RuntimeError(run_resp.content)
            else:
                print("Successful Server response: " + str(run_resp.status_code))
                # Success, break out of the loop and continue with the rest of the code
                break

        # (5) Extract the relevant data from the response and return it
        if return_result:
            # when return_result is true, data is serialised (used for testing & debugging)
            return dill.loads(run_resp.content)
        else:
            # typically we expect json data
            type
            store_response(run_resp.content)
            return run_resp.json()
    except Exception as e:
        print(f"Error in send_request: {e}")
        print(traceback.format_exc())
        return None