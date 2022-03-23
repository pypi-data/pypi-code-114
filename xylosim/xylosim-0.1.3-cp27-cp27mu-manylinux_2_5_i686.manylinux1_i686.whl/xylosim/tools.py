import numpy as np
from pathlib import Path
from os import makedirs
import yaml
import json


def weight_mat_3d_to_synapses(weights):
    """
    Converts a 3d weight matrix to a list of Cimulator synapses.
    The weight matrix is supposed to be in the form (syn_id, pre, post)
    """
    weights = weights.T.swapaxes(0, 1)
    synapses = []
    for pre, w_pre in enumerate(weights):
        tmp = []
        for syn in np.dstack(np.where(w_pre))[0]:
            weight = weights[pre, syn[0], syn[1]]
            tmp.append(cim.Synapse(syn[0], syn[1], weight))
        synapses.append(tmp)

    return synapses

# helper functions 
def stochastic_round(x):
    ret = np.floor(x).astype(int)
    tmp = x - ret > 1 - np.random.random_sample(x.shape)
    ret += tmp.astype(int)
    return ret

def calc_bitshift_decay(tau, dt):
    dash = np.log2(np.array(tau) / dt)
    dash[dash < 0] = 0
    return dash

def to_hex(n, digits):
    return "%s" % ("0000%x" % (n & 0xFFFFFFFF))[-digits:]


