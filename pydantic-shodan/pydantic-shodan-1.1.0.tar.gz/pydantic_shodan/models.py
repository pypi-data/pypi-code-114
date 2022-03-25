from __future__ import annotations

from enum import Enum
from typing import Any, Dict, List, Optional, Union

from pydantic import BaseModel, Extra, Field


class EthereumPeer(BaseModel):
    ip: Optional[str] = Field(None, title="IP")
    pubkey: Optional[str] = Field(None, title="Public Key")
    udp_port: Optional[int] = Field(None, title="UDP Port")
    tcp_port: Optional[int] = Field(None, title="TCP Port")


class EthereumP2p(BaseModel):
    pubkey: Optional[str] = Field(None, title="Public Key")
    udp_port: Optional[int] = Field(None, title="UDP Port")
    tcp_port: Optional[int] = Field(None, title="TCP Port")
    neighbors: Optional[List[EthereumPeer]]


class MacAddressInfo(BaseModel):
    assignment: str = Field(..., title="Assignment")
    date: Optional[str] = Field(None, title="Date")
    org: str = Field(..., title="Org")


class Tag(Enum):
    c2 = "c2"
    cdn = "cdn"
    cloud = "cloud"
    compromised = "compromised"
    cryptocurrency = "cryptocurrency"
    database = "database"
    devops = "devops"
    doublepulsar = "doublepulsar"
    honeypot = "honeypot"
    ics = "ics"
    iot = "iot"
    malware = "malware"
    medical = "medical"
    onion = "onion"
    self_signed = "self-signed"
    scanner = "scanner"
    starttls = "starttls"
    tor = "tor"
    videogame = "videogame"
    vpn = "vpn"


class Vulnerability(BaseModel):
    cvss: float = Field(..., title="Cvss")
    references: List[str] = Field(..., title="References")
    summary: str = Field(..., title="Summary")
    verified: bool = Field(..., title="Verified")


class Location(BaseModel):
    area_code: Optional[str] = Field(None, description="Deprecated", title="Area Code")
    city: Optional[str] = Field(None, title="City")
    country_code: Optional[str] = Field(None, title="Country Code")
    country_code3: Optional[str] = Field(
        None, description="Deprecated", title="Country Code3"
    )
    country_name: Optional[str] = Field(None, title="Country Name")
    dma_code: Optional[str] = Field(None, title="Dma Code")
    latitude: Optional[float] = Field(None, title="Latitude")
    longitude: Optional[float] = Field(None, title="Longitude")
    postal_code: Optional[str] = Field(
        None, description="Deprecated", title="Postal Code"
    )
    region_code: Optional[str] = Field(None, title="Region Code")


class _ShodanOptions(BaseModel):
    hostname: Optional[str] = Field(
        None,
        description='Hostname that was used to talk to the service (ex. for HTTP it would set the "Host:" header to this hostname)',
        title="Hostname",
    )
    referrer: Optional[str] = Field(
        None,
        description="Banner ID that triggered the creation of the current banner",
        title="Referrer",
    )
    scan: Optional[str] = Field(
        None,
        description="Unique scan ID that identifies the request that launched the scan",
        title="Scan",
    )


class _Shodan(BaseModel):
    crawler: str = Field(..., description="Unique ID of the crawler", title="Crawler")
    id: str = Field(
        ...,
        description='Unique ID of the banner; used in the "_shodan.options.referrer" to indicate when the current banner was generated as a result of another banner',
        title="Id",
    )
    module: str = Field(
        ...,
        description="The initial protocol that the crawler used when talking to the service",
        title="Module",
    )
    options: _ShodanOptions
    ptr: Optional[bool] = Field(
        None, description="Whether or not the crawler has a PTR entry", title="Ptr"
    )


class AfpFlags(BaseModel):
    copy_file: bool = Field(..., title="Copy File")
    flag_hex: str = Field(..., title="Flag Hex")
    open_directory: bool = Field(..., title="Open Directory")
    password_changing: bool = Field(..., title="Password Changing")
    password_saving_prohibited: bool = Field(..., title="Password Saving Prohibited")
    reconnect: bool = Field(..., title="Reconnect")
    server_messages: bool = Field(..., title="Server Messages")
    server_notifications: bool = Field(..., title="Server Notifications")
    server_signature: bool = Field(..., title="Server Signature")
    super_client: bool = Field(..., title="Super Client")
    tcp_ip: bool = Field(..., title="Tcp Ip")
    utf8_server_name: bool = Field(..., title="Utf8 Server Name")
    uuids: bool = Field(..., title="Uuids")


class Afp(BaseModel):
    afp_versions: List[str] = Field(..., title="Afp Versions")
    directory_names: Optional[List[str]] = Field(None, title="Directory Names")
    machine_type: str = Field(..., title="Machine Type")
    network_addresses: Optional[List[Optional[str]]] = Field(
        None, title="Network Addresses"
    )
    server_flags: AfpFlags
    server_name: str = Field(..., title="Server Name")
    server_signature: Optional[str] = Field(None, title="Server Signature")
    uams: List[str] = Field(..., title="Uams")
    utf8_server_name: Optional[str] = Field(None, title="Utf8 Server Name")


class Airplay(BaseModel):
    access_control_level: Optional[str] = Field(None, title="Access Control Level")
    airplay_version: Optional[str] = Field(None, title="Airplay Version")
    bluetooth_address: Optional[str] = Field(None, title="Bluetooth Address")
    company: Optional[str] = Field(None, title="Company")
    device_id: Optional[str] = Field(None, title="Device Id")
    device_model: Optional[str] = Field(None, title="Device Model")
    firmware_build: Optional[str] = Field(None, title="Firmware Build")
    firmware_build_date: Optional[str] = Field(None, title="Firmware Build Date")
    firmware_version: Optional[str] = Field(None, title="Firmware Version")
    hardware_revision: Optional[str] = Field(None, title="Hardware Revision")
    mac_address: Optional[str] = Field(None, title="Mac Address")
    manufacturer: Optional[str] = Field(None, title="Manufacturer")
    name: Optional[str] = Field(None, title="Name")
    os_build_version: Optional[str] = Field(None, title="Os Build Version")
    os_version: Optional[str] = Field(None, title="Os Version")
    protocol_version: Optional[str] = Field(None, title="Protocol Version")
    sdk: Optional[str] = Field(None, title="Sdk")
    serial_number: Optional[str] = Field(None, title="Serial Number")
    vodka_version: Optional[int] = Field(None, title="Vodka Version")


class AndroidDebugBridge(BaseModel):
    device: str = Field(..., title="Device")
    model: str = Field(..., title="Model")
    name: str = Field(..., title="Name")


class BgpMessage(BaseModel):
    length: int = Field(..., title="Length")
    marker: Optional[str] = Field(None, title="Marker")
    type: str = Field(..., title="Type")
    asn: Optional[int] = Field(None, title="Asn")
    bgp_identifer: Optional[str] = Field(None, title="Bgp Identifer")
    hold_time: Optional[int] = Field(None, title="Hold Time")
    version: Optional[int] = Field(None, title="Version")
    error_code: Optional[str] = Field(None, title="Error Code")
    error_subcode: Optional[str] = Field(None, title="Error Subcode")


class Bgp(BaseModel):
    messages: List[BgpMessage] = Field(..., title="Messages")


class BitcoinPeer(BaseModel):
    ip: str = Field(..., title="Ip")
    port: int = Field(..., title="Port")


class BitcoinAddress(BaseModel):
    ipv4: str = Field(..., title="Ipv4")
    ipv6: str = Field(..., title="Ipv6")
    port: int = Field(..., title="Port")
    services: int = Field(..., title="Services")
    timestamp: Optional[int] = Field(None, title="Timestamp")


class BitcoinMessage(BaseModel):
    checksum: str = Field(..., title="Checksum")
    command: str = Field(..., title="Command")
    from_addr: Optional[BitcoinAddress] = None
    lastblock: Optional[int] = Field(None, title="Lastblock")
    length: int = Field(..., title="Length")
    magic_number: str = Field(..., title="Magic Number")
    nonce: Optional[int] = Field(None, title="Nonce")
    relay: Optional[bool] = Field(None, title="Relay")
    services: Optional[int] = Field(None, title="Services")
    timestamp: Optional[int] = Field(None, title="Timestamp")
    to_addr: Optional[BitcoinAddress] = None
    user_agent: Optional[str] = Field(None, title="User Agent")
    version: Optional[int] = Field(None, title="Version")


class Bitcoin(BaseModel):
    addresses: List[BitcoinPeer] = Field(..., title="Addresses")
    handshake: List[BitcoinMessage] = Field(..., title="Handshake")


class Cassandra(BaseModel):
    name: str = Field(..., title="Name")
    keyspaces: List[str] = Field(..., title="Keyspaces")
    partitioner: str = Field(..., title="Partitioner")
    snitch: str = Field(..., title="Snitch")
    version: str = Field(..., title="Version")


class Checkpoint(BaseModel):
    firewall_host: str = Field(..., title="Firewall Host")
    smartcenter_host: str = Field(..., title="Smartcenter Host")


class ChromecastBuildInfo(BaseModel):
    build_type: Optional[int] = Field(None, title="Build Type")
    cast_build_revision: Optional[str] = Field(None, title="Cast Build Revision")
    cast_control_version: Optional[int] = Field(None, title="Cast Control Version")
    release_track: Optional[str] = Field(None, title="Release Track")
    system_build_number: Optional[str] = Field(None, title="System Build Number")


