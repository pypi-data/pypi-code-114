from paddle import inference
import numpy as np

def create_predictor(args):
    model_dir = args.model_dir

    model_file_path = model_dir + "/inference.pdmodel"
    params_file_path = model_dir + "/inference.pdiparams"

    config = inference.Config(model_file_path, params_file_path)
    precision = inference.PrecisionType.Float32

    if args.use_gpu:
        config.enable_use_gpu(args.gpu_mem, 0)
        if args.use_tensorrt:
            config.enable_tensorrt_engine(
                workspace_size=1 << 30,
                precision_mode=precision,
                max_batch_size=1,
                min_subgraph_size=args.min_subgraph_size)
            # skip the minmum trt subgraph
        use_dynamic_shape = True
        min_input_shape = {
            "x": [1, 3, 50, 50],
            "conv2d_92.tmp_0": [1, 120, 20, 20],
            "conv2d_91.tmp_0": [1, 24, 10, 10],
            "conv2d_59.tmp_0": [1, 96, 20, 20],
            "nearest_interp_v2_1.tmp_0": [1, 256, 10, 10],
            "nearest_interp_v2_2.tmp_0": [1, 256, 20, 20],
            "conv2d_124.tmp_0": [1, 256, 20, 20],
            "nearest_interp_v2_3.tmp_0": [1, 64, 20, 20],
            "nearest_interp_v2_4.tmp_0": [1, 64, 20, 20],
            "nearest_interp_v2_5.tmp_0": [1, 64, 20, 20],
            "elementwise_add_7": [1, 56, 2, 2],
            "nearest_interp_v2_0.tmp_0": [1, 256, 2, 2],
            "conv2d_118.tmp_1": [1, 256, 10, 10],
            "conv2d_119.tmp_1": [1, 256, 10, 10],
            "deformable_conv_12.tmp_0": [1, 512, 10, 10],
            "relu_14.tmp_0": [1, 2048, 10, 10]
        }
        max_input_shape = {
            "x": [1, 3, 1536, 1536],
            "conv2d_92.tmp_0": [1, 120, 400, 400],
            "conv2d_91.tmp_0": [1, 24, 200, 200],
            "conv2d_59.tmp_0": [1, 96, 400, 400],
            "nearest_interp_v2_1.tmp_0": [1, 256, 200, 200],
            "conv2d_124.tmp_0": [1, 256, 400, 400],
            "nearest_interp_v2_2.tmp_0": [1, 256, 400, 400],
            "nearest_interp_v2_3.tmp_0": [1, 64, 400, 400],
            "nearest_interp_v2_4.tmp_0": [1, 64, 400, 400],
            "nearest_interp_v2_5.tmp_0": [1, 64, 400, 400],
            "elementwise_add_7": [1, 56, 400, 400],
            "nearest_interp_v2_0.tmp_0": [1, 256, 400, 400],
            "conv2d_118.tmp_1": [1, 256, 400, 400],
            "conv2d_119.tmp_1": [1, 256, 400, 400],
            "deformable_conv_12.tmp_0": [1, 512, 400, 400],
            "relu_14.tmp_0": [1, 2048, 400, 400]
        }
        opt_input_shape = {
            "x": [1, 3, 640, 640],
            "conv2d_92.tmp_0": [1, 120, 160, 160],
            "conv2d_91.tmp_0": [1, 24, 80, 80],
            "conv2d_59.tmp_0": [1, 96, 160, 160],
            "nearest_interp_v2_1.tmp_0": [1, 256, 80, 80],
            "nearest_interp_v2_2.tmp_0": [1, 256, 160, 160],
            "conv2d_124.tmp_0": [1, 256, 160, 160],
            "nearest_interp_v2_3.tmp_0": [1, 64, 160, 160],
            "nearest_interp_v2_4.tmp_0": [1, 64, 160, 160],
            "nearest_interp_v2_5.tmp_0": [1, 64, 160, 160],
            "elementwise_add_7": [1, 56, 40, 40],
            "nearest_interp_v2_0.tmp_0": [1, 256, 40, 40],
            "conv2d_118.tmp_1": [1, 256, 400, 400],
            "conv2d_119.tmp_1": [1, 256, 400, 400],
            "deformable_conv_12.tmp_0": [1, 512, 400, 400],
            "relu_14.tmp_0": [1, 2048, 400, 400]
        }
        min_pact_shape = {
            "nearest_interp_v2_26.tmp_0": [1, 256, 20, 20],
            "nearest_interp_v2_27.tmp_0": [1, 64, 20, 20],
            "nearest_interp_v2_28.tmp_0": [1, 64, 20, 20],
            "nearest_interp_v2_29.tmp_0": [1, 64, 20, 20]
        }
        max_pact_shape = {
            "nearest_interp_v2_26.tmp_0": [1, 256, 400, 400],
            "nearest_interp_v2_27.tmp_0": [1, 64, 400, 400],
            "nearest_interp_v2_28.tmp_0": [1, 64, 400, 400],
            "nearest_interp_v2_29.tmp_0": [1, 64, 400, 400]
        }
        opt_pact_shape = {
            "nearest_interp_v2_26.tmp_0": [1, 256, 160, 160],
            "nearest_interp_v2_27.tmp_0": [1, 64, 160, 160],
            "nearest_interp_v2_28.tmp_0": [1, 64, 160, 160],
            "nearest_interp_v2_29.tmp_0": [1, 64, 160, 160]
        }
        min_input_shape.update(min_pact_shape)
        max_input_shape.update(max_pact_shape)
        opt_input_shape.update(opt_pact_shape)
        config.set_trt_dynamic_shape_info(
                min_input_shape, max_input_shape, opt_input_shape)

    else:
        config.disable_gpu()
        if hasattr(args, "cpu_threads"):
            config.set_cpu_math_library_num_threads(args.cpu_threads)
        else:
            # default cpu threads as 10
            config.set_cpu_math_library_num_threads(10)
        if args.enable_mkldnn:
            # cache 10 different shapes for mkldnn to avoid memory leak
            config.set_mkldnn_cache_capacity(10)
            config.enable_mkldnn()
            if args.precision == "fp16":
                config.enable_mkldnn_bfloat16()
    # enable memory optim
    config.enable_memory_optim()
    # config.disable_glog_info()
    print("GLOG INFO is: {}".format(config.glog_info_disabled()))
    config.delete_pass("conv_transpose_eltwiseadd_bn_fuse_pass")
    config.switch_use_feed_fetch_ops(False)
    config.switch_ir_optim(True)

    # create predictor
    print(config.summary())
    predictor = inference.create_predictor(config)
    input_names = predictor.get_input_names()
    for name in input_names:
        input_tensor = predictor.get_input_handle(name)
    output_names = predictor.get_output_names()
    output_tensors = []
    for output_name in output_names:
        output_tensor = predictor.get_output_handle(output_name)
        output_tensors.append(output_tensor)
    return predictor, input_tensor, output_tensors, config

