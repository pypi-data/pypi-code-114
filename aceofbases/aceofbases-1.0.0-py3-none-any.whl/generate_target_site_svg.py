'''
Created on 16 Jun 2015

@author: juanlmateo
'''

from operator import attrgetter
from aceofbases.sequence_methods import get_window_translations

########################################################
# https://bsouthga.dev/posts/color-gradients-with-python
def hex_to_rgb(hex):
    ''' "#FFFFFF" -> [255,255,255] '''
    # Pass 16 to the integer function for change of base
    return [int(hex[i:i+2], 16) for i in range(1,6,2)]


def rgb_to_hex(rgb):
    ''' [255,255,255] -> "#FFFFFF" '''
    # Components need to be integers for hex to make sense
    rgb = [int(x) for x in rgb]
    return "#"+"".join(["0{0:x}".format(v) if v < 16 else
            "{0:x}".format(v) for v in rgb])

def color_dict(gradient):
    ''' Takes in a list of RGB sub-lists and returns dictionary of
    colors in RGB and hex form for use in a graphing function
    defined later on '''
    return {"hex":[rgb_to_hex(rgb) for rgb in gradient],
            "r":[rgb[0] for rgb in gradient],
            "g":[rgb[1] for rgb in gradient],
            "b":[rgb[2] for rgb in gradient]}


def linear_gradient(start_hex, end_hex="#FFFFFF", how_many=10):
    ''' returns a gradient list of (how_many) colors between
    two hex colors. start_hex and end_hex
    should be the full six-digit color string,
    inlcuding the number sign ("#FFFFFF") '''
    # Starting and ending colors in RGB form
    start = hex_to_rgb(start_hex)
    end = hex_to_rgb(end_hex)
    # Initilize a list of the output colors with the starting color
    rbg_list = [start]
    # Calcuate a color at each evenly spaced value of color from 1 to how_many
    for color in range(1, how_many):
    # Interpolate RGB vector for color at the current value of color
        curr_vector = [
            int(start[j] + (float(color)/(how_many-1))*(end[j]-start[j]))
            for j in range(3)
            ]
        # Add it to our list of output colors
        rbg_list.append(curr_vector)
    return color_dict(rbg_list)
########################################################

def get_coord_y(target_sites, width, box_height):
    '''Returns a list containing:
    a list with the value for the coordinate Y of each site the
    coordinate Y of the reference line (middle line to separate plus
    and minus strand) height of the box'''
    coord_y = [None] * len(target_sites)
    last_end_in_level = [-1] * len(target_sites)
    max_level_plus = 0
    max_level_minus = 0
    box_height = box_height + 2  # 2 px space between boxes
    for idx, target_site in enumerate(target_sites):
        # only sites in the forward strand
        if target_site.strand == "-":
            break
        for idx2 in range(len(target_sites)):
            if target_site.position > last_end_in_level[idx2]:
                coord_y[idx] = idx2 + 1
                last_end_in_level[idx2] = target_site.position + width
                max_level_plus = max(max_level_plus, coord_y[idx])
                break
    # now sites in reverse strand
    last_end_in_level = [-1] * len(target_sites)
    for idx, target_site in enumerate(target_sites):
        # only sites in the reverse strand
        if target_site.strand == "+":
            continue
        for idx2 in range(len(target_sites)):
            if target_site.position > last_end_in_level[idx2]:
                coord_y[idx] = idx2 + 1
                last_end_in_level[idx2] = target_site.position + width
                max_level_minus = max(max_level_minus, coord_y[idx])
                break

    middle_line = max_level_plus * box_height + 10
    height_box = (max_level_plus + max_level_minus) * box_height + 20
    # now adapt coordinates to the SVG system, (0,0) upper left corner
    for idx, target_site in enumerate(target_sites):
        if target_site.strand == "+":
            coord_y[idx] = (max_level_plus - coord_y[idx]) * box_height + 10
        else:
            coord_y[idx] = (coord_y[idx] + max_level_plus) * box_height + 12 - box_height
    return([coord_y, middle_line, height_box])

def scale_candidate_pos(position, coordinates_width, cds, base_editor, max_width=980.0, left_offset=10):
    "Returns the position of the candidates scaled wrt the plot length"
    sgrna_size = base_editor.get_target_size() + len(base_editor.pam.pam_str)
    real_position = position + sgrna_size + 1
    for idx in range(1,len(cds.exons)):
        exon1 = cds.exons[idx-1]
        exon2 = cds.exons[idx]
        if position < exon1.end-cds.start:
            break
        if position < exon2.start-cds.start:
            real_position -= (position - exon1.end + cds.start)
            real_position += sgrna_size - (exon2.start - cds.start - position)
            break
        real_position += sgrna_size - (exon2.start - exon1.end)

    return str(real_position * max_width / coordinates_width + left_offset)

