#levelRunnable/listener tests
import level, leveldatabase
from levelrunnable import LevelRunnable
from eval import Eval


#1st test-------------------------------------------------------------------------------------------------
print("Test 1 Level info:")
testLevel2 = leveldatabase.level2
testLevel2.display()

runningLevel = LevelRunnable(testLevel2)

#checkLevel() test
print("\ncheckLevel() test:")
print(runningLevel.checkLevel())


#runLevel() test
runningLevel.runLevel()


#eval tests
eval1 = Eval(testLevel2, runningLevel.userInput, runningLevel.userActions, runningLevel.elapsedTime)
eval1.evaluate()
eval1.display()



#2nd test-------------------------------------------------------------------------------------------------
print("\n\nTest 2 Level info:")
testLevel3 = leveldatabase.level3
testLevel3.display()

runningLevel = LevelRunnable(testLevel3)

#checkLevel() test
print("\ncheckLevel() test:")
print(runningLevel.checkLevel())


#runLevel() test
runningLevel.runLevel()


#eval tests
eval1 = Eval(testLevel3, runningLevel.userInput, runningLevel.userActions, runningLevel.elapsedTime)
eval1.evaluate()
eval1.display()


