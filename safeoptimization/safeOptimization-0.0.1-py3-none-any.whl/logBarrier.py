import numpy as np


class sLBM():


    def __init__(self, objective_function, constraints,  dimension, constraints_number, x_0, variable_boundaries=None,\
        algorithm_parameters={'max_num_iteration':100, 'smoothness_constant':10, 'lipschitz_constant':10, 'eta':0.5, 'mu':1 + 1e-3}): 
        self.name = 'sLBM'
        assert (callable(objective_function)), "function must be callable" 
        self.objective_function = objective_function
        assert (callable(constraints)), "constraints must be callable" 
        self.constraints = constraints
        self.dimension = dimension
        self.constraints_number = constraints_number
        self.algorithm_parameters = algorithm_parameters
        self.variable_boundaries = variable_boundaries
        self.x_0 = x_0
        self.denominator = max(self.algorithm_parameters['lipschitz_constant'], self.constraints_number*np.sqrt(self.dimension)*self.algorithm_parameters['smoothness_constant'])
        self.traj = np.zeros([self.dimension,self.algorithm_parameters['max_num_iteration'] + 1])
        self.traj[:,0] = self.x_0
        

        
        
     
    def e_i(d, i): 
        y = np.array([0]*(i - 1) + [1] + [0]*(d - i))
        return y

    def grad_approximation(self, x, d, delta):
        u = np.random.uniform(-1, 1, d )
        u[u >= 0] = 1
        u[u < 0] = -1 
        grad = (d/delta)*self.f(x + delta*u)*u
        return grad

    def run(self):
        objective_function_measure = np.zeros(self.dimension + 1)
        constraints_measure = np.zeros([self.constraints_number, self.dimension+1])

        for i in range(self.algorithm_parameters['max_num_iteration']):
        #     if i > 50:
        #          eta = 0.01/5
            x_t = self.traj[:,i]
            const_t = np.array(self.constraints(x_t))
            v_t = min(self.algorithm_parameters['eta']/(np.sqrt(self.dimension)*self.algorithm_parameters['smoothness_constant']), min(const_t*(-1))/self.denominator)
            constraints_measure[:,0] = const_t
            objective_function_measure[0] = self.objective_function(x_t)
            for j in range(1, self.dimension + 1):
                x_t_2 = x_t + v_t*sLBM.e_i(self.dimension, j)
                constraints_measure[:,j] = self.constraints(x_t_2)
                objective_function_measure[j] = self.objective_function(x_t_2)

            f_x_t = -const_t
            g_t = constraints_measure - constraints_measure[:,0].reshape(self.constraints_number,1)
            g_t = g_t[:,1:]/v_t
            g_t_0 = objective_function_measure - objective_function_measure[0]
            g_t_0 = g_t_0[1:]/v_t

            gradient = g_t_0 + (self.algorithm_parameters['eta'])/(self.algorithm_parameters['mu']**i)*sum(g_t/f_x_t.reshape(self.constraints_number,1))
            L_2 = self.algorithm_parameters['smoothness_constant'] \
                + sum(2*self.algorithm_parameters['eta']\
                *self.algorithm_parameters['smoothness_constant']/f_x_t) \
                + sum(4*self.algorithm_parameters['eta']\
                *self.algorithm_parameters['lipschitz_constant']**2/f_x_t**2)
            gamma_t = min(min(f_x_t)/(2*self.algorithm_parameters['lipschitz_constant']*np.linalg.norm(gradient)), 1/L_2)
            x_next = x_t - gamma_t*gradient 
            self.traj[:,i+1] = x_next




