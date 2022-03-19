"""
test.test_get_params
~~~

    * test e2e params against output with

    * boilerplate
    * crispresso2
    * rnaseq
"""
from textwrap import dedent

crispresso_params = dedent('''"""Run `latch execute latch.crispresso2_wf.params.py` to execute this workflow"""

from latch.types import LatchFile
from latch.types import LatchDir

params = {
    "_name": "latch.crispresso2_wf", # Dont edit this value.
    "allele_plot_pcts_only_for_assigned_reference": False, # <class 'bool'>
    "amplicon_min_alignment_score": [0], # typing.Optional[typing.List[int]]
    "amplicon_name": ['foo'], # typing.Optional[typing.List[str]]
    "amplicon_seq": ['foo'], # typing.List[str]
    "annotate_wildtype_allele": "foo", # typing.Optional[str]
    "auto": False, # <class 'bool'>
    "bam_chr_loc": "foo", # typing.Optional[str]
    "bam_input": "foo", # typing.Optional[str]
    "base_editor_output": False, # <class 'bool'>
    "coding_seq": "foo", # typing.Optional[str]
    "conversion_nuc_from": "foo", # <class 'str'>
    "conversion_nuc_to": "foo", # <class 'str'>
    "crispresso1_mode": False, # <class 'bool'>
    "debug": False, # <class 'bool'>
    "default_min_aln_score": 0, # <class 'int'>
    "discard_guide_positions_overhanging_amplicon_edge": False, # <class 'bool'>
    "discard_indel_reads": False, # <class 'bool'>
    "dsODN": "foo", # typing.Optional[str]
    "dump": False, # <class 'bool'>
    "exclude_bp_from_left": 0, # <class 'int'>
    "exclude_bp_from_right": 0, # <class 'int'>
    "expand_allele_plots_by_quantification": False, # <class 'bool'>
    "expand_ambiguous_alignments": False, # <class 'bool'>
    "expected_hdr_amplicon_seq": "foo", # typing.Optional[str]
    "fastq_output": False, # <class 'bool'>
    "fastq_r1": LatchFile("latch:///foobar"), # <class 'latch.types.file.LatchFile'>
    "fastq_r2": LatchFile("latch:///foobar"), # typing.Optional[latch.types.file.LatchFile]
    "file_prefix": "foo", # typing.Optional[str]
    "flexiguide": "foo", # typing.Optional[str]
    "flexiguide_homology": 0, # typing.Optional[int]
    "flexiguide_name": "foo", # typing.Optional[str]
    "guide_name": ['foo'], # typing.Optional[typing.List[str]]
    "guide_seq": ['foo'], # typing.Optional[typing.List[str]]
    "ignore_deletions": False, # <class 'bool'>
    "ignore_insertions": False, # <class 'bool'>
    "ignore_substitutions": False, # <class 'bool'>
    "keep_intermediate": False, # <class 'bool'>
    "max_paired_end_reads_overlap": 0, # <class 'int'>
    "max_rows_alleles_around_cut_to_plot": 0, # <class 'int'>
    "min_average_read_quality": 0, # <class 'int'>
    "min_bp_quality_or_N": 0, # <class 'int'>
    "min_frequency_alleles_around_cut_to_plot": 0.0, # <class 'float'>
    "min_paired_end_reads_overlap": 0, # <class 'int'>
    "min_single_bp_quality": 0, # <class 'int'>
    "name": "foo", # typing.Optional[str]
    "needleman_wunsch_aln_matrix_loc": "foo", # <class 'str'>
    "needleman_wunsch_gap_extend": 0, # <class 'int'>
    "needleman_wunsch_gap_incentive": 0, # <class 'int'>
    "needleman_wunsch_gap_open": 0, # <class 'int'>
    "no_rerun": False, # <class 'bool'>
    "output_folder": LatchDir("latch:///foobar"), # <class 'latch.types.directory.LatchDir'>
    "place_report_in_output_folder": False, # <class 'bool'>
    "plot_histogram_outliers": False, # <class 'bool'>
    "plot_window_size": 0, # <class 'int'>
    "prime_editing_nicking_guide_seq": "foo", # typing.Optional[str]
    "prime_editing_override_prime_edited_ref_seq": "foo", # typing.Optional[str]
    "prime_editing_pegRNA_extension_quantification_window_size": 0, # <class 'int'>
    "prime_editing_pegRNA_extension_seq": "foo", # typing.Optional[str]
    "prime_editing_pegRNA_scaffold_min_match_length": 0, # typing.Optional[int]
    "prime_editing_pegRNA_scaffold_seq": "foo", # typing.Optional[str]
    "prime_editing_pegRNA_spacer_seq": "foo", # typing.Optional[str]
    "quantification_window_center": 0, # <class 'int'>
    "quantification_window_coordinates": "foo", # typing.Optional[str]
    "quantification_window_size": 0, # <class 'int'>
    "split_interleaved_input": False, # <class 'bool'>
    "stringent_flash_merging": False, # <class 'bool'>
    "suppress_plots": False, # <class 'bool'>
    "suppress_report": False, # <class 'bool'>
    "trim_sequences": False, # <class 'bool'>
    "trimmomatic_command": "foo", # typing.Optional[str]
    "trimmomatic_options_string": "foo", # typing.Optional[str]
    "write_detailed_allele_table": False, # <class 'bool'>
}''')

assemble_params = textwrap.dedent('''"""Run `latch execute wf.assemble_and_sort.params.py` to execute this workflow"""

from latch.types import LatchFile

params = {
    "_name": "wf.assemble_and_sort", # Dont edit this value.
    "read1": LatchFile("latch:///foobar"), # <class 'latch.types.file.LatchFile'>
    "read2": LatchFile("latch:///foobar"), # <class 'latch.types.file.LatchFile'>
}''')


def test_assemble:
    ...


def test_crispresso:
    ...


def test_rnaseq:
    ...
