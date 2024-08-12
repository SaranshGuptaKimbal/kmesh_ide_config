# Installation

 1. Create a folder named .vscode inside the kimbal_workspace/kmesh folder
 2. Clone the repo inside the folder

# Usage

 1. Open the Kmesh folder in VScode.
 2. Open the Run and Debug panel
 3. Select the desired configuration from the drop down menu

Note: Intellisense for the project will not work properly unless the build task for the project has been executed for some target.

# settings.json
The file .vscode/settings.json contains variables for the configuration. 

 - zephyr.applicationPath: Change this to specify which application to build and run. Rerun the build configuration after changing this
 - zephyr.board: Specifies board name. Irrelevant if you are using qemu or native_sim
 - zephyr.prevCommand: If you are using the python virtual environment as shown in the zephyr Getting Started guide, leave this variable as is. If not, set the variable to "";
