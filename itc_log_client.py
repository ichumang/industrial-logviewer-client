#!/usr/bin/env python3
"""
Industrial Log Viewer — UDP Client Module (Sprint 1)
=====================================================
Standalone test client that communicates with the Log Data Server
over UDP and displays structured log data in a PyQt6 window.

This module will be merged into the main LogViewerWindow in Sprint 4
as the networking layer of the full application.

Protocol:
    Transport : UDP
    Request   : 4-byte packet (cmd group ID + sub-command ID), little-endian
    Reply     : binary struct — header + typed payload
    Timeout   : 2s default

Implemented commands:
    GET_ACTIVATION_DAYS_REQ / REPLY  — bitfield of active calendar days per year/month
    GET_ACTIVATION_DATA_REQ / REPLY  — typed log entries (String or DriveField struct)

See docs/architecture.md for full protocol description.

Dependencies:
    pip install PyQt6
"""

# Full implementation in private working branch.
# Public interface summary:
#
#   class UdpClient:
#       def request(self, cmdid) -> bytes    # send request, return raw reply
#
#   def parse_activation_days_reply(data: bytes) -> list[(year, month, day)]
#   def parse_activation_data_reply(data: bytes) -> list[str]
#
#   class MainWindow(QMainWindow):           # PyQt6 GUI
#       buttons: Get activation days, Get activation data, OK, Abbrechen
#       output:  QTextEdit (monospace, read-only)
#       status:  QStatusBar showing connection info + last action
