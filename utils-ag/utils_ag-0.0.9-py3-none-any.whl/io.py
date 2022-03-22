from pyfzf.pyfzf import FzfPrompt


def select_from_list(options):
    fzf = FzfPrompt()
    answer = fzf.prompt(options, fzf_options="--cycle --layout reverse")
    if len(answer) == 0:
        return None
    return answer[0]


def select_index_from_list(options):
    answer = select_from_list(options)
    if answer is None:
        return None
    return options.index(answer)