def save_to_RAM_files_V1(
        path:str, 
        model, 
        inp_spks, 
        dt):

    """
    Function for saving a simulation, including network specifications and activities to RAM files for hardware tests.
    """

    from xylosim.v1 import XyloLayer, XyloSynapse
    from pathlib import Path
    import os
    import json
    
    path = Path(path)
    if not path.exists():
        os.makedirs(path)
    
    Nin = len(model.synapses_in)
    Nrec = len(model.iaf_neurons)
    Nout = len(model.iaf_neurons_out)
    
    
    # iwtram and iwt2ram (input neurons of synapse IDs 0 and 1)
    
    print(f"Writing iwtram.ini", end="\r")
    with open(path / f"iwtram.ini", "w+") as f:
        for pre, syns in enumerate(model.synapses_in):
            f.write(f"// iwt for IN{pre} \n")
            for post in range(Nrec):
                weight_found = False
                for syn in syns:
                    if syn.target_neuron_id == post and syn.target_synapse_id == 0:
                        f.write(to_hex(syn.weight, 2))
                        weight_found = True
                if not weight_found:
                    f.write(to_hex(0, 2))
                f.write("\n")
    
    print(f"Writing iwt2ram.ini", end="\r")
    with open(path / f"iwt2ram.ini", "w+") as f:
        for pre, syns in enumerate(model.synapses_in):
            f.write(f"// iwt2 for IN{pre} \n")
            for post in range(Nrec):
                weight_found = False
                for syn in syns:
                    if syn.target_neuron_id == post and syn.target_synapse_id == 1:
                        f.write(to_hex(syn.weight, 2))
                        weight_found = True
                if not weight_found:
                    f.write(to_hex(0, 2))
                f.write("\n")

    rwtram = open(path / "rwtram.ini", "w+")
    rwt2ram = open(path / "rwt2ram.ini", "w+")
    rforam = open(path / "rforam.ini", "w+")
    refocram = open(path / "refocram.ini", "w+")

    for pre, syns in enumerate(model.synapses_rec):
        rwtram.write(f"// rwt of RSN{pre} \n")
        rwt2ram.write(f"// rwt2 of RSN{pre} \n")
        rforam.write(f"// rfo of RSN{pre} \n")

        if len(syns) == 0:
            refocram.write(to_hex(0, 2))
            refocram.write("\n")
            continue

        target_ids = [s.target_neuron_id for s in syns]
        unique_target_ids, target_id_counts = np.unique(target_ids, return_counts=True)

        weights = {target_id: [] for target_id in unique_target_ids}

        for syn in syns:
            ws = weights[syn.target_neuron_id]

            if len(ws) == 0:
                # first synapse for this target
                if syn.target_synapse_id == 0:
                    ws.append([syn.weight])
                else:
                    ws.append([0, syn.weight])
            else:
                if len(ws[-1]) == 1:
                    if syn.target_synapse_id == 0:
                        ws[-1].append(0)
                        ws.append([syn.weight])
                    else:
                        ws[-1].append(syn.weight)
                else:
                    if syn.target_synapse_id == 0:
                        ws.append([syn.weight])
                    else:
                        ws.append([0, syn.weight])


        max_len = max([len(v) for v in list(weights.values())])

        last_target_id = -1 
        counts = 0

        i = 0
        while i < max_len:

            for target_id in unique_target_ids:
                if len(weights[target_id]) <= i:
                    # no more multapse for that connection
                    continue

                try:
                    weight_0, weight_1 = weights[target_id][i]
                except:
                    weight_0 = weights[target_id][i][0]
                    weight_1 = 0

                if weight_0 == 0 and weight_1 == 0:
                    i += 1
                    continue

                # check if this target id was written in the line abouve
                # if so, add a dummy synapse
                if target_id == last_target_id:
                    i -= 1
                    target_id = Nrec - 1
                    syn = XyloSynapse(target_neuron_id=target_id, target_synapse_id=0, weight=0)
                    syns.append(syn)

                    if n_syns == 2:
                        syn2 = XyloSynapse(target_neuron_id=target_id, target_synapse_id=1, weight=0)
                        syns.append(syn2)

                    weight_0 = 0
                    weight_1 = 0

                last_target_id = target_id
                counts += 1

                # write target neuron id to rforam
                rforam.write(to_hex(target_id, 3))
                rforam.write("\n")
                
                rwtram.write(to_hex(weight_0, 2))
                rwtram.write("\n")

                rwt2ram.write(to_hex(weight_1, 2))
                rwt2ram.write("\n")
            i += 1

        refocram.write(to_hex(counts, 2))
        refocram.write("\n")

    rwtram.close()
    rwt2ram.close()
    rforam.close()
    refocram.close()
    
    # owtram (output weights)
    print("Writing owtram.ini", end="\r")
    with open(path / "owtram.ini", "w+") as f:
        for pre, syns in enumerate(model.synapses_out):
            f.write(f"// owt for RSN{pre} \n")
            for post in range(Nout):
                weight_found = False
                for syn in syns:
                    if syn.target_neuron_id == post:
                        weight_found = True
                        f.write(to_hex(syn.weight, 2))
                        f.write("\n")
                if not weight_found:
                    f.write(to_hex(0, 2))
                    f.write("\n")

    
    # ndmram (membrane dashes) 
    print("Writing ndmram.ini", end="\r")
    with open(path / "ndmram.ini", "w+") as f:
        for pre, neuron in enumerate(model.iaf_neurons):
            f.write(to_hex(neuron.dash_mem, 1))
            f.write("\n")
        for pre, neuron in enumerate(model.iaf_neurons_out):
            f.write(to_hex(neuron.dash_mem, 1))
            f.write("\n")
    
    # ndsram (synaptic dashes)
    print("Writing ndsram.ini", end="\r")
    with open(path / "ndsram.ini", "w+") as f:
        for pre, neuron in enumerate(model.iaf_neurons):
            f.write(to_hex(neuron.dash_syns[0], 1))
            f.write("\n")
        for pre, neuron in enumerate(model.iaf_neurons_out):
            f.write(to_hex(neuron.dash_syns[0], 1))
            f.write("\n")
    
    # rds2ram (synaptic dashes of second synapse)
    print("Writing rds2ram.ini", end="\r")
    with open(path / "rds2ram.ini", "w+") as f:
        for pre, neuron in enumerate(model.iaf_neurons):
            f.write(to_hex(neuron.dash_syns[1], 1))
            f.write("\n")
    
    # nthram (thresholds) 
    print("Writing nthram.ini", end="\r")
    with open(path / "nthram.ini", "w+") as f:
        for pre, neuron in enumerate(model.iaf_neurons):
            f.write(to_hex(neuron.v_th, 4))
            f.write("\n")
        for pre, neuron in enumerate(model.iaf_neurons_out):
            f.write(to_hex(neuron.v_th, 4))
            f.write("\n")
    
    # raram and rcram (aliases)
    all_aliases = np.zeros(Nrec, dtype=int) - 1
    is_source = np.zeros(Nrec, dtype=int)
    is_target = np.zeros(Nrec, dtype=int)
    for i, aliases in enumerate(model.aliases):
        if len(aliases) > 0:
            all_aliases[i] = aliases[0]
            is_source[i] = 1
            is_target[aliases[0]] = 1
    
    # save to file
    print("Writing raram.ini", end="\r")
    with open(path / "raram.ini", "w+") as f:
        for pre, alias in enumerate(all_aliases):
            f.write(to_hex(alias, 3))
            f.write("\n")
    
    # save to file
    print("Writing rcram.ini", end="\r")
    with open(path / "rcram.ini", "w+") as f:
        for pre, issource in enumerate(is_source):
            f.write(to_hex(issource * 2 + is_target[pre], 1))
            f.write("\n")
    
    
    ## dynamical data (vmem, isyns and spikes)
    
    # rspkram
    mat = np.zeros((np.shape(model.rec_recurrent_spikes)[0], Nrec), dtype=int)
    spks = np.array(model.rec_recurrent_spikes).astype(int)
    
    if len(spks) > 0:
        mat[:, : spks.shape[1]] = spks
    
        path_spkr = path / "spk_res"
        if not path_spkr.exists():
            os.makedirs(path_spkr)
    
        print("Writing rspkram files in spk_res", end="\r")
        for t, spks in enumerate(mat):
            with open(path_spkr / f"rspkram_{t}.txt", "w+") as f:
                for val in spks:
                    f.write(to_hex(val, 2))
                    f.write("\n")
    
    # ospkram
    mat = np.zeros((np.shape(model.rec_out_spikes)[0], Nout), dtype=int)
    spks = np.array(model.rec_out_spikes).astype(int)
    
    if len(spks) > 0:
        mat[:, : spks.shape[1]] = spks
    
        path_spko = path / "spk_out"
        if not path_spko.exists():
            os.makedirs(path_spko)
    
        print("Writing ospkram files in spk_out", end="\r")
        for t, spks in enumerate(mat):
            with open(path_spko / f"ospkram_{t}.txt", "w+") as f:
                for val in spks:
                    f.write(to_hex(val, 2))
                    f.write("\n")
    
    # input spikes
    path_spki = path / "spk_in"
    if not path_spki.exists():
        os.makedirs(path_spki)
    
    print("Writing inp_spks.txt", end="\r")
    with open(path_spki / "inp_spks.txt", "w+") as f:
        idle = -1
        for t, chans in enumerate(inp_spks):
            idle += 1
            if not np.all(chans == 0):
                f.write(f"// time step {t}\n")
                if idle > 0:
                    f.write(f"idle {idle}\n")
                idle = 0
                for chan, num_spikes in enumerate(chans):
                    for _ in range(num_spikes):
                        f.write(f"wr IN{to_hex(chan, 1)}\n")
    
    # nscram
    mat = np.zeros((np.shape(model.rec_i_syn)[1], Nrec + Nout), dtype=int)
    isyns = np.array(model.rec_i_syn).T.astype(int)
    mat[:, : isyns.shape[1]] = isyns
    isyns_out = np.array(model.rec_i_syn_out).T.astype(int)
    mat[:, Nrec : Nrec + isyns_out.shape[1]] = isyns_out
    
    path_isyn = path / "isyn"
    if not path_isyn.exists():
        os.makedirs(path_isyn)
    
    print("Writing nscram files in isyn", end="\r")
    for t, vals in enumerate(mat):
        with open(path_isyn / f"nscram_{t}.txt", "w+") as f:
            for i_neur, val in enumerate(vals):
                f.write(to_hex(val, 4))
                f.write("\n")
    
    # nsc2ram
    if not hasattr(model, "rec_i_syn2"):
        mat = np.zeros((0, Nrec), int)
    else:
        mat = np.zeros((np.shape(model.rec_i_syn2)[1], Nrec), dtype=int)
        isyns2 = np.array(model.rec_i_syn2).T.astype(int)
        mat[:, : isyns2.shape[1]] = isyns2
    
    path_isyn2 = path / "isyn2"
    if not path_isyn2.exists():
        os.makedirs(path_isyn2)
    
    print("Writing nsc2ram files in isyn2", end="\r")
    for t, vals in enumerate(mat):
        with open(path_isyn2 / f"nsc2ram_{t}.txt", "w+") as f:
            for val in vals:
                f.write(to_hex(val, 4))
                f.write("\n")
    
    # nmpram
    mat = np.zeros((np.shape(model.rec_v_mem)[1], Nrec + Nout), dtype=int)
    vmems = np.array(model.rec_v_mem).T.astype(int)
    mat[:, : vmems.shape[1]] = vmems
    vmems_out = np.array(model.rec_v_mem_out).T.astype(int)
    mat[:, Nrec : Nrec + vmems_out.shape[1]] = vmems_out
    
    path_vmem = path / "vmem"
    if not path_vmem.exists():
        os.makedirs(path_vmem)
    
    print("Writing nmpram files in vmem", end="\r")
    for t, vals in enumerate(mat):
        with open(path_vmem / f"nmpram_{t}.txt", "w+") as f:
            for i_neur, val in enumerate(vals):
                f.write(to_hex(val, 4))
                f.write("\n")
    
    # basic config
    print("Writing basic_config.json", end="\r")
    with open(path / "basic_config.json", "w+") as f:
        config = {}
    
        # number of neurons
        config["IN"] = len(model.synapses_in)
        config["RSN"] = len(model.synapses_rec)
    
        # determine output size by getting the largest target neuron id
        syns = np.hstack(model.synapses_out)
        config["ON"] = int(np.max([s.target_neuron_id for s in syns]) + 1)
    
        # bit shift values
        config["IWBS"] = model.weight_shift_inp
        config["RWBS"] = model.weight_shift_rec
        config["OWBS"] = model.weight_shift_out
    
        # expansion neurons
        #if num_expansion is not None:
        #    config["IEN"] = num_expansion

        config['time_resolution_wrap'] = 0
    
        # dt
        config["DT"] = dt
    
        # number of synapses
        n_syns = 1
        syns_in = np.hstack(model.synapses_in)
        if np.any(np.array([s.target_synapse_id for s in syns_in]) == 1):
            n_syns = 2
        syns_rec = np.hstack(model.synapses_rec)
        if np.any(np.array([s.target_synapse_id for s in syns_rec]) == 1):
            n_syns = 2
    
        config["N_SYNS"] = n_syns
    
        # aliasing
        if max([len(a) for a in model.aliases]) > 0:
            config["RA"] = True
        else:
            config["RA"] = False
    
        json.dump(config, f)


