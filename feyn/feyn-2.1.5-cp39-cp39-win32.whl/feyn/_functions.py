import numpy as np

# TODO: This breaks some qepler philosophies, the model needs to know what trainer
# was used to replicate the function protections of that trainer.
import _qepler


def cat_func(params, vcat):
    cat_weights = dict(params["categories"])
    return np.array([cat_weights.get(c, 0.0) for c in vcat]) + params["bias"]

def in_linear_func(params, v):
    if not np.isfinite(v).all():
        raise ValueError("nan values in input")
    return (v - params["scale_offset"]) * params["scale"] * params["w"] + params["bias"]

def exp_protected(params, v):
    ix_bad = v > _qepler.EXP_MAX
    v[ix_bad] = _qepler.EXP_MAX
    return np.exp(v)

def inverse_protected(params, v):
    ix_bad = np.abs(v) < _qepler.DIVISOR_ABSMIN
    ix_bad_pos = ix_bad & (v > 0)
    ix_bad_neg = ix_bad & (v <= 0)
    v[ix_bad_pos] = _qepler.DIVISOR_ABSMIN
    v[ix_bad_neg] = -_qepler.DIVISOR_ABSMIN
    return 1 / v

def log_protected(params, v):
    ix_bad = v < _qepler.LOG_MIN
    v[ix_bad] = _qepler.LOG_MIN
    return np.log(v)

def sqrt_protected(params, v):
    ix_bad = v < _qepler.SQRT_MIN
    v[ix_bad] = _qepler.SQRT_MIN
    return np.sqrt(v)

def squared_protected(params, v):
    ix_bad = v > _qepler.SQUARED_MAX
    v[ix_bad] = _qepler.SQUARED_MAX
    return v * v

FNAME_MAP = {
    "in:cat": {
        "paramcount": 0,
        "func": cat_func
    },
    "in:linear": {
        "paramcount": 0,
        "func": in_linear_func
    },
    "out:linear": {
        "paramcount": 0,
        "func": lambda params, v: (v*params["w"] + params["bias"]) * params["scale"]
    },
    "out:lr": {
        "paramcount": 0,
        "func": lambda params, v: 1 / (1 + np.exp(-(v*params["w"]+params["bias"])))
    },

    "exp": {
        "opcode": 1000,
        "paramcount": 1,
        "func": lambda params, v: exp(v),
        "func_protected": exp_protected
    },
    "gaussian1": {
        "opcode": 1001,
        "paramcount": 3,
        "func": lambda params, v: np.exp(-(v*v / 0.5))
    },
    "inverse": {
        "opcode": 1002,
        "paramcount": 1,
        "func": lambda params, v: 1/v,
        "func_protected": inverse_protected
    },
    "linear": {
        "opcode": 1003,
        "paramcount": 2,
        "func": lambda params, v: v*params["w"] + params["bias"]
    },
    "log": {
        "opcode": 1004,
        "paramcount": 1,
        "func": lambda params, v: np.log(v),
        "func_protected": log_protected
    },
    "sqrt": {
        "opcode": 1005,
        "paramcount": 1,
        "func": lambda params, v: np.sqrt(v),
        "func_protected": sqrt_protected
    },
    "squared": {
        "opcode": 1006,
        "paramcount": 1,
        "func": lambda params, v: v*v,
        "func_protected": squared_protected
    },
    "tanh": {
        "opcode": 1007,
        "paramcount": 1,
        "func": lambda params, v: np.tanh(v)
    },

    "add": {
        "opcode": 2000,
        "paramcount": 1,
        "func": lambda params, v1, v2: v1+v2
    },
    "gaussian2": {
        "opcode": 2001,
        "paramcount": 4,
        "func": lambda params, v1, v2: np.exp(- (v1*v1 / 0.5 + v2*v2 / 0.5))
    },
    "multiply": {
        "opcode": 2002,
        "paramcount": 2,
        "func": lambda params, v1, v2: v1*v2
    },
}

OPCODE_MAP = {desc["opcode"]: fname for fname, desc in FNAME_MAP.items() if "opcode" in desc}
