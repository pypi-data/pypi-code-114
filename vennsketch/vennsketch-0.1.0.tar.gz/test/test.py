from vennsketch import create_blob, check_overlap


def run_check(frac):
    salt = 'TEST_SALT'
    n_samples = 3000
    seed = 62849
    n_tot = 10000
    delta = 1.5

    x = ['id_' + str(i) for i in range(n_tot)]
    blob = create_blob(x, n_samples, seed=seed, salt=salt)

    n_overlap = round(n_tot * frac)
    y = x[0:n_overlap] + ['junk_' + str(i) for i in range(300)]
    perc, perc_error = check_overlap(blob, y, salt=salt)

    expect = frac * 100
    lower = expect - delta
    upper = expect + delta
    assert lower < perc < upper


def test():
    run_check(0.75)
    run_check(0.10)
    run_check(0.56)
    run_check(0.001)
    run_check(0.99)
