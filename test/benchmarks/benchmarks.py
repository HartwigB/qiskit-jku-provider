# -*- coding: utf-8 -*-

# Copyright 2019, IBM.
#
# This source code is licensed under the Apache License, Version 2.0 found in
# the LICENSE.txt file in the root directory of this source tree.

# pylint: disable=missing-docstring,redefined-builtin

import unittest
import os

from qiskit              import QuantumCircuit
from qiskit              import execute
from qiskit_jku_provider import QasmSimulator




class QasmSimulatorJKUBenchmarkSuite:
    """Runs the Basic qasm_simulator tests from Terra on JKU."""

    def setup(self):
        QASM_FILES    = ["3_17_13.qasm", "4_49_16.qasm", "4gt4-v0_72.qasm"]
        self.seed     = 88
        self.backend  = QasmSimulator(silent=True)
        self.circuits = []
        for file in QASM_FILES:
            full_file             = os.path.join(os.path.dirname(__file__), 'qasms', file)
            compiled_circuit      = QuantumCircuit.from_qasm_file(full_file)
            compiled_circuit.name = file
            self.circuits.append(compiled_circuit)
        self.circuit = compiled_circuit

    def time_qasm_simulator_single_shot(self):
        """Test single shot run."""
        for circuit in self.circuits:
            result = execute(circuit, self.backend, seed_transpiler=34342, shots=1).result()
            self.assertEqual(result.success, True)

    def time_qasm_simulator(self):
        """Test data counts output for single circuit run against reference."""
        shots = 1024
        for circuit in self.circuits:
            result = execute(circuit, self.backend, seed_transpiler=34342, shots=shots).result()
            result = execute(circuit, self.backend, seed_transpiler=34342, shots=shots).result()
            self.assertEqual(result.success, True)
            #threshold = 0.04 * shots
            #counts = result.get_counts('test')
            #target = {'100 100': shots / 8, '011 011': shots / 8,
            #          '101 101': shots / 8, '111 111': shots / 8,
            #          '000 000': shots / 8, '010 010': shots / 8,
            #          '110 110': shots / 8, '001 001': shots / 8}
            #self.assertDictAlmostEqual(counts, target, threshold)

