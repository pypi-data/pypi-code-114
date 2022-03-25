#  Copyright 2022 Zeppelin Bend Pty Ltd
#
#  This Source Code Form is subject to the terms of the Mozilla Public
#  License, v. 2.0. If a copy of the MPL was not distributed with this
#  file, You can obtain one at https://mozilla.org/MPL/2.0/.

from typing import Optional, Dict, Set

__all__ = ["NetworkModel"]

from zepben.opendss import LoadConnection, Circuit, Bus, Line, LineCode, Transformer, RegControl


class NetworkModel:

    def __init__(
            self,
            default_base_frequency: int = 50,
            circuit: Optional[Circuit] = None,
            buses: Dict[str, Bus] = None,
            lines: Dict[str, Line] = None,
            line_codes: Dict[str, LineCode] = None,
            transformers: Dict[str, Transformer] = None,
            load_connections: Dict[str, LoadConnection] = None,
            reg_controls: Dict[str, RegControl] = None
    ):
        self.default_base_frequency = default_base_frequency
        self.circuit = circuit
        self.buses = {} if buses is None else buses
        self.lines = {} if lines is None else lines
        self.line_codes = {} if line_codes is None else line_codes
        self.transformers = {} if transformers is None else transformers
        self.load_connections = {} if load_connections is None else load_connections
        self.reg_controls = {} if reg_controls is None else reg_controls

    @property
    def voltage_bases(self) -> Set[float]:
        voltage_bases = set()

        voltage_bases.add(self.circuit.base_kv)

        for tx in self.transformers.values():
            for w in tx.windings:
                voltage_bases.add(w.kv)

        for load_conn in self.load_connections.values():
            voltage_bases.add(load_conn.kv)

        return voltage_bases

    def set_default_base_frequency(self, default_base_frequency: int):
        self.default_base_frequency = default_base_frequency

    def set_circuit(self, circuit: Optional[Circuit] = None):
        self.circuit = circuit

    def add_bus(self, bus: Bus):
        self.buses[bus.uid] = bus

    def add_line(self, line: Line):
        self.lines[line.uid] = line

    def add_line_code(self, line_code: LineCode):
        self.line_codes[line_code.uid] = line_code

    def add_transformer(self, transformer: Transformer):
        self.transformers[transformer.uid] = transformer

    def add_load_connection(self, load_connection: LoadConnection):
        self.load_connections[load_connection.uid] = load_connection

    def add_reg_control(self, reg_control: RegControl):
        self.reg_controls[reg_control.uid] = reg_control

    def remove_line(self, uid: str):
        del self.lines[uid]

    def remove_line_code(self, uid: str):
        del self.line_codes[uid]

    def remove_transformer(self, uid: str):
        del self.transformers[uid]

    def remove_load_connection(self, uid: str):
        del self.load_connections[uid]

    def remove_reg_control(self, uid: str):
        del self.reg_controls[uid]

    def copy(self):
        raise NotImplementedError("Copy method is not implemented")