def save_to_RAM_files_V2(
        path:str, 
        model, 
        inp_spks, 
        dt):

    """
    Function for saving a simulation, including network specifications and activities to RAM files for hardware tests.
    """

    from xylosim.v2 import XyloLayer, XyloSynapse
    from pathlib import Path
    import os
    import json
    
    path = Path(path)
    if not path.exists():
        os.makedirs(path)
    
    Nin = len(model.synapses_in)
    Nrec = len(model.iaf_neurons)
    Nout = len(model.iaf_neurons_out)

    # number of synapses
    n_syns = 1
    syns_in = np.hstack(model.synapses_in)
    if np.any(np.array([s.target_synapse_id for s in syns_in]) == 1):
        n_syns = 2
    syns_rec = np.hstack(model.synapses_rec)
    if np.any(np.array([s.target_synapse_id for s in syns_rec]) == 1):
        n_syns = 2
    
    # iwtram and iwt2ram (input neurons of synapse IDs 0 and 1)
    
    print(f"Writing iwtram.ini", end="\r")
    with open(path / f"iwtram.ini", "w+") as f:
        for pre, syns in enumerate(model.synapses_in):
            f.write(f"// iwt for IN{pre} \n")
            for post in range(Nrec):
                weight_found = False
                for syn in syns:
                    if syn.target_neuron_id == post and syn.target_synapse_id == 0:
                        f.write(to_hex(syn.weight, 2))
                        weight_found = True
                if not weight_found:
                    f.write(to_hex(0, 2))
                f.write("\n")
    
    print(f"Writing iwt2ram.ini", end="\r")
    with open(path / f"iwt2ram.ini", "w+") as f:
        for pre, syns in enumerate(model.synapses_in):
            f.write(f"// iwt2 for IN{pre} \n")
            for post in range(Nrec):
                weight_found = False
                for syn in syns:
                    if syn.target_neuron_id == post and syn.target_synapse_id == 1:
                        f.write(to_hex(syn.weight, 2))
                        weight_found = True
                if not weight_found:
                    f.write(to_hex(0, 2))
                f.write("\n")

    rwtram = open(path / "rwtram.ini", "w+")
    rwt2ram = open(path / "rwt2ram.ini", "w+")
    rforam = open(path / "rforam.ini", "w+")
    refocram = open(path / "refocram.ini", "w+")

    for pre, syns in enumerate(model.synapses_rec):
        rwtram.write(f"// rwt of RSN{pre} \n")
        rwt2ram.write(f"// rwt2 of RSN{pre} \n")
        rforam.write(f"// rfo of RSN{pre} \n")

        if len(syns) == 0:
            refocram.write(to_hex(0, 2))
            refocram.write("\n")
            continue

        target_ids = [s.target_neuron_id for s in syns]
        unique_target_ids, target_id_counts = np.unique(target_ids, return_counts=True)

        weights = {target_id: [] for target_id in unique_target_ids}

        for syn in syns:
            ws = weights[syn.target_neuron_id]

            if len(ws) == 0:
                # first synapse for this target
                if syn.target_synapse_id == 0:
                    ws.append([syn.weight])
                else:
                    ws.append([0, syn.weight])
            else:
                if len(ws[-1]) == 1:
                    if syn.target_synapse_id == 0:
                        ws[-1].append(0)
                        ws.append([syn.weight])
                    else:
                        ws[-1].append(syn.weight)
                else:
                    if syn.target_synapse_id == 0:
                        ws.append([syn.weight])
                    else:
                        ws.append([0, syn.weight])


        max_len = max([len(v) for v in list(weights.values())])

        last_target_id = -1 
        counts = 0 
        i = 0
        while i < max_len:

            for target_id in unique_target_ids:
                if len(weights[target_id]) <= i:
                    # no more multapse for that connection
                    continue

                try:
                    weight_0, weight_1 = weights[target_id][i]
                except:
                    weight_0 = weights[target_id][i][0]
                    weight_1 = 0

                if weight_0 == 0 and weight_1 == 0:
                    i += 1
                    continue

                # check if this target id was written in the line abouve
                # if so, add a dummy synapse
                if target_id == last_target_id:
                    i -= 1
                    target_id = Nrec - 1
                    syn = XyloSynapse(target_neuron_id=target_id, target_synapse_id=0, weight=0)
                    syns.append(syn)

                    if n_syns == 2:
                        syn2 = XyloSynapse(target_neuron_id=target_id, target_synapse_id=1, weight=0)
                        syns.append(syn2)

                    weight_0 = 0
                    weight_1 = 0

                last_target_id = target_id

                counts += 1

                # write target neuron id to rforam
                rforam.write(to_hex(target_id, 3))
                rforam.write("\n")
                
                rwtram.write(to_hex(weight_0, 2))
                rwtram.write("\n")

                rwt2ram.write(to_hex(weight_1, 2))
                rwt2ram.write("\n")
            i += 1

        refocram.write(to_hex(counts, 2))
        refocram.write("\n")

    rwtram.close()
    rwt2ram.close()
    rforam.close()
    refocram.close()

    # owtram (output weights)
    print("Writing owtram.ini", end="\r")
    with open(path / "owtram.ini", "w+") as f:
        for pre, syns in enumerate(model.synapses_out):
            f.write(f"// owt for RSN{pre} \n")
            for post in range(Nout):
                weight_found = False
                for syn in syns:
                    if syn.target_neuron_id == post:
                        weight_found = True
                        f.write(to_hex(syn.weight, 2))
                        f.write("\n")
                if not weight_found:
                    f.write(to_hex(0, 2))
                    f.write("\n")

    
    # ndmram (membrane dashes) 
    print("Writing ndmram.ini", end="\r")
    with open(path / "ndmram.ini", "w+") as f:
        for pre, neuron in enumerate(model.iaf_neurons):
            f.write(to_hex(neuron.dash_mem, 1))
            f.write("\n")
        for pre, neuron in enumerate(model.iaf_neurons_out):
            f.write(to_hex(neuron.dash_mem, 1))
            f.write("\n")
    
    # ndsram (synaptic dashes)
    print("Writing ndsram.ini", end="\r")
    with open(path / "ndsram.ini", "w+") as f:
        for pre, neuron in enumerate(model.iaf_neurons):
            f.write(to_hex(neuron.dash_syns[0], 1))
            f.write("\n")
        for pre, neuron in enumerate(model.iaf_neurons_out):
            f.write(to_hex(neuron.dash_syns[0], 1))
            f.write("\n")
    
    # rds2ram (synaptic dashes of second synapse)
    print("Writing rds2ram.ini", end="\r")
    with open(path / "rds2ram.ini", "w+") as f:
        for pre, neuron in enumerate(model.iaf_neurons):
            f.write(to_hex(neuron.dash_syns[1], 1))
            f.write("\n")
    
    # nthram (thresholds) 
    print("Writing nthram.ini", end="\r")
    with open(path / "nthram.ini", "w+") as f:
        for pre, neuron in enumerate(model.iaf_neurons):
            f.write(to_hex(neuron.v_th, 4))
            f.write("\n")
        for pre, neuron in enumerate(model.iaf_neurons_out):
            f.write(to_hex(neuron.v_th, 4))
            f.write("\n")

    # nbram (biases) 
    print("Writing nbram.ini", end="\r")
    with open(path / "nbram.ini", "w+") as f:
        for pre, neuron in enumerate(model.iaf_neurons):
            f.write(to_hex(neuron.bias, 2))
            f.write("\n")
        for pre, neuron in enumerate(model.iaf_neurons_out):
            f.write(to_hex(neuron.bias, 2))
            f.write("\n")
    
    # raram and rcram (aliases)
    all_aliases = np.zeros(Nrec, dtype=int) - 1
    is_source = np.zeros(Nrec, dtype=int)
    is_target = np.zeros(Nrec, dtype=int)
    for i, aliases in enumerate(model.aliases):
        if len(aliases) > 0:
            all_aliases[i] = aliases[0]
            is_source[i] = 1
            is_target[aliases[0]] = 1
    
    # save to file
    print("Writing raram.ini", end="\r")
    with open(path / "raram.ini", "w+") as f:
        for pre, alias in enumerate(all_aliases):
            f.write(to_hex(alias, 3))
            f.write("\n")
    
    # save to file
    print("Writing rcram.ini", end="\r")
    with open(path / "rcram.ini", "w+") as f:
        for pre, issource in enumerate(is_source):
            f.write(to_hex(issource * 2 + is_target[pre], 1))
            f.write("\n")
    
    
    ## dynamical data (vmem, isyns and spikes)
    
    # rspkram
    mat = np.zeros((np.shape(model.rec_recurrent_spikes)[0], Nrec), dtype=int)
    spks = np.array(model.rec_recurrent_spikes).astype(int)

    # remove all parts where Xylo is in hibernation mode
    mat = np.delete(mat, model.rec_hibernation_mode, axis=0)
    spks = np.delete(spks, model.rec_hibernation_mode, axis=0)
    
    if len(spks) > 0:
        mat[:, : spks.shape[1]] = spks
    
        path_spkr = path / "spk_res"
        if not path_spkr.exists():
            os.makedirs(path_spkr)
    
        print("Writing rspkram files in spk_res", end="\r")
        for t, spks in enumerate(mat):
            with open(path_spkr / f"rspkram_{t}.txt", "w+") as f:
                for val in spks:
                    f.write(to_hex(val, 2))
                    f.write("\n")
    
    # ospkram
    mat = np.zeros((np.shape(model.rec_out_spikes)[0], Nout), dtype=int)
    spks = np.array(model.rec_out_spikes).astype(int)

    # remove all parts where Xylo is in hibernation mode
    mat = np.delete(mat, model.rec_hibernation_mode, axis=0)
    spks = np.delete(spks, model.rec_hibernation_mode, axis=0)
    
    if len(spks) > 0:
        mat[:, : spks.shape[1]] = spks
    
        path_spko = path / "spk_out"
        if not path_spko.exists():
            os.makedirs(path_spko)
    
        print("Writing ospkram files in spk_out", end="\r")
        for t, spks in enumerate(mat):
            with open(path_spko / f"ospkram_{t}.txt", "w+") as f:
                for val in spks:
                    f.write(to_hex(val, 2))
                    f.write("\n")
    
    # input spikes
    path_spki = path / "spk_in"
    if not path_spki.exists():
        os.makedirs(path_spki)
    
    print("Writing inp_spks.txt", end="\r")
    with open(path_spki / "inp_spks.txt", "w+") as f:
        idle = -1
        for t, chans in enumerate(inp_spks):
            idle += 1
            if not np.all(chans == 0):
                f.write(f"// time step {t}\n")
                if idle > 0:
                    f.write(f"idle {idle}\n")
                idle = 0
                for chan, num_spikes in enumerate(chans):
                    for _ in range(num_spikes):
                        f.write(f"wr IN{to_hex(chan, 1)}\n")
    
    # nscram
    mat = np.zeros((np.shape(model.rec_i_syn)[1], Nrec + Nout), dtype=int)
    isyns = np.array(model.rec_i_syn).T.astype(int)

    # remove all parts where Xylo is in hibernation mode
    mat = np.delete(mat, model.rec_hibernation_mode, axis=0)
    isyns = np.delete(isyns, model.rec_hibernation_mode, axis=0)

    mat[:, : isyns.shape[1]] = isyns
    isyns_out = np.array(model.rec_i_syn_out).T.astype(int)

    # remove all parts where Xylo is in hibernation mode
    isyns_out = np.delete(isyns_out, model.rec_hibernation_mode, axis=0)

    mat[:, Nrec : Nrec + isyns_out.shape[1]] = isyns_out
    
    path_isyn = path / "isyn"
    if not path_isyn.exists():
        os.makedirs(path_isyn)
    
    print("Writing nscram files in isyn", end="\r")
    for t, vals in enumerate(mat):
        with open(path_isyn / f"nscram_{t}.txt", "w+") as f:
            for i_neur, val in enumerate(vals):
                f.write(to_hex(val, 4))
                f.write("\n")
    
    # nsc2ram
    if not hasattr(model, "rec_i_syn2"):
        mat = np.zeros((0, Nrec), int)
    else:
        mat = np.zeros((np.shape(model.rec_i_syn2)[1], Nrec), dtype=int)
        isyns2 = np.array(model.rec_i_syn2).T.astype(int)

        # remove all parts where Xylo is in hibernation mode
        mat = np.delete(mat, model.rec_hibernation_mode, axis=0)
        isyns2= np.delete(isyns2, model.rec_hibernation_mode, axis=0)

        mat[:, : isyns2.shape[1]] = isyns2
    
    path_isyn2 = path / "isyn2"
    if not path_isyn2.exists():
        os.makedirs(path_isyn2)
    
    print("Writing nsc2ram files in isyn2", end="\r")
    for t, vals in enumerate(mat):
        with open(path_isyn2 / f"nsc2ram_{t}.txt", "w+") as f:
            for val in vals:
                f.write(to_hex(val, 4))
                f.write("\n")
    
    # nmpram
    mat = np.zeros((np.shape(model.rec_v_mem)[1], Nrec + Nout), dtype=int)
    vmems = np.array(model.rec_v_mem).T.astype(int)

    # remove all parts where Xylo is in hibernation mode
    mat = np.delete(mat, model.rec_hibernation_mode, axis=0)
    vmems = np.delete(vmems, model.rec_hibernation_mode, axis=0)

    mat[:, : vmems.shape[1]] = vmems
    vmems_out = np.array(model.rec_v_mem_out).T.astype(int)

    # remove all parts where Xylo is in hibernation mode
    vmems_out = np.delete(vmems_out, model.rec_hibernation_mode, axis=0)

    mat[:, Nrec : Nrec + vmems_out.shape[1]] = vmems_out
    
    path_vmem = path / "vmem"
    if not path_vmem.exists():
        os.makedirs(path_vmem)
    
    print("Writing nmpram files in vmem", end="\r")
    for t, vals in enumerate(mat):
        with open(path_vmem / f"nmpram_{t}.txt", "w+") as f:
            for i_neur, val in enumerate(vals):
                f.write(to_hex(val, 4))
                f.write("\n")
    
    # basic config
    print("Writing basic_config.json", end="\r")
    with open(path / "basic_config.json", "w+") as f:
        config = {}
    
        # number of neurons
        config["IN"] = len(model.synapses_in)
        config["RSN"] = len(model.synapses_rec)
    
        # determine output size by getting the largest target neuron id
        syns = np.hstack(model.synapses_out)
        config["ON"] = int(np.max([s.target_neuron_id for s in syns]) + 1)
    
        # bit shift values
        config["IWBS"] = model.weight_shift_inp
        config["RWBS"] = model.weight_shift_rec
        config["OWBS"] = model.weight_shift_out
    
        # expansion neurons
        #if num_expansion is not None:
        #    config["IEN"] = num_expansion

        config['time_resolution_wrap'] = 0
    
        # dt
        config["DT"] = dt
    
        # n_syns
        config["N_SYNS"] = n_syns
    
        # aliasing
        if max([len(a) for a in model.aliases]) > 0:
            config["RA"] = True
        else:
            config["RA"] = False

        config['BIAS'] = any([n.has_bias for n in model.iaf_neurons]) or any([n.has_bias for n in model.iaf_neurons_out])
    
        json.dump(config, f)