class ChromecastDeviceInfo(BaseModel):
    cloud_device_id: Optional[str] = Field(None, title="Cloud Device Id")
    device_name: Optional[str] = Field(None, title="Device Name")
    hotspot_bssid: Optional[str] = Field(None, title="Hotspot Bssid")
    mac_address: Optional[str] = Field(None, title="Mac Address")
    manufacturer: Optional[str] = Field(None, title="Manufacturer")
    model_name: Optional[str] = Field(None, title="Model Name")
    product_name: Optional[str] = Field(None, title="Product Name")
    public_key: Optional[str] = Field(None, title="Public Key")
    ssdp_udn: Optional[str] = Field(None, title="Ssdp Udn")
    uma_client_id: Optional[str] = Field(None, title="Uma Client Id")


class ChromecastNet(BaseModel):
    ethernet_connected: Optional[bool] = Field(None, title="Ethernet Connected")
    ip_address: Optional[str] = Field(None, title="Ip Address")
    online: Optional[bool] = Field(None, title="Online")


class ChromecastWifi(BaseModel):
    ssid: Optional[str] = Field(None, title="Ssid")
    bssid: Optional[str] = Field(None, title="Bssid")


class Chromecast(BaseModel):
    build_info: Optional[ChromecastBuildInfo] = None
    device_info: Optional[ChromecastDeviceInfo] = None
    net: Optional[ChromecastNet] = None
    version: int = Field(..., title="Version")
    wifi: Optional[ChromecastWifi] = None


class Cloud(BaseModel):
    provider: str = Field(..., title="Provider")
    region: Optional[str] = Field(None, title="Region")
    service: Optional[str] = Field(None, title="Service")


class Coap(BaseModel):
    resources: Dict[str, Dict[str, Any]] = Field(..., title="Resources")


class CobaltStrikeBeaconDetails(BaseModel):
    beacon_type: str = Field(..., title="Beacon Type")
    dns_beacon_strategy_fail_seconds: Optional[int] = Field(
        None,
        alias="dns-beacon.strategy_fail_seconds",
        title="Dns-Beacon.Strategy Fail Seconds",
    )
    dns_beacon_strategy_fail_x: Optional[int] = Field(
        None, alias="dns-beacon.strategy_fail_x", title="Dns-Beacon.Strategy Fail X"
    )
    dns_beacon_strategy_rotate_seconds: Optional[int] = Field(
        None,
        alias="dns-beacon.strategy_rotate_seconds",
        title="Dns-Beacon.Strategy Rotate Seconds",
    )
    http_get_client: List[str] = Field(
        ..., alias="http-get.client", title="Http-Get.Client"
    )
    http_get_uri: str = Field(..., alias="http-get.uri", title="Http-Get.Uri")
    http_get_verb: str = Field(..., alias="http-get.verb", title="Http-Get.Verb")
    http_post_client: List[str] = Field(
        ..., alias="http-post.client", title="Http-Post.Client"
    )
    http_post_uri: str = Field(..., alias="http-post.uri", title="Http-Post.Uri")
    http_post_verb: str = Field(..., alias="http-post.verb", title="Http-Post.Verb")
    jitter: Optional[int] = Field(None, title="Jitter")
    kill_date: Optional[int] = Field(None, title="Kill Date")
    maxgetsize: int = Field(..., title="Maxgetsize")
    port: int = Field(..., title="Port")
    post_ex_spawnto_x64: str = Field(
        ..., alias="post-ex.spawnto_x64", title="Post-Ex.Spawnto X64"
    )
    post_ex_spawnto_x86: str = Field(
        ..., alias="post-ex.spawnto_x86", title="Post-Ex.Spawnto X86"
    )
    process_inject_execute: Optional[List[str]] = Field(
        None, alias="process-inject.execute", title="Process-Inject.Execute"
    )
    process_inject_min_alloc: Optional[int] = Field(
        None, alias="process-inject.min_alloc", title="Process-Inject.Min Alloc"
    )
    process_inject_startrwx: Optional[int] = Field(
        None, alias="process-inject.startrwx", title="Process-Inject.Startrwx"
    )
    process_inject_userwx: Optional[int] = Field(
        None, alias="process-inject.userwx", title="Process-Inject.Userwx"
    )
    proxy_behavior: Optional[Union[int, str]] = Field(
        None, alias="proxy.behavior", title="Proxy.Behavior"
    )
    sleeptime: int = Field(..., title="Sleeptime")
    stage_cleanup: Optional[int] = Field(
        None, alias="stage.cleanup", title="Stage.Cleanup"
    )
    useragent_header: str = Field(..., title="Useragent Header")
    watermark: Optional[int] = Field(None, title="Watermark")


class CobaltStrikeBeacon(BaseModel):
    x86: Optional[CobaltStrikeBeaconDetails] = None
    x64: Optional[CobaltStrikeBeaconDetails] = None


class Consul(BaseModel):
    Datacenter: Optional[str] = Field(None, title="Datacenter")
    NodeID: Optional[str] = Field(None, title="Nodeid")
    NodeName: Optional[str] = Field(None, title="Nodename")
    PrimaryDatacenter: Optional[str] = Field(None, title="Primarydatacenter")
    Revision: Optional[str] = Field(None, title="Revision")
    Server: bool = Field(..., title="Server")
    Version: Optional[str] = Field(None, title="Version")


class Couchdb(BaseModel):
    couchdb: Optional[str] = Field(None, title="Couchdb")
    features: Optional[List[str]] = Field(None, title="Features")
    git_sha: Optional[str] = Field(None, title="Git Sha")
    http_headers: str = Field(..., title="Http Headers")
    uuid: Optional[str] = Field(None, title="Uuid")
    vendor: Optional[Dict[str, str]] = Field(None, title="Vendor")
    version: Optional[str] = Field(None, title="Version")


class Dahua(BaseModel):
    serial_number: Optional[str] = Field(None, title="Serial Number")


class DahuaDvrWebPlugin(BaseModel):
    classid: str = Field(..., title="Classid")
    mac_version: Optional[str] = Field(None, title="Mac Version")
    name: str = Field(..., title="Name")
    version: str = Field(..., title="Version")


class DahuaDvrWeb(BaseModel):
    channel_names: Optional[List[str]] = Field(None, title="Channel Names")
    plugin: Optional[DahuaDvrWebPlugin] = None
    user_info: Optional[str] = Field(None, title="User Info")
    web_version: Optional[str] = Field(None, title="Web Version")


class Dns(BaseModel):
    recursive: bool = Field(..., title="Recursive")
    resolver_hostname: Optional[str] = Field(None, title="Resolver Hostname")
    resolver_id: Optional[str] = Field(None, title="Resolver Id")
    software: Optional[str] = Field(None, title="Software")


class Docker(BaseModel):
    ApiVersion: str = Field(..., title="Apiversion")
    Arch: str = Field(..., title="Arch")
    BuildTime: str = Field(..., title="Buildtime")
    GitCommit: str = Field(..., title="Gitcommit")
    GoVersion: str = Field(..., title="Goversion")
    KernelVersion: str = Field(..., title="Kernelversion")
    MinAPIVersion: str = Field(..., title="Minapiversion")
    Os: str = Field(..., title="Os")
    Version: str = Field(..., title="Version")


class Domoticz(BaseModel):
    build_time: Optional[str] = Field(None, title="Build Time")
    dzevents_version: Optional[str] = Field(None, title="Dzevents Version")
    hash: Optional[str] = Field(None, title="Hash")
    python_version: Optional[str] = Field(None, title="Python Version")
    version: Optional[str] = Field(None, title="Version")


class Elastic(BaseModel):
    cluster: Optional[Dict[str, Any]] = Field(None, title="Cluster")
    indices: Optional[Dict[str, Any]] = Field(None, title="Indices")
    nodes: Optional[Dict[str, Any]] = Field(None, title="Nodes")


class Etcd(BaseModel):
    api: str = Field(..., title="Api")
    clientURLs: Optional[List[str]] = Field(None, title="Clienturls")
    dbSize: Optional[int] = Field(None, title="Dbsize")
    id: Union[int, str] = Field(..., title="Id")
    leaderInfo: Optional[Dict[str, str]] = Field(None, title="Leaderinfo")
    name: str = Field(..., title="Name")
    peerURLs: Optional[List[str]] = Field(None, title="Peerurls")
    recvAppendRequestCnt: Optional[int] = Field(None, title="Recvappendrequestcnt")
    sendAppendRequestCnt: Optional[int] = Field(None, title="Sendappendrequestcnt")
    startTime: Optional[str] = Field(None, title="Starttime")
    state: Optional[str] = Field(None, title="State")


class EthereumRpc(BaseModel):
    client: str = Field(..., title="Client")
    compiler: Optional[str] = Field(None, title="Compiler")
    hashrate: Optional[str] = Field(None, title="Hashrate")
    platform: Optional[str] = Field(None, title="Platform")
    version: Optional[str] = Field(None, title="Version")


class Ethernetip(BaseModel):
    command: int = Field(..., title="Command")
    command_status: int = Field(..., title="Command Status")
    device_type: str = Field(..., title="Device Type")
    encapsulation_length: int = Field(..., title="Encapsulation Length")
    item_count: int = Field(..., title="Item Count")
    options: int = Field(..., title="Options")
    product_code: int = Field(..., title="Product Code")
    product_name: str = Field(..., title="Product Name")
    raw: str = Field(..., title="Raw")
    revision_major: int = Field(..., title="Revision Major")
    revision_minor: int = Field(..., title="Revision Minor")
    sender_context: str = Field(..., title="Sender Context")
    serial: int = Field(..., title="Serial")
    session: int = Field(..., title="Session")
    socket_addr: str = Field(..., title="Socket Addr")
    state: int = Field(..., title="State")
    vendor_id: str = Field(..., title="Vendor Id")
    version: int = Field(..., title="Version")


class FtpFeature(BaseModel):
    parameters: List[str] = Field(..., title="Parameters")


