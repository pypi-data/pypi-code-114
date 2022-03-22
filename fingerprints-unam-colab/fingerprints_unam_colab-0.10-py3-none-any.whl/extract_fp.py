import os
import sys

from collections import OrderedDict, Counter

import matplotlib.pyplot as plt

import pandas as pd

from scipy.spatial import distance_matrix

from skimage.segmentation import felzenszwalb
from skimage.segmentation import mark_boundaries
from skimage.util import img_as_float

from skimage import io

from sklearn.cluster import DBSCAN

try:
    from regions import Region
except:
    from huellas.regions import Region

try:
    from auxiliar import *
except:
    from huellas.auxiliar import *

def remove_small_particles(min_size, label_mask, label_counts):
    new_mask = np.copy(label_mask)
    for label, count in label_counts:
        if label == 0:
            continue
        elif count < min_size:
            new_mask[new_mask == label] = 0
    new_mask[new_mask != 0] = 255
    return new_mask.astype("uint8")

def main(input_img_path, output_folder_path, BORDER_OFFSET=100):
  
    # Read
    img = cv2.imread(input_img_path, 
                    cv2.IMREAD_GRAYSCALE)
    img_color = cv2.imread(input_img_path)
    #mostrar_imagen(img, "Original")
    
    # Normalize
    img_norm = cv2.normalize(img, None, 0, 255, cv2.NORM_MINMAX)
    #mostrar_imagen(img_norm, "Normalizacion")

    median = cv2.medianBlur(img_norm, 7)
    #mostrar_imagen(median, "F. Mediana")
    
    # Threshold
    umbral = cv2.adaptiveThreshold(median,
                                   255,
                                   cv2.ADAPTIVE_THRESH_GAUSSIAN_C,
                                   cv2.THRESH_BINARY,
                                   13,
                                   2)
    not_umbral = 255 - umbral
    #mostrar_imagen(not_umbral, "Umbral Local")
  
    # Try to remove long lines
    horizontal_kernel = cv2.getStructuringElement(cv2.MORPH_RECT, (25,1))
    detected_lines = cv2.morphologyEx(not_umbral, cv2.MORPH_OPEN, horizontal_kernel, iterations=2)
    cnts = cv2.findContours(detected_lines, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
    cnts = cnts[0] if len(cnts) == 2 else cnts[1]
    for c in cnts:
        cv2.drawContours(umbral, [c], -1, (255,255,255), 2)
    
    vertical_kernel = cv2.getStructuringElement(cv2.MORPH_RECT, (1,25))
    detected_lines = cv2.morphologyEx(not_umbral, cv2.MORPH_OPEN, vertical_kernel, iterations=2)
    cnts = cv2.findContours(detected_lines, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
    cnts = cnts[0] if len(cnts) == 2 else cnts[1]
    for c in cnts:
        cv2.drawContours(umbral, [c], -1, (255,255,255), 2)

    not_umbral = 255 - umbral
    #mostrar_imagen(255 - umbral, "Umbral Local")
    
    not_umbral_float = img_as_float(not_umbral)
    segments_fz = felzenszwalb(not_umbral_float, scale=100, sigma=0.5, min_size=50)
    c = Counter(segments_fz.flatten())
    background_label = max(c, key=c.get)
    superpixel_mask = (segments_fz != background_label).astype("uint8") * 255
    #mostrar_imagen(segments_fz, "superpixel")
    #mostrar_imagen(superpixel_mask, "superpixel mask")
    #guardar_imagen(superpixel_mask, output_folder_path + "superpixel_mask.png")
    
    ##io.imshow(mark_boundaries(img_color, segments_fz))
    ##io.show()
    
    qty, label_mask = cv2.connectedComponents(superpixel_mask)
    labels, counts = np.unique(label_mask, return_counts=True)
    label_counts = [*zip(labels, counts)]
    label_counts.sort(key=lambda x:x[1], reverse=True)

    # Reference segmentation using superpixels
    # TODO: Avoid arbitrary sizes (why 10000?)
    clean_label_mask = remove_small_particles(10000, label_mask, label_counts)
    #guardar_imagen(clean_label_mask, output_folder_path + "clean_label_mask.png")
    #mostrar_imagen(clean_label_mask, "clean label mask")
    
    # Fill holes with morphology
    N8 = np.ones((3, 3))

    # TODO: Using arbitrary filters
    dilatacion = cv2.dilate(clean_label_mask, N8, iterations=10)
    #mostrar_imagen(dilatacion, "Dilatacion")
    
    erosion = cv2.erode(dilatacion, N8, iterations=5)
    #mostrar_imagen(erosion, "Erosion")
    
    #guardar_imagen(erosion, output_folder_path + "opening_clean_label_mask.png")
   
    # Re-map connected components in clean image
    qty, label_mask = cv2.connectedComponents(erosion)
    labels, counts = np.unique(label_mask, return_counts=True)
    label_counts = [*zip(labels, counts)]
    label_counts.sort(key=lambda x:x[1], reverse=True)
    
    # Color connected components for visualization
    clean_blobs_color = colorear_componentes_conexas(label_mask)

    ## TODO: just debugging
    #label_mask[label_mask != 0] = 255
    #label_mask = label_mask.astype("uint8")
    #mostrar_imagen(label_mask, "clean remap")
    #import ipdb;ipdb.set_trace()
    
    # Segmentation
    regions = []
    i = 0
    for label, count in label_counts:
        if label == 0 :
            continue
        cut_mask = label_mask == label
        
        # Calculate contours
        contours, _  = cv2.findContours(cut_mask.astype("uint8"), 
                                        cv2.RETR_EXTERNAL, 
                                        cv2.CHAIN_APPROX_SIMPLE)
       
        # Don't process images with less than one contour
        if len(contours) > 0:
            # Fill entire region as marked by contour
            cut_mask = cut_mask.astype("float32") * 255
            cut_mask = cv2.fillPoly(cut_mask, contours, 255)
            cut_mask = cut_mask == 255
            # Process region
            r = Region(contours[0], cut_mask, img)
            regions.append((i, r))
            i +=1

    # Classification starts
    regions.sort(key=lambda x: x[1], reverse=True)
    
    # Check some indicators
    moment_data = pd.DataFrame(columns=["h0", "h1", "h2", "h3", "h4", "h5", "h6"])
    for i, region in regions:
        #cv2.putText(img_color, 
        #            str(region.area),
        #            region.centroid,
        #            cv2.FONT_HERSHEY_COMPLEX,
        #            1, 0, 2)
        cv2.putText(clean_blobs_color,
                    str(i),
                    region.centroid,
                    cv2.FONT_HERSHEY_COMPLEX,
                    1, (255, 255, 255), 2)
        moment_data.loc[i] = region.log_hu_invariants
        for j, region2 in regions:
            d1 = cv2.matchShapes(region.contour, 
                                 region2.contour,
                                 cv2.CONTOURS_MATCH_I1,
                                 0)
            d2 = cv2.matchShapes(region.contour, 
                                 region2.contour,
                                 cv2.CONTOURS_MATCH_I2,
                                 0)
            d3 = cv2.matchShapes(region.contour, 
                                 region2.contour,
                                 cv2.CONTOURS_MATCH_I3,
                                 0)
            #print(i,", ",j,"\n")
            #print("\t d1: ", d1)
            #print("\t d2: ", d2)
            #print("\t d3: ", d3)
            #print("\t dt: ", d1 + d2 + d3)
    
    guardar_imagen(clean_blobs_color, output_folder_path + "blob_numbers.png")
    #mostrar_imagen(clean_label_mask, "region numbers")
    #guardar_imagen(img_color, output_folder_path + "blob_sizes.png")
    #mostrar_imagen(img_color, "sizes")

    # Get isolated fingerprint candidates
    f_candidates = []
    border_height = int(img.shape[0]/4)
    border_width = int(img.shape[1]/4)
    for i, region in regions:
        is_candidate = False
        w, h = region.centroid
        if h <= border_height or h >= img.shape[0] - border_height:
            is_candidate = True
        else:
            if w <= border_width or w >= img.shape[1] - border_width:
                is_candidate = True
        if is_candidate:
            # Check if it is square-like
            poly = region.approx_poly(0.05)
            #print(i, len(poly))
            if len(poly) == 4:
                # Check ratio
                max_value = max(region.rect[1])
                min_value = min(region.rect[1])
                ratio = max_value / min_value
                #print(i, ratio, max_value, min_value)
                if ratio < 2 and max_value < 500 and min_value > 150:
                    f_candidates.append((i, region))
    
    # Check distance between all pairs and remove the ones that are too far away
    if len(f_candidates) > 1:
        candidate_centroids = []
        candidate_labels = []
        for i, region in f_candidates:
            candidate_centroids.append(region.centroid)
            candidate_labels.append(i)
        distances = distance_matrix(candidate_centroids, 
                                    candidate_centroids)
        distances_df = pd.DataFrame(distances, 
                                    index=candidate_labels, 
                                    columns=candidate_labels)
        candidate_labels = np.array(candidate_labels)
        #print("\nFingerprint candidates:")
        #print(distances_df.describe())
        #print(distances_df.quantile(.25) < 1000)
        final_candidate_labels = candidate_labels[distances_df.quantile(.25) < 1000]
    else:
        # Assume that the single candidate is a false positive
        final_candidate_labels = []

    # Save remaining fingerprint candidates
    for i, region in f_candidates:
        if i in final_candidate_labels:
            region.save_cropped(output_folder_path + "fprint%d.png" % i)

    # For every non-candidate, assume it may be part of a hand
    img_height, img_width = img.shape
    left_limit = BORDER_OFFSET
    right_limit = img_width - BORDER_OFFSET
    up_limit = BORDER_OFFSET
    down_limit = img_height - BORDER_OFFSET
    hand_candidates = []
    hand_region_coordinates = []
    for i, region in regions:
        is_in_border = False
        if i not in final_candidate_labels:
            # Check if it's not a border artifact
            x_left, y_up = region.left_most_coordinate
            x_right, y_down = region.right_most_coordinate

            if x_left <= left_limit or x_right >= right_limit or\
                    y_up <= up_limit or y_down >= down_limit:
                        #print("Removed: ", i)
                        is_in_border = True

            if not is_in_border:
                hand_candidates.append((i, region))
                hand_region_coordinates.append(region.left_most_coordinate)
                hand_region_coordinates.append(region.right_most_coordinate)

    # Remove non-candidates from mask:
    hand_candidates_ids = [i for i, _ in hand_candidates]
    for i, region in regions:
        if i not in hand_candidates_ids:
           (min_x, min_y) = region.left_most_coordinate
           (max_x, max_y) = region.right_most_coordinate

           clean_label_mask[min_y:max_y, min_x:max_x] = 0

    # Get hand bounding box
    hand_region_coordinates.sort()
    min_x, _ = hand_region_coordinates[0]
    max_x, _ = hand_region_coordinates[-1]
    hand_region_coordinates.sort(key=lambda x: x[1])
    _, min_y = hand_region_coordinates[0]
    _, max_y = hand_region_coordinates[-1]
    hand_rect = (min_x, min_y, max_x-min_x, max_y-min_y)
    
    # Creating new mask on initial segmentation
    # TODO: using arbitrary filters
    hand_dilate = cv2.dilate(not_umbral, N8, iterations=15)
    #mostrar_imagen(dilatacion, "Dilatacion")
    
    hand_erode = cv2.erode(hand_dilate, N8, iterations=5)
    #mostrar_imagen(erosion, "Erosion")

    # Cut regions in both simple and superpixel-clean segmentation
    hand_region = hand_erode[min_y:max_y, min_x:max_x]
    clean_hand_region = clean_label_mask[min_y:max_y, min_x:max_x]
    #guardar_imagen(hand_region, output_folder_path + "hand_simple_threshold.png")
    #guardar_imagen(clean_hand_region, output_folder_path + "hand_clean_mask.png")
   
    # Count connected components in simple segmentation
    _, hand_label_mask = cv2.connectedComponents(hand_region)
   
    # Apply mask
    twomask_combination = img_as_float(clean_hand_region) * hand_label_mask
    selected_components = np.unique(twomask_combination)
    selected_components = selected_components[selected_components != 0]
    for c in selected_components:
        hand_label_mask[hand_label_mask == c] = 255
    hand_label_mask[hand_label_mask != 255] = 0
    hand_label_mask = hand_label_mask.astype("uint8")
    #guardar_imagen(hand_label_mask, output_folder_path + "combined_hand_mask.png")
    
    color_hand_region = img_color[min_y:max_y, min_x:max_x]
    extracted_hand = cv2.bitwise_and(color_hand_region, color_hand_region, mask=hand_label_mask)
    
    b, g, r = cv2.split(extracted_hand)
    alpha_channel = hand_label_mask 
    extracted_hand_alpha = cv2.merge([b, g, r, alpha_channel])

    cv2.imwrite(output_folder_path + "hand0.png", extracted_hand_alpha)
    #import ipdb;ipdb.set_trace()

def entry_point():
    if len(sys.argv) < 3:
        raise ValueError("Usage: %s INPUT_IMG OUTPUT_FOLDER" % sys.argv[0])

    input_img_path = sys.argv[1]
    output_folder_path = sys.argv[2]
    if not os.path.exists(input_img_path):
        raise ValueError("%s doesn't exist" % input_img_path)
    if os.path.exists(output_folder_path):
        if not os.path.isdir(output_folder_path):
            raise ValueError("%s is not a folder" % output_folder_path)
    if not output_folder_path.endswith(os.sep):
        output_folder_path += os.sep
    image_name = os.path.basename(input_img_path).split(".")[0]
    output_folder_path += image_name + os.sep
    if not os.path.exists(output_folder_path):
        os.makedirs(output_folder_path)
    main(input_img_path, output_folder_path)

if __name__ == "__main__":
    entry_point()