def plot_activity(model, inp_spks):
    import matplotlib.pyplot as plt
    
    # plot everything
    time = np.arange(0, len(inp_spks))

    fig = plt.figure(figsize=(16, 10))

    ax1 = fig.add_subplot(4, 2, 1)
    ax1.set_title("Input Spikes")
    ax1.imshow(np.transpose(inp_spks), aspect='auto', interpolation='None')

    ax2 = fig.add_subplot(4, 2, 2, sharex=ax1)
    ax2.set_title("Recurrent Synaptic Currents")
    ax2.plot(time, np.transpose(model.rec_i_syn))
    ax2.plot(time, np.transpose(model.rec_i_syn2))

    ax3 = fig.add_subplot(4, 2, 3, sharex=ax1)
    ax3.set_title("Recurrent Spikes")
    ax3.imshow(np.transpose(model.rec_recurrent_spikes), aspect='auto', interpolation='None')

    ax4 = fig.add_subplot(4, 2, 4, sharex=ax1)
    ax4.set_title("Recurrent Membrane Potentials")
    ax4.plot(time, np.transpose(model.rec_v_mem))

    ax5 = fig.add_subplot(4, 2, 5, sharex=ax1)
    ax5.set_title("Output Spikes")
    ax5.imshow(np.transpose(model.rec_out_spikes), aspect='auto', interpolation='None')
    ax5.set_xlabel('Time (s)')

    ax6 = fig.add_subplot(4, 2, 6, sharex=ax1)
    ax6.set_title("Output Synaptic Currents")
    ax6.plot(time, np.transpose(model.rec_i_syn_out))

    ax8 = fig.add_subplot(4, 2, 8, sharex=ax1)
    ax8.set_title("Output Membrane Potentials")
    ax8.plot(time, np.transpose(model.rec_v_mem_out))
    ax8.set_xlabel('Time (s)')
    
    plt.tight_layout()
    plt.show(block=True)
