# kpi_calculator.py

def calculate_throughput(total_data_bytes, time_seconds):
    if time_seconds <= 0:
        raise ValueError("Time must be greater than 0")
    return (total_data_bytes * 8) / (time_seconds * 1e6) 


def calculate_latency(time_sent_ms, time_received_ms):
    if time_received_ms < time_sent_ms:
        raise ValueError("Received time must be greater than or equal to sent time")
    return time_received_ms - time_sent_ms 


def calculate_packet_loss(total_packets, lost_packets):
    if total_packets <= 0:
        raise ValueError("Total packets must be greater than 0")
    if lost_packets > total_packets:
        raise ValueError("Lost packets cannot exceed total packets")
    return (lost_packets / total_packets) * 100  


def calculate_signal_strength(signal_power_dBm):
    if signal_power_dBm > 0:
        raise ValueError("Signal strength in dBm cannot be positive")
    return signal_power_dBm  


def calculate_kpi_summary(total_data_bytes, time_seconds, time_sent_ms, time_received_ms, total_packets, lost_packets, signal_power_dBm):
    throughput = calculate_throughput(total_data_bytes, time_seconds)
    latency = calculate_latency(time_sent_ms, time_received_ms)
    packet_loss = calculate_packet_loss(total_packets, lost_packets)
    signal_strength = calculate_signal_strength(signal_power_dBm)

    return {
        "Throughput (Mbps)": throughput,
        "Latency (ms)": latency,
        "Packet Loss (%)": packet_loss,
        "Signal Strength (dBm)": signal_strength,
    }
