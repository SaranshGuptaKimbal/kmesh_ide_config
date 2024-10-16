import subprocess

delay_msec_values = []
packet_count_values = []
payload_size_values = []
transmission_power_db_values = []
attenuation_db_values = []
val_indexes = [0, 0, 0, 0, 0]

def configure_sender():
    print("Configuring sender")

def configure_receiver():
    print("Configuring receiver")

def print_sender_stats():
    print("Getting sender stats")

def print_receiver_stats():
    print("Getting receiver stats")

def increment_stats(index = 0):
    if(index >= len(val_indexes)):
        return False
    
    global val_indexes
    val_indexes[index] += 1
    if(val_indexes[index] >= len(delay_msec_values)):
        val_indexes[index] = 0
        return increment_stats(index + 1)

    return True

def run_phyTester():
    print("Running phyTester")

def main():
    continueLoop = True
    while(continueLoop):
        configure_sender()
        configure_receiver()
        run_phyTester()
        print_sender_stats()
        print_receiver_stats()
        continueLoop = increment_stats()