class Ftp(BaseModel):
    anonymous: bool = Field(..., title="Anonymous")
    features: Dict[str, FtpFeature] = Field(..., title="Features")
    features_hash: Optional[int] = Field(None, title="Features Hash")


class Handpunch(BaseModel):
    adapter_type: str = Field(..., title="Adapter Type")
    eprom_version: str = Field(..., title="Eprom Version")
    max_logs: int = Field(..., title="Max Logs")
    max_users: int = Field(..., title="Max Users")
    memory_size: str = Field(..., title="Memory Size")
    model: str = Field(..., title="Model")
    model_name: str = Field(..., title="Model Name")
    serial_number: int = Field(..., title="Serial Number")
    total_logs: int = Field(..., title="Total Logs")
    total_users: int = Field(..., title="Total Users")


class Hikvision(BaseModel):
    activex_files: Optional[Dict[str, str]] = Field(None, title="Activex Files")
    custom_version: Optional[str] = Field(None, title="Custom Version")
    custom_version_2: Optional[str] = Field(None, title="Custom Version 2")
    device_description: Optional[str] = Field(None, title="Device Description")
    device_model: Optional[str] = Field(None, title="Device Model")
    device_name: Optional[str] = Field(None, title="Device Name")
    device_version: Optional[str] = Field(None, title="Device Version")
    plugin_version: Optional[str] = Field(None, title="Plugin Version")
    web_version: Optional[str] = Field(None, title="Web Version")


class ApacheHiveTable(BaseModel):
    name: str = Field(..., title="Name")
    properties: List[Dict[str, str]] = Field(..., title="Properties")


class ApacheHiveDatabase(BaseModel):
    tables: List[ApacheHiveTable] = Field(..., title="Tables")


class ApacheHive(BaseModel):
    databases: List[ApacheHiveDatabase] = Field(..., title="Databases")


class HomeAssistant(BaseModel):
    base_url: Optional[str] = Field(None, title="Base Url")
    external_url: Optional[str] = Field(None, title="External Url")
    location_name: Optional[str] = Field(None, title="Location Name")
    installation_type: Optional[str] = Field(None, title="Installation Type")
    internal_url: Optional[str] = Field(None, title="Internal Url")
    uuid: Optional[str] = Field(None, title="Uuid")
    version: str = Field(..., title="Version")


class Homebridge(BaseModel):
    enable_terminal_access: bool = Field(..., title="Enable Terminal Access")
    enable_accessories: bool = Field(..., title="Enable Accessories")
    instance_id: Optional[str] = Field(None, title="Instance Id")
    instance_name: str = Field(..., title="Instance Name")
    node_version: str = Field(..., title="Node Version")
    platform: Optional[str] = Field(None, title="Platform")
    running_in_docker: bool = Field(..., title="Running In Docker")
    running_in_linux: bool = Field(..., title="Running In Linux")
    service_mode: Optional[bool] = Field(None, title="Service Mode")
    ui_package_name: str = Field(..., title="Ui Package Name")
    ui_package_version: str = Field(..., title="Ui Package Version")


class HoobsBridge(BaseModel):
    name: str = Field(..., title="Name")
    pin: str = Field(..., title="Pin")
    port: int = Field(..., title="Port")
    username: str = Field(..., title="Username")


class HoobsClient(BaseModel):
    country_code: str = Field(..., title="Country Code")
    postal_code: Optional[str] = Field(None, title="Postal Code")


class HoobsServer(BaseModel):
    application_path: Optional[str] = Field(None, title="Application Path")
    configuration_path: Optional[str] = Field(None, title="Configuration Path")
    global_modules_path: Optional[str] = Field(None, title="Global Modules Path")
    home_setup_id: Optional[str] = Field(None, title="Home Setup Id")
    hoobs_version: Optional[str] = Field(None, title="Hoobs Version")
    local_modules_path: Optional[str] = Field(None, title="Local Modules Path")
    node_version: str = Field(..., title="Node Version")
    port: Optional[int] = Field(None, title="Port")


class Hoobs(BaseModel):
    bridge: Optional[HoobsBridge] = None
    client: Optional[HoobsClient] = None
    server: Optional[HoobsServer] = None


class HpIloNic(BaseModel):
    description: Optional[str] = Field(None, title="Description")
    ip_address: Optional[str] = Field(None, title="Ip Address")
    location: Optional[str] = Field(None, title="Location")
    mac_address: Optional[str] = Field(None, title="Mac Address")
    port: str = Field(..., title="Port")
    status: Optional[str] = Field(None, title="Status")


class HpIlo(BaseModel):
    cuuid: Optional[str] = Field(None, title="Cuuid")
    ilo_firmware: str = Field(..., title="Ilo Firmware")
    ilo_serial_number: str = Field(..., title="Ilo Serial Number")
    ilo_type: str = Field(..., title="Ilo Type")
    ilo_uuid: str = Field(..., title="Ilo Uuid")
    nics: Optional[List[HpIloNic]] = Field(None, title="Nics")
    product_id: Optional[str] = Field(None, title="Product Id")
    serial_number: Optional[str] = Field(None, title="Serial Number")
    server_type: Optional[str] = Field(None, title="Server Type")
    uuid: Optional[str] = Field(None, title="Uuid")


class HttpComponent(BaseModel):
    categories: List[str] = Field(..., title="Categories")


class HttpFavicon(BaseModel):
    data: str = Field(..., title="Data")
    hash: int = Field(..., title="Hash")
    location: str = Field(..., title="Location")


class HttpRedirect(BaseModel):
    data: Optional[str] = Field(None, title="Data")
    host: str = Field(..., title="Host")
    location: str = Field(..., title="Location")


class Http(BaseModel):
    components: Optional[Dict[str, HttpComponent]] = Field(
        None,
        description="The web technologies (ex. jQuery) that a website uses.",
        title="Components",
    )
    favicon: Optional[HttpFavicon] = Field(
        None,
        description="Favicon for the website. Helpful to find phishing websites, fingerprinting products or locating websites from the same vendor/ company.",
        title="Favicon",
    )
    host: Optional[str] = Field(None, title="Host")
    html: Optional[str] = Field(None, title="Html")
    html_hash: Optional[int] = Field(
        None,
        description='Numeric hash of the "http.html" property. Useful for finding other IPs with the exact same website.',
        title="Html Hash",
    )
    location: Optional[str] = Field(None, title="Location")
    redirects: List[HttpRedirect] = Field(..., title="Redirects")
    robots: Optional[str] = Field(
        None, description="Contents of the robots.txt file.", title="Robots"
    )
    robots_hash: Optional[int] = Field(
        None,
        description="Numeric hash of the robots.txt file which can be used to find websites that have the same robots.txt.",
        title="Robots Hash",
    )
    securitytxt: Optional[str] = Field(
        None,
        description="The security.txt file is an emerging standard for knowing how to contact the website owner for security issues.",
        title="Securitytxt",
    )
    securitytxt_hash: Optional[int] = Field(None, title="Securitytxt Hash")
    server: Optional[str] = Field(
        None,
        description='Short-hand for accessing the value from the "Server" HTTP header.',
        title="Server",
    )
    sitemap: Optional[str] = Field(None, title="Sitemap")
    sitemap_hash: Optional[int] = Field(None, title="Sitemap Hash")
    title: Optional[str] = Field(None, title="Title")
    waf: Optional[str] = Field(
        None,
        description="Web application firewall that is protecting this website.",
        title="Waf",
    )


class Hubitat(BaseModel):
    hardware_version: Optional[str] = Field(None, title="Hardware Version")
    hub_uid: Optional[str] = Field(None, title="Hub Uid")
    ip_address: Optional[str] = Field(None, title="Ip Address")
    mac_address: Optional[str] = Field(None, title="Mac Address")
    version: str = Field(..., title="Version")


class IbmDb2(BaseModel):
    db2_version: str = Field(..., title="Db2 Version")
    instance_name: str = Field(..., title="Instance Name")
    server_platform: str = Field(..., title="Server Platform")
    external_name: str = Field(..., title="External Name")


class Influxdb(BaseModel):
    bind_address: Optional[str] = Field(None, title="Bind Address")
    build: Optional[str] = Field(None, title="Build")
    databases: Optional[List[str]] = Field(None, title="Databases")
    go_arch: Optional[str] = Field(None, title="Go Arch")
    go_max_procs: Optional[int] = Field(None, title="Go Max Procs")
    go_os: Optional[str] = Field(None, title="Go Os")
    go_version: Optional[str] = Field(None, title="Go Version")
    network_hostname: Optional[str] = Field(None, title="Network Hostname")
    uptime: Optional[str] = Field(None, title="Uptime")
    version: Optional[str] = Field(None, title="Version")


class IpCamera(BaseModel):
    alias_name: Optional[str] = Field(None, title="Alias Name")
    app_version: Optional[str] = Field(None, title="App Version")
    brand: Optional[str] = Field(None, title="Brand")
    build: Optional[str] = Field(None, title="Build")
    client_version: Optional[str] = Field(None, title="Client Version")
    ddns_host: Optional[str] = Field(None, title="Ddns Host")
    hardware_version: Optional[str] = Field(None, title="Hardware Version")
    id: Optional[str] = Field(None, title="Id")
    ip_address: Optional[str] = Field(None, title="Ip Address")
    mac_address: Optional[str] = Field(None, title="Mac Address")
    model: Optional[str] = Field(None, title="Model")
    name: Optional[str] = Field(None, title="Name")
    product: Optional[str] = Field(None, title="Product")
    server_version: Optional[str] = Field(None, title="Server Version")
    software_version: Optional[str] = Field(None, title="Software Version")
    system_version: Optional[str] = Field(None, title="System Version")
    version: Optional[str] = Field(None, title="Version")


