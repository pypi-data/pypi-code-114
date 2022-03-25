from typing import List
from feyn import Model
from feyn._context import Context
from feyn._program import Program


def get_identity_model(inputs=["x"], output="y") -> Model:
    # Returns a model that predicts it's input, but scales it down and up internally
    ctx = Context()
    ctx.registers += sorted([output] + inputs)

    output_code = ctx.get_codes(arity=0, names=[output])[0]
    input_codes = ctx.get_codes(arity=0, names=inputs)

    program = Program([output_code, input_codes[0]], qid=1, autopad=True)
    model = ctx.to_model(program, output, {})
    assert model is not None

    model[0].params.update({"scale": 1, "w":2.0, "bias": +1})
    model[1].params.update({"scale": 1, "w":0.5, "bias": -.5})
    return model


def get_unary_model(inputs=["x"], output="y", fname="exp", stypes={}) -> Model:
    ctx = Context()
    ctx.registers += sorted([output] + inputs)

    output_code = ctx.get_codes(arity=0, names=[output])[0]
    input_codes = ctx.get_codes(arity=0, names=inputs)

    opcode = ctx.lookup_by_fname(fname, 1)
    program = Program([output_code, opcode, input_codes[0]], qid=1, autopad=True)
    model = ctx.to_model(program, output, stypes)
    assert model is not None

    return model


def get_simple_binary_model(inputs, output, stypes={}) -> Model:
    ctx = Context()
    ctx.registers += sorted([output] + inputs)

    output_code = ctx.get_codes(arity=0, names=[output])[0]
    input_codes = ctx.get_codes(arity=0, names=inputs)

    program = Program([output_code, 2000, input_codes[0], input_codes[1]], qid=1, autopad=True)
    model = ctx.to_model(program, output, stypes)
    assert model is not None

    return model

def get_complicated_binary_model(inputs, output, fname, stypes={}) -> Model:
    ctx = Context()
    ctx.registers += sorted([output] + inputs)

    output_code = ctx.get_codes(arity=0, names=[output])[0]
    input_codes = ctx.get_codes(arity=0, names=inputs)

    opcode = ctx.lookup_by_fname(fname, 1)

    program = Program([output_code, 2000, opcode, input_codes[0], input_codes[1]], qid=1, autopad=True)
    model = ctx.to_model(program, output, stypes)
    assert model is not None

    return model


def get_ternary_model(inputs, output, stypes={}) -> Model:
    ctx = Context()
    ctx.registers += sorted([output] + inputs)

    output_code = ctx.get_codes(arity=0, names=[output])[0]
    input_codes = ctx.get_codes(arity=0, names=inputs)

    program = Program([output_code, 2000, 2001, input_codes[0], input_codes[1], input_codes[2]], qid=1, autopad=True)
    model = ctx.to_model(program, output, stypes)
    assert model is not None

    return model


def get_quaternary_model(inputs, output, stypes={}) -> Model:
    ctx = Context()
    ctx.registers += sorted([output] + inputs)

    output_code = ctx.get_codes(arity=0, names=[output])[0]
    input_codes = ctx.get_codes(arity=0, names=inputs)

    program = Program([output_code, 2000, 2002, 2002, input_codes[0], input_codes[1], input_codes[2], input_codes[3]], qid=1, autopad=True)
    model = ctx.to_model(program, output, stypes)
    assert model is not None

    return model


def get_n_unique_models(n: int) -> List[Model]:
    ctx = Context()
    ctx.registers += ["y", "a"] + [f"x{i}" for i in range(n)]

    models: List[Model] = []
    for i in range(n):
        codes = [10000, 2000, 10001, 10002 + i]

        program = Program(codes, qid=1, autopad=True)
        model = ctx.to_model(program, "y")
        assert model is not None

        models.append(model)

    return models


def get_fixed_model() -> Model:
    """
    Used in test_shap and test_importance_table.
    They expect specific states for the registers to be able to test against fixed shap values.
    """
    model = get_simple_binary_model(["x", "y"], "z")

    model[0].params.update({"scale": 1.7049912214279175, "w": 0.6332976222038269, "bias": 0.0})
    model[2].params.update({"scale": 1.0, "w": 0.9261354804039001, "bias": 0.18130099773406982})
    model[3].params.update({"scale": 1.0, "w": 2.7783772945404053, "bias": -0.18129898607730865})
    return model


def get_specific_model(inputs: List[str], output: str, equation: str) -> Model:
    """Auxiliary function for generating a model by an equation using the query language"""

    ctx = Context()
    ctx.registers += inputs
    ctx.registers.append(output)

    program = Program(ctx.query_to_codes(output, equation)[1], -1, True)
    model = ctx.to_model(program, output)
    assert model is not None

    return model
