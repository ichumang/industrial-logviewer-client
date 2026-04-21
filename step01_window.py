#!/usr/bin/env python3
"""
Industrial Log Viewer — Main GUI Window (scaffold)
===================================================
Four-category log viewer:
    - Log Data Parameterization
    - Activation Data
    - Dynamic Drive Data
    - Drive Error

Layout:
    Top bar    : category tabs, year selector, server IP, connection status dot
    Left panel : date explorer (tree: year > month > day), populated from UDP server
    Right panel: content viewer (table or list depending on data type)
    Status bar : category | year | root path

Sprint 4 target: merge UdpClient from itc_log_client.py as the
networking layer. Left panel dates come from GET_*_DAYS_REPLY.
Right panel content comes from GET_*_DATA_REPLY.

Dependencies:
    pip install PyQt6
"""

# Main window scaffold — active development.
# Integration with UDP module planned for Sprint 4.