class IpSymconHouse(BaseModel):
    name: str = Field(..., title="Name")
    password: bool = Field(..., title="Password")


class IpSymcon(BaseModel):
    api_version: str = Field(..., title="Api Version")
    houses: Optional[List[IpSymconHouse]] = Field(None, title="Houses")
    version: str = Field(..., title="Version")


class IppCupsPrinter(BaseModel):
    authentication_type: Optional[str] = Field(None, title="Authentication Type")
    dns_sd_name: Optional[str] = Field(None, title="Dns Sd Name")
    info: Optional[str] = Field(None, title="Info")
    make_and_model: Optional[str] = Field(None, title="Make And Model")
    name: Optional[str] = Field(None, title="Name")
    uri_supported: str = Field(..., title="Uri Supported")


class IppCups(BaseModel):
    printers: Optional[List[IppCupsPrinter]] = Field(None, title="Printers")
    status_message: Optional[str] = Field(None, title="Status Message")


class IsakmpFlags(BaseModel):
    authentication: bool = Field(..., title="Authentication")
    commit: bool = Field(..., title="Commit")
    encryption: bool = Field(..., title="Encryption")


class Isakmp(BaseModel):
    aggressive: Optional[Isakmp] = None
    exchange_type: int = Field(..., title="Exchange Type")
    flags: IsakmpFlags
    initiator_spi: str = Field(..., title="Initiator Spi")
    length: int = Field(..., title="Length")
    msg_id: str = Field(..., title="Msg Id")
    next_payload: int = Field(..., title="Next Payload")
    responder_spi: str = Field(..., title="Responder Spi")
    vendor_ids: List[str] = Field(..., title="Vendor Ids")
    version: str = Field(..., title="Version")


class IscsiTarget(BaseModel):
    addresses: Optional[List[str]] = Field(None, title="Addresses")
    auth_enabled: Optional[bool] = Field(None, title="Auth Enabled")
    auth_error: Optional[str] = Field(None, title="Auth Error")
    name: str = Field(..., title="Name")


class Iscsi(BaseModel):
    targets: List[IscsiTarget] = Field(..., title="Targets")


class KafkaBroker(BaseModel):
    id: str = Field(..., title="Id")
    name: str = Field(..., title="Name")
    port: int = Field(..., title="Port")
    rack: Optional[str] = Field(None, title="Rack")


class KafkaHost(BaseModel):
    name: str = Field(..., title="Name")
    port: int = Field(..., title="Port")


class Kafka(BaseModel):
    brokers: List[KafkaBroker] = Field(..., title="Brokers")
    hosts: List[KafkaHost] = Field(..., title="Hosts")
    topics: List[str] = Field(..., title="Topics")


class KnxDevice(BaseModel):
    friendly_name: str = Field(..., title="Friendly Name")
    knx_address: str = Field(..., title="Knx Address")
    mac: str = Field(..., title="Mac")
    multicast_address: str = Field(..., title="Multicast Address")
    serial: str = Field(..., title="Serial")


class KnxServices(BaseModel):
    core: str = Field(..., title="Core")
    device_management: Optional[str] = Field(None, title="Device Management")
    routing: Optional[str] = Field(None, title="Routing")
    tunneling: Optional[str] = Field(None, title="Tunneling")


class Knx(BaseModel):
    device: KnxDevice
    supported_services: KnxServices


class KubernetesContainer(BaseModel):
    image: str = Field(..., title="Image")
    name: str = Field(..., title="Name")


class KubernetesNode(BaseModel):
    name: str = Field(..., title="Name")
    containers: List[KubernetesContainer] = Field(..., title="Containers")


class Kubernetes(BaseModel):
    build_date: Optional[str] = Field(None, title="Build Date")
    go_version: Optional[str] = Field(None, title="Go Version")
    nodes: Optional[List[KubernetesNode]] = Field(None, title="Nodes")
    platform: Optional[str] = Field(None, title="Platform")
    version: Optional[str] = Field(None, title="Version")


class Lantronix(BaseModel):
    gateway: Optional[str] = Field(None, title="Gateway")
    ip: Optional[str] = Field(None, title="Ip")
    mac: Optional[str] = Field(None, title="Mac")
    password: Optional[str] = Field(None, title="Password")
    type: Optional[str] = Field(None, title="Type")
    version: Optional[str] = Field(None, title="Version")


class MdnsService(BaseModel):
    ipv4: Optional[List[str]] = Field(None, title="Ipv4")
    ipv6: Optional[List[str]] = Field(None, title="Ipv6")
    name: Optional[str] = Field(None, title="Name")
    port: Optional[int] = Field(None, title="Port")
    ptr: str = Field(..., title="Ptr")


class Mdns(BaseModel):
    additionals: Optional[Dict[str, Union[List[str], str]]] = Field(
        None, title="Additionals"
    )
    answers: Optional[Dict[str, Union[List[str], str]]] = Field(None, title="Answers")
    authorities: Optional[Dict[str, Union[List[str], str]]] = Field(
        None, title="Authorities"
    )
    services: Optional[Dict[str, MdnsService]] = Field(None, title="Services")


class MikrotikRouteros(BaseModel):
    interfaces: Optional[List[str]] = Field(None, title="Interfaces")
    version: str = Field(..., title="Version")


class MinecraftDescription(BaseModel):
    extra: Optional[List[Union[MinecraftDescription, str]]] = Field(None, title="Extra")
    text: Optional[str] = Field(None, title="Text")
    translate: Optional[str] = Field(None, title="Translate")


class MinecraftPlayer(BaseModel):
    id: str = Field(..., title="Id")
    name: str = Field(..., title="Name")


class MinecraftPlayers(BaseModel):
    max: int = Field(..., title="Max")
    online: int = Field(..., title="Online")
    sample: Optional[List[MinecraftPlayer]] = Field(None, title="Sample")


class MinecraftVersion(BaseModel):
    name: str = Field(..., title="Name")
    protocol: int = Field(..., title="Protocol")


class Minecraft(BaseModel):
    description: Optional[Union[str, List[str], MinecraftDescription]] = Field(
        None, title="Description"
    )
    favicon: Optional[str] = Field(None, title="Favicon")
    modinfo: Optional[Dict[str, Any]] = Field(None, title="Modinfo")
    players: Optional[MinecraftPlayers] = None
    version: Optional[MinecraftVersion] = None


class MitsubishiQ(BaseModel):
    cpu: str = Field(..., title="Cpu")


class Mongodb(BaseModel):
    authentication: bool = Field(..., title="Authentication")
    buildInfo: Optional[Dict[str, Any]] = Field(None, title="Buildinfo")
    listDatabases: Optional[Dict[str, Any]] = Field(None, title="Listdatabases")
    serverStatus: Optional[Dict[str, Any]] = Field(None, title="Serverstatus")


class MsrpcTower(BaseModel):
    annotation: Optional[str] = Field(None, title="Annotation")
    bindings: List[Dict[str, str]] = Field(..., title="Bindings")
    version: Optional[str] = Field(None, title="Version")


class Msrpc(BaseModel):
    actual_count: int = Field(..., title="Actual Count")
    max_count: int = Field(..., title="Max Count")
    num_towers: int = Field(..., title="Num Towers")
    towers: Dict[str, MsrpcTower] = Field(..., title="Towers")


class Mssql(BaseModel):
    dns_computer_name: Optional[str] = Field(None, title="Dns Computer Name")
    dns_domain_name: Optional[str] = Field(None, title="Dns Domain Name")
    netbios_computer_name: Optional[str] = Field(None, title="Netbios Computer Name")
    netbios_domain_name: Optional[str] = Field(None, title="Netbios Domain Name")
    os_version: str = Field(..., title="Os Version")
    target_realm: Optional[str] = Field(None, title="Target Realm")
    timestamp: Optional[int] = Field(None, title="Timestamp")


class MqttMessage(BaseModel):
    payload: Optional[str] = Field(None, title="Payload")
    topic: str = Field(..., title="Topic")


class Mqtt(BaseModel):
    code: int = Field(..., title="Code")
    messages: List[MqttMessage] = Field(..., title="Messages")


class Nats(BaseModel):
    auth_required: Optional[bool] = Field(None, title="Auth Required")
    client_id: Optional[int] = Field(None, title="Client Id")
    client_ip: Optional[str] = Field(None, title="Client Ip")
    cluster: Optional[str] = Field(None, title="Cluster")
    git_commit: Optional[str] = Field(None, title="Git Commit")
    go: Optional[str] = Field(None, title="Go")
    headers: Optional[bool] = Field(None, title="Headers")
    host: str = Field(..., title="Host")
    max_payload: Optional[int] = Field(None, title="Max Payload")
    nonce: Optional[str] = Field(None, title="Nonce")
    port: int = Field(..., title="Port")
    proto: Optional[int] = Field(None, title="Proto")
    server_id: Optional[str] = Field(None, title="Server Id")
    server_name: Optional[str] = Field(None, title="Server Name")
    tls_required: Optional[bool] = Field(None, title="Tls Required")
    version: str = Field(..., title="Version")


class NdmpDevice(BaseModel):
    fs_logical_device: str = Field(..., title="Fs Logical Device")
    fs_physical_device: str = Field(..., title="Fs Physical Device")
    fs_type: str = Field(..., title="Fs Type")


class Ndmp(BaseModel):
    devices: List[NdmpDevice] = Field(..., title="Devices")


class NetbiosShare(BaseModel):
    flags: int = Field(..., title="Flags")
    name: str = Field(..., title="Name")
    suffix: int = Field(..., title="Suffix")


