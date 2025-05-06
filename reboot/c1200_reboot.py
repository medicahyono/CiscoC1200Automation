from netmiko import ConnectHandler

device = {
    "device_type": "cisco_ios",      # cocok untuk switch Cisco Catalyst
    "host": "192.168.110.195",           # ganti dengan IP switch Anda
    "username": "@@@@@",             # username
    "password": "@@@@!",     # password
}

try:
    connection = ConnectHandler(**device)

    # Kirim perintah reload
    output = connection.send_command_timing("reload")

    # Cek apakah ada prompt konfirmasi
    if "Do you want to continue" in output or "(Y/N)" in output:
        output += connection.send_command_timing("Y")

    print("Output:\n", output)

    connection.disconnect()
except Exception as e:
    print("Gagal terkoneksi atau kirim perintah:", e)
