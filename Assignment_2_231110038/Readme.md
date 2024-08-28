# structure of folder

1- My five .tl files of the Kachua code are placed in "KachuaCore\example".
   For each test case I have created two files e.g: task1-1.tl and task1-2.tl, where task1-2.tl is the one with constant parameters and task2-2.tl is the one without constant parameters.
2- Outputs of all 5 programs are in  "Test\Output" folder.
3- Report file is in "Test" folder.

### Deatils to run the program

First, to generate json file pass input parameters and constant parameters for task1-1.tl and same input parameters without constamt parameters to task1-2.tl. 
It is requires to explicitly change the name of testData.json for task1-1.tl as testData1.json and for task1-2.tl as testData2.json
Then create a optimized.kw file for task1-2.tl and rename it as task1-2.kw
Now, run eqality check on the both kachua programs by specifying the output variable names under -e flag.

### Commands to run each of the testcases (inside KachuaCore folder):-

1- 
python kachua.py -t 100 -se example/task1-1.tl -d{':x':10, ':y':20} -c{':c1':1, ':c2':1}	
python kachua.py -t 100 -se tests/test1-2.tl -d{':x':10, ':y':20}		
python kachua.py --opt example/task1-2.tl			
python..\Submission\symbSubmission.py -b task1-2.kw -e{'x' , 'y'}

2- 
python kachua.py -t 100 -se example/task2-1.tl -d{':x':11,':y':33} -c{':c1':1}	
python kachua.py -t 100 -se example/task2-2.tl -d{':x':11,':y':33}		
python kachua.py --opt example/task2-2.tl		
python..\Submission\symbSubmission.py -b task2-2.kw -e{'x' , 'y'}

3- 
python kachua.py -t 100 -se example/task3-1.tl -d{':x':11,':y':33} -c{':c1':1,':c2':1}	
python kachua.py -t 100 -se example/task3-2.tl -d{':x':11,':y':33}		
python kachua.py --opt example/task3-2.tl		
python..\Submission\symbSubmission.py -b task3-2.kw -e{'x' , 'y'}

4- 
python kachua.py -t 100 -se example/task4-1.tl -d{':x':11,':y':33} -c{':c1':1,':c2':1,':c3':1,':c4':1}	
python kachua.py -t 100 -se example/task4-2.tl -d{':x':11,':y':33}		
python kachua.py --opt example/task4-2.tl		
python..\Submission\symbSubmission.py -b task4-2.kw -e{'x' , 'y'}

5- 
python kachua.py -t 100 -se example/task5-1.tl -d{':x':11,':y':33} -c{':c1':1,':c2':1,':c3':1}	
python kachua.py -t 100 -se example/task5-2.tl -d{':x':11,':y':33}		
python kachua.py --opt example/task5-2.tl		
python..\Submission\symbSubmission.py -b task5-2.kw -e{'x' , 'y'}