# QE Docset Autobuild

The script that can easily build [QE Docset](https://github.com/chazeon/qe-docset) for multiple versions of Quantum ESPRESSO under one line of command.

# Usage

Clone the repo and the submodules, install Python submodule, and run
```
python3 check.py
```
and take a nap.

The script automatically pulls source code from Quantum ESPRESSO's official repo, and build the docsets.

Then you can run
```
python3 build_json.py
```
to build the required `docset.json` file that is required for submission.

# Performance

I don't expect the script being executed on a daily basis so the performance is not my prior concentration. However, based on my observation, `configure`ing and compiling documentation using `pdflatex` is the most time-consuming job. I have been running this job on my ThinkPad, it is equipped with an i5-7300U CPU, and the hard-drive is NVMe SSD drive. The test is perfomed on Linux Subsystem under Windows 10.

Under this setup, each take approximately 10-13 minutes, and total 13 jobs needs to be performed as of the day this README is authored, it is about 2 hours or so to finish the entire job.
