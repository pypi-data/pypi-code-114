"""
Constants for csle collector
"""
import re

class DOCKER_STATS:
    CPU_STATS = "cpu_stats"
    CPU_USAGE = "cpu_usage"
    PERCPU_USAGE = "percpu_usage"
    PRECPU_STATS = "precpu_stats"
    TOTAL_USAGE = "total_usage"
    SYSTEM_CPU_USAGE = "system_cpu_usage"
    ONLINE_CPUS = "online_cpus"
    BLKIO_STATS = "blkio_stats"
    IO_SERVICE_BYTES_RECURSIVE = "io_service_bytes_recursive"
    OP = "op"
    READ = "Read"
    VALUE = "value"
    WRITE = "Write"
    NETWORKS = "networks"
    RX_BYTES = "rx_bytes"
    TX_BYTES = "tx_bytes"
    MEMORY_STATS = "memory_stats"
    USAGE = "usage"
    LIMIT = "limit"
    PIDS = "pids"
    TIMESTAMP = "timestamp"
    CPU_PERCENT = "cpu_percent"
    MEM_CURRENT = "mem_current"
    MEM_TOTAL = "mem_total"
    MEM_PERCENT = "mem_percent"
    BLK_READ = "blk_read"
    BLK_WRITE = "blk_write"
    NET_RX = "net_rx"
    NET_TX = "net_tx"
    PIDS_STATS = "pids_stats"
    CURRENT = "current"
    CONTAINER_NAME = "container_name"
    CONTAINER_ID = "container_id"
    CONTAINER_IP = "container_ip"
    UNIX_DOCKER_SOCK_URL = "unix://var/run/docker.sock"



class IDS_ROUTER:
    """
    Constants related to the IDS
    """
    MAX_ALERTS = 1000
    UPDATE_RULESET = "/pulledpork/pulledpork.pl -c /pulledpork/etc/pulledpork.conf -l -P -E -H SIGHUP"
    FAST_LOG_FILE = "/var/snort/fast.log"
    ALERTS_FILE = "/var/snort/alert.csv"
    STATS_FILE = "/var/snort/snort.stats"
    TAIL_ALERTS_COMMAND = "sudo tail -" + str(MAX_ALERTS)
    TAIL_FAST_LOG_COMMAND = "sudo tail -" + str(str(MAX_ALERTS))
    TAIL_ALERTS_LATEST_COMMAND = "sudo tail -1"
    PRIORITY_REGEX = re.compile(r"Priority: \d")
    CLASSIFICATION_REGEX = re.compile(r"(?<=Classification: )(.*?)(?=])")
    SEVERE_ALERT_PRIORITY_THRESHOLD = 3
    ALERT_IDS_ID = {}
    ALERT_IDS_ID["tcp-connection"] = 0
    ALERT_IDS_ID["unknown"] = 1
    ALERT_IDS_ID["string-detect"] = 2
    ALERT_IDS_ID["protocol-command-decode"] = 3
    ALERT_IDS_ID["not-suspicious"] = 4
    ALERT_IDS_ID["network-scan"] = 5
    ALERT_IDS_ID["misc-activity"] = 6
    ALERT_IDS_ID["icmp-event"] = 7
    ALERT_IDS_ID["web-application-activity"] = 8
    ALERT_IDS_ID["unusual-client-port-connection"] = 9
    ALERT_IDS_ID["system-call-detect"] = 10
    ALERT_IDS_ID["suspicious-login"] = 11
    ALERT_IDS_ID["suspicious-filename-detect"] = 12
    ALERT_IDS_ID["successful-recon-limited"] = 13
    ALERT_IDS_ID["successful-recon-largescale"] = 14
    ALERT_IDS_ID["successful-dos"] = 15
    ALERT_IDS_ID["rpc-portmap-decode"] = 16
    ALERT_IDS_ID["non-standard-protocol"] = 17
    ALERT_IDS_ID["misc-attack"] = 18
    ALERT_IDS_ID["denial-of-service"] = 19
    ALERT_IDS_ID["default-login-attempt"] = 20
    ALERT_IDS_ID["bad-unknown"] = 21
    ALERT_IDS_ID["attempted-recon"] = 22
    ALERT_IDS_ID["attempted-dos"] = 23
    ALERT_IDS_ID["web-application-attack"] = 24
    ALERT_IDS_ID["unsuccessful-user"] = 25
    ALERT_IDS_ID["trojan-activity"] = 26
    ALERT_IDS_ID["successful-user"] = 27
    ALERT_IDS_ID["successful-admin"] = 28
    ALERT_IDS_ID["shellcode-detect"] = 29
    ALERT_IDS_ID["policy-violation"] = 30
    ALERT_IDS_ID["inappropriate-content"] = 31
    ALERT_IDS_ID["attempted-user"] = 32
    ALERT_IDS_ID["attempted-admin"] = 33