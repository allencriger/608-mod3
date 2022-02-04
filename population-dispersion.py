import statistics
populationVariance = statistics.pvariance([1, 3, 4, 2, 6, 5, 3, 4, 5, 2])
standardDeviation = statistics.pstdev([1, 3, 4, 2, 6, 5, 3, 4, 5, 2])
import math
confirmationResults = math.sqrt(statistics.pvariance([1, 3, 4, 2, 6, 5, 3, 4, 5, 2]))
print(' ')
print('The data set for these calculations is (1, 3, 4, 2, 6, 5, 3, 4, 5, 2):')
print(' ')
print('The population variance for the data set is: ', populationVariance)
print('The standard deviation for the data set is: ', standardDeviation)
print('The confirmation result (square root of population variance) is: ', confirmationResults)


