# structure of folder

1- My five test examples of the Kachua code are placed in "KachuaCore\example".
   For each test case I have created two files e.g: sbfl1.tl and sbfl1_buggy.tl, where sbfl1 is the correct program and sbfl1_buggy is the one with faults.
2- Outputs of all 5 programs are in  "Test\Output" folder.
3- Report file is in "Test" folder.

### Commands to run each of the testcases:-

1-
python chiron.py --SBFL ./example/sbfl1.tl --buggy ./example/sbfl1_buggy.tl -vars [':x',':y',':z'] --timeout 10 --ntests 20 --popsize 50 --cxpb 1.0 --mutpb 1.0 --ngen 50 --verbose True

2- 
python chiron.py --SBFL ./example/sbfl2.tl --buggy ./example/sbfl2_buggy.tl -vars [':x',':y',':z'] --timeout 10 --ntests 20 --popsize 50 --cxpb 1.0 --mutpb 1.0 --ngen 50 --verbose True

3- 
python chiron.py --SBFL ./example/sbfl3.tl --buggy ./example/sbfl3_buggy.tl -vars [':x',':y',':z'] --timeout 10 --ntests 20 --popsize 20 --cxpb 1.0 --mutpb 1.0 --ngen 20 --verbose True

4-
python chiron.py --SBFL ./example/sbfl4.tl --buggy ./example/sbfl4_buggy.tl -vars [':x',':y',':z'] --timeout 10 --ntests 20 --popsize 20 --cxpb 1.0 --mutpb 1.0 --ngen 20 --verbose True

5-
python chiron.py --SBFL ./example/sbfl5.tl --buggy ./example/sbfl5_buggy.tl -vars [':x',':y',':z'] --timeout 10 --ntests 20 --popsize 20 --cxpb 1.0 --mutpb 1.0 --ngen 20 --verbose True