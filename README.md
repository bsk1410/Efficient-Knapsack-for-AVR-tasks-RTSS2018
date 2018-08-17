# Efficient-Knapsack-based-approach-for-AVR-task-Demand

## Table of Contents

* [Features](#features)
* [Quickstart - Quick Evaluation](#quickstart---quick-evaluation)
  * [Option A - Open Virtual Appliance](#option-a---open-virtual-appliance)
  * [Option B - Manual Install - Ubuntu 18.04](#option-b---manual-install---ubuntu-1804)
* [How to Use this Artifact - Getting Started - Basic Evaluation](#how-to-use-this-artifact---getting-started---basic-evaluation)
  * [Evaluation Elements](#evaluation-elements)
  * [Element No.1 - At Least 10 Times Faster - Abstract](#element-no1---at-least-10-times-faster---abstract)
  * [Element No.2 - Average Improvement of 77 Times - Abstract](#element-no2---average-improvement-of-77-times---abstract)
  * [Element No.3 - Task Set Used by Existing Work - Task Set 1 - Table I](#element-no3---task-set-used-by-existing-work---task-set-1---table-i)
  * [Element No.4 - A More General Task Set - Task Set 2 - Table II](#element-no4---a-more-general-task-set---task-set-2---table-ii)
  * [Element No.5 - Runtime Comparison of Different Algorithms - Table III.a](#element-no5---runtime-comparison-of-different-algorithms---table-iiia)
  * [Element No.6 - Runtime Comparison of Different Algorithms - Table III.b](#element-no6---runtime-comparison-of-different-algorithms---table-iiib)
  * [Element No.7 - Runtime Comparison of Different Algorithms - Table III.c](#element-no7---runtime-comparison-of-different-algorithms---table-iiic)
  * [Folder Structure Explanation](#folder-structure-explanation)
* [Customizing Execution (Extended Evaluation)](#customizing-execution--extended-evaluation-)
  * [Editing Custom Task Sets](#editing-custom-task-sets)
    * [Configuring Adaptive-Variable Rate Worst-Case Execution Time Profiles (and Number of Modes)](#configuring-adaptive-variable-rate-worst-case-execution-time-profiles--and-number-of-modes-)
    * [Configuring Right Boundary Speed Profiles](#configuring-right-boundary-speed-profiles)
    * [Configuring Acceleration](#configuring-acceleration)
  * [Running Custom Task Sets](#running-custom-task-sets)
    * [Knapsack-Based Demand Calculation](#knapsack-based-demand-calculation)
    * [DRT-Based Demand Calculation](#drt-based-demand-calculation)
* [File-by-File Descriptions](#file-by-file-descriptions)
* [Publication Information](#publication-information)
  * [Research Publication](#research-publication)
  * [Authors & Contact](#authors---contact)
* [Appendix](#appendix)
* [Appendix A - Dependencies](#appendix-a---dependencies)
* [Appendix B - Tested System Specifications](#appendix-b---tested-system-specifications)
  * [Original System - Publication Data](#original-system---publication-data)
  * [OVA Host and Guest Systems](#ova-host-and-guest-systems)
* [Appendix C - OVA Account Information](#appendix-c---ova-account-information)
* [Appendix D - Step-By-Step Installation and Execution](#appendix-d---step-by-step-installation-and-execution)
* [Appendix E: Version Checking](#appendix-e--version-checking)

<small><i><a href='http://ecotrust-canada.github.io/markdown-toc/'>Table of contents generated with markdown-toc</a></i></small>


## Features

- A Python3 implementation of the Knapsack-based demand calculations as found in Bijinemula et al.
- A Python3 implementation of the Digraph Real-Time (DRT) demand calculations as found in [_Refinement of Workload Models for Engine Controllers by State Space Partitioning_](http://user.it.uu.se/~yi/pdf-files/2017/ecrts17.pdf) by Mohaqeqi et al.
- A graphical comparison of the above implementations using matplotlib

## Quickstart - Quick Evaluation

Evaluators are encouraged to:
1. Select a Quickstart Option (A or B)
2. Navigate to the  [How to Use This Artifact](#how-to-use-this-artifact---getting-started---basic-evaluation) for instructions on evaluating all elements

### Option A - Open Virtual Appliance

0. __If not already installed, download and install [Oracle VirtualBox](https://www.virtualbox.org/) from the VirtualBox [downloads page](https://www.virtualbox.org/wiki/Downloads).__.

2. Download the Knapsack AVR Open Virtual Appliance (OVA): [Mirror 1](https://waynestateprod-my.sharepoint.com/:f:/g/personal/ez9213_wayne_edu/Em0cgsbtXSRJs5vxJfcFpeAB-LUFyp5K6H0cxSClSs6Syg?e=NJsR2H), [Mirror 2](https://drive.google.com/drive/folders/1guxYVvrhUcTXSJjurjI1SzDScWlTfgQE?usp=sharing), [Mirror 3](https://drive.google.com/drive/folders/110dwYOQ2a_2hlBj0471JiFwSE_Fzc2Uf?usp=sharing).

3. Import the OVA by opening __VirtualBox__, selecting __File > Import Appliance__, browsing to the _Knapsack-Based Approach Worst-Case AVR Demand.OVA_ file, and following on-screen instructions. Step-by-step import instructions can be found in Oracle's VirtualBox [documentation](https://docs.oracle.com/cd/E26217_01/E26796/html/qs-import-vm.html).

4. __Start__ the newly imported _Knapsack-Based Approach Worst-Case AVR Demand_ virtual machine.

5. _Open_ the _Efficient-Knapsack-for-AVR-tasks-RTSS2018_ folder on the _Desktop_.

6. __Right click the whitespace__ and select __Open in Terminal__.

7. In the terminal, __enter__:

    ```sh
    python3 runAll.py
    ```

8. Upon completion, a graph of algorithm runtime vs number of modes will display. This graph can be compared with the results resented in [Bijinemula et al.](https://waynestateprod-my.sharepoint.com/:f:/g/personal/ez9213_wayne_edu/Em0cgsbtXSRJs5vxJfcFpeAB-LUFyp5K6H0cxSClSs6Syg?e=NJsR2H)

_Note: Completion time for __one run__ (the default) may take at least __7 minutes__ for the Knapsack-Based algorithm and __15.8 hours__ for the DRT-based algorithm under __[Tested System Specifications](#tested-system-specifications)__._

### Option B - Manual Install - Ubuntu 18.04

1. Navigate to the desired cloning directory and execute the following script in the terminal:

    ```sh
    sudo apt-get update &&
    sudo apt-get install git python3 python3-pip python3-tk && pip3 install -U numpy matplotlib && git clone https://github.com/bsk1410/Efficient-Knapsack-for-AVR-tasks-RTSS2018.git && cd Efficient-Knapsack-for-AVR-tasks-RTSS2018 && python3 runAll.py
    ```

2. Upon completion, a graph of algorithm runtime vs number of modes will display. This graph can be compared with the results resented in [Bijinemula et al.](https://waynestateprod-my.sharepoint.com/:f:/g/personal/ez9213_wayne_edu/Em0cgsbtXSRJs5vxJfcFpeAB-LUFyp5K6H0cxSClSs6Syg?e=NJsR2H)

_Note: Completion time for __one run__ (the default) may take at least __7 minutes__ for the Knapsack-Based algorithm and __15.8 hours__ for the DRT-based algorithm under __[Tested System Specifications](#tested-system-specifications)__._

## How to Use this Artifact - Getting Started - Basic Evaluation

This artifact serves as a demonstration of repeatability for claims, tables, and figures provided in the RTSS 2018 publication _An Efficient Knapsack-Based Approach for Calculating the Worst-Case Demand of AVR Tasks_ by Bijinemula et al. (Accepted).

### Evaluation Elements

Important claims, figures, and tables in the paper which can be reproduced and validated with this artifact include:

1. The knapsack approach, "is at least 10 times faster" - Abstract
2. The knapsack approach has, "an average improvement of 77 times when compared with the state-of-the-art technique - Abstract
3. Task Set Used by Existing Work (Task Set #1) - Table I
4. A More General Task Set (Task Set #2) - Table II
5. Runtime Comparison of Different Algorithms - Table III.a
6. Runtime Comparison of Different Algorithms - Table III.b
7. Runtime Comparison of Different Algorithms - Table III.c

The remaining sections will guide evaluators through evaluating each claim independent of installation method.

### Element No.1 - At Least 10 Times Faster - Abstract

### Element No.2 - Average Improvement of 77 Times - Abstract

### Element No.3 - Task Set Used by Existing Work - Task Set 1 - Table I

1. Navigate to the root folder of the cloned repository (the desktop folder if using the OVA) and, in the terminal, __enter__:

    ```sh
    cat taskSet1.json
    ```

2. The file displayed is the json encoding of the Table I data, "Task Set Used by Existing Work".

3. To execute this task set for runtime comparison, see Element No.5: Runtime Comparison of Different Algorithms - Table III.a

### Element No.4 - A More General Task Set - Task Set 2 - Table II

1. Navigate to the root folder of the cloned repository (the desktop folder if using the OVA) and, in the terminal, __enter__:

    ```sh
    cat taskSet2.json
    ```

2. The file displayed is the json encoding of the Table II data, "A more general task set".

3. To execute this task set for runtime comparison, see Element No.6: Runtime Comparison of Different Algorithms - Table III.b

### Element No.5 - Runtime Comparison of Different Algorithms - Table III.a

1. Navigate to the root folder of the cloned repository (the desktop folder if using the OVA) and, in the terminal, __enter__:

    ```sh
    python3 NewAlg.py -t 1
    ```

    This will execute the Knapsack-based algorithm on the Table I Task Set - "Task Set Used by Existing Work". The time to compute the demand will display in the terminal.

2. When the above execution is completed, in the terminal __enter__:

    ```sh
    python3 DRTAlg.py -t 1
    ```

    This will execute the Knapsack-based algorithm on the Table I Task Set - "Task Set Used by Existing Work". The time to compute the demand will display in the terminal

3. To validate the demand calculations, we can view the last lines of the log files `NewAlgOutput.txt` and `DRTAlgOutput.txt`. In the terminal __enter__:

    ```sh
    tail -l NewAlgOutput.txt
    ```

    and

    ```sh
    tail -l DRTAlgOutput.txt
    ```

    The calculated maximum demands should be the same.

4. To view the entire log file for each algorithm's execution, in the terminal __enter__:

    ```sh
    cat NewAlgOutput.txt
    ```

    and

    ```sh
    cat DRTAlgOutput.txt
    ```

### Element No.6 - Runtime Comparison of Different Algorithms - Table III.b

1. Repeat the steps for Claim #5 replacing the parameter `-t 1` with `-t 2` in steps 1. and 2.

2. Repating the steps for Claim #5 replacing the parameter `-t 1` with `-t 2` will execute the Knapsack and DRT-based algorithms on the Table II Task Set - "A more general task set". The time to compute the demand will display in the terminal.

### Element No.7 - Runtime Comparison of Different Algorithms - Table III.c

1. Navigate to the root folder of the cloned repository (the desktop folder if using the OVA) and, in the terminal, __enter__:

    ```sh
    python3 runAll.py
    ```
2. Upon completion, a graph of algorithm runtime vs number of modes will display. This graph can be compared with the results resented in [Bijinemula et al.](https://waynestateprod-my.sharepoint.com/:f:/g/personal/ez9213_wayne_edu/Em0cgsbtXSRJs5vxJfcFpeAB-LUFyp5K6H0cxSClSs6Syg?e=NJsR2H)

To run the default tests, follow the instructions in the [Quick Start / Quick Evaluation](#quickstart--quick-evaluation) section

### Folder Structure Explanation

```
Efficient-Knapsack-For-AVR-Tasks-RTSS2018
├── diffInFiles.py                  Script for step-by-step DRT/Knapsack Comparison 
├── DRTAlgOutput.txt                Output of DRTAlg.py
├── DRTAlg.py                       DRT-Based Demand Calculation
├── DRTMultiAVROutputs              Directory for DRTMultiAVR.py outputs
│   └── DRTAlg_MultiAVR_XX.txt          Example DRTMultiAVR.py output with XX modes
├── DRTMultiAVR.py                  Multi-Run DRT-Based Demand Calculation
├── README.md                       README
├── NewAlgOutput.txt                Output of NewAlg.py
├── NewAlg.py                       Knapsack-Based Demand Calculation
├── NewMultiAVROutputs              Directory for NewMultiAVR.py outputs
│   └── NewAlg_Multi_XX.txt             Example DRTMultiAVR.py output with XX modes
├── NewMultiAVR.py                  Multi-Run Knapsack-Based Demand Calculation
├── plotGraphs.py                   DRT and Knapsack Runtime vs Mode Comparison Graph Plotter
├── pubData                         Raw Publication Data 
│   ├── DRTAlgMultiAVRPubTests          DRT-Based Demand Calculation Run Data
│   └── NewAlgMultipleAVRPubTests       Knapsack-Based Demand Calculation Run Data
├── requirements.txt                
├── runAll.py                       Script for autorunning and graphing algorithm runtimes
├── taskSet1.json                   Publication Task Set 1
├── taskSet2.json                   Publication Task Set 2
└── taskSetCustom.json              Custom, User-Defined Task Set
```
## Customizing Execution (Extended Evaluation)

### Editing Custom Task Sets

1. To __view__ the current task set, navigate to the root folder of the cloned repository (the desktop folder if using the OVA) and, in the terminal, __enter__:

    ```sh
    cat taskSetCustom.json
    ```
    
    Example:

    ```json
    {
	"boundarySpeeds": [500, 1500, 2500, 3500, 4500, 5500, 6500], 
	"executionTimes": [965, 576, 424, 343, 277, 246], 
	"a_max": 600000
    }
    ```

#### Configuring Adaptive-Variable Rate Worst-Case Execution Time Profiles (and Number of Modes)

An Adaptive Variable Rate (AVR) Worst-Case Execution Times (WCET) profile specifies WCETs for the speed ranges between right boundaries.

1. To __edit__ the execution times, use a command line editor (like `nano` or `vi`) or graphical editor (like _gedit_ if using the OVA) to change the  `taskSetCustom.json` file. Edit __line 3 - Execution Times__. Example:

    ```sh
    "executionTimes": [965, 576, 424, 343, 277, 246]
    ```

    ...and replace the default execution times with your own.

    _Note: Execution times are in microseconds. The number of items in `"executionTimes"` is the __number of modes__. There must be __one less WCET__ than `"boundarySpeeds"` - to edit `"boundarySpeeds"`, see below._

#### Configuring Right Boundary Speed Profiles

1. To __edit__ the right boundary speeds, use a command line editor (like `nano` or `vi`) or graphical editor (like _gedit_ if using the OVA) to change the  `taskSetCustom.json` file. Edit __line 2 - Boundary Speeds__. Example:

    ```sh
    "boundarySpeeds": [500, 1500, 2500, 3500, 4500, 5500, 6500],
    ```

    ...and replace the default right boundary speeds with your own.

    _Note: Right boundary speeds are in revolutions / minute. There must be __one more element in `"boundarySpeeds"` than in `"executionTimes"`__._

#### Configuring Acceleration

1. To __edit__ the acceleration, use a command line editor (like `nano` or `vi`) or graphical editor (like _gedit_ if using the OVA) to change the  `taskSetCustom.json` file. Edit __line 4 - Acceleration__. Example:

    ```sh
    "a_max": 600000
    ```

    ...and replace the default acceleration with your own.

    _Note: Acceleration is in revolutions / minute^2. Minimum acceleration `a_min` is not listed as `a_max` must be equal in magnitude (but opposite in direction) to `a_max`_.

### Running Custom Task Sets

#### Knapsack-Based Demand Calculation

1. To execute the Knapsack-Based Demand Calculation on the custom task set, navigate to the root folder of the cloned repository (the desktop folder if using the OVA) and, in the terminal, __enter__:

    ```sh
    python3 NewAlg.py -t 3
    ```

  The `-t 3` parameter specifies execution with the taskset parameters in `taskSetCustom.json`.

2. Upon completion, the running time will be printed in the terminal.
3. To view the calculated demand, in the terminal, __enter__:

    ```sh
    tail -l NewAlgOutput.txt
    ```
4. To view the entire demand calculation log, in the terminal, __enter__:

    ```sh
    cat NewAlgOutput.txt
    ```

#### DRT-Based Demand Calculation

- To execute the Knapsack-Based Demand Calculation on the custom task set, repeat steps 1-4 above for [Knapsack-Based Demand Calculation](#Knapsack-Based-Demand-Calculation) replacing __`NewAlg.py`__ with __`DRTAlg.py`__ and __`NewAlgOutput.txt`__ with __`DRTAlgOutput.txt`__.  

## File-by-File Descriptions

## Publication Information

### Research Publication

_An Efficient Knapsack-Based Approach for Calculating the Worst-Case Demand of AVR Tasks_ by Bijinemula et al. (Accepted)  
Real-Time Systems Symposium ([RTSS](http://2018.rtss.org/)) 2018 - Main Real-Time Track  
Nashville, Tennessee, USA

### Authors & Contact

| Author | Department | University | Location | Email |
| ------ | ---------- | ---------- | -------- | ----- |
| Sandeep Kumar Bijinemula | Electrical and Computer Engineering | [Virginia Tech](https://vt.edu/index.html) | Arlington, USA | bsk1410@vt.edu |
| [Aaron Willcock](https://www.linkedin.com/in/aaronwillcock/) | Computer Science | [Wayne State University](https://wayne.edu/) | Detroit, USA | aaron.willcock@wayne.edu |
| [Thidapat Chantem](https://ece.vt.edu/people/profile/chantem) | Electrical and Computer Engineering | [Virginia Tech](https://vt.edu/index.html) | Arlington, USA | tchantem@vt.edu |
| [Nathan Fisher](https://engineering.wayne.edu/profile/dx3281) | Computer Science | [Wayne State University](https://wayne.edu/) | Detroit, USA | fishern@wayne.edu |

## Appendix

## Appendix A - Dependencies

| Link | Version Tested |
| ------ | ----------- |
| [Python3](https://www.python.org/) | 3.6.5 |
| [pip](https://pypi.org/project/pip/) | 9.0.1 |
| [NumPy](http://www.numpy.org/) | 1.13.3 |
| [matplotlib](https://matplotlib.org/api/pyplot_summary.html) | 2.2.3 |
| [tkinter](https://wiki.python.org/moin/TkInter) | 8.6 |

## Appendix B - Tested System Specifications

The following section describes system specifications for all systems (virtual and real) used in the creation of this artifact, publication data, and virtual appliance. 

### Original System - Publication Data

The data displayed in the RTSS 2018 publication can be found in the `pubData/` folder. This data was obtained by running on a system with the following specifications:

| Property | Description |
| ------ | ----------- |
| OS | Ubuntu 18.04 LTS |
| Arch | 64-bit |
| CPU | Intel Core i7-6700 CPU @ 3.40 GHz x 8 |
| RAM | 8GB (7.7GB Available) |

### OVA Host and Guest Systems

The OVA for use by the RTSS 2018 Artifact Evaluation Committee and the public was created and tested with the following system specifications:

| Host Property | Description |
| ------ | ----------- |
| OS | Ubuntu 18.04 LTS |
| Arch | 64-bit |
| CPU | Intel Core i7-6700HQ CPU @ 2.60GHz __× 8__ |
| RAM | __16GB (15.7GB Available)__ |

<br>

| Guest Property | Description |
| ------ | ----------- |
| OS | Ubuntu 18.04 LTS |
| Arch | 64-bit |
| CPU | Intel Core i7-6700HQ CPU @ 2.60GHz __× 4__ |
| RAM | __8GB (7.8GB Available)__ |

## Appendix C - OVA Account Information

```sh
Login:      knapsackavr
Password:   RTSS2018
```

## Appendix D - Step-By-Step Installation and Execution

1. Installing [git](https://git-scm.com/) [[1](https://www.digitalocean.com/community/tutorials/how-to-install-git-on-ubuntu-14-04)]:

    ```sh
    sudo apt-get install git
    ```

2. Installing [Python3](https://www.python.org/) [[2](https://askubuntu.com/questions/798123/how-do-i-install-python-3-5-2)]:

    ```sh
    sudo apt-get update
    sudo apt-get install python3
    ```

3. Installing [pip](https://pypi.org/project/pip/) [[3](https://askubuntu.com/questions/748929/no-module-named-numpy)]:

    ```sh
    sudo apt-get install python-pip python3-pip
    ```

4. Installing [Tkinter](https://wiki.python.org/moin/TkInter) [[4](https://stackoverflow.com/questions/4783810/install-tkinter-for-python)]:

    ```sh
    sudo apt-get install python3-tk
    ```

5. Installing [NumPy](http://www.numpy.org/) via pip [[3](https://askubuntu.com/questions/748929/no-module-named-numpy)]:

    ```sh
    sudo pip3 install -U numpy
    ```

6. Installing [matplotlib](https://matplotlib.org/api/pyplot_summary.html) via pip [[5](https://matplotlib.org/users/installing.html)]:

    ```sh
    sudo pip3 install -U matplotlib
    ```

7. Clone the git repo:

    ```sh
    git clone https://github.com/bsk1410/Efficient-Knapsack-for-AVR-tasks-RTSS2018.git
    ```

8. Navigate to the git repo:

    ```sh
    cd Efficient-Knapsack-for-AVR-tasks-RTSS2018
    ```

9. Run the default script:

    ```sh
    python3 runAll.py
    ```

10. Upon completion, a graph of algorithm runtime vs number of modes will display. This graph can be compared with the results resented in [Bijinemula et al.](https://waynestateprod-my.sharepoint.com/:f:/g/personal/ez9213_wayne_edu/Em0cgsbtXSRJs5vxJfcFpeAB-LUFyp5K6H0cxSClSs6Syg?e=NJsR2H)

[[1](https://www.digitalocean.com/community/tutorials/how-to-install-git-on-ubuntu-14-04)] [https://www.digitalocean.com/community/tutorials/how-to-install-git-on-ubuntu-14-04](https://www.digitalocean.com/community/tutorials/how-to-install-git-on-ubuntu-14-04)  
[[2](https://askubuntu.com/questions/798123/how-do-i-install-python-3-5-2)] [https://askubuntu.com/questions/798123/how-do-i-install-python-3-5-2](https://askubuntu.com/questions/798123/how-do-i-install-python-3-5-2)  
[[3](https://askubuntu.com/questions/748929/no-module-named-numpy)]  [https://askubuntu.com/questions/748929/no-module-named-numpy](https://askubuntu.com/questions/748929/no-module-named-numpy)  
[[4](https://stackoverflow.com/questions/4783810/install-tkinter-for-python)] [https://stackoverflow.com/questions/4783810/install-tkinter-for-python](https://stackoverflow.com/questions/4783810/install-tkinter-for-python)  
[[5](https://matplotlib.org/users/installing.html)] [https://matplotlib.org/users/installing.html](https://matplotlib.org/users/installing.html)  

## Appendix E: Version Checking

Checking [Python3](https://www.python.org/) version [[6](https://askubuntu.com/questions/505081/what-version-of-python-do-i-have)]:

```sh
python3 --version
```

Checking [NumPy](http://www.numpy.org/) version in python3 [[7](https://stackoverflow.com/questions/1a520234/how-do-i-check-which-version-of-numpy-im-using)]:

```python3
>>>import numpy
>>>numpy.version.version
```

Checking [tkinter](https://wiki.python.org/moin/TkInter) version in python3 [[8](https://stackoverflow.com/questions/35999344/how-to-determine-what-version-of-python3-tkinter-is-installed-on-my-linux-machin)]:

```python3
>>> import tkinter
>>> tkinter.TkVersion
```

Checking [matplotlib](https://matplotlib.org/api/pyplot_summary.html) version in python3 [[9](https://stackoverflow.com/questions/21473600/matplotlib-version)]:

```python3
>>>import matplotlib
>>>print('matplotlib: {}'.format(matplotlib.__version__))
```

[[6](https://askubuntu.com/questions/505081/what-version-of-python-do-i-have)] [https://askubuntu.com/questions/505081/what-version-of-python-do-i-have](https://askubuntu.com/questions/505081/what-version-of-python-do-i-have)  
[[7](https://stackoverflow.com/questions/1a520234/how-do-i-check-which-version-of-numpy-im-using)] [https://stackoverflow.com/questions/1a520234/how-do-i-check-which-version-of-numpy-im-using](https://stackoverflow.com/questions/1a520234/how-do-i-check-which-version-of-numpy-im-using)  
[[8](https://stackoverflow.com/questions/35999344/how-to-determine-what-version-of-python3-tkinter-is-installed-on-my-linux-machin)] [https://stackoverflow.com/questions/35999344/how-to-determine-what-version-of-python3-tkinter-is-installed-on-my-linux-machin](https://stackoverflow.com/questions/35999344/how-to-determine-what-version-of-python3-tkinter-is-installed-on-my-linux-machin)  
[[9](https://stackoverflow.com/questions/21473600/matplotlib-version)] [https://stackoverflow.com/questions/21473600/matplotlib-version](https://stackoverflow.com/questions/21473600/matplotlib-version)