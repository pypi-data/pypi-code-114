import pkg_resources
import numpy
import warnings
import array
import plotly.graph_objects as go
from b2tsf.belle_CDC_layer import CDCLayer
from b2tsf.belle_CDC_frame import CDCFrame

class TrackSegmentFinderHourglas:
    """
    Track Segement Finder implenmenting the conventional hourglas solution.

    ---------------------------------------------------------------------------
    Methods:
    ---------------------------------------------------------------------------
    detect:     Detects hits in incoming frame <frame_in> and saves result in
                internal data strucutre. Two possible detetction modes are
                available. 'hits' returns real hardware hits whereas 'candidates'
                returns all hit candidates of a hit bin.

    get_frame:  Retruns internal data frame as reference.

    clear:      Clears internal data structure.

    """

    def __init__(self):
        """
        A priori probabilities are saved in a txt look up table and loaded
        during object creation. Make sure the path is provided accordingly.
        """

        self._frame = CDCFrame(0)
        self.mode = 'hits'
        self._outer_lr_lut = numpy.loadtxt(pkg_resources.resource_filename(__name__, 'data/outerLRLUT.mif'),
                                           comments="#",
                                           delimiter=",",
                                           converters={0: lambda x: int(x,2)},
                                           unpack=False)
        self._inner_lr_lut = numpy.loadtxt(pkg_resources.resource_filename(__name__, 'data/innerLRLUT.mif'),
                                           comments="#",
                                           delimiter=",",
                                           converters={0: lambda x: int(x,2)},
                                           unpack=False)

    def _detect_hit_inner(self,hitmap):
        """
        Hitmap is an encoded 1D array with 16 elements.
        Elements 0-A are hits at respective addresses.
        Element B is buffer element an therefore 0.
        Line Number |     Hits     |   Address
        ------------|--------------|-------------
            5       | -X-X-X-X-X-- | -0-1-2-3-4--
            4       | --X-X-X-X-O- | --5-6-7-8---
            3       | -O-X-X-X-O-- | ---9-A-B----
            2       | --O-X-X-O-O- | ----C-D-----
            1       | -O-O-X-O-O-- | -----E------
        ------------|--------------|-------------
        As defined in CDC Merger Board Specification v1.
        """
        #TODO: Improve this code for efficiency and readability.
        #It is True only when first priority
        #cell is not hit and the left secondary one is hit.
        hitmap[15] = int((not hitmap[14]) and hitmap[12])
        #Calculate Look-Up-Table address
        #Use hitmap array, convert to string and convert string to integer
        lr_addr = int(''.join(map(str,hitmap)),2)
        lr = self._inner_lr_lut[lr_addr]

        hitline5 = hitmap[0] or hitmap[1] or hitmap[2] or hitmap[3] or hitmap[4]
        hitline4 = hitmap[5] or hitmap[6] or hitmap[7] or hitmap[8]
        hitline3 = hitmap[9] or hitmap[10] or hitmap[11]
        hitline2 = hitmap[12] or hitmap[13]
        hitline1 = hitmap[14]

        result = (hitline4 and hitline3 and hitline2 and hitline1 and  lr) or \
                 (hitline5 and hitline3 and hitline2 and hitline1 and  lr) or \
                 (hitline5 and hitline4 and hitline2 and hitline1 and  lr) or \
                 (hitline5 and hitline4 and hitline3 and hitline1 and  lr) or \
                 (hitline5 and hitline4 and hitline3 and hitline2 and  lr) or \
                 (hitline5 and hitline4 and hitline3 and hitline2 and hitline1 and lr)

        return result


    def _detect_hit_outer(self,hitmap):
        """
        Hitmap is an encoded 1D array with 12 elements.
        Elements 0-A are hits at respective addresses.
        Element B is buffer element an therefore 0.
        Line Number |     Hits     |   Address
        ------------|--------------|-------------
            5       | -X-O-O-O-X-- | ---0-1-2----
            4       | --X-O-O-X-X- | ----3-4-----
            3       | -X-X-O-X-X-- | -----5------
            2       | --X-O-O-X-X- | ----6-7-----
            1       | -X-O-O-O-X-- | ---8-9-A----
        ------------|--------------|-------------
        As defined in CDC Merger Board Specification v1.
        """
        #TODO: Improve this code for efficiency and readability.
        #It is True only when first priority
        #cell is not hit and the left secondary one is hit.
        hitmap[11] = int((not hitmap[5]) and hitmap[3])
        #Calculate Look-Up-Table address
        #Use hitmap array, convert to string and convert string to integer
        lr_addr = int(''.join(map(str,hitmap)),2)
        lr = self._outer_lr_lut[lr_addr]

        hitline5 = hitmap[0] or hitmap[1] or hitmap[2]
        hitline4 = hitmap[3] or hitmap[4]
        hitline2 = hitmap[6] or hitmap[7]
        hitline1 = hitmap[8] or hitmap[9] or hitmap[10]

        result = (hitmap[5] and lr) or \
                 (hitline5 and hitline4 and hitline2 and hitline1 and lr)

        return result

    def _populate_bin_inner(self,seg_pre, seg_act, seg_suc, edge_hit):
        """
        Populate bins for detection algorithm. Each segment has got 16 bins as specified.
        Furthermore edge_hits of sectors can be toggeled on/off.
        This function returns bins of a layer segment.
        """
        hit_bin = 16 * [None]

        if(edge_hit):
            # Circulation counterclockwise - successor left, predecessor right
            # Add 0 element as placeholder for lr value
            hit_bin[0] = list(map(int,[seg_act[4,2],seg_act[4,1],seg_act[4,0],seg_pre[4,15],seg_pre[4,14],
                                       seg_act[3,1],seg_act[3,0],seg_pre[3,15],seg_pre[3,14],
                                       seg_act[2,1],seg_act[2,0],seg_pre[2,15],
                                       seg_act[1,0],seg_pre[1,15],
                                       seg_act[0,0],
                                       0]))
            hit_bin[1] = list(map(int,[seg_act[4,3],seg_act[4,2],seg_act[4,1],seg_act[4,0],seg_pre[4,15],
                                       seg_act[3,2],seg_act[3,1],seg_act[3,0],seg_pre[3,15],
                                       seg_act[2,2],seg_act[2,1],seg_act[2,0],
                                       seg_act[1,1],seg_act[1,0],
                                       seg_act[0,1],
                                       0]))
            hit_bin[14] =  list(map(int,[seg_suc[4,0],seg_act[4,15],seg_act[4,14],seg_act[4,13],seg_act[4,12],
                                         seg_suc[3,0],seg_act[3,15],seg_act[3,14],seg_act[3,13],
                                         seg_act[2,15],seg_act[2,14],seg_act[2,13],
                                         seg_act[1,15],seg_act[1,14],
                                         seg_act[0,14],
                                         0]))
            hit_bin[15] =  list(map(int,[seg_suc[4,1],seg_suc[4,0],seg_act[4,15],seg_act[4,14],seg_act[4,13],
                                         seg_suc[3,0],seg_act[3,15],seg_act[3,14],seg_act[3,13],
                                         seg_suc[2,0],seg_act[2,15],seg_act[2,14],
                                         seg_act[1,15],seg_act[1,14],
                                         seg_act[0,15],
                                         0]))
        else:
            hit_bin[0] = list(map(int,[seg_act[4,2],seg_act[4,1],seg_act[4,0],0,0,
                                       seg_act[3,1],seg_act[3,0],0,0,
                                       seg_act[2,1],seg_act[2,0],0,
                                       seg_act[1,0],0,
                                       seg_act[0,0],
                                       0]))
            hit_bin[1] = list(map(int,[seg_act[4,3],seg_act[4,2],seg_act[4,1],seg_act[4,0],0,
                                       seg_act[3,2],seg_act[3,1],seg_act[3,0],0,
                                       seg_act[2,2],seg_act[2,1],seg_act[2,0],
                                       seg_act[1,1],seg_act[1,0],
                                       seg_act[0,1],
                                       0]))
            hit_bin[14] =  list(map(int,[0,seg_act[4,15],seg_act[4,14],seg_act[4,13],seg_act[4,12],
                                         0,seg_act[3,15],seg_act[3,14],seg_act[3,13],
                                         seg_act[2,15],seg_act[2,14],seg_act[2,13],
                                         seg_act[1,15],seg_act[1,14],
                                         seg_act[0,14],
                                         0]))
            hit_bin[15] =  list(map(int,[0,0,seg_act[4,15],seg_act[4,14],seg_act[4,13],
                                         0,seg_act[3,15],seg_act[3,14],seg_act[3,13],
                                         0,seg_act[2,15],seg_act[2,14],
                                         seg_act[1,15],seg_act[1,14],
                                         seg_act[0,15],
                                         0]))

        for i in range(2,16-2):
            hit_bin[i] =  list(map(int,[seg_act[4,i+2],seg_act[4,i+1],seg_act[4,i],seg_act[4,i-1],seg_act[4,i-2],
                                        seg_act[3,i+1],seg_act[3,i],seg_act[3,i-1],seg_act[3,i-2],
                                        seg_act[2,i+1],seg_act[2,i],seg_act[2,i-1],
                                        seg_act[1,i],seg_act[1,i-1],
                                        seg_act[0,i],
                                        0]))
        return hit_bin


    def _populate_bin_outer(self,seg_pre, seg_act, seg_suc, edge_hit):
        """
        Populate bins for detection algorithm. Each segment has got 16 bins as specified.
        Furthermore edge_hits of sectors can be toggeled on/off.
        This function returns bins of a layer segment.
        """
        hit_bin = 16 * [None]

        if(edge_hit):
            # Circulation counterclockwise - successor left, predecessor right
            # Add 0 element as placeholder for lr value
            hit_bin[0] = list(map(int,[seg_act[4,1],seg_act[4,0],seg_pre[4,15],
                                    seg_act[3,0],seg_pre[3,15],
                                    seg_act[2,0],
                                    seg_act[1,0],seg_pre[1,15],
                                    seg_act[0,1],seg_act[0,0],seg_pre[0,15],
                                    0]))
            hit_bin[15] =  list(map(int,[seg_suc[4,0],seg_act[4,15],seg_act[4,14],
                                    seg_act[3,15],seg_act[3,14],
                                    seg_act[2,15],
                                    seg_act[1,15],seg_act[1,14],
                                    seg_suc[0,0],seg_act[0,15],seg_act[0,14],
                                    0]))
        else:
            hit_bin[0] =  list(map(int,[seg_act[4,1],seg_act[4,0],0,
                                    seg_act[3,0],0,
                                    seg_act[2,0],
                                    seg_act[1,0],0,
                                    seg_act[0,1],seg_act[0,0],0,
                                    0]))
            hit_bin[15] =  list(map(int,[0,seg_act[4,15],seg_act[4,14],
                                    seg_act[3,15],seg_act[3,14],
                                    seg_act[2,15],
                                    seg_act[1,15],seg_act[1,14],
                                    0,seg_act[0,15],seg_act[0,14],
                                    0]))

        for i in range(1,16-1):
            hit_bin[i] =  list(map(int,[seg_act[4,i+1],seg_act[4,i],seg_act[4,i-1],
                                    seg_act[3,i],seg_act[3,i-1],
                                    seg_act[2,i],
                                    seg_act[1,i],seg_act[1,i-1],
                                    seg_act[0,i+1],seg_act[0,i],seg_act[0,i],
                                    0]))
        return hit_bin



    def _check_layer_hit(self,layer_in, edge_hit):
        """
        Checks frame layer <layer_in> for hits. Using edge_hit True/False segemnt edge mode can be
        choosen. For production use edge_hit=True as non edge_hit is only used for hardware module
        testing.
        """
        if(layer_in.layer_id == 0):
            n_segs = layer_in.n_segs
            hits = numpy.zeros(shape=(n_segs,16))
            # Segment 0
            seg_pre = layer_in.get_segment(n_segs-1)
            seg_act = layer_in.get_segment(0)
            seg_suc = layer_in.get_segment(1)
            hit_bin = self._populate_bin_inner(seg_pre, seg_act, seg_suc,edge_hit)
            hits[0] = numpy.array(list(map(self._detect_hit_inner, hit_bin)))
            # Inner segments
            for i in range (1,n_segs-1):
                seg_pre = layer_in.get_segment(i-1)
                seg_act = layer_in.get_segment(i)
                seg_suc = layer_in.get_segment(i+1)
                hit_bin = self._populate_bin_inner(seg_pre, seg_act, seg_suc,edge_hit)
                hits[i] = numpy.array(list(map(self._detect_hit_inner, hit_bin)))
            # Segment n_seg
            seg_pre = layer_in.get_segment(n_segs-2)
            seg_act = layer_in.get_segment(n_segs-1)
            seg_suc = layer_in.get_segment(0)
            hit_bin = self._populate_bin_inner(seg_pre, seg_act, seg_suc,edge_hit)
            hits[n_segs-1] = numpy.array(list(map(self._detect_hit_inner, hit_bin)))
        else:
            n_segs = layer_in.n_segs
            hits = numpy.zeros(shape=(n_segs,16))
            # Segment 0
            seg_pre = layer_in.get_segment(n_segs-1)
            seg_act = layer_in.get_segment(0)
            seg_suc = layer_in.get_segment(1)
            hit_bin = self._populate_bin_outer(seg_pre, seg_act, seg_suc,edge_hit)
            hits[0] = numpy.array(list(map(self._detect_hit_outer, hit_bin)))
            # Inner segments
            for i in range (1,n_segs-1):
                seg_pre = layer_in.get_segment(i-1)
                seg_act = layer_in.get_segment(i)
                seg_suc = layer_in.get_segment(i+1)
                hit_bin = self._populate_bin_outer(seg_pre, seg_act, seg_suc,edge_hit)
                hits[i] = numpy.array(list(map(self._detect_hit_outer, hit_bin)))
            # Segment n_seg
            seg_pre = layer_in.get_segment(n_segs-2)
            seg_act = layer_in.get_segment(n_segs-1)
            seg_suc = layer_in.get_segment(0)
            hit_bin = self._populate_bin_outer(seg_pre, seg_act, seg_suc,edge_hit)
            hits[n_segs-1] = numpy.array(list(map(self._detect_hit_outer, hit_bin)))

        return hits

    def _detect_hits(self,frame_in,edge_hit):
        """
        Detects hits of all layers in <frame_in> and saves output in tsf frame.
        Hardcoded to layer 0...8.

        Step 1: Calculate hits for each layer. Returns 2D Array of hits
                with indices <segment_id> whose range depends on the layer
                and 0...15 for each checked hit bin inside the dection algorithm.
                E.g. Bin 5 in Segment 3 was hit => hits[2,4] == True

        Step 2: Find all hits and fill output frame accordingly.
        """
        layer_id = 0
        layer_in = frame_in.get_layer(layer_id)
        layer_segments = self._frame.get_layer(layer_id).get_tsf_segments()
        hits = self._check_layer_hit(layer_in,edge_hit)

        for i in range(0,layer_in.n_segs):
            segment_id = i
            for j in range(0,16):
                if(hits[segment_id,j] == True):
                    layer_segments[segment_id,0,j] = 1

        for layer_id in range(1,9):
            layer_in = frame_in.get_layer(layer_id)
            layer_segments = self._frame.get_layer(layer_id).get_tsf_segments()
            hits = self._check_layer_hit(layer_in,edge_hit)

            for i in range(0,layer_in.n_segs):
                segment_id = i
                for j in range(0,16):
                    if(hits[segment_id,j] == True):
                        layer_segments[segment_id,2,j] = 1

        return self._frame


    def _detect_candidates(self,frame_in,edge_hit):
        """
        Detects hits of all layers in <frame_in> and saves output in tsf frame.
        Hardcoded to layer 1...8, because hardware implementation for layer 0
        is non existent. This feature could be implemented later.

        Step 1: Calculate hits for each layer. Returns 2D Array of hits
                with indices <segment_id> whose range depends on the layer
                and 0...15 for each checked hit bin inside the dection
                algorithm, e.g. Bin 5 in Segment 3 was hit => hits[2,4] == True

        Step 2: Find all hits and fill output frame accordingly.

        Identical to _detect_hit_outers() except that it populates all hit bin
        candidates to the internal output data frame.
        """
        layer_id = 0
        layer_in = frame_in.get_layer(layer_id)
        layer_segments = self._frame.get_layer(layer_id).get_tsf_segments()
        hits = self._check_layer_hit(layer_in,edge_hit)

        for i in range(0,layer_in.n_segs):
            segment_id = i
            for j in range(1,16-1):
                if(hits[segment_id,j] == True):
                    if(j==0):
                        layer_segments[segment_id-1,4,15] = 1
                        layer_segments[segment_id-1,4,14] = 1
                        layer_segments[segment_id,4,0] = 1
                        layer_segments[segment_id,4,1] = 1
                        layer_segments[segment_id,4,2] = 1
                        layer_segments[segment_id-1,3,14] = 1
                        layer_segments[segment_id-1,3,15] = 1
                        layer_segments[segment_id,3,0] = 1
                        layer_segments[segment_id,3,1] = 1
                        layer_segments[segment_id-1,2,15] = 1
                        layer_segments[segment_id,2,0] = 1
                        layer_segments[segment_id,2,1] = 1
                        layer_segments[segment_id-1,1,15] = 1
                        layer_segments[segment_id,1,0] = 1
                        layer_segments[segment_id,0,0] = 1
                    elif(j==1):
                        layer_segments[segment_id-1,4,15] = 1
                        layer_segments[segment_id,4,0] = 1
                        layer_segments[segment_id,4,1] = 1
                        layer_segments[segment_id,4,2] = 1
                        layer_segments[segment_id,4,3] = 1
                        layer_segments[segment_id-1,3,15] = 1
                        layer_segments[segment_id,3,0] = 1
                        layer_segments[segment_id,3,1] = 1
                        layer_segments[segment_id,3,2] = 1
                        layer_segments[segment_id,2,0] = 1
                        layer_segments[segment_id,2,1] = 1
                        layer_segments[segment_id,2,2] = 1
                        layer_segments[segment_id,1,0] = 1
                        layer_segments[segment_id,1,1] = 1
                        layer_segments[segment_id,0,1] = 1
                    elif(j==14):
                        layer_segments[segment_id,4,12] = 1
                        layer_segments[segment_id,4,13] = 1
                        layer_segments[segment_id,4,14] = 1
                        layer_segments[segment_id,4,15] = 1
                        layer_segments[(segment_id+1) % layer_in.n_segs,4,0] = 1
                        layer_segments[segment_id,3,12] = 1
                        layer_segments[segment_id,3,13] = 1
                        layer_segments[segment_id,3,14] = 1
                        layer_segments[segment_id,3,15] = 1
                        layer_segments[segment_id,2,13] = 1
                        layer_segments[segment_id,2,14] = 1
                        layer_segments[segment_id,2,15] = 1
                        layer_segments[segment_id,1,13] = 1
                        layer_segments[segment_id,1,14] = 1
                        layer_segments[segment_id,0,14] = 1
                    elif(j==15):
                        layer_segments[segment_id,4,13] = 1
                        layer_segments[segment_id,4,14] = 1
                        layer_segments[segment_id,4,15] = 1
                        layer_segments[segment_id+1 % layer_in.n_segs,4,0] = 1
                        layer_segments[segment_id+1 % layer_in.n_segs,4,1] = 1
                        layer_segments[segment_id,3,13] = 1
                        layer_segments[segment_id,3,14] = 1
                        layer_segments[segment_id,3,15] = 1
                        layer_segments[(segment_id+1) % layer_in.n_segs,3,0] = 1
                        layer_segments[segment_id,2,14] = 1
                        layer_segments[segment_id,2,15] = 1
                        layer_segments[(segment_id+1) % layer_in.n_segs,2,0] = 1
                        layer_segments[segment_id,1,14] = 1
                        layer_segments[segment_id,1,15] = 1
                        layer_segments[segment_id,0,15] = 1
                    else:
                        layer_segments[segment_id,4,j-2] = 1
                        layer_segments[segment_id,4,j-1] = 1
                        layer_segments[segment_id,4,j] = 1
                        layer_segments[segment_id,4,j+1] = 1
                        layer_segments[segment_id,4,j+2] = 1
                        layer_segments[segment_id,3,j-2] = 1
                        layer_segments[segment_id,3,j-1] = 1
                        layer_segments[segment_id,3,j] = 1
                        layer_segments[segment_id,3,j+1] = 1
                        layer_segments[segment_id,2,j-1] = 1
                        layer_segments[segment_id,2,j] = 1
                        layer_segments[segment_id,2,j+1] = 1
                        layer_segments[segment_id,1,j-1] = 1
                        layer_segments[segment_id,1,j] = 1
                        layer_segments[segment_id,0,j] = 1

        for layer_id in range(1,9):
            layer_in = frame_in.get_layer(layer_id)
            layer_segments = self._frame.get_layer(layer_id).get_tsf_segments()
            hits = self._check_layer_hit(layer_in,edge_hit)

            for i in range(0,layer_in.n_segs):
                segment_id = i
                for j in range(1,16-1):
                    if(hits[segment_id,j] == True):
                        if(j==0):
                            layer_segments[segment_id-1,4,15] = 1
                            layer_segments[segment_id,4,0] = 1
                            layer_segments[segment_id,4,1] = 1
                            layer_segments[segment_id-1,3,15] = 1
                            layer_segments[segment_id,3,0] = 1
                            layer_segments[segment_id,2,0] = 1
                            layer_segments[segment_id-1,1,15] = 1
                            layer_segments[segment_id,1,0] = 1
                            layer_segments[segment_id,0,1] = 1
                            layer_segments[segment_id-1,0,15] = 1
                            layer_segments[segment_id,0,0] = 1
                        elif(j==15):
                            layer_segments[segment_id,4,14] = 1
                            layer_segments[segment_id,4,15] = 1
                            layer_segments[(segment_id+1) % layer_in.n_segs,4,0] = 1
                            layer_segments[segment_id,3,14] = 1
                            layer_segments[segment_id,3,15] = 1
                            layer_segments[segment_id,2,15] = 1
                            layer_segments[segment_id,1,14] = 1
                            layer_segments[segment_id,1,15] = 1
                            layer_segments[(segment_id+1) % layer_in.n_segs,0,0] = 1
                            layer_segments[segment_id,0,14] = 1
                            layer_segments[segment_id,0,15] = 1
                        else:
                            layer_segments[segment_id,4,j-1] = 1
                            layer_segments[segment_id,4,j] = 1
                            layer_segments[segment_id,4,j+1] = 1
                            layer_segments[segment_id,3,j-1] = 1
                            layer_segments[segment_id,3,j] = 1
                            layer_segments[segment_id,2,j] = 1
                            layer_segments[segment_id,1,j-1] = 1
                            layer_segments[segment_id,1,j] = 1
                            layer_segments[segment_id,0,j+1] = 1
                            layer_segments[segment_id,0,j-1] = 1
                            layer_segments[segment_id,0,j] = 1
        return self._frame


    def get_frame(self):
        return self._frame


    def detect(self,frame_in,mode='hits',edge_hit=True):
        frame_out = None
        if(mode == 'hits'):
            self.mode = 'hits'
            frame_out = self._detect_hits(frame_in,edge_hit)
        elif(mode == 'candidates'):
            self._mode = 'candidates'
            frame_out = self._detect_candidates(frame_in,edge_hit)
        else:
            raise ValueError(mode)

        return frame_out


    def clear(self):
        self._frame = self._frame.clear()
        return self._frame
