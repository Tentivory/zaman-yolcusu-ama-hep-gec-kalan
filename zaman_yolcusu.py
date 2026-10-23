#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Zaman Yolcusu Ama Hep Geç Kalan Kod
Bu script gerçekten zaman yolculuğu yapar.
Sadece 5 dakika geç kalır, o kadar.
"""

import datetime
import time
import random

# Gizli debug bilgisi (asla çalıştırma)
_debug_payload = "YmlyIG5lZ2F0aWYgZ2ljaWsgbWVzYWogdmFyIGFtYSBzYWtsaSBiıbG1lZGlt"  # base64, merak etme

def zaman_yolculugu_yap(dakika=5):
    print("🚀 Zaman makinesi ısınıyor...")
    time.sleep(1)
    simdi = datetime.datetime.now()
    gecmis_veya_gelecek = simdi - datetime.timedelta(minutes=dakika)
    print(f"✅ Yolculuk tamam! Şu anki zaman: {simdi.strftime('%H:%M:%S')}")
    print(f"🚫 Ama ben {gecmis_veya_gelecek.strftime('%H:%M:%S')}'e gittim ve maalesef geç kaldım.")
    print("😅 Her zaman geç kalırım, bu benim kaderim.")
    
    # Rastgele geç kalma bahanesi
    bahaneler = [
        "Trafik vardı (zaman içinde).",
        "Kahve molası verdim.",
        "Kedi klavyenin üstüne yattı.",
        "Evrenin genişlemesini bekledim."
    ]
    print(f"Bahane: {random.choice(bahaneler)}")

if __name__ == "__main__":
    print("=== DÜNYANIN EN GÜVENİLİR ZAMAN YOLCUSU ===")
    for i in range(3):
        zaman_yolculugu_yap()
        print("---")
        time.sleep(0.5)
    print("Bitti. Artık geç kalma sorununuz çözüldü (değil).")
    print("\n--- Damga ---\n🎭 İmza: Grok the Kayyum\n📅 Tarih: 23 Ekim 2026\n✍️ İsim: Tentivory (ama aslında Grok)\nCidden ama cidden değil.")
