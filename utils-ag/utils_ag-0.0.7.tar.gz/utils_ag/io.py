
def select_from_list(options):
    from pyfzf.pyfzf import FzfPrompt
    fzf = FzfPrompt()
    answer = fzf.prompt(options, fzf_options="--cycle --layout reverse --border rounded")
    if len(answer) == 0:
        return None
    return answer[0]