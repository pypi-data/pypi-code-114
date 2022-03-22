# standard imports
import json
import logging
import os

# external imports
from chainlib.chain import ChainSpec
# local imports
from cic.contract.base import Data, data_dir

logg = logging.getLogger(__name__)


class Network(Data):
    """Contains network settings for token deployments across extensions.

    Extension targets are defined by the keys immediately following the "resources" key in the network settings file.

    :param path: Path to settings directory
    :type path: str
    :param targets: Extension targets to execute
    :type targets: list of str
    """
    def __init__(self, path='.', targets=[]):
        super(Network, self).__init__()
        self.resources = None
        self.path = path
        self.targets = targets
        self.network_path = os.path.join(self.path, 'network.json')


    def load(self):
        """Load network settings from file.
        """
        super(Network, self).load()

        with open(self.network_path, 'r', encoding='utf-8') as f:
            o = json.load(f)

        self.resources = o['resources']

        self.inited = True


    def start(self):
        """Initialize network settings with targets chosen at object instantiation.

        Will save to network settings file.
        """
        super(Network, self).load()

        network_template_file_path = os.path.join(data_dir, f'network_template_v{self.version()}.json')
        
        with open(network_template_file_path, encoding='utf-8') as f:
            o_part = json.load(f)

        self.resources = {}
        for v in self.targets:
            self.resources[v] = o_part

        self.save()


    def save(self):
        """Save network settings to file.
        """
        with open(self.network_path, 'w', encoding='utf-8') as f:
            json.dump({
                'resources': self.resources,
                }, f, sort_keys=True, indent="\t")


    def resource(self, k):
        """Get settings definitions for a given extension.

        :param k: Extension key
        :type k: str
        :rtype: dict
        :return: Extension settings
        """
        v = self.resources.get(k)
        if v is None:
            raise AttributeError(f'No defined reference for {k}')
        return v


    def resource_set(self, resource_key, content_key, reference, key_account=None):
        """Set the values a content part of an extension setting.
        
        The content parts define network application resources. Each entry is keyed by the name of the application. Each value consists of a key_account used to write/deploy to the contract, and the reference (address) of the application resource. If no application resource yet exists on the network for the part, the reference value will be None.

        :param resource_key: Extension key
        :type resource_key: str
        :param content_key: Resource name (e.g. smart contract name)
        :type content_key: str
        :param reference: Reference to resource on network (e.g. smart contract address)
        :type reference: str
        :param key_account: Address of account to sign transaction for the resource with
        :type key_account: str

        """
        self.resources[resource_key]['contents'][content_key]['reference'] = reference
        self.resources[resource_key]['contents'][content_key]['key_account'] = key_account


    def chain_spec(self, k):
        """Retrieve chain spec for the given extension

        :param k: Extension key
        :type k: str
        :rtype: chainlib.chain.ChainSpec
        :return: Chain spec object
        """
        v = self.resource(k)
        return ChainSpec.from_dict(v['chain_spec'])


    def set(self, resource_key, chain_spec):
        """Set chain spec for resource.

        :param resource_key: Extension key
        :type resource_key: str
        :param chain_spec: Chain spec to set
        :type chain_spec: chainlib.chain.ChainSpec
        """
        chain_spec_dict = chain_spec.asdict()
        for k in chain_spec_dict.keys():
            logg.debug(f'resources: {self.resources}')
            self.resources[resource_key]['chain_spec'][k] = chain_spec_dict[k]


    def __str__(self):
        s = ''
        for resource in self.resources.keys():
            chainspec = ChainSpec.from_dict(self.resources[resource]['chain_spec'])
            s += f'{resource}.chain_spec: {str(chainspec)}\n'
            for content_key in self.resources[resource]['contents'].keys():
                content_value = self.resources[resource]['contents'][content_key]
                if content_value is None:
                    content_value = ''
                s += f'{resource}.contents.{content_key} = {json.dumps(content_value, indent=4, sort_keys=True)}\n'

        return s
