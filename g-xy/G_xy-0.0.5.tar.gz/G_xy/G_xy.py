import numpy as np
import matplotlib.pyplot as plt

class G_xy:
    def __init__(self):
        '''
        กราฟ 1 \n
        V_initial = 5.7 \n
        กราฟ 2 \n
        V_initial1 = 5.7 ,g1 = 9.8 \n
        กราฟ 3 \n
        V_initial2 = 5.7 \n
        กราฟ 4 \n
        V_initial3 = 5.7 ,g3 = 9.8 \n
        ปรับเวลา \n
        plt.pause(t) ,t=0.01
        '''
        self.t = 0.1
        
        self.V_initial = 5.7
        self.theta = (np.pi)/4
        self.v_x = self.V_initial * np.cos(self.theta)
        self.r_x = 0
        self.lr_x = []
        self.lr_y = []

        self.V_initial1 = 5.7
        self.theta1 = (np.pi)/4
        self.g1 = 9.8
        self.v_y1 = self.V_initial1 * np.sin(self.theta1)
        self.r_y1 = 0
        self.lr_x1 = []
        self.lr_y1 = []
        
        self.V_initial2 = 5.7
        self.theta2 = (np.pi) / 4
        self.v_x2 = self.V_initial2 * np.cos(self.theta2)
        self.lr_x2 = []
        self.lr_y2 = []

        self.V_initial3 = 5.7
        self.theta3 = (np.pi) / 4
        self.g3 = 9.8
        self.v_y3 = self.V_initial3 * np.sin(self.theta3)
        self.time3 = np.linspace(0, 100, 10000)
        self.r_y3 = 0
        self.lr_x3 = []
        self.lr_y3 = []
    def xy(self):
        plt.figure(figsize=[35,6],dpi=40)
        for t3 in self.time3:
            r_x = self.v_x * t3
            
            r_y1 = (self.v_y1 * t3) - 1/2 * self.g1 * (t3 ** 2) + 0.6
            
            r_y3 = (self.v_y3 * t3) - 1 / 2 * self.g3 * (t3 ** 2) + 0.6
            
            abv3 = self.v_y3 - self.g3 * t3
            if r_y3 >= 0:
                self.lr_x.append(t3)
                self.lr_y.append(r_x)
                
                self.lr_x1.append(t3)
                self.lr_y1.append(r_y1)
                
                self.lr_x2.append(t3)
                self.lr_y2.append(self.v_x2)
                
                self.lr_x3.append(t3)
                self.lr_y3.append(abv3)
            else:
                break
            plt.subplot(1, 4, 1)
            plt.plot(self.lr_x, self.lr_y, color='red',)
            
            plt.subplot(1, 4, 2)
            plt.plot(self.lr_x1, self.lr_y1, color='green')
            
            plt.subplot(1, 4, 3)
            plt.plot(self.lr_x2, self.lr_y2, color='blue')
            
            plt.subplot(1, 4, 4)
            plt.plot(self.lr_x3, self.lr_y3, color='yellow')
            plt.pause(self.t)
        plt.show()

    def __str__(self):
        return 'x = G_xy()\nx.g1 = 9\nx.t = 0.01\nx.V_initial3 = 6\nx.xy()'
    
if __name__ == '__main__':
    print(G_xy())
    # x = G_xy()
    # x.g1 = 9
    # x.t = 0.01
    # x.V_initial3 = 6
    # x.xy()