def scale_x_axis_ticks(value_x, coordinates_width, cds, base_editor, max_width=980.0, left_offset=10):
    "Returns the scaled values of the X axis ticks"
    sgrna_size = base_editor.get_target_size() + len(base_editor.pam.pam_str)
    real_value_x = value_x + sgrna_size
    for exon in cds.exons:
        if value_x <= (exon.end-cds.start+1):
            break
        real_value_x += sgrna_size

    return str(real_value_x * max_width / coordinates_width + left_offset)

def scale_width(value_x, coordinates_width, max_width=980.0):
    "Returns the scaled value wrt the total width in the plot"
    return str(value_x * max_width / coordinates_width)

def get_axis_ticks(cds):
    "Returns a list with the values of the X axis ticks"
    tick_sep = 10
    first = 0
    ticks = list(range(first, cds.length, tick_sep))
    # a maximum of 10 ticks are returned
    return [1] + [ticks[m] for m in range(0,len(ticks),max(1,round(len(ticks)/10)))][1:]

def get_non_synonymous_changes(candidate, cds, query_length, base_editor, coord_y, box_height):
    "Returns the SVG code to represent non synonumous changes in the ORF"
    translations = get_window_translations(candidate,cds,base_editor)
    code_svg = ""
    scaled_pos = scale_candidate_pos(candidate.position, query_length, cds, base_editor)

    for frame,translation in enumerate(translations.frames):
        for idx, residue in enumerate(translation.translation):
            if ">" in residue:
                if "*" in residue:
                    color = "black"#"#d95f0e"
                else:
                    color = "purple"#"#fec44f"
                if candidate.strand == "+":
                    if frame<3:
                        nss_position = float(scaled_pos) + float(scale_width(idx * 3 - (translation.window_start_nt - base_editor.window_start), query_length))
                    else:
                        new_idx = len(translation.translation)-idx-1
                        new_window_start_nt = len(translation.translation)*3-translation.window_end_nt
                        nss_position = float(scaled_pos) + float(scale_width(new_idx * 3 - (new_window_start_nt - base_editor.window_start), query_length))
                else:
                    if frame<3:
                        rev_window_start_nt = len(candidate.sequence)-base_editor.window_end
                        nss_position = float(scaled_pos) + float(scale_width(idx*3 + rev_window_start_nt-translation.window_start_nt, query_length))
                    else:
                        new_idx = len(translation.translation)-idx-1
                        rev_window_start_nt = len(candidate.sequence)-base_editor.window_end
                        nss_position = float(scaled_pos) + float(scale_width(new_idx*3 + rev_window_start_nt-translation.window_end_nt, query_length))
                code_svg = code_svg \
                    + '<rect class="non-synonymous nss-F' + str((frame%3+1)*pow(-1,int(frame>2))) + '" style="display:none" x="' \
                    + str(nss_position) \
                    + '" y="' + str(coord_y) + '" fill="' + color \
                    + '" width="' + scale_width(3, query_length) + '" height="' + str(box_height) + '">' \
                    + '<title>' + residue + '</title></rect>\n'
    return code_svg

def generate_targets_pam_3prime(sorted_candidates, candidate_colors, cds, base_editor, coord_width, coord_y, box_height, font_size):
    "Returns the SVG code to represent the target sites when the PAM considered is 3 prime"
    pam_size = len(base_editor.pam.pam_str)
    target_size = base_editor.target_size
    code_svg = ""
    for idx, sorted_candidate in enumerate(sorted_candidates):
        scaled_pos = scale_candidate_pos(sorted_candidate.position,coord_width,cds,base_editor)
        scaled_pam_size = scale_width(pam_size, coord_width)
        scaled_target_size = scale_width(target_size, coord_width)
        scaled_size = str(float(scaled_pam_size)+float(scaled_target_size))
        scaled_text_pos = str(float(scaled_pos)-1)

        code_svg = code_svg + '<rect x="' + scaled_pos + '" y="' + str(coord_y[idx]) + '" opacity="0.5" fill="' + candidate_colors["hex"][int(sorted_candidate.label[1:])-1] + '" stroke="none" width="' + scaled_size + '" height="' + str(box_height) + '"/>\n'

        if sorted_candidate.strand == '+':
            code_svg = code_svg + '<rect x="' + str(float(scaled_pos)+float(scaled_target_size)) + '" y="' + str(coord_y[idx]) + '" fill="green" width="' + scaled_pam_size + '" height="' + str(box_height) + '"/><!-- PAM -->\n'\
            + '<a xlink:href="#' + sorted_candidate.label + '" title="' + sorted_candidate.label + '">\n'\
            + '<rect x="' + scaled_pos + '" y="' + str(coord_y[idx]) + '" opacity="0.1" fill="#FFFFFF" stroke="#000000" stroke-width="3" width="' + scaled_size + '" height="' + str(box_height) + '" onmouseover="fire(this);" onmouseout="setoff(this);"/>\n'
            # + '</a>\n'
        else:
            code_svg = code_svg + '<rect x="' + scaled_pos + '" y="' + str(coord_y[idx]) + '" fill="green" width="' + scaled_pam_size + '" height="' + str(box_height) + '"/><!-- PAM -->\n'\
            + '<a xlink:href="#' + sorted_candidate.label + '" title="' + sorted_candidate.label + '">\n'\
            + '<rect x="' + scaled_pos + '" y="' + str(coord_y[idx]) + '" opacity="0.1" fill="#FFFFFF" stroke="#000000" stroke-width="3" width="' + scaled_size + '" height="' + str(box_height) + '" onmouseover="fire(this);" onmouseout="setoff(this);"/>\n'
            # + '</a>\n'

        code_svg += get_non_synonymous_changes(sorted_candidate,cds,coord_width,base_editor,coord_y[idx],box_height)
        code_svg += '<text x="' + scaled_text_pos + '" y="' + str(coord_y[idx] + box_height - 3) + '" style="text-anchor: end" font-family="\'Helvetica\'" font-size="' + str(font_size) + '">' + sorted_candidate.label + '</text>\n'

        code_svg += '</a>\n'

    return code_svg

