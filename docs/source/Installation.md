# Installation
First, you need to install Python and Pyomo on your computer.

## Installing Python

1. **Download Python**:
   - Go to the [official Python website](https://www.python.org/downloads/).
   - Download the latest version of Python for your operating system.

2. **Install Python**:
   - Run the downloaded installer.
   - Make sure to check the box that says "Add Python to PATH" during the installation process.
   - Follow the prompts to complete the installation.



## Installing Pyomo

1. **Install Pyomo**:
   - Open a terminal or command prompt.
   - Type the following command and press Enter:
     ```sh
     pip install pyomo
     ```

## GitHub
To clone the code please use the following command from a terminal:

```sh
git clone https://github.com/fsartore/Schedule_MIL_optimization_pyomo.git
```

## Additional Dependencies

Depending on your optimization needs, you might need to install additional solvers. Common solvers include:

- **GLPK (free)**:

- **CBC (free)**:

- **Gurobi (free with academeic license, overall the best)**:

Make sure to install the appropriate solver for your optimization problem. 

You need to install also all the dependencies of the project. You can do this by running the following command from the root directory of the project:

```python
pip install -r requirements.txt
```
## Build the Model

Then you can start build your model:

First, we need to import the necessary libraries.

```python
import pyomo.environ as pyo
```

Then, we can start building the model.

```python
m = pyo.ConcreteModel()
```

