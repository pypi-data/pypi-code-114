import argparse
import csv
import pprint

from haystack.nodes import FARMReader, TfidfRetriever, QuestionGenerator
from haystack.document_stores import InMemoryDocumentStore
from haystack.pipelines import QuestionAnswerGenerationPipeline
from haystack.utils import convert_files_to_dicts
from tqdm import tqdm


def init_argparse():
    parser = argparse.ArgumentParser(
        usage="%(prog)s [OPTION] [VALUE]...",
        description="Transform all documents (pdf, txt, doc) from a folder to a anki deck"
    )
    parser.add_argument(
        "-v", "--version", action="version",
        version=f"{parser.prog} version 0.1.15"
    )

    parser.add_argument("-i", "--input",
                        help="specify a folder with the documents for processing",
                        required=True
                        )

    return parser.parse_args()


def main():
    args = init_argparse()

    input_folder = args.input

    document_store = InMemoryDocumentStore()

    dicts = convert_files_to_dicts(dir_path=input_folder, split_paragraphs=True)

    document_store.write_documents(dicts)

    reader = FARMReader(model_name_or_path="deepset/roberta-base-squad2", use_gpu=True)

    question_generator = QuestionGenerator()

    qag_pipeline = QuestionAnswerGenerationPipeline(question_generator, reader)

    questions_answers = []
    for idx, document in enumerate(tqdm(document_store)):
        print(f"\n * Generating questions and answers for document {idx}: {document.content[:100]}...\n")
        results = qag_pipeline.run(documents=[document])

        for pair in results["results"]:
            pprint.pprint(pair)
            print("########################")
            try:
                print(pair['query'])
                print(pair["answers"][0].answer)
                questions_answers.append(
                    [
                        pair['query'],
                        pair["answer"][0].answer
                    ]
                )
            except IndexError:
                pass
            except KeyError:
                pass
            except Exception:
                print("hummm i need to debug this")
            continue

    print("Writing the csv file for import into anki ...")
    with open('matrixbrain.csv', 'w') as f:
        write = csv.writer(f)
        write.writerows(questions_answers)
    print("Deck created: MatrixDeck.csv")

