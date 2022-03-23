import json
from argparse import ArgumentParser
from functools import partial
from itertools import chain
from pathlib import Path
from typing import Dict

from tdm.datamodel import TalismanDocument
from tdm.datamodel.fact import ConceptFact, ValueFact

from talisman_tools.configure import load_or_configure
from talisman_tools.plugin import ReaderPlugins
from talisman_tools.processor.quality_test.disambiguation_quality import evaluate_dmb
from talisman_tools.processor.quality_test.evaluation import evaluate_nerc, evaluate_relext, evaluate_relext_upper_bound
from talisman_tools.servers.helper import add_extra_cli_argumants
from tp_interfaces.helpers.io import read_json


def print_scores(scores: Dict[str, dict]):
    def round_floats(val, precision=4):
        if isinstance(val, float):
            return round(val, precision)
        if isinstance(val, dict):
            return {k: round_floats(v) for k, v in val.items()}
        raise ValueError

    def stringify_keys(d: dict):
        ret = {}
        for key, val in d.items():
            if isinstance(key, (tuple, frozenset)):
                key = str(key)
            if isinstance(val, dict):
                val = stringify_keys(val)

            ret[key] = val

        return ret

    json_repr = json.dumps(stringify_keys(round_floats(scores)), sort_keys=True, indent=2)
    print(json_repr)


def keep_nerc(doc: TalismanDocument) -> TalismanDocument:
    facts = chain(
        map(lambda f: f.with_changes(value=tuple()), doc.filter_facts(ConceptFact)),  # TODO: replace value with None instead of empty tuple
        doc.filter_facts(ValueFact)
    )
    return doc.without_facts().with_facts(facts)


def clear_values(doc: TalismanDocument) -> TalismanDocument:
    return doc.with_facts(
        map(lambda f: f.with_changes(value=tuple()), doc.filter_facts(ConceptFact)),  # TODO: replace value with None instead of empty tuple
    )


mode = {
    "all": lambda doc: doc.without_facts(),  # start from clear document (no facts provided)
    "relext": keep_nerc,  # start from document with concept and value facts (no link facts, no fact values)
    "dmb": clear_values,  # start from document with facts without values
}

evaluators = {
    'all': {
        'nerc': evaluate_nerc,
        'relext': evaluate_relext,
        'relext-upper-bound': evaluate_relext_upper_bound,
        'dmb': partial(evaluate_dmb, at_ks=[1, 2, 3])  # TODO: make configurable from cli
    },
    'relext': {
        'relext': evaluate_relext,
        'relext-upper-bound': evaluate_relext_upper_bound,
        'dmb': partial(evaluate_dmb, at_ks=[1, 2, 3])  # TODO: make configurable from cli
    },
    'dmb': {
        'dmb': partial(evaluate_dmb, at_ks=[1, 2, 3])  # TODO: make configurable from cli
    }
}


def main():
    readers = ReaderPlugins.flattened

    parser = ArgumentParser()
    parser.add_argument('eval_mode', type=str, choices=set(mode), metavar='<evaluation mode>')

    parser.add_argument('reader', metavar='<reader type>', choices=set(readers.keys()))
    parser.add_argument('docs_path', type=str, metavar='<test docs path>')

    parser.add_argument('-models', nargs='+', type=Path, metavar='<model path>', default=[])
    parser.add_argument('-cfg', nargs='+', type=Path, metavar='<model json config path>', default=[])

    parser.add_argument('-config', type=Path, metavar='<document processing config path>')

    extra_actions = add_extra_cli_argumants(parser)

    args = parser.parse_args()

    for action in extra_actions:
        action(args)

    gold_docs = tuple(readers[args.reader](Path(args.docs_path)).read())  # assuming only facts matter
    actual_docs = tuple(map(mode[args.eval_mode], gold_docs))

    processor = load_or_configure(args.models, args.cfg)

    with processor:
        processor_config_type = processor.config_type
        config = processor_config_type.parse_obj(read_json(args.config)) if args.config else processor_config_type()
        actual_docs = processor.process_docs(actual_docs, config)

    scores = {name: evaluate(actual_docs, gold_docs) for name, evaluate in evaluators[args.eval_mode].items()}

    print_scores(scores)


if __name__ == '__main__':
    main()
