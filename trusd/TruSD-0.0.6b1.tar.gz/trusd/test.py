
import numpy as np
from scipy.special import gammaln, comb

def wright_fisher_trans_matrix(selection_coefficient, num_generations, genepop):
	'''
	Calculates the Wrigth-Fisher transition matrix given the selection coefficient,
	the number of generations and the genetic population. The calculation is
	computatinally very expensive, so the result is cached.

	@param selection_coefficient: The selection coefficient as float
	@param num_generations: The generation number as integer
	@param genepop: Gene population as integer
	@returns: The Wright-Fisher transition matrix as numpy array with shape (genepop+1, genepop+1)
	'''

	matrix = np.full((genepop + 1, genepop + 1), np.nan, dtype=np.float64)

	for n in range(genepop + 1):
		for m in range(genepop + 1):
			m_over_genepop = m / genepop
			try:
				first_product = (m_over_genepop + selection_coefficient * \
								m_over_genepop * (1 - m_over_genepop)) ** n
				second_product = (1 - m_over_genepop - selection_coefficient * \
								m_over_genepop * (1 - m_over_genepop)) ** (genepop - n)
				matrix[n, m] = comb(genepop, n) * first_product * second_product
			except FloatingPointError:
				# If genepop is too big, x**n or x**genepop may become very small
				# (under approx.10**-308) or comb(genepop, n) may become infinity.
				# In this case, we set the matrix value to 0.
				matrix[n, m] = 0

	print('Old method before matrix_power')
	print(matrix)

	##matrix = np.linalg.matrix_power(matrix, num_generations)

	#print('Old method after matrix_power')
	#print(matrix)


def new_method(selcoeff, genepop):

	allels = 1

	X = np.arange(allels * genepop + 1).conj().T/allels/genepop
	matrix = np.zeros((allels * genepop + 1, allels * genepop + 1))

	#print(X)

	for n in range(allels * genepop + 1):
		for m in range(allels * genepop + 1):
			x = X[m]
			D = x + selcoeff * x * (1 - x)
			matrix[n, m] = np.exp(
				gammaln(allels * genepop + 1) -
				gammaln(n + 1) -
				gammaln(allels * genepop - n + 1) +
				n * np.log(D) +
				(allels * genepop - n) * np.log(1 - D)
			)

	matrix[0, 0] = 1
	matrix[allels * genepop, allels * genepop] = 1

	#print('New method')
	#print(matrix)

wright_fisher_trans_matrix(0.01, 10, 1000)
#new_method(0.01, 1000)