def str2bool(v):
    return v.lower() in ("true", "t", "1")


def init_args():
    import argparse
    parser = argparse.ArgumentParser()
    # params for prediction engine
    parser.add_argument("--model_dir", type=str, default='')
    parser.add_argument("--use_gpu", type=str2bool, default=True)
    parser.add_argument("--ir_optim", type=str2bool, default=True)
    parser.add_argument("--use_tensorrt", type=str2bool, default=False)
    parser.add_argument("--min_subgraph_size", type=int, default=15)
    parser.add_argument("--precision", type=str, default="fp32")
    parser.add_argument("--gpu_mem", type=int, default=500)

    # FCE parmas
    parser.add_argument("--scales", type=list, default=[8, 16, 32])
    parser.add_argument("--alpha", type=float, default=1.0)
    parser.add_argument("--beta", type=float, default=1.0)
    parser.add_argument("--fourier_degree", type=int, default=5)
    parser.add_argument("--det_fce_box_type", type=str, default='poly')

    parser.add_argument("--enable_mkldnn", type=str2bool, default=False)
    parser.add_argument("--cpu_threads", type=int, default=10)
    parser.add_argument("--use_pdserving", type=str2bool, default=False)
    parser.add_argument("--warmup", type=str2bool, default=False)

    return parser


if __name__ == "__main__":
    args = init_args().parse_args()
    predictor, input_tensor, output_tensors, config = create_predictor(
            args)
    
    img = np.ones([1,3,640,640]).astype('float32')
    input_tensor.copy_from_cpu(img)
    predictor.run()
    for output_tensor in output_tensors:
        output = output_tensor.copy_to_cpu()
        print(output.shape)
