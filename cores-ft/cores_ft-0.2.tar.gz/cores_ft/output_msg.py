def mount_msg_output(freq, temp):
    msg = []

    if freq and temp:
        for (k, f), t in zip(freq.items(), temp.values()):
            msg.append(f'| {k} : {f:.4f} Ghz {t} |')

    elif not temp:
        for (k, f) in freq.items():
            msg.append(f'| {k} : {f:.4f} Ghz |')

    return '\n'.join(msg)
