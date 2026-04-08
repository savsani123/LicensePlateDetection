@echo off
setlocal ENABLEDELAYEDEXPANSION

echo ================================
echo Setting up Python environment
echo ================================

REM Move to py directory
cd py || (
  echo ERROR: py directory not found
  exit /b 1
)

REM Step 1: Create .venv if it doesn't exist
if not exist .venv (
  echo Creating virtual environment...
  py -3.10 -m venv .venv
) else (
  echo Virtual environment already exists
)

REM Step 2: Activate .venv
echo Activating virtual environment...
call .venv\Scripts\activate.bat || (
  echo ERROR: Failed to activate virtual environment
  exit /b 1
)

REM Step 3: Upgrade pip
echo Upgrading pip...
python -m pip install --upgrade pip

REM Step 4: Install dependencies from local wheel cache
echo Installing requirements from wheelfiles...
pip install --no-index --find-links=../../wheelfiles -r requirements.txt || (
  echo ERROR: Failed to install requirements
  exit /b 1
)

REM Step 5: Install LicensePlateDetectionInference wheel
echo Installing LicensePlateDetectionInference...
pip install LicensePlateDetectionInference-0.0.1-py3-none-any.whl || (
  echo ERROR: Failed to install LicensePlateDetectionInference
  exit /b 1
)

REM Step 6: Move back and run the executor
cd .. || (
  echo ERROR: Failed to move to project root
  exit /b 1
)

echo Running PythonModelExecutor.py...
python PythonModelExecutor.py

echo ================================
echo Environment setup complete
echo ================================

endlocal