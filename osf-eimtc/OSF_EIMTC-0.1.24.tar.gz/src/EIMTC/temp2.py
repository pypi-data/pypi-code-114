from third_party.tshark.dataframe_utils import add_packet_clump_num_column, add_packet_directions_column, convert_to_correct_dtypes, drop_lengthless_tls_records, get_tls_clump_stats, get_tls_record_stats, groupby_biflows, merge_df_by_biflows, read_tshark_csv_output
tshark_output_filepath = './temp/tshark_outfile.csv'
df = read_tshark_csv_output(tshark_output_filepath)
df = drop_lengthless_tls_records(df)
if df.empty:
    tls_features_per_session = None
else:   
    df = convert_to_correct_dtypes(df)
    df = add_packet_directions_column(df)
    df = add_packet_clump_num_column(df)
    record_tls_per_session = get_tls_record_stats(df)
    clump_stats_per_session = get_tls_clump_stats(df)
    tls_features_per_session = record_tls_per_session.join(clump_stats_per_session)