class Netbios(BaseModel):
    mac: Optional[str] = Field(None, title="Mac")
    names: Optional[List[NetbiosShare]] = Field(None, title="Names")
    raw: List[str] = Field(..., title="Raw")
    server_name: Optional[str] = Field(None, title="Server Name")
    username: Optional[str] = Field(None, title="Username")


class Netgear(BaseModel):
    description: str = Field(..., title="Description")
    firewall_version: str = Field(..., title="Firewall Version")
    firmware_version: str = Field(..., title="Firmware Version")
    first_use_date: str = Field(..., title="First Use Date")
    model_name: str = Field(..., title="Model Name")
    serial_number: str = Field(..., title="Serial Number")
    smartagent_version: str = Field(..., title="Smartagent Version")
    vpn_version: Optional[str] = Field(None, title="Vpn Version")


class NtpMonlist(BaseModel):
    connections: List[str] = Field(..., title="Connections")
    more: bool = Field(..., title="More")


class Ntp(BaseModel):
    clk_jitter: Optional[Union[float, str]] = Field(None, title="Clk Jitter")
    clk_wander: Optional[Union[float, str]] = Field(None, title="Clk Wander")
    clock: Optional[str] = Field(None, title="Clock")
    clock_offset: float = Field(..., title="Clock Offset")
    delay: float = Field(..., title="Delay")
    frequency: Optional[Union[float, str]] = Field(None, title="Frequency")
    jitter: Optional[Union[float, str]] = Field(None, title="Jitter")
    leap: Union[int, str] = Field(..., title="Leap")
    mintc: Optional[int] = Field(None, title="Mintc")
    monlist: Optional[NtpMonlist] = None
    noise: Optional[Union[float, str]] = Field(None, title="Noise")
    offset: Optional[Union[float, str]] = Field(None, title="Offset")
    peer: Optional[Union[int, str]] = Field(None, title="Peer")
    poll: Union[int, str] = Field(..., title="Poll")
    precision: int = Field(..., title="Precision")
    processor: Optional[str] = Field(None, title="Processor")
    refid: str = Field(..., title="Refid")
    reftime: str = Field(..., title="Reftime")
    root_delay: Union[float, str] = Field(..., title="Root Delay")
    root_dispersion: Union[float, str] = Field(..., title="Root Dispersion")
    rootdelay: Optional[Union[float, str]] = Field(None, title="Rootdelay")
    rootdisp: Optional[Union[float, str]] = Field(None, title="Rootdisp")
    stability: Optional[Union[float, str]] = Field(None, title="Stability")
    stratum: int = Field(..., title="Stratum")
    sys_jitter: Optional[Union[float, str]] = Field(None, title="Sys Jitter")
    system: Optional[str] = Field(None, title="System")
    tc: Optional[int] = Field(None, title="Tc")
    version: str = Field(..., title="Version")


class Openflow(BaseModel):
    supported_versions: Optional[Union[str, List[str]]] = Field(
        None, title="Supported Versions"
    )
    version: str = Field(..., title="Version")


class Openhab(BaseModel):
    build: str = Field(..., title="Build")
    version: str = Field(..., title="Version")


class OpenwebnetSystems(BaseModel):
    automation: int = Field(..., title="Automation")
    burglar_alarm: Optional[int] = Field(None, title="Burglar Alarm")
    heating: int = Field(..., title="Heating")
    lighting: int = Field(..., title="Lighting")
    power_management: int = Field(..., title="Power Management")


class Openwebnet(BaseModel):
    date_and_time: str = Field(..., title="Date And Time")
    device_type: str = Field(..., title="Device Type")
    distribution_version: Optional[str] = Field(None, title="Distribution Version")
    firmware_version: str = Field(..., title="Firmware Version")
    ip_address: str = Field(..., title="Ip Address")
    kernel_version: str = Field(..., title="Kernel Version")
    mac_address: str = Field(..., title="Mac Address")
    net_mask: str = Field(..., title="Net Mask")
    systems: OpenwebnetSystems
    uptime: str = Field(..., title="Uptime")


class Pcworx(BaseModel):
    firmware_date: str = Field(..., title="Firmware Date")
    firmware_time: str = Field(..., title="Firmware Time")
    firmware_version: str = Field(..., title="Firmware Version")
    model_number: str = Field(..., title="Model Number")
    plc_type: str = Field(..., title="Plc Type")


class Plex(BaseModel):
    machine_identifier: Optional[str] = Field(None, title="Machine Identifier")
    version: Optional[str] = Field(None, title="Version")


class QnapStationInfo(BaseModel):
    build: str = Field(..., title="Build")
    checksum: Optional[str] = Field(None, title="Checksum")
    version: Optional[str] = Field(None, title="Version")


class QnapFirmware(BaseModel):
    build: Optional[str] = Field(None, title="Build")
    number: Optional[str] = Field(None, title="Number")
    patch: Optional[str] = Field(None, title="Patch")
    version: Optional[str] = Field(None, title="Version")


class QnapModel(BaseModel):
    custom_model_name: Optional[str] = Field(None, title="Custom Model Name")
    display_model_name: Optional[str] = Field(None, title="Display Model Name")
    internal_model_name: Optional[str] = Field(None, title="Internal Model Name")
    model_name: Optional[str] = Field(None, title="Model Name")
    platform: Optional[str] = Field(None, title="Platform")
    platform_ex: Optional[str] = Field(None, title="Platform Ex")
    project_name: Optional[str] = Field(None, title="Project Name")


class Qnap(BaseModel):
    apps: Optional[Dict[str, QnapStationInfo]] = Field(None, title="Apps")
    firmware: Optional[QnapFirmware] = None
    hostname: Optional[str] = Field(None, title="Hostname")
    model: Optional[QnapModel] = None


class Rdp(BaseModel):
    dns_domain_name: Optional[str] = Field(None, title="Dns Domain Name")
    dns_forest_name: Optional[str] = Field(None, title="Dns Forest Name")
    fqdn: Optional[str] = Field(None, title="Fqdn")
    netbios_computer_name: Optional[str] = Field(None, title="Netbios Computer Name")
    netbios_domain_name: Optional[str] = Field(None, title="Netbios Domain Name")
    os: Optional[List[str]] = Field(None, title="Os")
    os_build_version: Optional[int] = Field(None, title="Os Build Version")
    os_major_version: Optional[int] = Field(None, title="Os Major Version")
    os_minor_version: Optional[int] = Field(None, title="Os Minor Version")
    target_realm: Optional[str] = Field(None, title="Target Realm")
    timestamp: Optional[int] = Field(None, title="Timestamp")


class Realport(BaseModel):
    name: str = Field(..., title="Name")
    ports: Optional[int] = Field(None, title="Ports")


class RedisKeys(BaseModel):
    data: List[str] = Field(..., title="Data")
    more: bool = Field(..., title="More")


class Redis(BaseModel):
    clients: Optional[Union[List[Dict[str, Any]], Dict[str, Any]]] = Field(
        None, title="Clients"
    )
    cluster: Optional[Union[Dict[str, Any], List[str]]] = Field(None, title="Cluster")
    cpu: Optional[Dict[str, Any]] = Field(None, title="Cpu")
    errorstats: Optional[Dict[str, Any]] = Field(None, title="Errorstats")
    keys: Optional[RedisKeys] = None
    keyspace: Optional[Dict[str, str]] = Field(None, title="Keyspace")
    memory: Optional[Dict[str, Any]] = Field(None, title="Memory")
    modules: Optional[Dict[str, Any]] = Field(None, title="Modules")
    persistence: Optional[Dict[str, Any]] = Field(None, title="Persistence")
    replication: Optional[Dict[str, Any]] = Field(None, title="Replication")
    server: Optional[Dict[str, Any]] = Field(None, title="Server")
    stats: Optional[Dict[str, Any]] = Field(None, title="Stats")


class RipAddress(BaseModel):
    addr: str = Field(..., title="Addr")
    family: str = Field(..., title="Family")
    metric: int = Field(..., title="Metric")
    next_hop: Optional[str] = Field(None, title="Next Hop")
    subnet: Optional[str] = Field(None, title="Subnet")
    tag: Optional[int] = Field(None, title="Tag")


class RipAuthentication(BaseModel):
    password: str = Field(..., title="Password")
    type: int = Field(..., title="Type")


class Rip(BaseModel):
    addresses: List[RipAddress] = Field(..., title="Addresses")
    auth: Optional[RipAuthentication] = None
    command: int = Field(..., title="Command")
    version: int = Field(..., title="Version")


class RipplePeer(BaseModel):
    complete_ledgers: Optional[str] = Field(None, title="Complete Ledgers")
    ip: Optional[str] = Field(None, title="Ip")
    port: Optional[str] = Field(None, title="Port")
    public_key: str = Field(..., title="Public Key")
    type: str = Field(..., title="Type")
    uptime: int = Field(..., title="Uptime")
    version: str = Field(..., title="Version")


class Ripple(BaseModel):
    peers: List[RipplePeer] = Field(..., title="Peers")


class Rsync(BaseModel):
    authentication: bool = Field(..., title="Authentication")
    modules: Dict[str, Optional[str]] = Field(..., title="Modules")


class SamsungTv(BaseModel):
    device_id: Optional[str] = Field(None, title="Device Id")
    device_name: str = Field(..., title="Device Name")
    model: Optional[str] = Field(None, title="Model")
    model_description: str = Field(..., title="Model Description")
    model_name: str = Field(..., title="Model Name")
    msf_version: Optional[str] = Field(None, title="Msf Version")
    ssid: Optional[str] = Field(None, title="Ssid")
    wifi_mac: Optional[str] = Field(None, title="Wifi Mac")


class SmbFile(BaseModel):
    directory: bool = Field(..., title="Directory")
    name: str = Field(..., title="Name")
    read_only: bool = Field(..., alias="read-only", title="Read-Only")
    size: int = Field(..., title="Size")


