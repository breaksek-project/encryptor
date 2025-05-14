import os
import time
import base64
import marshal
import zlib
import platform
import datetime
from random import randint
from rich.panel import Panel
from rich import print as tulis
from rich import print

Hitam = "\u001b[30m"
Merah = "\u001b[31m"
Hijau = "\u001b[32m"
Kuning = "\u001b[33m"
Orange = "\u001b[38;5;208m"
Biru = "\u001b[34m"
Biru_muda = "\u001b[36m"
Pink = "\u001b[38;5;205m"
Violet = "\u001b[35m"
Abu = "\u001b[90m"
Orange_muda = "\u001b[38;5;214m"
Putih = "\u001b[37m"

Z2 = "[#000000]"  # Hitam
M2 = "[#FF0000]"  # Merah
H2 = "[#00FF00]"  # Hijau
K2 = "[#FFFF00]"  # Kuning
B2 = "[#00C8FF]"  # Biru
U2 = "[#AF00FF]"  # Ungu
N2 = "[#FF00FF]"  # Pink
O2 = "[#00FFFF]"  # Biru Muda
P2 = "[#FFFFFF]"  # Putih
J2 = "[#FF8F00]"  # Jingga
A2 = "[#AAAAAA]"  # Abu-Abu
T2 = "[#FFA500]"  # Oranye

class ____LambdaObfuscators____:
    def __init__(self):
        current_time = datetime.datetime.now()
        self.mzb = f"""#     *copyright: (C) © 2023 ~ breaksek
# Time : {current_time}
# Platform : {platform.platform()}
# Obfuscated by : breaksek

Kontolivo=(eval((lambda ____,__,_ : ____.join([_(___) for ___ in __]))('',[95, 95, 105, 109, 112, 111, 114, 116, 95, 95, 40, 39, 109, 97, 114, 115, 104, 97, 108, 39, 41, 46, 108, 111, 97, 100, 115],chr))(eval((lambda ____,__,_ : ____.join([_(___) for ___ in __]))('',[95, 95, 105, 109, 112, 111, 114, 116, 95, 95, 40, 34, 122, 108, 105, 98, 34, 41, 46, 100, 101, 99, 111, 109, 112, 114, 101, 115, 115],chr))(eval((lambda ____,__,_ : ____.join([_(___) for ___ in __]))('',[95, 95, 105, 109, 112, 111, 114, 116, 95, 95, 40, 34, 98, 97, 115, 101, 54, 52, 34, 41, 46, 98, 54, 52, 100, 101, 99, 111, 100, 101],chr))(%s))));exec(Kontolivo)"""

    def encrypt_file(self, input_file, output_file, count):
        try:
            xos = open(input_file, 'rb').read()
            xxx = compile(xos, '<Ryougaacoli>', 'exec')
            cum = repr(base64.b64encode(zlib.compress(marshal.dumps(xxx))))

            with open(output_file, 'w') as f:
                f.write(self.mzb % cum)

            for komter in range(count):
                sui = open(output_file, 'rb').read()
                sux = compile(sui, '<Ryougaacoli>', 'exec')
                ses = repr(base64.b64encode(zlib.compress(marshal.dumps(sux))))

                with open(output_file, 'w') as f:
                    f.write(self.mzb % ses)

                print(f"{P2}└──>{B2}[{A2}+{B2}]{P2}Compile ke {A2}: {T2}{komter}")
                time.sleep(1)

            print(f"\n{H2}[{A2}!!{H2}]{P2} Berhasil, File tersimpan di {A2}: {output_file}")
            exit()
        except Exception as e:
            print(f"{M2}[{A2}•{M2}]{P2} Error : {P2}\n└──>{M2}[{A2}•{M2}] {P2}Isi Yang Benar {M2}!")

if __name__ == "__main__":
    encryptor = ____LambdaObfuscators____()
    os.system("clear")
    tulis(Panel("""[#00BFFF]                                                        _   _                         _____    
                           ___ _ __   ___   _ __  _   _| |_| |__   ___  _ __   __   _|___ /    
                          / _ \ '_ \ / __| | '_ \| | | | __| '_ \ / _ \| '_ \  \ \ / / |_ \    
                         |  __/ | | | (__  | |_) | |_| | |_| | | | (_) | | | |  \ V / ___) |   
                          \___|_| |_|\___| | .__/ \__, |\__|_| |_|\___/|_| |_|   \_/ |____/    
                                           |_|    |___/                                        
        """, title='[#FF8F00][ [#00FF33]By breaksek [#FF8F00]]',
        subtitle='[#FF8F00][ [#00FF33]Obfuscate Your Python3 File [#FF8F00]]', style='#FFFFFF'))
    input_file = input(f"└──>{Hijau}[{Abu}•{Hijau}]{Putih} Input File Name{Abu} : {Putih}")
    count = int(input(f"     └──>{Biru}[{Abu}+{Biru}]{Putih} Count {Orange_muda}({Putih}Ex{Orange_muda}) •4• : {Putih}"))
    
    if count < 300:
        output_file = input(f"     └──>{Hijau}[{Abu}•{Hijau}]{Putih} Output File {Abu}: {Putih}")
        encryptor.encrypt_file(input_file, output_file, count)
    else:
        print(f"{B2}[{A2}!{B2}]{P2} Count must be < 300")
