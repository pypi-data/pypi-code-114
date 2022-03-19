#!/usr/bin/env python3
# -*- coding: utf-8 -*-
#
#  add-vpn-client.py
#
#  Maintainers: Eng. Alexis Janero
#
#  This program is free software; you can redistribute it and/or modify
#  it under the terms of the GNU General Public License as published by
#  the Free Software Foundation; either version 2 of the License, or
#  (at your option) any later version.
#  
#  This program is distributed in the hope that it will be useful,
#  but WITHOUT ANY WARRANTY; without even the implied warranty of
#  MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#  GNU General Public License for more details.
#  
#  You should have received a copy of the GNU General Public License
#  along with this program; if not, write to the Free Software
#  Foundation, Inc., 51 Franklin Street, Fifth Floor, Boston,
#  MA 02110-1301, USA.
#  
#

import shutil
import subprocess
import os
import argparse
import sys
# from dotenv import load_dotenv
# load_dotenv()


def deploy_local():
    
    print("deploy local cluster with vagrant")
    vagrant_dir = f'{os.environ.get("HOME")}/vagrant_cluster'
    if os.path.exists(vagrant_dir):
        os.makedirs(vagrant_dir)
        print("el dir existe")
        sys.exit(0)
    shutil.copytree("infrastructure/vagrant", vagrant_dir)
    os.chdir(vagrant_dir)
    subprocess.run(["vagrant", "up"])
    # subprocess.run(["vagrant", "up"])



if __name__ == '__main__':
    """
    Main function of the script, reads parameters from command and executes operations.
    :return:
    """
    script_description = '''
    This script deploys Kubernetes on a cluster of virtual machines.
    '''
    # if os.geteuid() != 0:
    #     exit("You need to have root privileges to run this script. \n"
    #          "Please, try again, this time using 'sudo'. Exiting.")

    # Initiate the parser with a description
    parser = argparse.ArgumentParser(description=script_description)

    parser.add_argument("--local", "-L" , action="store_true", help="Deploy local cluster")
    parser.add_argument("--openstack", "-O", action="store_true", help="Deploy OpenStack cluster")
    parser.add_argument("--master-count", "-m", type=int, help="Number of master nodes to deploy")
    parser.add_argument("--worker-count", "-c", type=int, help="Number of worker nodes to deploy")
    parser.add_argument("--flavour", "-F", type=str, help="To define OS and size of VMs")
    parser.add_argument("--config-file", "-f", type=str, help="To read configuration from config file")
    parser.add_argument("--destory", "-D", type=str, help="To destroy the cluster")

    # Read arguments from the command line
    args = parser.parse_args()

    if args.local:
        
        deploy_local()
        
    elif args.openstack:
        
        print('deploy OpenStack cluster')
    
    else:
        print('You need to add one of the following options '
              '-A or -F or -D')
