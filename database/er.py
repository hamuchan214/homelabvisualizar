from graphviz import Digraph

# Create a new directed graph
er_diagram = Digraph("ER Diagram", node_attr={"shape": "box", "style": "rounded, filled", "fillcolor": "lightgrey"})

# Define the main entities and their attributes
er_diagram.node("Devices", "Devices\n- id\n- name\n- ip_address\n- vendor\n- model\n- serial_number\n- type\n- location\n- proxmox_node\n- created_at\n- updated_at")
er_diagram.node("NetworkConfig", "NetworkConfig\n- id\n- device_id (FK)\n- interface\n- mac_address\n- subnet\n- gateway\n- vlan\n- status\n- connected_port\n- created_at\n- updated_at")
er_diagram.node("SNMPMetrics", "SNMPMetrics\n- id\n- device_id (FK)\n- metric_name\n- value\n- timestamp\n- unit")
er_diagram.node("ProxmoxMetrics", "ProxmoxMetrics\n- id\n- device_id (FK)\n- cpu_usage\n- memory_usage\n- disk_usage\n- network_usage\n- timestamp")
er_diagram.node("Alerts", "Alerts\n- id\n- device_id (FK)\n- alert_type\n- description\n- severity\n- timestamp\n- resolved")
er_diagram.node("DeviceLogs", "DeviceLogs\n- id\n- device_id (FK)\n- log_type\n- message\n- timestamp")
er_diagram.node("DeviceLinks", "DeviceLinks\n- id\n- device_a_id (FK)\n- device_a_port\n- device_b_id (FK)\n- device_b_port\n- link_type\n- status\n- created_at\n- updated_at")

# Define relationships between entities
er_diagram.edge("Devices", "NetworkConfig", label="1 to many")
er_diagram.edge("Devices", "SNMPMetrics", label="1 to many")
er_diagram.edge("Devices", "ProxmoxMetrics", label="1 to many")
er_diagram.edge("Devices", "Alerts", label="1 to many")
er_diagram.edge("Devices", "DeviceLogs", label="1 to many")
er_diagram.edge("Devices", "DeviceLinks", label="1 to many (device_a_id, device_b_id)")

# Render and display the ER diagram
er_diagram.format = "png"
er_diagram_output_path = "/Documents/GitHub/Homelabvisualizar/database/ER_Diagram_Home_Network_Monitoring.png"
er_diagram.render(filename=er_diagram_output_path, cleanup=True)

er_diagram_output_path
