import os
import csv
import sys

BASE_SOURCE_PATH="{}_{}_seed.{}/{}"
BASE_COTRAINED_PATH="{}_{}_seed.{}/{}"

def get_single_result(log_path):
    """
    Get results from single file
    """
    try:
        with open(os.path.join(log_path, "log.txt"), 'r') as f:
            lines = f.readlines()
    except:
        return

    metrics_start = None

    for i, line in enumerate(lines):
        if "Eval on test split" in line:
            metrics_start = i+1
            break
    
    if not metrics_start:
        return
    
    metrics = {}
    for line in lines[metrics_start:]:
        metric_line = line.strip()

        # contine searching until empty line
        if metric_line:
            if len(metric_line.split(": ")) == 2:
                metric, value = metric_line.split(": ")
                metrics[metric] = float(value)
        else:
            break

    return metrics

def get_results(path_prefix, source_tasks, target_task, model, dataset, seed, fewshot_percent):
    source_prefix = "PRETRAINED" if not fewshot_percent else f"PRETRAINED_{fewshot_percent}_FEWSHOT"
    datasets = [f"{dataset}.{source_task}" for source_task in source_tasks]
    datasets = "_".join(datasets)
    original_target_path = BASE_SOURCE_PATH.format(os.path.join(path_prefix,source_prefix), f"{dataset}.{target_task}", seed, model)
    source_path = BASE_SOURCE_PATH.format(os.path.join(path_prefix, source_prefix), datasets, seed, model)
    results = {}
    results[target_task] = get_single_result(original_target_path)
    
    target_prefix = "FINETUNED" if not fewshot_percent else f"FINETUNED_{fewshot_percent}_FEWSHOT"
    base_target_path=f"{target_prefix}_{dataset}.{target_task}_seed.{seed}"
    target_path = os.path.join(source_path,base_target_path)
    results["_".join(source_tasks)] = get_single_result(target_path)


    # get cotraining results
    cotrained_prefix = "COTRAINED" if not fewshot_percent else f"COTRAINED_{fewshot_percent}_FEWSHOT"
    datasets += f"_{dataset}.{target_task}"
    cotrain_target_path = BASE_COTRAINED_PATH.format(os.path.join(path_prefix,cotrained_prefix), datasets, seed, model)
    # first, get cotraining only results
    results["COTRAINED"] = get_single_result(cotrain_target_path)
    # then, get cotraining/finetune results
    target_prefix = "FINETUNED" if not fewshot_percent else f"FINETUNED_{fewshot_percent}_FEWSHOT"
    base_target_path=f"{target_prefix}_{dataset}.{target_task}_seed.{seed}"
    finetune_target_path = os.path.join(cotrain_target_path,base_target_path)
    results['COTRAINED_FINETUNED'] = get_single_result(finetune_target_path)
    return results

def print_results(results):
    """
    Print results to terminal
    """
    for k, v in results.items():
        print(k)
        for k1, v1 in v.items():
            print(f"\t{k1}: {v1}")
        print()

def convert_results_to_table(results, target_task, aggregation="average"):
    """
    Convert results to table

    Args:
        results (dict): results dictionary
        aggregation (str): aggregation method, either average or sum
    """
    headers = []
    rows = []
    columns = []


    for seed, result in results.items():
        headers.append(seed)
        column = []
        for source, metrics in result.items():
            if metrics:
                aggregate_value = sum(metrics.values()) if aggregation == "sum" else sum(metrics.values())/len(metrics)
                aggregate_value = round(aggregate_value, 4)
            else:
                aggregate_value = "N/A"
            column.append(aggregate_value)
        columns.append(column)
    return columns,headers

def convert_columns_to_differences(columns):
    for column in columns:
        for i, _ in enumerate(column):
            if i == 0:
                continue
            column[i] = column[i] - column[0] if (column[i] != "N/A" and column[0] != "N/A") else "N/A"
            column[i] = round(column[i], 4) if column[i] != "N/A" else "N/A"
    return columns

def save_results_as_csv(columns, headers, row_headers, save_path):
    """
    Save results as table in csv format
    """

    rows = list(zip(*columns))
    with open(save_path, 'w') as f:
        writer = csv.writer(f)
        writer.writerow(["Train method\Seed"] + headers)
        for header, row in zip(row_headers, rows):
            writer.writerow([header, *row])

if __name__ == "__main__":
    if len(sys.argv) < 8:
        print("Usage: python3 results_analysis.py <path_prefix> <source_tasks> <target_task> <model> <dataset> <seeds> [<fewshot_percent>]")
        print('Example: python3 results_analysis.py logs_and_models "reading_comprehension question_answering relation_extraction" "character_identification" t5-base DailyDialog "42 100" 0.1')
        exit(1)

    path_prefix = sys.argv[1]
    source_tasks = sys.argv[2].split()
    target_task = sys.argv[3]
    model = sys.argv[4]
    dataset = sys.argv[5]
    seeds = sys.argv[6].split()
    fewshot_percent = None if len(sys.argv) < 8 else float(sys.argv[7])

    results = {}
    for seed in seeds:
        results[seed] = get_results(path_prefix,source_tasks,target_task,model,dataset,seed,fewshot_percent)

    print(f"Results for:\n\t{model}\n\t{target_task} on {dataset}")

    print_results(results)

    base_save_path = os.path.join(path_prefix, f"TARGETED_{model}_{dataset}_source.{'.'.join(source_tasks)}_target.{target_task}")
    row_headers = list(results[seeds[0]].keys())
    columns, headers = convert_results_to_table(results, target_task)
    save_results_as_csv(columns, headers, row_headers, base_save_path+"_results.csv")
    columns = convert_columns_to_differences(columns)
    save_results_as_csv(columns, headers, row_headers, base_save_path+"_results_differences.csv")
