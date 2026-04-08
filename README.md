
# **License Plate Detection – IMIL Inference Module**

License Plate Detection finds the license plate in a vehicle image and marks its position. This helps text‑reading systems accurately read the plate, even in different lighting conditions or camera angles.

---

##  **Project Information**

|  **Section**                   |  **Details**
|--------------------------------|----------------
| **Project name**               | License Plate Detection           
| **Version**                    | 0.1.0            
| **Python Compatibility**       | 3.10              
---

## **Overview**
This package provides a production‑ready **License Plate Detection** inference module built on IMIL.

###  It abstracts:
**Model loading**  
Initializes `LicensePlateDetection` using config entries for WPOD-Net (JSON & weights) and a MobileNets-based character recognition head (JSON & weights), plus character classes; wires them into `LicensePlateDetectionInference`. 

**Pre-processing**  
Takes a base64-encoded input image via `Base_64` and an optional confidence threshold `C_threshold` (`Cs`), passing both—along with any extra `req_data`—directly to `executeModel` of the inference class. 

**Post-processing**  
Merges select request metadata fields (e.g., `Tid`, `Did`, `Fid`, timestamps, versions) into the model result; normalizes keys: `RC`→`Rc`, `RM`→`Rm`; maps `Objects`→`Fs` when `Fs` is absent; and ensures defaults for `Obase_64` and `Img_url`.


##  **Prerequisites**
- git
- python>=3.10

## **Supported Devices**
- CPU, GPU


##  **Folder Structure**
```
|── mil_config.json                       -- configuration setting for model loader class, API and model weight files 
├── SampleInputOutput
      ├── Input.txt                       -- sample Input file for testing
      ├── Output.txt                      -- sample output file for validation
├── modelloader
      ├── base_model_loader.py            -- base model loader class
      ├── licenseplatedetection_model_loader.py                      -- custom model loader class which implements base model loader class
├── ModelInference_wheel_file
      ├── LicensePlateDetectionInference-0.0.1-py3-none-any.whl                           -- contains all dependencies and source code of the model
├── sharedfastapi                         -- API server engine
      ├── api_utils.py
├── milutils                              -- Utility modules folder
├── references
      ├── documentation on working of IMIL
├── milapi                                -- FastAPI integration
      ├── utils.py
      ├── fastapi_caller.py
├── py
      ├── pyproject.toml                  -- describes the dependencies required by the project
      ├── uv.lock                         -- records what in installed 
      ├── LicensePlateDetectionInference-0.0.1-py3-none-any.whl               -- wheel file
├── .gitignore
├── LICENSE
├── README
├── setup_env.bat                         -- batch file for setting up virtual env and installing wheel file
├── Contribution License Agreement        
├── PythonModelExecutor.py                -- main python file

```

## --- STEPS TO RUN THE SOLUTION USING COPILOT ---

### Step 1: Open project repository in same visual studio where copilot is running
      

### Step 2: Download Model Weights

      Download the model weight files from the GitHub repository:
      Link: https://github.com/quangnhat185/Plate_detect_and_recognize/blob/master/
      Save them to your local machine.

### Step 3: Update Configuration File

      Open mil_config.json and update the file path of the model weights under the LicensePlateDetection section.


### Step 4: Commands to RUN (Run each command one after the other)
      - cd py     // go inside the py folder of the project repository
      - uv sync
      - cd .venv\Scripts
      - activate
      - cd ../../../
      - python PythonModelExecutor.py


### Step 5: Open Swagger UI

      Once the service starts, open Swagger in the browser:
      ```
      http://localhost:8448/docs
      ```

### Step 6: Test with Example Data
      
      Use the sample input provided in the SampleInputOutput folder.

### Step 7: Verify Output

      Compare the output from Swagger with the sample output to confirm the model is working correctly.


##  --- STEPS TO USE THE SOLUTION IN MANUAL WAY---

### Step 1: Open Command Prompt
     
      Navigate to the project folder and open command prompt in that location.

### Step 2: Set Up the Virtual Environment

      Run the following script to create and activate the virtual environment:
      ```
      setup_env.bat
      ```

### Step 3: Download Model Weights

      Download the model weight files from the GitHub repository:
      Link: https://github.com/quangnhat185/Plate_detect_and_recognize/blob/master/
      Save them to your local machine.

### Step 4: Update Configuration File

      Open mil_config.json and update the file path of the model weights under the LicensePlateDetection section.

### Step 5: Start the Model Executor:

      Run the Python executor using:
      ```
      python PythonModelExecutor.py
      ```

### Step 6: Open Swagger UI

      Once the service starts, open Swagger in your browser:
      ```
      http://localhost:8448/docs
      ```

### Step 7: Test with Example Data
      
      Use the sample input provided in the SampleInputOutput folder.

### Step 8: Verify Output

      Compare the output from Swagger with the sample output to confirm the model is working correctly.


## Important Output JSON Fields Explained

      Below are the key output fields for this use case.
``` json
      {
  "Fs": [
    {
      "Dm": {					// this field contains bounding box of the vehicle number plate
        "X": 0.419,
        "Y": 0.354,
        "H": 0.129,
        "W": 0.333
      },
      "Lb": "D0T",				// vehicle number plate identified by the model
      "Cs": "",
      "Kp": {},
      "Info": "",
      "Uid": "",
      "Nobj": ""
    }
  ]
}

```

## Schema definition
| Key         | Description                                          | 
|-------------|------------------------------------------------------|
| Tid         | Tenant ID                                            |
| Did         | Device ID                                            | 
| Fid         | Frame ID                                             | 
| Base_64     | Base-64 encoding string of an image                  |
| C_threshold | Confidence threshold value. Data type is float       |
| Per         | Previous frame's metadata                            |
| Mtp         | Message Travel Path                                  | 
| Ts          | Time Stamp                                           |
| Ts_ntp      | NTP Time Stamp                                       | 
| Inf_ver     | Infosys Version                                      | 
| Msg_ver     | Message Version                                      |
| Model       | Name of the Model that is being triggered            |
| Ad          | Additional Parameters                                |
| Ffp         | First Frame passing                                  |   
| Ltsize      | Lot size                                             |
| Lfp         | Last Frame Passing                                   | 
| Fs          | It contains all the predicted output of the model    | 
| Rc          | Response Code. Denotes success or failure code       |
| Rm          | Response Message. Denotes success or failure message |
| I_fn        | Input file name                                      |
| Msk_img     | List of mask images                                  |   
| Rep_img     | Replaces images as a list                            |
| Prompt      | List of text prompts                                 | 
| Img_url     | List of urls of output images                        | 
| Obase_64    | List of output images in base64 format               |




/* Copyright © 2026 Infosys Limited
*
* Licensed under the Apache License, Version 2.0
*/
 
