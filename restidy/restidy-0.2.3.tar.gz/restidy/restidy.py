import os
import sys
import argparse
import pandas as pd
import numpy as np


def args_parse():
    "Parse the input argument, use '-h' for help."
    parser = argparse.ArgumentParser(
        usage='restidy -i < resfinder4.0_result_directory > -o < output_file_directory > \n\nAuthor: Qingpo Cui(SZQ Lab, China Agricultural University)')
    parser.add_argument("-i", help="<input_path>: resfinder_result_path")
    parser.add_argument("-o", help="<output_file_path>: output_file_path")
    if len(sys.argv) == 1:
        parser.print_help(sys.stderr)
        sys.exit(1)
    return parser.parse_args()


def cate_mapping_dict(file):
    """
    create mapping dict {"gene"=>"Resistance Category"}
    """
    df_map = pd.read_csv(file, names=['Database', 'Gene'], sep='\t')
    mapping_dict = dict(zip(df_map['Gene'], df_map['Database']))
    return mapping_dict


def drug_mapping_dict(file):
    """
    create mapping dict {"gene"=>"Antibiotics"}
    """
    df_drug = pd.read_csv(file, sep='\t')
    drug_dict = dict(zip(df_drug['Gene'], df_drug['Phenotype']))
    return drug_dict


# def drug_parse(df):
#     # print("Input Dataframe")
#     # print(df)
#     df1 = df.groupby('Strain')['Drugs'].apply(
#         lambda x: ', '.join(x.unique())).to_frame()
#     # print(df1)
#     df2 = df1['Drugs'].str.split(', ', expand=True).stack().to_frame().rename(
#         columns={0: 'Drug'}).reset_index(level=1, drop=True).reset_index()
#     df3 = df2.groupby(['Strain', 'Drug'])['Drug'].size(
#     ).to_frame().rename(columns={'Drug': 'Count'})
#     df3.reset_index(inplace=True)
#     df4 = df3.pivot_table(index='Strain', columns='Drug', values='Count')
#     df4[df4.notnull()] = 1
#     return df4


def join(f):
    return os.path.join(os.path.dirname(__file__), f)


def res_concate(path):
    df_point_final = pd.DataFrame()
    df_resistance_final = pd.DataFrame()
    # print(path)
    for file in os.listdir(path):
        file_path = os.path.join(path, file)
        if os.path.isdir(file_path):
            point_file = os.path.join(file_path, 'PointFinder_results.txt')
            resistance_file = os.path.join(
                file_path, 'ResFinder_results_tab.txt')
            if os.path.isfile(point_file):
                # print(point_file)
                df_point_tmp = pd.read_csv(point_file, sep='\t')
                df_point_tmp['Strain'] = file
                df_point_final = pd.concat([df_point_final, df_point_tmp])
            if os.path.isfile(resistance_file):
                # print(resistance_file)
                df_resistance_tmp = pd.read_csv(resistance_file, sep='\t')
                df_resistance_tmp['Strain'] = file
                df_resistance_final = pd.concat(
                    [df_resistance_final, df_resistance_tmp])
    # print(df_point_final)
    return df_point_final, df_resistance_final


def resistance_count(df_resistance, df_point):
    """
    count the number of isolates resistance to different drugs
    df_resistance should cotain the drugs column
    """
    df1 = df_resistance[['Strain', 'Resistance gene', 'Drugs']].copy()
    df1.rename(columns={'Resistance gene': 'AMR'}, inplace=True)
    df1.reset_index(drop=True, inplace=True)
    df1_index = df1['Drugs'].str.split(',', expand=True).stack(
    ).to_frame().reset_index(level=1, drop=True)
    df1_tmp = df1.join(df1_index).rename(columns={0: 'Drug'})
    df2 = df_point[['Strain', 'Mutation', 'Resistance']].copy()
    df2.rename(columns={'Mutation': 'AMR',
                        'Resistance': 'Drugs'}, inplace=True)
    df2.reset_index(drop=True, inplace=True)
    df2_index = df2['Drugs'].str.split(',', expand=True).stack(
    ).to_frame().reset_index(level=1, drop=True)
    df2_tmp = df2.join(df2_index).rename(columns={0: 'Drug'})
    df3 = pd.concat([df1_tmp, df2_tmp])
    df3_tmp = df3.groupby(['Strain', 'Drug'])['Drug'].size(
    ).to_frame().rename(columns={'Drug': 'Count'})
    df3_tmp.reset_index(inplace=True)
    df4 = df3_tmp.pivot_table(index='Strain', columns='Drug', values='Count')
    df4[df4.notna()] = 1
    df_drug_pivot = df4.copy()
    df_rr_count = df4.sum().to_frame().rename(
        columns={0: 'No. of resistance isolates'})
    return df_drug_pivot, df_rr_count


def main():
    args = args_parse()
    input_path = args.i
    input_path = os.path.abspath(input_path)

    # check if the output directory exists
    if not os.path.exists(args.o):
        os.mkdir(args.o)

    # create output files handler
    output_file_path = os.path.abspath(args.o)
    output_resistance_file = os.path.join(
        output_file_path, 'resfinder_sum.csv')
    output_point_file = os.path.join(output_file_path, 'point_sum.csv')
    drug_output_file = os.path.join(output_file_path, 'drug_pivot.csv')
    resis_count_file = os.path.join(
        output_file_path, 'resistance_statistic.csv')

    # print info
    print('The results will be write into following files:\n')
    print(output_resistance_file + '\n')
    print(output_point_file + '\n')
    print(drug_output_file + '\n')
    print(resis_count_file + '\n')

    # Get the directory of script and read mapping file
    cate_mapping_file = join("gene_db_mapping.tsv")
    cate_map_dict = cate_mapping_dict(cate_mapping_file)

    # process drugs parsing method
    drug_mapping_file = join("gene_drugs_mapping.tsv")
    drug_map_dict = drug_mapping_dict(drug_mapping_file)

    df_point, df_resistance = res_concate(input_path)

    # Generate acquired resistance genes dataframe with drugs column
    df_resistance['Drugs'] = df_resistance['Resistance gene'].map(
        drug_map_dict)

    # Generate the pivot table of drugs which combined with acquired and mutation resistance genes
    df_pivot_drugs, df_rr_statistics = resistance_count(
        df_resistance, df_point)

    # mapping resistance gene to database
    df_resistance['Database'] = df_resistance['Resistance gene'].map(
        cate_map_dict)

    # Generate the pivot table acquired resistance genes
    df_resistance_final = df_resistance.pivot_table(index='Strain', columns=[
        'Database', 'Resistance gene'], values='Identity', aggfunc=lambda x: ','.join(map(str, x)))

    # Process point mutation results
    df_point_final = df_point.groupby(['Strain'])['Mutation'].apply(
        lambda x: ','.join(x)).to_frame()

    # print(df_final)
    df_resistance_final.to_csv(output_resistance_file)
    df_point_final.to_csv(output_point_file)
    df_pivot_drugs.to_csv(drug_output_file)
    df_rr_statistics.to_csv(resis_count_file)


if __name__ == '__main__':
    main()
