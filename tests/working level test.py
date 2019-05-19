#levelRunnable/listener tests
import level, leveldatabase
from levelrunnable import LevelRunnable
from eval import Eval

print("Test Level info:")
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
eval1.display()

print("\nYour score is: " + eval1.evaluate())


