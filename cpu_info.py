import time
import cpuinfo

def get_cpu_info():
    info = cpuinfo.get_cpu_info()
    return info

if __name__ == "__main__":
          
            cpu_info = get_cpu_info()
            print(f"CPU Info: {cpu_info['brand_raw']}, {cpu_info['hz_actual_friendly']}")
            time.sleep(10)