class SmbItem(BaseModel):
    comments: str = Field(..., title="Comments")
    files: Optional[List[SmbFile]] = Field(None, title="Files")
    name: str = Field(..., title="Name")
    special: bool = Field(..., title="Special")
    temporary: bool = Field(..., title="Temporary")
    type: str = Field(..., title="Type")


class Smb(BaseModel):
    anonymous: Optional[bool] = Field(None, title="Anonymous")
    capabilities: List[str] = Field(..., title="Capabilities")
    os: Optional[str] = Field(None, title="Os")
    raw: List[str] = Field(..., title="Raw")
    shares: Optional[List[SmbItem]] = Field(None, title="Shares")
    software: Optional[str] = Field(None, title="Software")
    smb_version: int = Field(..., title="Smb Version")


class Snmp(BaseModel):
    contact: Optional[str] = Field(None, title="Contact")
    description: Optional[str] = Field(None, title="Description")
    location: Optional[str] = Field(None, title="Location")
    name: Optional[str] = Field(None, title="Name")
    objectid: Optional[str] = Field(None, title="Objectid")
    uptime: Optional[str] = Field(None, title="Uptime")
    services: Optional[str] = Field(None, title="Services")


class Sonicwall(BaseModel):
    sonicos_version: Optional[str] = Field(None, title="Sonicos Version")
    serial_number: Optional[str] = Field(None, title="Serial Number")


class Sonos(BaseModel):
    friendly_name: str = Field(..., title="Friendly Name")
    hardware_version: str = Field(..., title="Hardware Version")
    mac_address: Optional[str] = Field(None, title="Mac Address")
    model_name: str = Field(..., title="Model Name")
    raw: str = Field(..., title="Raw")
    room_name: str = Field(..., title="Room Name")
    serial_number: str = Field(..., title="Serial Number")
    software_version: str = Field(..., title="Software Version")
    udn: str = Field(..., title="Udn")


class SpotifyConnect(BaseModel):
    active_user: Optional[str] = Field(None, title="Active User")
    brand_display_name: Optional[str] = Field(None, title="Brand Display Name")
    client_id: Optional[str] = Field(None, title="Client Id")
    device_id: Optional[str] = Field(None, title="Device Id")
    device_type: Optional[str] = Field(None, title="Device Type")
    library_version: Optional[str] = Field(None, title="Library Version")
    model_display_name: Optional[str] = Field(None, title="Model Display Name")
    remote_name: Optional[str] = Field(None, title="Remote Name")
    public_key: Optional[str] = Field(None, title="Public Key")
    scope: Optional[str] = Field(None, title="Scope")
    version: str = Field(..., title="Version")


class SshKeyExchange(BaseModel):
    compression_algorithms: List[str] = Field(..., title="Compression Algorithms")
    encryption_algorithms: List[str] = Field(..., title="Encryption Algorithms")
    kex_algorithms: List[str] = Field(..., title="Kex Algorithms")
    kex_follows: bool = Field(..., title="Kex Follows")
    languages: List[str] = Field(..., title="Languages")
    mac_algorithms: List[str] = Field(..., title="Mac Algorithms")
    server_host_key_algorithms: List[str] = Field(
        ..., title="Server Host Key Algorithms"
    )
    unused: int = Field(..., title="Unused")


class Ssh(BaseModel):
    cipher: str = Field(..., title="Cipher")
    fingerprint: str = Field(..., title="Fingerprint")
    hassh: str = Field(..., title="Hassh")
    kex: SshKeyExchange
    key: str = Field(..., title="Key")
    mac: str = Field(..., title="Mac")


class SslCas(BaseModel):
    components: Dict[str, Any] = Field(..., title="Components")
    hash: int = Field(..., title="Hash")
    raw: str = Field(..., title="Raw")


class SslCertificateExtension(BaseModel):
    critical: Optional[bool] = Field(None, title="Critical")
    data: str = Field(..., title="Data")
    name: str = Field(..., title="Name")


class SslCertificateFingerprint(BaseModel):
    sha1: str = Field(..., title="Sha1")
    sha256: str = Field(..., title="Sha256")


class SslCertificate(BaseModel):
    expired: bool = Field(..., title="Expired")
    expires: str = Field(..., title="Expires")
    extensions: List[SslCertificateExtension] = Field(..., title="Extensions")
    fingerprint: SslCertificateFingerprint
    issuer: Dict[str, str] = Field(..., title="Issuer")
    issued: Optional[str] = Field(None, title="Issued")
    serial: int = Field(..., title="Serial")
    sig_alg: str = Field(..., title="Sig Alg")
    subject: Dict[str, str] = Field(..., title="Subject")
    version: int = Field(..., title="Version")


class SslCipher(BaseModel):
    bits: int = Field(..., title="Bits")
    name: str = Field(..., title="Name")
    version: str = Field(..., title="Version")


class SslDhparams(BaseModel):
    bits: int = Field(..., title="Bits")
    fingerprint: Optional[str] = Field(None, title="Fingerprint")
    generator: Union[int, str] = Field(..., title="Generator")
    prime: str = Field(..., title="Prime")
    public_key: str = Field(..., title="Public Key")


class SslOcspCertId(BaseModel):
    hash_algorithm: str = Field(..., title="Hash Algorithm")
    issuer_name_hash: str = Field(..., title="Issuer Name Hash")
    issuer_name_key: str = Field(..., title="Issuer Name Key")
    serial_number: str = Field(..., title="Serial Number")


class SslOcsp(BaseModel):
    certificate_id: SslOcspCertId
    cert_status: str = Field(..., title="Cert Status")
    next_update: str = Field(..., title="Next Update")
    produced_at: str = Field(..., title="Produced At")
    responder_id: str = Field(..., title="Responder Id")
    response_status: str = Field(..., title="Response Status")
    signature_algorithm: str = Field(..., title="Signature Algorithm")
    this_update: str = Field(..., title="This Update")
    version: str = Field(..., title="Version")


class SslExtension(BaseModel):
    id: str = Field(..., title="Id")
    name: str = Field(..., title="Name")


class SslBrowserTrustVendor(BaseModel):
    apple: bool = Field(..., title="Apple")
    microsoft: bool = Field(..., title="Microsoft")
    mozilla: bool = Field(..., title="Mozilla")


class SslBrowserTrust(BaseModel):
    browser: Optional[SslBrowserTrustVendor] = None
    revoked: Optional[Union[bool, Dict[str, bool]]] = Field(None, title="Revoked")


class Ssl(BaseModel):
    acceptable_cas: List[SslCas] = Field(..., title="Acceptable Cas")
    alpn: Optional[List[str]] = Field(None, title="Alpn")
    cert: Optional[SslCertificate] = None
    chain: List[str] = Field(
        ..., description="List of certificates in PEM format", title="Chain"
    )
    chain_sha256: List[str] = Field(..., title="Chain Sha256")
    cipher: Optional[SslCipher] = Field(
        None, description="Default cipher used for the connection", title="Cipher"
    )
    dhparams: Optional[SslDhparams] = None
    handshake_states: List[str] = Field(
        ...,
        description="Detailed breakdown of how the SSL/TLS connection was negotiated.",
        title="Handshake States",
    )
    ja3s: Optional[str] = Field(
        None,
        description="JA3 fingerprint for the server SSL/TLS connection. Useful for pivoting or identifying SSL/TLS implementations.",
        title="Ja3S",
    )
    jarm: Optional[str] = Field(
        None,
        description="JARM fingerprint for the server SSL/TLS connection. Useful for pivoting or identifying SSL/TLS implementations.",
        title="Jarm",
    )
    ocsp: Optional[Union[SslOcsp, Dict[str, Any]]] = Field(None, title="Ocsp")
    tlsext: Optional[List[SslExtension]] = Field(None, title="Tlsext")
    trust: Optional[SslBrowserTrust] = None
    unstable: Optional[List[str]] = Field(
        None,
        description='If the crawlers couldn\'t gather a property (ex. "versions") due to an unstable connection then the name of that property is added here.',
        title="Unstable",
    )
    versions: Optional[List[str]] = Field(
        None,
        description='The crawlers explicitly check every SSL/TLS version. If the server doesn\'t support a version then a "-" is in front of the version value.',
        title="Versions",
    )


class SteamIhsUser(BaseModel):
    auth_key_id: int = Field(..., title="Auth Key Id")
    steam_id: str = Field(..., title="Steam Id")


class SteamIhs(BaseModel):
    client_id: Optional[str] = Field(None, title="Client Id")
    connect_port: Optional[int] = Field(None, title="Connect Port")
    enabled_services: Optional[int] = Field(None, title="Enabled Services")
    euniverse: Optional[int] = Field(None, title="Euniverse")
    hostname: Optional[str] = Field(None, title="Hostname")
    instance_id: Optional[str] = Field(None, title="Instance Id")
    ip_addresses: Optional[List[str]] = Field(None, title="Ip Addresses")
    is_64bit: Optional[bool] = Field(None, title="Is 64Bit")
    mac_addresses: Optional[List[str]] = Field(None, title="Mac Addresses")
    min_version: Optional[int] = Field(None, title="Min Version")
    os_type: Optional[int] = Field(None, title="Os Type")
    public_ip_address: Optional[str] = Field(None, title="Public Ip Address")
    timestamp: Optional[int] = Field(None, title="Timestamp")
    users: Optional[List[SteamIhsUser]] = Field(None, title="Users")
    version: int = Field(..., title="Version")


class Synology(BaseModel):
    hostname: Optional[str] = Field(None, title="Hostname")
    custom_login_title: Optional[str] = Field(None, title="Custom Login Title")
    login_welcome_title: Optional[str] = Field(None, title="Login Welcome Title")
    login_welcome_msg: Optional[str] = Field(None, title="Login Welcome Msg")
    version: Optional[str] = Field(None, title="Version")


