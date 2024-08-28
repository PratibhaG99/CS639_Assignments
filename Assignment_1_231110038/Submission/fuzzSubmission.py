from multiprocessing.sharedctypes import Value
from random import random
from secrets import choice
from select import select
from kast import kachuaAST
import random
import sys
from z3 import *
sys.path.insert(0, "KachuaCore/interfaces/")
from interfaces.fuzzerInterface import *
sys.path.insert(0, '../KachuaCore/')

# Each input is of this type.
#class InputObject():
#    def __init__(self, data):
#        self.id = str(uuid.uuid4())
#        self.data = data
#        # Flag to check if ever picked
#        # for mutation or not.
#        self.pickedOnce = False
        
class CustomCoverageMetric(CoverageMetricBase):
    # Statements covered is used for
    # coverage information.
    def __init__(self):
        super().__init__()

    # TODO : Implement this
    def compareCoverage(self, curr_metric, total_metric):
        # must compare curr_metric and total_metric
        # True if Improved Coverage else False
        return True if set(curr_metric) - set(total_metric) else False

    # TODO : Implement this
    def updateTotalCoverage(self, curr_metric, total_metric):
        # Compute the total_metric coverage and return it (list)
        # this changes if new coverage is seen for a
        # given input.
        for i in range(len(curr_metric)):
            if curr_metric[i] not in total_metric:
                total_metric.append(curr_metric[i])
        return total_metric

class CustomMutator(MutatorBase):
    def __init__(self):
        pass

    # TODO : Implement this
    def mutate(self, input_data, coverageInfo, irList):
        # Mutate the input data and return it
        # coverageInfo is of type CoverageMetricBase
        # Don't mutate coverageInfo
        # irList : List of IR Statments (Don't Modify)
        # input_data.data -> type dict() with {key : variable(str), value : int}
        # must return input_data after mutation.
        
        # Select variable will ensure the random selection of mutation function
        select=random.randint(0,3)
    
        print("=================================",select)

        if select==0:
            #FIRST MUTATION FUNCTION
            for key,Value in input_data.data.items():
                input_data.data[key]+=random.randint(-300,300)
            return input_data

        elif select==1:
            #SECOND MUTATION FUNCTION
            for key,Value in input_data.data.items():
                input_data.data[key]= ~input_data.data[key]
            return input_data

        elif select==2:
            #THIRD MUTATION FUNCTION
            for key,Value in input_data.data.items():
                binary_string = bin(input_data.data[key])[2:]
                res=[]
                for bit in binary_string:
                    if(bit=='b'):
                        continue
                    else:
                        res.append(int(bit))
                # res = [int(bit) for bit in binary_string]
                index = random.randint(0, len(res) - 1)
                res[index]^=1
                index = random.randint(0, len(res) - 1)
                res[index]^=1
                ans=0
                for i in range(0, len(res)):
                    ans+= res[len(res)-i-1]*(2**i)
            return input_data

        elif select==3:
            #FOURTH MUTATAION FUNCTION
            for key,Value in input_data.data.items():
                binary_string = bin(input_data.data[key])[2:]
                res=[]
                for bit in binary_string:
                    if(bit=='b'):
                        continue
                    else:
                        res.append(int(bit))
                # res = [int(bit) for bit in binary_string]
                random.shuffle(res)
                ans=0
                for i in range(0, len(res)):
                    ans+= res[len(res)-i-1]*(2**i)
            return input_data


# Reuse code and imports from
# earlier submissions (if any).
