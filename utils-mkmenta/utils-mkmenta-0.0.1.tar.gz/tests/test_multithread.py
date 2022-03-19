from mkutils import run_multithread


def _function(x):
    return x.split(' ')


def test_run_multithread():
    run_multithread(["Lorem ipsum dolor sit amet, consectetur adipiscing elit.",
                     "Etiam lectus sapien, lobortis quis ultrices quis, commodo vitae erat.",
                     "Sed eu aliquet nunc."],
                    _function, threads=2)