class Tacacs(BaseModel):
    flags: int = Field(..., title="Flags")
    length: int = Field(..., title="Length")
    sequence: int = Field(..., title="Sequence")
    session: int = Field(..., title="Session")
    type: int = Field(..., title="Type")
    version: str = Field(..., title="Version")


class TasmotaFirmware(BaseModel):
    build_date: str = Field(..., title="Build Date")
    core: str = Field(..., title="Core")
    sdk: str = Field(..., title="Sdk")
    version: str = Field(..., title="Version")


class TasmotaNetwork(BaseModel):
    hostname: str = Field(..., title="Hostname")
    ip_address: str = Field(..., title="Ip Address")
    mac_address: str = Field(..., title="Mac Address")


class TasmotaWifi(BaseModel):
    bssid: Optional[str] = Field(None, title="Bssid")
    ssid: str = Field(..., title="Ssid")


class Tasmota(BaseModel):
    firmware: Optional[TasmotaFirmware] = None
    friendly_names: Optional[Union[str, List[str]]] = Field(
        None, title="Friendly Names"
    )
    module: Optional[str] = Field(None, title="Module")
    network: Optional[TasmotaNetwork] = None
    wifi: Optional[TasmotaWifi] = None


class Telnet(BaseModel):
    do: List[str] = Field(..., title="Do")
    dont: List[str] = Field(..., title="Dont")
    will: List[str] = Field(..., title="Will")
    wont: List[str] = Field(..., title="Wont")


class Tibia(BaseModel):
    map: Optional[Dict[str, Any]] = Field(None, title="Map")
    monsters: Optional[Dict[str, Any]] = Field(None, title="Monsters")
    motd: Optional[Dict[str, Any]] = Field(None, title="Motd")
    npcs: Optional[Dict[str, Any]] = Field(None, title="Npcs")
    owner: Optional[Dict[str, Any]] = Field(None, title="Owner")
    players: Optional[Dict[str, Any]] = Field(None, title="Players")
    serverinfo: Optional[Dict[str, Any]] = Field(None, title="Serverinfo")


class TraneEquipment(BaseModel):
    device_name: str = Field(..., title="Device Name")
    display_name: str = Field(..., title="Display Name")
    equipment_family: str = Field(..., title="Equipment Family")
    equipment_uri: str = Field(..., title="Equipment Uri")
    is_offline: bool = Field(..., title="Is Offline")
    role_document: str = Field(..., title="Role Document")


class Trane(BaseModel):
    equipment: Optional[List[TraneEquipment]] = Field(None, title="Equipment")
    hardware_serial_number: Optional[str] = Field(None, title="Hardware Serial Number")
    hardware_type: Optional[str] = Field(None, title="Hardware Type")
    kernel_version: Optional[str] = Field(None, title="Kernel Version")
    product_name: Optional[str] = Field(None, title="Product Name")
    product_version: Optional[str] = Field(None, title="Product Version")
    server_boot_time: Optional[str] = Field(None, title="Server Boot Time")
    server_name: Optional[str] = Field(None, title="Server Name")
    server_time: Optional[str] = Field(None, title="Server Time")
    vendor_name: Optional[str] = Field(None, title="Vendor Name")


class Ubiquiti(BaseModel):
    hostname: Optional[str] = Field(None, title="Hostname")
    ip: Optional[str] = Field(None, title="Ip")
    ip_alt: Optional[str] = Field(None, title="Ip Alt")
    mac: Optional[str] = Field(None, title="Mac")
    mac_alt: Optional[str] = Field(None, title="Mac Alt")
    product: Optional[str] = Field(None, title="Product")
    version: Optional[str] = Field(None, title="Version")


class UnitronicsPcom(BaseModel):
    hardware_version: str = Field(..., title="Hardware Version")
    model: str = Field(..., title="Model")
    os_build: int = Field(..., title="Os Build")
    os_version: float = Field(..., title="Os Version")
    plc_name: Optional[str] = Field(None, title="Plc Name")
    plc_unique_id: int = Field(..., title="Plc Unique Id")
    uid_master: int = Field(..., title="Uid Master")


class UpnpService(BaseModel):
    control_url: Optional[str] = Field(None, title="Control Url")
    event_sub_url: Optional[str] = Field(None, title="Event Sub Url")
    scpdurl: Optional[str] = Field(None, title="Scpdurl")
    service_id: Optional[str] = Field(None, title="Service Id")
    service_type: Optional[str] = Field(None, title="Service Type")


class Upnp(BaseModel):
    device_type: Optional[str] = Field(None, title="Device Type")
    friendly_name: Optional[str] = Field(None, title="Friendly Name")
    manufacturer: Optional[str] = Field(None, title="Manufacturer")
    manufacturer_url: Optional[str] = Field(None, title="Manufacturer Url")
    model_description: Optional[str] = Field(None, title="Model Description")
    model_name: Optional[str] = Field(None, title="Model Name")
    model_number: Optional[str] = Field(None, title="Model Number")
    model_url: Optional[str] = Field(None, title="Model Url")
    presentation_url: Optional[str] = Field(None, title="Presentation Url")
    serial_number: Optional[str] = Field(None, title="Serial Number")
    services: Optional[List[UpnpService]] = Field(None, title="Services")
    sub_devices: Optional[List[Upnp]] = Field(None, title="Sub Devices")
    udn: Optional[str] = Field(None, title="Udn")
    upc: Optional[str] = Field(None, title="Upc")


class Vault(BaseModel):
    cluster_id: Optional[str] = Field(None, title="Cluster Id")
    cluster_name: Optional[str] = Field(None, title="Cluster Name")
    initialized: Optional[bool] = Field(None, title="Initialized")
    performance_standby: Optional[bool] = Field(None, title="Performance Standby")
    replication_dr_mode: Optional[str] = Field(None, title="Replication Dr Mode")
    replication_performance_mode: Optional[str] = Field(
        None, title="Replication Performance Mode"
    )
    sealed: Optional[bool] = Field(None, title="Sealed")
    server_time_utc: Optional[int] = Field(None, title="Server Time Utc")
    standby: Optional[bool] = Field(None, title="Standby")
    version: Optional[str] = Field(None, title="Version")


class VertxDoor(BaseModel):
    firmware_date: str = Field(..., title="Firmware Date")
    firmware_version: str = Field(..., title="Firmware Version")
    internal_ip: str = Field(..., title="Internal Ip")
    mac: str = Field(..., title="Mac")
    name: str = Field(..., title="Name")
    type: str = Field(..., title="Type")


class Vmware(BaseModel):
    api_type: Optional[str] = Field(None, title="Api Type")
    api_version: Optional[str] = Field(None, title="Api Version")
    build: Optional[str] = Field(None, title="Build")
    full_name: Optional[str] = Field(None, title="Full Name")
    instance_uuid: Optional[str] = Field(None, title="Instance Uuid")
    license_product_name: Optional[str] = Field(None, title="License Product Name")
    license_product_version: Optional[str] = Field(
        None, title="License Product Version"
    )
    locale_build: Optional[str] = Field(None, title="Locale Build")
    locale_version: Optional[str] = Field(None, title="Locale Version")
    name: Optional[str] = Field(None, title="Name")
    os_type: Optional[str] = Field(None, title="Os Type")
    product_line_id: Optional[str] = Field(None, title="Product Line Id")
    vendor: Optional[str] = Field(None, title="Vendor")
    version: Optional[str] = Field(None, title="Version")


class XiaomiMiio(BaseModel):
    device_id: str = Field(..., title="Device Id")
    token: str = Field(..., title="Token")


class SonyBravia(BaseModel):
    interface_version: str = Field(..., title='Interface Version')
    model_name: str = Field(..., title='Model Name')
    mac_address: Optional[str] = Field(None, title='Mac Address')


class PhilipsHue(BaseModel):
    api_version: str = Field(..., title='Api Version')
    bridge_id: str = Field(..., title='Bridge Id')
    data_store_version: Optional[str] = Field(None, title='Data Store Version')
    factory_new: bool = Field(..., title='Factory New')
    mac: str = Field(..., title='Mac')
    model_id: str = Field(..., title='Model Id')
    name: str = Field(..., title='Name')
    sw_version: str = Field(..., title='Sw Version')


class EthereumP2PNeighbour(BaseModel):
    ip: str = Field(..., title='Ip')
    pubkey: str = Field(..., title='Pubkey')
    tcp_port: int = Field(..., title='Tcp Port')
    udp_port: int = Field(..., title='Udp Port')


class EthereumP2P(BaseModel):
    pubkey: str = Field(..., title='Pubkey')
    tcp_port: Optional[int] = Field(None, title='Tcp Port')
    udp_port: Optional[int] = Field(None, title='Udp Port')
    neighbours: Optional[List[EthereumP2PNeighbour]] = Field(None, title='Neighbours')


class MssqlSsrpInstance(BaseModel):
    instance_name: str = Field(..., title='Instance Name')
    is_clustered: Optional[bool] = Field(None, title='Is Clustered')
    server_name: str = Field(..., title='Server Name')
    tcp: Optional[int] = Field(None, title='Tcp')
    version: str = Field(..., title='Version')
    version_name: Optional[str] = Field(None, title='Version Name')


class MssqlSsrp(BaseModel):
    instances: List[MssqlSsrpInstance] = Field(..., title='Instances')


