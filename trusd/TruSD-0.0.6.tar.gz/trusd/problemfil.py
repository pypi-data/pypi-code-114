import numpy as np
from scipy.special import comb

# Python (and Numpy) array as 0-based!

def wright_fisher_trans_matrix(selcoeff, gens, pop):

	# https://numpy.org/doc/stable/reference/generated/numpy.full.html
	# Return a new array of given shape and type, filled with fill_value.
	matrix = np.full((pop + 1, pop + 1), np.nan, dtype=np.float64)

	for n in range(pop + 1):
		for m in range(pop + 1):
			m_over_pop = m / pop

			first_product = (m_over_pop + selcoeff * m_over_pop * (1 - m_over_pop)) ** n
			second_product = (1 - m_over_pop - selcoeff * m_over_pop * (1 - m_over_pop)) ** (pop - n)

			# https://docs.scipy.org/doc/scipy/reference/generated/scipy.special.comb.html
			# The number of combinations of N things taken k at a time. This is often expressed as “N choose k”.
			matrix[n, m] = comb(pop, n) * first_product * second_product

	# https://numpy.org/doc/stable/reference/generated/numpy.linalg.matrix_power.html
	# Raise a square matrix to the (integer) power n.
	matrix = np.linalg.matrix_power(matrix, gens)

	return matrix


def single_likelihood(selcoeff, prop, gens, pop):

	matrix_sel = wright_fisher_trans_matrix(selcoeff, gens, pop)
	matrix_neut = wright_fisher_trans_matrix(0, gens, pop)

	# There is a fancy method to choose row and col, independent of the
	# contents of the matrices. Left out here for better overview.
	row = 10
	col = 10

	a = matrix_sel[row, col]
	b = matrix_neut[row, col]

	result = np.log(prop * a + (1 - prop) * b)

	return result


print(single_likelihood(0.05, 0.5, 10, 100))
