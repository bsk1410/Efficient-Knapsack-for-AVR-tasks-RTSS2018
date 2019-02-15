# Efficient-Knapsack-based-approach-for-AVR-task-Demand

## Acknowledgments

<table width="100%" style="text-align: center" cellpadding="20">
  <tr>
    <td style="vertical-align:middle">
        <a href="https://www.nsf.gov">
            <img src="https://www.nsf.gov/images/logos/NSF_4-Color_bitmap_Logo.png" alt="NSF" height="100px"/>
        </a>
    </td>
    <td style="vertical-align:middle">
        <a href="https://vt.edu">
            <img src="https://www.assets.cms.vt.edu/images/HorizontalStacked/HorizontalStacked_RGB.svg" height="63px"/>
        </a>
    </td>
    <td style="vertical-align:middle">
        <a href="https://wayne.edu">
            <img src="https://mac.wayne.edu/images/wsu_primary_horz_color.png" height="50px"/>
        </a>
    </td>
  </tr>
</table> 

This research has been supported in part by the [US National
Science  Foundation](https://www.nsf.gov/)  ([CNS](https://www.nsf.gov/div/index.jsp?div=CNS)  Grant  Nos. [1618185](https://nsf.gov/awardsearch/showAward?AWD_ID=1618185) \& [1618979](https://nsf.gov/awardsearch/showAward?AWD_ID=1618979)) and a [Thomas C. Rumble Graduate Fellowship](https://gradschool.wayne.edu/fellowships/rumble-fellowships) from
[Wayne State University](https://wayne.edu).

## Authors - Contact

| Author | Department | University | Location | Email |
| ------ | ---------- | ---------- | -------- | ----- |
| [Sandeep Kumar Bijinemula](https://www.linkedin.com/in/sandeep-bijinemula/) | Electrical and Computer Engineering | [Virginia Tech](https://vt.edu/index.html) | Arlington, VA, USA | bsk1410@vt.edu |
| [Aaron Willcock](https://www.linkedin.com/in/aaronwillcock/) | Computer Science | [Wayne State University](https://wayne.edu/) | Detroit, MI, USA | aaron.willcock@wayne.edu |
| [Thidapat Chantem](https://ece.vt.edu/people/profile/chantem) | Electrical and Computer Engineering | [Virginia Tech](https://vt.edu/index.html) | Arlington, VA, USA | tchantem@vt.edu |
| [Nathan Fisher](https://engineering.wayne.edu/profile/dx3281) | Computer Science | [Wayne State University](https://wayne.edu/) | Detroit, MI, USA | fishern@wayne.edu |

## Table of Contents

* [Acknowledgments](#acknowledgments)
* [Authors - Contact](#authors---contact)
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
  * [Folder and File Structure Explanation](#folder-and-file-structure-explanation)
* [Customizing Execution - Extended Evaluation](#customizing-execution---extended-evaluation)
  * [Editing Custom Task Sets](#editing-custom-task-sets)
    * [Configuring Adaptive-Variable Rate Worst-Case Execution Time Profiles and Number of Modes](#configuring-adaptive-variable-rate-worst-case-execution-time-profiles-and-number-of-modes)
    * [Configuring Right Boundary Speed Profiles](#configuring-right-boundary-speed-profiles)
    * [Configuring Acceleration](#configuring-acceleration)
  * [Running Custom Task Sets](#running-custom-task-sets)
    * [Knapsack-Based Demand Calculation](#knapsack-based-demand-calculation)
    * [DRT-Based Demand Calculation](#drt-based-demand-calculation)
* [File-by-File Description and Operation](#file-by-file-description-and-operation)
  * [diffInFiles.py](#diffinfilespy)
  * [DRTAlgOutput.txt](#drtalgoutputtxt)
  * [DRTAlg.py](#drtalgpy)
  * [DRTMultiAVR.py](#drtmultiavrpy)
  * [README.md](#readmemd)
  * [NewAlgOutput.txt](#newalgoutputtxt)
  * [NewAlg.py](#newalgpy)
  * [NewMultiAVR.py](#newmultiavrpy)
  * [plotGraphs.py](#plotgraphspy)
  * [runAll.py](#runallpy)
  * [taskSet1.json](#taskset1json)
  * [taskSet2.json](#taskset2json)
  * [taskSetCustom.json](#tasksetcustomjson)
* [RTSS 2018 Publication](#rtss-2018-publication)
* [Appendix](#appendix)
* [Appendix A - Dependencies](#appendix-a---dependencies)
* [Appendix B - Tested System Specifications](#appendix-b---tested-system-specifications)
  * [Original System - Publication Data](#original-system---publication-data)
  * [OVA Host and Guest Systems](#ova-host-and-guest-systems)
* [Appendix C - OVA Account Information](#appendix-c---ova-account-information)
* [Appendix D - Step-By-Step Installation and Execution](#appendix-d---step-by-step-installation-and-execution)
* [Appendix E - Version Checking](#appendix-e---version-checking)
* [Appendix F - Known Issues](#appendix-f---known-issues)

<small><i><a href='http://ecotrust-canada.github.io/markdown-toc/'>Table of contents generated with markdown-toc</a></i></small>

## Features

* A Python3 implementation of the Knapsack-based demand calculations as found in [Bijinemula et al](https://waynestateprod-my.sharepoint.com/:f:/g/personal/ez9213_wayne_edu/Em0cgsbtXSRJs5vxJfcFpeAB-LUFyp5K6H0cxSClSs6Syg?e=NJsR2H).
* A Python3 implementation of the Digraph Real-Time (DRT) demand calculations as found in [_Refinement of Workload Models for Engine Controllers by State Space Partitioning_](http://user.it.uu.se/~yi/pdf-files/2017/ecrts17.pdf) by Mohaqeqi et al. This is the most closely related work.
* A graphical comparison of the above implementations using matplotlib

## Quickstart - Quick Evaluation

Evaluators are encouraged to:

1. Select a Quickstart Option (A or B)
2. Navigate to the  [How to Use This Artifact](#how-to-use-this-artifact---getting-started---basic-evaluation) for instructions on evaluating all elements

### Option A - Open Virtual Appliance

1. __If not already installed, download and install [Oracle VirtualBox](https://www.virtualbox.org/) from the VirtualBox [downloads page](https://www.virtualbox.org/wiki/Downloads).__.

2. Download the Knapsack AVR Open Virtual Appliance (OVA): [Mirror 1](https://waynestateprod-my.sharepoint.com/:f:/g/personal/ez9213_wayne_edu/Em0cgsbtXSRJs5vxJfcFpeAB-LUFyp5K6H0cxSClSs6Syg?e=NJsR2H), [Mirror 2](https://drive.google.com/drive/folders/1guxYVvrhUcTXSJjurjI1SzDScWlTfgQE?usp=sharing), [Mirror 3](https://drive.google.com/drive/folders/110dwYOQ2a_2hlBj0471JiFwSE_Fzc2Uf?usp=sharing).

3. Import the OVA by opening __VirtualBox__, selecting __File > Import Appliance__, browsing to the _Knapsack-Based Approach Worst-Case AVR Demand.OVA_ file, and following on-screen instructions. Step-by-step import instructions can be found in Oracle's VirtualBox [documentation](https://docs.oracle.com/cd/E26217_01/E26796/html/qs-import-vm.html).

4. __Start__ the newly imported _Knapsack-Based Approach Worst-Case AVR Demand_ virtual machine.

5. _Open_ the _Efficient-Knapsack-for-AVR-tasks-RTSS2018_ folder on the _Desktop_.

6. __Right click the whitespace__ and select __Open in Terminal__.

7. In the terminal, __enter__:

    ```sh
    git pull
    python3 runAll.py
    ```

8. Upon completion, a graph of algorithm runtime vs number of modes will display. This graph can be compared with the results resented in [Bijinemula et al.](https://waynestateprod-my.sharepoint.com/:f:/g/personal/ez9213_wayne_edu/Em0cgsbtXSRJs5vxJfcFpeAB-LUFyp5K6H0cxSClSs6Syg?e=NJsR2H)

_Note: Completion time for __one run__ (the default) may take at least __16 hours__ under __[Tested System Specifications](#tested-system-specifications)__._

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

1. [The knapsack approach, "is at least 10 times faster" - Abstract](https://github.com/bsk1410/Efficient-Knapsack-for-AVR-tasks-RTSS2018#element-no1---at-least-10-times-faster---abstract)
2. [The knapsack approach has, "an average improvement of 77 times when compared with the state-of-the-art technique - Abstract](https://github.com/bsk1410/Efficient-Knapsack-for-AVR-tasks-RTSS2018#element-no2---average-improvement-of-77-times---abstract)
3. [Task Set Used by Existing Work (Task Set #1) - Table I](https://github.com/bsk1410/Efficient-Knapsack-for-AVR-tasks-RTSS2018#element-no3---task-set-used-by-existing-work---task-set-1---table-i)
4. [A More General Task Set (Task Set #2) - Table II](https://github.com/bsk1410/Efficient-Knapsack-for-AVR-tasks-RTSS2018#element-no4---a-more-general-task-set---task-set-2---table-ii)
5. [Runtime Comparison of Different Algorithms - Table III.a](https://github.com/bsk1410/Efficient-Knapsack-for-AVR-tasks-RTSS2018#element-no5---runtime-comparison-of-different-algorithms---table-iiia)
6. [Runtime Comparison of Different Algorithms - Table III.b](https://github.com/bsk1410/Efficient-Knapsack-for-AVR-tasks-RTSS2018#element-no6---runtime-comparison-of-different-algorithms---table-iiib)
7. [Runtime Comparison of Different Algorithms - Table III.c](https://github.com/bsk1410/Efficient-Knapsack-for-AVR-tasks-RTSS2018#element-no7---runtime-comparison-of-different-algorithms---table-iiic)

The remaining sections will guide evaluators through evaluating each claim independent of installation method.

### Element No.1 - At Least 10 Times Faster - Abstract

1. In the terminal, navigate to the root folder of the cloned repository (the desktop folder if using the OVA) and __enter__:

    ```sh
    python3 runAll.py -r 10
    ```

2. Upon completion, a graph of algorithm runtime vs number of modes will display. This graph can be compared with the results resented in [Bijinemula et al.](https://waynestateprod-my.sharepoint.com/:f:/g/personal/ez9213_wayne_edu/Em0cgsbtXSRJs5vxJfcFpeAB-LUFyp5K6H0cxSClSs6Syg?e=NJsR2H). __The minimum, maximum, and average improvements will display in the terminal.__

    _Warning: Completion time for __one run__ (the default) may take at least __16 hours__ for the DRT-based algorithm under __[Tested System Specifications](#tested-system-specifications)__. Executing the 10 runs in the above script may take __over 160 hours__._

### Element No.2 - Average Improvement of 77 Times - Abstract

1. Repeat the steps in [Element No.1 - At Least 10 Times Faster - Abstract](#element-no1---at-least-10-times-faster---abstract). __The minimum, maximum, and average improvements will display in the terminal.__

### Element No.3 - Task Set Used by Existing Work - Task Set 1 - Table I

1. In the terminal navigate to the root folder of the cloned repository (the desktop folder if using the OVA) and, __enter__:

    ```sh
    cat taskSet1.json
    ```

2. The file displayed is the json encoding of the Table I data, "Task Set Used by Existing Work".

3. To execute this task set for runtime comparison, see [Element No.5: Runtime Comparison of Different Algorithms - Table III.a](https://github.com/bsk1410/Efficient-Knapsack-for-AVR-tasks-RTSS2018#element-no5---runtime-comparison-of-different-algorithms---table-iiia)

### Element No.4 - A More General Task Set - Task Set 2 - Table II

1. In the terminal navigate to the root folder of the cloned repository (the desktop folder if using the OVA) and, __enter__:

    ```sh
    cat taskSet2.json
    ```

2. The file displayed is the json encoding of the Table II data, "A more general task set".

3. To execute this task set for runtime comparison, see [Element No.6: Runtime Comparison of Different Algorithms - Table III.b](https://github.com/bsk1410/Efficient-Knapsack-for-AVR-tasks-RTSS2018#element-no6---runtime-comparison-of-different-algorithms---table-iiib)

### Element No.5 - Runtime Comparison of Different Algorithms - Table III.a

1. In the terminal, navigate to the root folder of the cloned repository (the desktop folder if using the OVA) and __enter__:

    ```sh
    python3 NewAlg.py -t 1 -v
    ```

    This will execute the Knapsack-based algorithm on the Table I Task Set - "Task Set Used by Existing Work". The time to compute the demand will display in the terminal.

2. When the above execution is completed, in the terminal __enter__:

    ```sh
    python3 DRTAlg.py -t 1 -v
    ```

    This will execute the DRT-based algorithm on the Table I Task Set - "Task Set Used by Existing Work". The time to compute the demand will display in the terminal

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

### Folder and File Structure Explanation

```txt
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
├── runAll.py                       Script for autorunning and graphing algorithm runtimes
├── taskSet1.json                   Publication Task Set 1
├── taskSet2.json                   Publication Task Set 2
└── taskSetCustom.json              Custom, User-Defined Task Set
```

## Customizing Execution - Extended Evaluation

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

#### Configuring Adaptive-Variable Rate Worst-Case Execution Time Profiles and Number of Modes

An Adaptive Variable Rate (AVR) Worst-Case Execution Times (WCET) profile specifies WCETs for the speed ranges between right boundaries.

1. To __edit__ the execution times, use a command line editor (like `nano` or `vi`) or graphical editor (like _gedit_ if using the OVA) to change the  `taskSetCustom.json` file. Edit __line 3 - Execution Times__. Example:

    ```sh
    "executionTimes": [965, 576, 424, 343, 277, 246],
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
    python3 NewAlg.py -t 3 -v
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

* To execute the DRT-Based Demand Calculation on the custom task set, repeat steps 1-4 above for [Knapsack-Based Demand Calculation](#Knapsack-Based-Demand-Calculation) replacing __`NewAlg.py`__ with __`DRTAlg.py`__ and __`NewAlgOutput.txt`__ with __`DRTAlgOutput.txt`__.  

## File-by-File Description and Operation

### diffInFiles.py

* Description:

    Python3 script for auto-comparing DRTAlgOutput.txt and NewAlgOutput.txt log files.

* Inputs: None

* Example:

    ```sh
    python3 diffInFiles.py
    ```

* Output:

    Terminal output of differences in log files and number of differences.

### DRTAlgOutput.txt

* Description:

    Output log for DRTAlg.py containing calculated demand and demand update timestamps.

### DRTAlg.py

* Description:

    Python3 script for executing __DRT-based demand calculations__ on one of three task sets.

* Inputs:
  * __-h__ : Help flag for showing detailed help
  * __-t #__ : Task Set Indicator identifying the task set number to use where:
    * 1 - Use Task Set #1 in Bijinemula et al.
    * 2 - Use Task Set #2 in Bijinemula et al.
    * 3 - Use the custom, user-defined task set defined in `taskSetCustom.json`

  * __-v__ : Verbose output flag for generating detailed output logs

* Example:

    The following example completes one run of the __DRT-Based Demand Calculation__ using the __Task Set #2__ in Bijinemula et al. and logs the demand for each time-step in DRTAlgOutput.txt:

    ```sh
    python3 DRTAlg.py -t 2 -v
    ```

* Output:

    If `-v` is entered, the calculated demand and demand update timestamps are logged in `DRTAlgOutput.txt`.
    Runtime is printed to the terminal.

### DRTMultiAVR.py

* Description:

    Python3 script for generating randomized AVR task set with _M_ modes and calculating the demand using __DRT-based calculations__.

    ```sh
    python3 DRTMultiAVR.py M
    ```

* Inputs:

  * __M__ : A positive integer indicating the number of modes the randomized AVR task set has.

* Example:

    The following example completes one run of the __DRT-Based Demand Calculation__ on a randomized AVR task set split into __6__ modes:

    ```sh
    python3 DRTMultiAVR.py 6
    ```

* Output:

    The runtime is logged in __`DRTMultiAVROutputs/DRTAlg_MultiAVR_M.txt`__ where __`M`__ is the number of modes passed in via the command line.

### README.md

* Description:

    README for Efficient-Knapsack-For-AVR-Tasks-RTSS2018 artifact.

### NewAlgOutput.txt

* Description:

    Output log for NewAlg.py containing calculated demand and demand update timestamps.

### NewAlg.py

* Description:

    Python3 script for executing __Knapsack-based demand calculations__ on one of three task sets.

* Inputs:
  * __-h__ : Help flag for showing detailed help
  * __-t #__ : Task Set Indicator identifying the task set number to use where:
    * 1 - Use Task Set #1 in Bijinemula et al.
    * 2 - Use Task Set #2 in Bijinemula et al.
    * 3 - Use the custom, user-defined task set defined in `taskSetCustom.json`

    * __-v__ : Verbose output flag for generating detailed output logs

* Example:

    The following example completes one run of the __Knapsack-Based Demand Calculation__ using the __Custom, User-Defined Task Set__ in `taskSetCustom.json`:

    ```sh
    python3 DRTAlg.py -t 3
    ```

* Output:

    If `-v` is entered, the calculated demand and demand update timestamps are logged in `NewAlgOutput.txt`.
    Runtime is printed to the terminal.

### NewMultiAVR.py

* Description:

    Python3 script for generating randomized AVR task set with _M_ modes and calculating the demand using __Knapsack-based__ calculations.

    ```sh
    python3 NewMultiAVR.py M
    ```

* Inputs:

  * __M__ : A positive integer indicating the number of modes the randomized AVR task set has.

* Example:

    The following example completes one run of the __Knapsack-Based Demand Calculation__ on a randomized AVR task set split into __6__ modes:

    ```sh
    python3 NewMultiAVR.py 6
    ```

* Output:

    The runtime is logged in __`NewMultiAVROutputs/NewAlg_Multi_M.txt`__ where __`M`__ is the number of modes passed in via the command line.

### plotGraphs.py

* Description:

    Python3 script for printing speed improvement calculations and graphing DRT and Knapsack-based demand calculation runtimes in `NewMultiAVROutputs/` and `DRTMultiAVROutputs/`.

* Inputs: None

* Example:

    ```sh
    python3 plotGraphs.py
    ```

* Output:

    Improvement calculations are printed to terminal.
    A graph of runtime vs number of modes is generated based on data in `NewMultiAVROutputs/` and `DRTMultiAVROutputs/`.

### runAll.py

* Description:

    Python3 script for executing multiple runs of DRT and Knapsack-based demand calculations over task sets with varying number of modes, generating improvement calculations, and graphing runtime vs number of modes to compare both algorithms.  

* Inputs:

  * __-h__ : Help flag for showing detailed help
  * __-r N__ : Run Count Indicator identifying the number of runs per mode to execute where __N__ is a positive integer.  _Default:_ 1 run.
  * __-m N__ : Minimum Number of Modes Indicator identifying the starting number of modes to assign to the generated task sets where __N__ is a positive integer. _Default:_ 6 mode split.
  * __-M N__ : Maximum Number of Modes Indicator identifying the number of modes to assign to the generated task sets where __N__ is a positive integer __greater than the Minimum Number of Modes__. _Default:_ 15 mode split.

* Example:

    The following example completes 10 runs of the __DRT-Based Demand Calculation__ and __Knapsack-Based Demand Calculation__ on a randomized AVR task sets with modes from __6__ to __15__:

    ```sh
    python3 runAll.py -r 10 -m 6 -M 15
    ```

    _Note: The above example is the __same process__ for generating the data presented in the publication. 10 runs x 2 algorithms x 10 mode splits_.

    __Warning:__ Executing the [runAll.py](#runAll.py) script with large run counts, mode counts, or a combination thereof can greatly increase runtime and might cause a RAM overload and make the system unstable. However, the file runAll.py can be executed multiple times with a smaller value of run count each time and get a graph updated with the runtime values averaged till the current run each time.

    Example: Completion time for __one run__ (the default) may take at least __16 hours__ for the DRT-based algorithm under __[Tested System Specifications](#tested-system-specifications)__.

* Output:

  * The runtime of Knapsack-based calculations for randomized task sets is logged in __`NewMultiAVROutputs/NewAlg_Multi_M.txt`__ where __`M`__ is the number of modes passed in via command line.
  * The runtime of DRT-based calculations for randomized task sets is logged in __`DRTMultiAVROutputs/DRTAlg_MultiAVR_M.txt`__ where __`M`__ is the number of modes passed in via command line.
  * The runtime of Knapsack-based calculations for [task set-1](https://github.com/bsk1410/Efficient-Knapsack-for-AVR-tasks-RTSS2018#element-no3---task-set-used-by-existing-work---task-set-1---table-i) and [task set-2](https://github.com/bsk1410/Efficient-Knapsack-for-AVR-tasks-RTSS2018#element-no4---a-more-general-task-set---task-set-2---table-ii) is logged in __`NewMultiAVROutputs/NewAlg_N.txt`__ where `N=1` represents [task set-1](https://github.com/bsk1410/Efficient-Knapsack-for-AVR-tasks-RTSS2018#element-no3---task-set-used-by-existing-work---task-set-1---table-i)
  * The runtime of DRT-based calculations for [task set-1](https://github.com/bsk1410/Efficient-Knapsack-for-AVR-tasks-RTSS2018#element-no3---task-set-used-by-existing-work---task-set-1---table-i) and [task set-2](https://github.com/bsk1410/Efficient-Knapsack-for-AVR-tasks-RTSS2018#element-no4---a-more-general-task-set---task-set-2---table-ii) is logged in __`DRTMultiAVROutputs/DRTAlg_N.txt`__ where `N=1` represents [task set-1](https://github.com/bsk1410/Efficient-Knapsack-for-AVR-tasks-RTSS2018#element-no3---task-set-used-by-existing-work---task-set-1---table-i)
  * Improvement calculations are printed to terminal.
  * A graph of runtime vs number of modes is generated based on data in `NewMultiAVROutputs/` and `DRTMultiAVROutputs/`.

### taskSet1.json

* Description:

    JSON file specifying Task Set 1 per [Bijinemula et al.](https://waynestateprod-my.sharepoint.com/:f:/g/personal/ez9213_wayne_edu/Em0cgsbtXSRJs5vxJfcFpeAB-LUFyp5K6H0cxSClSs6Syg?e=NJsR2H)

    ```json
    {
        "boundarySpeeds": [500, 1500, 2500, 3500, 4500, 5500, 6500],
        "executionTimes": [965, 576, 424, 343, 277, 246],
        "a_max": 600000
    }
    ```

### taskSet2.json

* Description:

    JSON file specifying Task Set 2 per [Bijinemula et al.](https://waynestateprod-my.sharepoint.com/:f:/g/personal/ez9213_wayne_edu/Em0cgsbtXSRJs5vxJfcFpeAB-LUFyp5K6H0cxSClSs6Syg?e=NJsR2H)

    ```json
    {
        "boundarySpeeds": [1200, 2200, 3200, 4200, 5200, 6200, 7200],
        "executionTimes": [965, 576, 424, 343, 277, 246],
        "a_max": 600000
    }
    ```

### taskSetCustom.json

* Description:

    JSON file specifying the custom, user-defined task set.

    ```json
    {
        "boundarySpeeds": [1000, 2000, 3000, 4000, 5000, 6000, 7000],
        "executionTimes": [950, 550, 450, 350, 250, 150],
        "a_max": 500000
    }
    ```

## RTSS 2018 Publication

_An Efficient Knapsack-Based Approach for Calculating the Worst-Case Demand of AVR Tasks_ by [Bijinemula et al.](https://waynestateprod-my.sharepoint.com/:f:/g/personal/ez9213_wayne_edu/Em0cgsbtXSRJs5vxJfcFpeAB-LUFyp5K6H0cxSClSs6Syg?e=NJsR2H) (Accepted)  
Real-Time Systems Symposium ([RTSS](http://2018.rtss.org/)) 2018 - Main Real-Time Track  
Nashville, Tennessee, USA

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

## Appendix E - Version Checking

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

## Appendix F - Known Issues

1. Windows Compatibility via Anaconda: Attempts to execute the scripts using the __Anaconda Distribution__ on __Windows__ have lead to issues with [matplotlib](https://matplotlib.org/api/pyplot_summary.html). _Recommendation_: Use the provided OVA or Ubuntu 18.04 install instructions.

2. Execution Termination: High Number of Modes or run counts requested during script execution (especially on slower hardware) can greatly increase CPU and RAM usage, sometimes leading to process termination. _Recommendation_: Beware of long runtimes (15+ hours for one run) and terminations via SIGKILL if memory consumption is deemed too high. Avoid high Number of Modes and run count requests for the DRTAlg.py and DRTMultiAVR.py scripts.