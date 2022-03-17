import argparse
import torch
import torch.backends.cudnn as cudnn
from torchvision import models
from data_aug.contrastive_learning_dataset import ContrastiveLearningDataset_PCL
from models.resnet_simclr import ResNetSimCLR, ResNetSimCLR_pretrained
from simclr import SimCLR
from data_aug.view_generator import ContrastiveLearningViewGenerator
from torchvision.transforms import transforms
from data_aug.gaussian_blur import GaussianBlur

model_names = sorted(name for name in models.__dict__
                     if name.islower() and not name.startswith("__")
                     and callable(models.__dict__[name]))

parser = argparse.ArgumentParser(description='PyTorch SimCLR')
parser.add_argument('-data_dir', metavar='DIR', default='/mnt/g/Mi Unidad/Proyectos/NaroNet/Datasets/Tumor_subtype/', 
                    help='path to dataset')
parser.add_argument('-a', '--arch', metavar='ARCH', default='resnet50',
                    choices=model_names, help='model architecture: ' + ' | '.join(model_names) + ' (default: resnet50)')
parser.add_argument('-j', '--workers', default=0, type=int, metavar='N',
                    help='number of data loading workers (default: 32)')
parser.add_argument('--epochs', default=60, type=int, metavar='N', help='number of total epochs to run')
parser.add_argument('-n_crops_per_image', default=10, type=int,                    
                    help='Number of images used in each iteration')    
parser.add_argument('-patch_size', default=400, type=int,                 
                    help='Number of images used in each iteration')     
parser.add_argument('-n_channels', default=3, type=int,                 
                    help='Number of images used in each iteration')                     
parser.add_argument('-stride', default=0, type=int,                 
                    help='Number of images used in each iteration')                         
parser.add_argument('-alpha_L', default=1.1, type=int,                 
                    help='ALPHA_L')  
parser.add_argument('-z_score', default=True, type=bool,                 
                    help='z_score')                                                                          
parser.add_argument('-batch_size', default=5, type=int,
                    metavar='N',
                    help='mini-batch size (default: 256), this is the total '
                         'batch size of all GPUs on the current node when '
                         'using Data Parallel or Distributed Data Parallel')
parser.add_argument('--lr', '--learning-rate', default=0.003, type=float,
                    metavar='LR', help='initial learning rate', dest='lr')
parser.add_argument('--wd', '--weight-decay', default=1e-4, type=float,
                    metavar='W', help='weight decay (default: 1e-4)',
                    dest='weight_decay')
parser.add_argument('--seed', default=None, type=int,
                    help='seed for initializing training. ')
parser.add_argument('--disable-cuda', action='store_true',
                    help='Disable CUDA')
parser.add_argument('--fp16-precision', action='store_true',
                    help='Whether or not to use 16-bit precision GPU training.')
parser.add_argument('--out_dim', default=256, type=int,
                    help='feature dimension (default: 128)')
parser.add_argument('--log-every-n-steps', default=1, type=int,
                    help='Log every n steps')
parser.add_argument('--temperature', default=0.07, type=float,
                    help='softmax temperature (default: 0.07)')
parser.add_argument('--n-views', default=2, type=int, metavar='N',
                    help='Number of views for contrastive learning training.')
parser.add_argument('--gpu-index', default=0, type=int, help='Gpu index.')


def main():
    args = parser.parse_args()
    assert args.n_views == 2, "Only two view training is supported. Please use --n-views 2."
    
    # check if gpu training is available
    if not args.disable_cuda and torch.cuda.is_available():
        args.device = torch.device('cuda:0')
        cudnn.deterministic = True
        cudnn.benchmark = True
    else:
        args.device = torch.device('cpu')
        args.gpu_index = -1    
            
    # Create train_loader
    dataset_PCL = ContrastiveLearningDataset_PCL(args,training=True)
    train_loader = torch.utils.data.DataLoader(
        dataset_PCL, batch_size=args.batch_size, shuffle=True,
        num_workers=args.workers, pin_memory=True, drop_last=True)

    # Create infer_loader
    dataset_PCL = ContrastiveLearningDataset_PCL(args,training=False)
    infer_loader = torch.utils.data.DataLoader(
        dataset_PCL, batch_size=1, shuffle=False,
        num_workers=args.workers, pin_memory=False, drop_last=True)

    # Create ResNet model
    model = ResNetSimCLR_pretrained(in_channels= dataset_PCL.in_channels, base_model=args.arch, out_dim=args.out_dim)

    # Create optimizer
    optimizer = torch.optim.Adam(model.parameters(), args.lr, weight_decay=args.weight_decay)

    # Create scheduler
    scheduler = torch.optim.lr_scheduler.CosineAnnealingLR(optimizer, T_max=len(train_loader), eta_min=0,
                                                           last_epoch=-1)

    #  It’s a no-op if the 'gpu_index' argument is a negative integer or None.
    with torch.cuda.device(args.gpu_index):
        simclr = SimCLR(model=model, optimizer=optimizer, scheduler=scheduler, args=args)
        # simclr.train(train_loader)
        args.device = torch.device('cpu')
        simclr.infer(infer_loader)

if __name__ == "__main__":
    main()
