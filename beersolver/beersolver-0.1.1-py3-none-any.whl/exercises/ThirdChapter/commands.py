import logging
import sys
import numpy as np
import exercises.ThirdChapter.csix as csix
import configparser
import click
from utils.log import InternalLogger

def get_float(value: str):
    """
    simplifies processing of slashes on numbers
    :param value:
    :return:
    """
    # TODO Analyse probable security flaw with eval
    return eval(value)


def float_ndarray(value):
    new_value = []
    for val in value:
        # TODO Verify if this way of conversion is ok.
        new_value.append(float(eval(val)))

    new_value = tuple(new_value)
    return np.array(new_value)


def float_ndarray_callback(ctx, param, value):
    # TODO Analyse probable security flaw with eval
    if not value or ctx.resilient_parsing:
        return

    return float_ndarray(value)


def get_three_dimensional_array(point: str) -> np.ndarray:
    """
    Function to easily get a ndarray to use
    :param point: what point it refers to
    :return:
    """
    position_x = click.prompt(f"{point.capitalize()}[x]", value_proc=get_float)
    position_y = click.prompt(f"{point.capitalize()}[y]", value_proc=get_float)
    position_z = click.prompt(f"{point.capitalize()}[z]", value_proc=get_float)
    position = np.array([position_x, position_y, position_z])

    return position


def get_config_from_file(path: str):
    """
    Gets parameters from a file
    :param path: location of the configuration file
    :return:
    """
    parser = configparser.ConfigParser()
    parser.read(path)

    config = {}
    for sect in parser.sections():
        for k, v in parser.items(sect):
            config[k] = v
    return config


@click.group()
@click.option("--debug", is_flag=True, help="Start debugging mode")
@click.pass_context
def cli(ctx, debug):
    if debug:
        print("Debugging mode is ON")
        logger = InternalLogger(debug)
    else:
        logger = InternalLogger()

    ctx.obj = logger


@cli.command()
@click.pass_obj
@click.option('--position_a', '--pos-a', nargs=3, type=click.UNPROCESSED, callback=float_ndarray_callback,
              help='Position A in format x y z (Required)')
@click.option('--position_e', '--pos-e', nargs=3, type=click.UNPROCESSED, callback=float_ndarray_callback,
              help='Position E in format x y z (Required)')
@click.option('--position_c', '--pos-c', nargs=3, type=click.UNPROCESSED, callback=float_ndarray_callback,
              help='Position C in format x y z (Required)')
@click.option('--lambda_ab', '-lab', nargs=3, type=click.UNPROCESSED, callback=float_ndarray_callback,
              help='Position C in format x y z (Required)')
@click.option('--lambda_cd', '-lcd', nargs=3, type=click.UNPROCESSED, callback=float_ndarray_callback,
              help='Position C in format x y z (Required)')
@click.option('--upper_range', '-ur', type=float,
              help='upper part of the range that determines the size of A and the size C')
@click.option('--lower_range', '-lr', type=float,
              help='Lower part of the range that determines the size of A and the size C')
@click.option('--step', type=float,
              help='Step to move on the range, also determines the precision of the answer')
@click.option('--input', '-i', type=click.Path(exists=True),
              help='Get information for the exercise from input file. WARNING: THIS '
                   'CONFIGURATION TAKES PRECEDENCE OVER THE OTHER ARGUMENTS')
@click.option('--generate_config', '--gen', '-g', is_flag=True, help='Generate skeleton config on the current path', )
def exercise_three_c_6(logger, position_a: np.ndarray, position_e: np.ndarray, position_c: np.ndarray,
                       lambda_ab: np.ndarray,
                       lambda_cd: np.ndarray,
                       upper_range: float, lower_range: float, step: float, input: str, generate_config: bool) -> None:
    """
    3C.6 exercise cli access
    """
    if generate_config:
        problem_instance = csix.ThreeCSix(logger)
        config_parser = problem_instance.get_config()
        with open('example.ini', 'w') as configfile:
            config_parser.write(configfile)

        sys.exit()

    if input:
        config = get_config_from_file(input)
        if config:
            position_a = float_ndarray((config['position_a_x'], config['position_a_y'], config['position_a_z']))
            position_e = float_ndarray((config['position_e_x'], config['position_e_y'], config['position_e_z']))
            position_c = float_ndarray((config['position_c_x'], config['position_c_y'], config['position_c_z']))
            lambda_ab = float_ndarray((config['lambda_ab_x'], config['lambda_ab_y'], config['lambda_ab_z']))
            lambda_cd = float_ndarray((config['lambda_cd_x'], config['lambda_cd_y'], config['lambda_cd_z']))
            upper_range = get_float(config['upper_range'])
            lower_range = get_float(config['lower_range'])
            step = get_float(config['step'])

    if position_a is None:
        position_a = get_three_dimensional_array("a")
    logger.log(f"position_a: {position_a}", logging.DEBUG)

    if position_e is None:
        position_e = get_three_dimensional_array("e")
    logger.log(f"position_e: {position_e}", logging.DEBUG)

    if position_c is None:
        position_c = get_three_dimensional_array("c")
    logger.log(f"position_c: {position_c}", logging.DEBUG)

    if lambda_ab is None:
        lambda_ab = get_three_dimensional_array("lambda_ab")
    logger.log(f"lambda_ab: {lambda_ab}", logging.DEBUG)

    if lambda_cd is None:
        lambda_cd = get_three_dimensional_array("lambda_cd")
    logger.log(f"lambda_cd: {lambda_cd}", logging.DEBUG)

    if upper_range is None:
        upper_range = click.prompt("upper_range", type=float)
    logger.log(f"upper_range: {upper_range}", logging.DEBUG)

    if lower_range is None:
        lower_range = click.prompt("lower_range", type=float)
    logger.log(f"lower_range: {lower_range}", logging.DEBUG)

    if step is None:
        step = click.prompt("step", type=float)
    logger.log(f"step: {step}", logging.DEBUG)

    problem_instance = csix.ThreeCSix(logger, position_a, position_e, position_c, lambda_ab, lambda_cd, upper_range,
                                      lower_range, step)

    logger.log(problem_instance, logging.DEBUG)

    result = problem_instance.solve()

    click.echo("")
    click.echo(f"The shortest distance is '{result.distance}'")
    click.echo(f"With the length of AB being '{result.ab_length}'")
    click.echo(f"With the length of CD being '{result.cd_length}'")
