import vcf


def get_alleles(call):
    if "/" in call.GT:
        return call.GT.split("/")
    elif "|" in call.GT:
        return call.GT.split("|")


def is_homozygous(call):
    """Determine if a call is homozygous"""
    allele1, allele2 = get_alleles(call)
    return allele1 == allele2


def is_heterozygous(call):
    """Determine if a call is heterozygous"""
    return not is_homozygous(call)


def ps_defined(call):
    try:
        call.PS
        return True
    except AttributeError:
        return False


def is_compatible(call1, call2):
    """Are two calls compatible"""
    # If both are phased, the phase set must match.
    if ps_defined(call1) and ps_defined(call2):
        return call1.PS == call2.PS

    # Any two calls where one is homozygous are compatible
    if is_homozygous(call1) or is_homozygous(call2):
        return True

    # Two heterozygous calls are not compatibhle
    if is_heterozygous(call1) and is_heterozygous(call2):
        return False


def are_compatible(calls, call):
    """Determine if a call is compatible with a list of calls"""
    return all((is_compatible(call, c) for c in calls))


def get_call(variant):
    """Return the call from a variant"""
    # Real data
    if isinstance(variant, vcf.model._Record):
        return variant.samples[0].data
    # Test data
    else:
        return variant.samples[0]


def get_phase_id(variants):
    for var in variants:
        call = get_call(var)
        if ps_defined(call):
            return call.PS


def add_group(grouped_variants, current_group, phased):
    """Add current_group to the grouped variants

    This can be tricky when there are phased variants
    """
    phase_id = get_phase_id(current_group)
    if not phase_id:
        grouped_variants.append(current_group)
    else:
        # If we have seen this phase ID before
        if phase_id in phased:
            index = phased[phase_id]
            grouped_variants[index] += current_group
        else:
            index = len(grouped_variants)
            grouped_variants.append(current_group)
            phased[phase_id] = index


def group_variants(variants):
    """Group compatible variants together"""

    # Store the grouped variants in a list of list of variants
    grouped_variants = list()

    # Store the index of phased groups, since they could be interleafed, so we
    # have to add more variants to them lates
    phased = dict()

    current_group = list()
    for record in variants:
        call = get_call(record)
        if are_compatible([get_call(rec) for rec in current_group], call):
            current_group.append(record)
        else:
            add_group(grouped_variants, current_group, phased)
            current_group = [record]

    # If we were still working on a group of variants when we got to the last
    # one
    if current_group:
        add_group(grouped_variants, current_group, phased)

    return grouped_variants


def generate_patterns(count):
    """Generate patterns for switching variants around

    >>> list(generate_patterns(3))
    [[0, 0, 0], [0, 0, 1], [0, 1, 0], [0, 1, 1]]

    """
    if count < 1:
        return list()

    for i in range(2 ** (count - 1)):
        yield [int(x) for x in format(i, "b").zfill(count)]


def switch(call):
    """Switch the genotype calls around"""
    allele1, allele2 = get_alleles(call)
    if "/" in call.GT:
        return call._replace(GT=f"{allele2}/{allele1}")
    elif "|" in call.GT:
        return call._replace(GT=f"{allele2}|{allele1}")


def switch_variant(var):
    """Switch the calls for a variant around (modifies in place)"""
    call = get_call(var)
    if isinstance(var, vcf.model._Record):
        var.samples[0].data = switch(call)
    else:
        var.samples = [switch(call)]
    return var


def switch_variants(variants):
    """Switch the calls for all variants"""
    return [switch_variant(var) for var in variants]


def all_combinations(variants, max_blocks):
    """Yield all possible combinations of variants"""
    grouped = group_variants(variants)

    if len(grouped) > max_blocks:
        msg = f"Identified {len(grouped)} blocks, only {max_blocks} are supported"
        raise RuntimeError(msg)

    for pattern in generate_patterns(len(grouped)):
        print(f"Running inversion pattern {pattern}")
        yield [
            switch_variants(group) if p else group for group, p in zip(grouped, pattern)
        ]
        # Switch again to restore the original variant calls, since we change
        # them in place
        [switch_variants(group) if p else group for group, p in zip(grouped, pattern)]
