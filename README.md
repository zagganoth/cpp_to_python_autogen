# Run instructions
From a terminal, run  ```py main.py``` (make sure you have autogen installed as a lib through pip, replace 'py' with the appropriate python alias on your system)

# Goal:
Convert C++ code to equivalent python using a series of autonomous agents

# Agents Used:
- User proxy
  - This agent executes code, orchestrates nested chats, and responds with "TERMINATE" otherwise
- Coder
  - This agent is tasked with for generating python code to read a specified file
- CPP_Describer
  - This agent converts C++ code into a series of detailed steps that the code executes
- CPP_Reviewer
  - This agent reads both C++ code and the description provided by CPP_Describer, then provides feedback to CPP_Describer to better describe the output
- Python_Coder:
  - This agent receives both the description and original C++ code and produces equivalent python code
- Python_Reviewer
  - This agent reviews output from Python_Coder to make sure it works and is well designed
 
 
