import pandas as pd


with open("rustscanS_outputS2.txt", "r") as file:
    data = file.readlines()


results_dict = {}
for line in data:
    if "Open" in line: 
        line = line.replace("Open ", "")  
        ip, port_info = line.split(":", 1)
        ports = port_info.strip()
        ip = ip.strip()

        if ip not in results_dict:
            results_dict[ip] = []
        results_dict[ip].append(ports)


results = [{"IP Address": ip, "Open Ports": ", ".join(ports)} for ip, ports in results_dict.items()]

df = pd.DataFrame(results)


df.to_excel("rustscan_results.xlsx", index=False)

print("Results saved to rustscan_results.xlsx")