def get_svg(cds, candidates, base_editor):
    '''Returns the SVG code to represent the target sites and their editions
    that will affect the ORF.
    NOTE:
        cds is in gff format, i.e. 1-index
        target site position are in bed format, i.e. 0-index'''

    pam_size = len(base_editor.pam.pam_str)
    target_size = base_editor.get_target_size()
    code_svg = ""
    box_height = 18

    coord_width = cds.length + (target_size+pam_size) * 2
    if len(cds.exons)>1:
        coord_width += (target_size+pam_size) * (len(cds.exons)-1)

    if coord_width <= 500:
        font_size = 16
    elif coord_width <= 1000:
        font_size = 11
    elif coord_width <= 1500:
        font_size = 8
    else:
        font_size = 0

    # order by strand and position
    sorted_candidates = sorted(candidates.get_sites(), key=attrgetter('strand', 'position'))
    # each candidates needs horizontal space for the sequence plus the label
    width = target_size + pam_size + font_size
    [coord_y, middle_line, height_box] = get_coord_y(sorted_candidates, width, box_height)
    height_plot = height_box + 40

    axis_ticks = get_axis_ticks(cds)

    candidate_colors = linear_gradient("#fff7bc", "#d95f0e", len(sorted_candidates))

    code_svg = code_svg + '<svg version="1.1" id="Layer_1" xmlns="http://www.w3.org/2000/svg" xmlns:xlink="http://www.w3.org/1999/xlink" x="0px" y="0px" width="1000px" height="' + str(height_plot + 20) + 'px" viewBox="0 0 1000 ' + str(height_plot + 20) + '" enable-background="new 0 0 1000 ' + str(height_plot + 20) + '" xml:space="preserve">\n'
    code_svg = code_svg + '<rect fill="#DBDBDB" width="1000" height="' + str(height_box) + '"/>\n'
    code_svg = code_svg + '<line fill="none" stroke="#231F20" x1="10" y1="' + str(middle_line) + '" x2="990" y2="' + str(middle_line) + '"/>\n'

    for tick in axis_ticks:
        scaled_tick_pos = scale_x_axis_ticks(tick, coord_width, cds, base_editor)
        code_svg = code_svg + '<text x="' + scaled_tick_pos + '" y="' + str(height_box + 20) + '" style="text-anchor: middle" fill="#808080" font-family="\'Helvetica\'" font-size="12">' + str(tick) + '</text>\n'
        code_svg = code_svg + '<line fill="none" stroke="#EFEFEF" stroke-width="2" x1="' + scaled_tick_pos + '" y1="0" x2="' + scaled_tick_pos + '" y2="' + str(height_box) + '"/>\n'

    exon_border = 1
    for exon in cds.exons:
        pos = scale_x_axis_ticks(exon_border, coord_width, cds, base_editor)
        code_svg = code_svg + '<line stroke-dasharray="5,5" stroke="black" stroke-width="2" x1="' + pos + '" y1="0" x2="' + pos + '" y2="' + str(height_box) + '"/>\n'
        pos = scale_x_axis_ticks(exon_border + exon.end-exon.start, coord_width, cds, base_editor)
        code_svg = code_svg + '<line stroke-dasharray="5,5" stroke="black" stroke-width="2" x1="' + pos + '" y1="0" x2="' + pos + '" y2="' + str(height_box) + '"/>\n'
        exon_border +=exon.end-exon.start+1

    if base_editor.pam.is5prime:
        raise NotImplementedError("The SVG output not implemented yet for 5 prime PAMs")
    else:
        code_svg = code_svg + generate_targets_pam_3prime(sorted_candidates, candidate_colors, cds, base_editor, coord_width, coord_y, box_height, font_size)

    # code_svg = code_svg + '<text x="500" y="' + str(height_plot) + '" style="text-anchor: middle" font-family="\'Helvetica\'" font-size="18">' + cds.chrom + '</text>'
    code_svg = code_svg + '</svg>'

    return code_svg
