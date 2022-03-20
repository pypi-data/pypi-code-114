from .symbolic import Symbolic, strip_symbolic
from .calls import Call, Lazy

# Pipe ========================================================================

class Pipeable:
    """Enable function composition through the right bitshift (>>) operator.

    Parameters
    ----------
    f :
        A function to be called.
    calls : sequence, optional
        A list-like of functions to be called, with each result chained into the next.

    Examples
    --------

    >>> f = lambda x: x + 1

    Eager evaluation:

    >>> 1 >> Pipeable(f)
    2

    Defer to a pipe:

    >>> p = Pipeable(f) >> Pipeable(f)
    >>> 1 >> p
    3

    >>> p_undo = p >> (lambda x: x - 3)
    >>> 1 >> p_undo
    0

    >>> from siuba.siu import _
    >>> p_undo_sym = p >> (_ - 3)
    >>> 1 >> p_undo_sym
    0

    """

    def __init__(self, f = None, calls = None):
        # symbolics like _.some_attr need to be stripped down to a call, because
        # calling _.some_attr() returns another symbolic.
        f = strip_symbolic(f)

        if f is not None:
            if calls is not None: raise Exception()
            self.calls = [f]
        elif calls is not None:
            self.calls = calls

    def __rshift__(self, x) -> "Pipeable":
        """Defer evaluation when pipe is on the left (lazy piping)."""
        if isinstance(x, Pipeable):
            return Pipeable(calls = self.calls + x.calls)
        elif isinstance(x, (Symbolic, Call)):
            call = strip_symbolic(x)
            return Pipeable(calls = self.calls + [call])
        elif callable(x):
            return Pipeable(calls = self.calls + [x])

        raise Exception()

    def __rrshift__(self, x):
        """Potentially evaluate result when pipe is on the right (eager piping).

        This function handles two cases:
            * callable >> pipe -> pipe
            * otherewise, evaluate the pipe

        """
        if isinstance(x, (Symbolic, Call)):
            call = strip_symbolic(x)
            return Pipeable(calls = [call] + self.calls)
        elif callable(x):
            return Pipeable(calls = [x] + self.calls)

        return self(x)

    def __call__(self, x):
        """Evaluate a pipe and return the result.

        Parameters
        ----------
        x :
            An object to be passed into the first function in the pipe.

        """
        res = x
        for f in self.calls:
            res = f(res)
        return res


def create_pipe_call(obj, *args, **kwargs) -> Pipeable:
    """Return a Call of a function on its args and kwargs, wrapped in a Pipeable."""
    first, *rest = args
    return Pipeable(Call(
            "__call__",
            strip_symbolic(obj),
            strip_symbolic(first),
            *(Lazy(strip_symbolic(x)) for x in rest),
            **{k: Lazy(strip_symbolic(v)) for k,v in kwargs.items()}
            ))


