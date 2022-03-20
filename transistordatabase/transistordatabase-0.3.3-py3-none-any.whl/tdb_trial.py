import transistordatabase as tdb
from matplotlib import pyplot as plt
#tdb.update_from_fileexchange()
#tdb.print_tdb()
import numpy as np

def minimal_example():
    #t1 = tdb.load('ROHMSemiconductor_SCT3120AW7')
    t1 = tdb.load('CREE_C3M0016120K')
    print(t1.datasheet_hyperlink)

    #t1.switch.plot_all_channel_data()
    t1.init_switch_channel_matrix_minimal()

    #
    # print(f"{t1.switch.m_i_channel = }")
    # print(f"{t1.switch.channel_loss_matrix = }")


    # plt.contourf(t1.switch.m_i_channel, t1.switch.m_t_j, t1.switch.channel_loss_matrix)
    # plt.xlabel('i_channel / A')
    # plt.ylabel('t_j / °C')
    # plt.title('voltage / V')
    # plt.grid()
    # plt.show()
    # plt.close()


    fig = plt.figure()
    ax = fig.add_subplot(projection='3d')
    #ax.plot_surface(t1.switch.m_i_channel, t1.switch.m_t_j, t1.switch.channel_loss_matrix)
    #for m_count, matrix in enumerate(t1.channel_matrices):
    matrix = t1.channel_matrices[1]
    ax.plot_surface(matrix.i_channel, matrix.t_j, matrix.matrix_v_channel, label=f"v_g = {matrix.v_g}")
    ax.set_xlabel('current / A')
    ax.set_ylabel('t_j / °C')
    ax.set_zlabel('voltage / V')
    plt.show()


def example():
    #t1 = tdb.load('ROHMSemiconductor_SCT3120AW7')
    t1 = tdb.load('CREE_C3M0016120K')
    # t1.switch.plot_all_channel_data()
    t1.init_loss_matrices()

    # plt.contourf(t1.switch.m_i_channel[:,:,1], t1.switch.m_t_j[:,:,1], t1.switch.channel_loss_matrix[:,:,1])
    # plt.xlabel('i_channel / A')
    # plt.ylabel('t_j / °C')
    # plt.title('voltage / V')
    # plt.grid()
    # plt.show()
    gate_voltage_number = 2
    #plt.close()



    fig = plt.figure()
    ax = fig.add_subplot(projection='3d')
    #for m_count, matrix in enumerate(t1.channel_matrices):
    matrix = t1.channel_matrices[0]
    ax.plot_surface(matrix.i_channel, matrix.t_j, matrix.matrix_v_channel, label=f"v_g = {matrix.v_g}")

    ax.set_xlabel('current / A')
    ax.set_ylabel('t_j / °C')
    ax.set_zlabel('voltage / V')
    #plt.legend()
    plt.show()


def check_input_data():
    t1 = tdb.load('CREE_C3M0016120K')
    t1.switch.plot_all_channel_data()

if __name__ == "__main__":
    #example()
    #check_input_data()
    minimal_example()
    #tdb.print_tdb()