class Ntlm(BaseModel):
    dns_domain_name: Optional[str] = Field(None, title='Dns Domain Name')
    fqdn: Optional[str] = Field(None, title='Fqdn')
    netbios_computer_name: Optional[str] = Field(None, title='Netbios Computer Name')
    netbios_domain_name: Optional[str] = Field(None, title='Netbios Domain Name')
    os: Optional[List[str]] = Field(None, title='Os')
    os_build: Optional[str] = Field(None, title='Os Build')
    target_realm: Optional[str] = Field(None, title='Target Realm')
    timestamp: Optional[int] = Field(None, title='Timestamp')


class SiemensS7Property(BaseModel):
    raw: str = Field(..., title='Raw')
    value: str = Field(..., title='Value')


class SiemensS7(BaseModel):
    dst_tsap: str = Field(..., title='Dst Tsap')
    identities: Dict[str, SiemensS7Property] = Field(..., title='Identities')
    src_tsap: str = Field(..., title='Src Tsap')


class TpLinkKasa(BaseModel):
    alias: str = Field(..., title='Alias')
    dev_name: str = Field(..., title='Dev Name')
    device_id: str = Field(..., title='Device Id')
    fw_id: Optional[str] = Field(None, title='Fw Id')
    hw_id: str = Field(..., title='Hw Id')
    hw_ver: str = Field(..., title='Hw Ver')
    latitude: float = Field(..., title='Latitude')
    longitude: float = Field(..., title='Longitude')
    mac_address: str = Field(..., title='Mac Address')
    model: str = Field(..., title='Model')
    oem_id: str = Field(..., title='Oem Id')
    sw_ver: str = Field(..., title='Sw Ver')
    type: str = Field(..., title='Type')


class Vnc(BaseModel):
    protocol_version: str = Field(..., title='Protocol Version')
    security_types: Optional[Dict[str, str]] = Field(None, title='Security Types')


class Yeelight(BaseModel):
    firmware_version: str = Field(..., title='Firmware Version')
    model: str = Field(..., title='Model')


class Banner(BaseModel):
    class Config:
        extra = Extra.forbid

    asn: Optional[str] = Field(None, title="Asn")
    cpe: Optional[List[str]] = Field(
        None, description="CPE information in the old, deprecated format.", title="Cpe"
    )
    cpe23: Optional[List[str]] = Field(
        None, description="CPE information in the 2.3 format.", title="Cpe23"
    )
    data: str = Field(..., title="Data")
    device: Optional[str] = Field(None, title="Device")
    devicetype: Optional[str] = Field(None, title="Devicetype")
    domains: List[str] = Field(..., title="Domains")
    hash: int = Field(
        ...,
        description='Numeric hash of the "data" property which is helpful for finding other IPs with the exact same information.',
        title="Hash",
    )
    hostnames: List[str] = Field(
        ...,
        description="Hostnames for the IP based on the PTR/ reverse DNS information.",
        title="Hostnames",
    )
    html: Optional[str] = Field(
        None,
        description='This property is deprecated. Use "http.html" instead.',
        title="Html",
    )
    ip: Optional[int] = Field(
        None,
        description="Numeric IP address which can be more efficient for storing/ indexing.",
        title="Ip",
    )
    ip_str: Optional[str] = Field(
        None,
        description="String representation of the IP address. This is most likely what you want to use.",
        title="Ip Str",
    )
    info: Optional[str] = Field(None, title="Info")
    ipv6: Optional[str] = Field(None, title="Ipv6")
    isp: Optional[str] = Field(None, title="Isp")
    link: Optional[str] = Field(None, title="Link")
    mac: Optional[Dict[str, Optional[MacAddressInfo]]] = Field(None, title="Mac")
    opts: Optional[Dict[str, Any]] = Field(
        None,
        description="Stores experimental data before it has been finalized into a top-level property.",
        title="Opts",
    )
    org: Optional[str] = Field(
        None, description="Name of the organization that manages the IP", title="Org"
    )
    os: Optional[str] = Field(None, description="Operating system", title="Os")
    platform: Optional[str] = Field(None, title="Platform")
    port: int = Field(..., title="Port")
    product: Optional[str] = Field(
        None,
        description="Name of the software that powers the service.",
        title="Product",
    )
    tags: Optional[List[Tag]] = None
    timestamp: str = Field(
        ...,
        description="Date and time that the banner was collected in UTC time.",
        title="Timestamp",
    )
    title: Optional[str] = Field(
        None,
        description='This property is deprecated. Use "http.title" instead.',
        title="Title",
    )
    transport: str = Field(..., title="Transport")
    uptime: Optional[int] = Field(None, title="Uptime")
    vendor: Optional[str] = Field(None, title="Vendor")
    version: Optional[str] = Field(None, title="Version")
    vulns: Optional[Dict[str, Vulnerability]] = Field(None, title="Vulns")
    location: Optional[Location] = None
    shodan: _Shodan = Field(alias="_shodan")
    afp: Optional[Afp] = None
    airplay: Optional[Airplay] = None
    android_debug_bridge: Optional[AndroidDebugBridge] = None
    bgp: Optional[Bgp] = None
    bitcoin: Optional[Bitcoin] = None
    cassandra: Optional[Cassandra] = None
    checkpoint: Optional[Checkpoint] = None
    chromecast: Optional[Chromecast] = None
    cloud: Optional[Cloud] = None
    coap: Optional[Coap] = None
    cobalt_strike_beacon: Optional[CobaltStrikeBeacon] = None
    consul: Optional[Consul] = None
    couchdb: Optional[Couchdb] = None
    dahua: Optional[Dahua] = None
    dahua_dvr_web: Optional[DahuaDvrWeb] = None
    dns: Optional[Dns] = None
    docker: Optional[Docker] = None
    domoticz: Optional[Domoticz] = None
    elastic: Optional[Elastic] = None
    etcd: Optional[Etcd] = None
    ethereum_rpc: Optional[EthereumRpc] = None
    ethereum_p2p: Optional[EthereumP2P] = None
    ethernetip: Optional[Ethernetip] = None
    ftp: Optional[Ftp] = None
    handpunch: Optional[Handpunch] = None
    hikvision: Optional[Hikvision] = None
    hive: Optional[ApacheHive] = None
    home_assistant: Optional[HomeAssistant] = None
    homebridge: Optional[Homebridge] = None
    hoobs: Optional[Hoobs] = None
    hp_ilo: Optional[HpIlo] = None
    http: Optional[Http] = None
    hubitat: Optional[Hubitat] = None
    ibm_db2: Optional[IbmDb2] = None
    influxdb: Optional[Influxdb] = None
    iota: Optional[Dict[str, Any]] = Field(None, title="Iota")
    ip_camera: Optional[IpCamera] = None
    ip_symcon: Optional[IpSymcon] = None
    ipp_cups: Optional[IppCups] = None
    isakmp: Optional[Isakmp] = None
    iscsi: Optional[Iscsi] = None
    kafka: Optional[Kafka] = None
    knx: Optional[Knx] = None
    kubernetes: Optional[Kubernetes] = None
    lantronix: Optional[Lantronix] = None
    mdns: Optional[Mdns] = None
    mikrotik_routeros: Optional[MikrotikRouteros] = None
    minecraft: Optional[Minecraft] = None
    mitsubishi_q: Optional[MitsubishiQ] = None
    monero: Optional[Dict[str, Any]] = Field(None, title="Monero")
    mongodb: Optional[Mongodb] = None
    msrpc: Optional[Msrpc] = None
    mssql: Optional[Mssql] = None
    mssql_ssrp: Optional[MssqlSsrp] = None
    mqtt: Optional[Mqtt] = None
    nats: Optional[Nats] = None
    ndmp: Optional[Ndmp] = None
    netbios: Optional[Netbios] = None
    netgear: Optional[Netgear] = None
    ntlm: Optional[Ntlm] = None
    ntp: Optional[Ntp] = None
    openflow: Optional[Openflow] = None
    openhab: Optional[Openhab] = None
    openwebnet: Optional[Openwebnet] = None
    pcworx: Optional[Pcworx] = None
    philips_hue: Optional[PhilipsHue] = None
    plex: Optional[Plex] = None
    qnap: Optional[Qnap] = None
    rdp: Optional[Rdp] = None
    realport: Optional[Realport] = None
    redis: Optional[Redis] = None
    rip: Optional[Rip] = None
    ripple: Optional[Ripple] = None
    rsync: Optional[Rsync] = None
    samsung_tv: Optional[SamsungTv] = None
    siemens_s7: Optional[SiemensS7] = None
    smb: Optional[Smb] = None
    snmp: Optional[Snmp] = None
    sonicwall: Optional[Sonicwall] = None
    sonos: Optional[Sonos] = None
    sony_bravia: Optional[SonyBravia] = None
    spotify_connect: Optional[SpotifyConnect] = None
    ssh: Optional[Ssh] = None
    ssl: Optional[Ssl] = None
    steam_ihs: Optional[SteamIhs] = None
    synology: Optional[Synology] = None
    synology_dsm: Optional[Synology] = None
    synology_srm: Optional[Synology] = None
    tacacs: Optional[Tacacs] = None
    tasmota: Optional[Tasmota] = None
    telnet: Optional[Telnet] = None
    tibia: Optional[Tibia] = None
    tp_link_kasa: Optional[TpLinkKasa] = None
    trane: Optional[Trane] = None
    ubiquiti: Optional[Ubiquiti] = None
    unitronics_pcom: Optional[UnitronicsPcom] = None
    upnp: Optional[Upnp] = None
    vault: Optional[Vault] = None
    vertx: Optional[VertxDoor] = None
    vmware: Optional[Vmware] = None
    vnc: Optional[Vnc] = None
    xiaomi_miio: Optional[XiaomiMiio] = None
    yeelight: Optional[Yeelight] = None


Isakmp.update_forward_refs()
MinecraftDescription.update_forward_refs()
Upnp.update_forward_refs()
