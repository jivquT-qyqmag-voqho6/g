<div align="center">

# Chris
### Unlock the fullest potential of your device

**The next evolution of iOS device customization.**  
More tweaks. More control. Better design.

![Platform](https://img.shields.io/badge/platform-macOS%20%7C%20Windows%20%7C%20Linux-blueviolet?style=flat-square)
![iOS](https://img.shields.io/badge/iOS-17.0%20–%2026.x-blueviolet?style=flat-square)
![Python](https://img.shields.io/badge/python-3.9+-blueviolet?style=flat-square)
![License](https://img.shields.io/badge/license-MIT-blueviolet?style=flat-square)

</div>

---

## What is Chris?

Chris is an open-source iOS customization tool that lets you unlock hidden features, customize your device's UI, and disable background daemons — all without a jailbreak.

It uses the **SparseRestore** exploit (iOS 17.0–18.1.1) and **BookRestore** (iOS 18.2–26.x) to write to protected system files on your device.

> ⚠️ **Back up your device before using Chris.** We are not responsible for any issues that arise.

---

## ✨ Features

### 🔮 Hidden iOS Features (MobileGestalt)
Unlock features Apple gated off by device model:

| Feature | iOS Range |
|---|---|
| Dynamic Island on any device | 17.0 – 18.1.1 |
| Always-On Display on any device | 18.0 – 18.1.1 |
| Apple Intelligence (AI Enabler) | 18.1 – 18.1.1 |
| ProMotion 120Hz on non-Pro devices ⭐ | 17.0 – 18.1.1 |
| Spatial Audio on all devices ⭐ | 17.0+ |
| Emergency SOS via Satellite ⭐ | 17.0 – 18.1.1 |
| USB 3 Speed on Lightning/USB-C ⭐ | 17.0 – 18.1.1 |
| Boot Chime | 17.0 – 18.1.1 |
| Charge Limit | 17.0 – 18.1.1 |
| Disable Wallpaper Parallax | 17.0 – 18.1.1 |
| Collision SOS | 17.0 – 18.1.1 |
| Stage Manager | 17.0 – 18.1.1 |
| Force Solarium Fallback (Liquid Glass) | 26.0+ |
| Suppress Dynamic Island | 26.2+ |

> ⭐ = Chris-exclusive feature

### 📶 Status Bar
- Change carrier name, battery %, WiFi/cell bars
- Override clock text, date text (iPad), breadcrumb
- Hide any status bar icon
- **Custom battery text** ⭐
- **Hide clock entirely** ⭐
- **Operator logo** ⭐

### 🖥 Springboard & System
- Lock screen footnote, auto-lock time, supervision text
- Disable screen dimming while charging
- Disable low battery alerts
- AirDrop time limit removal
- **Hide dock, home bar, app icon labels** ⭐
- **Custom wallpaper blur level** ⭐
- **Force notification grouping** ⭐
- **Never drop WiFi on sleep** ⭐
- **Custom shutdown message** ⭐

### 🔇 Disable Daemons (26 total)
Kill background processes to improve battery and privacy:

| Daemon | What it stops |
|---|---|
| OTAd | Automatic update downloads |
| UsageTrackingAgent | Apple analytics |
| Game Center | Game Center services |
| Screen Time | Screen Time monitoring |
| Spotlight | Search indexing |
| iCloud | Background iCloud sync |
| Siri ⭐ | All Siri services |
| Find My Friends ⭐ | Location sharing |
| Ad Services ⭐ | Apple advertising |
| Siri Suggestions ⭐ | Proactive suggestions |
| Maps Background ⭐ | Maps update daemon |
| + 15 more... | |

### ⚙️ Internal & Debug
- Build version in status bar
- Metal GPU HUD
- iPad keyboard on iPhone
- Force Dark Mode ⭐
- UI animation speed multiplier ⭐
- Force system-wide dark mode ⭐

---

## 📦 Installation

### Requirements

**Windows**
- [Apple Devices (Microsoft Store)](https://apps.microsoft.com/detail/9np83lwlpz9k) or [iTunes (Apple)](https://support.apple.com/en-us/106372)

**Linux**
- `usbmuxd` and `libimobiledevice`

**All Platforms**
- Python 3.9+
- See `requirements.txt`

### Setup

```bash
git clone https://github.com/your-username/chris
cd chris

# Create virtual environment (recommended)
python3 -m venv .env
source .env/bin/activate      # macOS/Linux
# .env\Scripts\activate.bat   # Windows

# Install dependencies
pip install -r requirements.txt

# Run Chris
python3 main_app.py
```

---

## 📱 Getting Your MobileGestalt File

Required for iOS 26.1 and below:

1. Install [Shortcuts](https://apps.apple.com/us/app/shortcuts/id915249334) on your iPhone
2. Download: [Save MobileGestalt](https://www.icloud.com/shortcuts/66bd3c822a0145b98d46cd1c9077e6e5)
3. Run the shortcut and share the file to your computer
4. Load it in Chris using the **Browse…** button

---

## 🔧 How It Works

Chris uses two exploit methods depending on your iOS version:

- **SparseRestore** (iOS 17.0–18.1.1) — writes files outside the intended restore location via MobileBackup2
- **BookRestore** (iOS 18.2–26.x) — uses the bl_sbx exploit to achieve the same result on newer iOS

Both methods require no jailbreak and work over USB.

---

## 🤝 Credits

Chris is built on the shoulders of giants:

- [leminlimez/Nugget](https://github.com/leminlimez/Nugget) — the original inspiration
- [JJTech](https://github.com/JJTech0130) — SparseRestore / TrollRestore
- [Duy Tran](https://github.com/khanhduytran0) & [Huy Nguyen](https://x.com/Little_34306) — BookRestore / bl_sbx
- [pymobiledevice3](https://github.com/doronz88/pymobiledevice3) — device communication
- [PySide6](https://doc.qt.io/qtforpython-6/) — GUI framework

---

## 📄 License

MIT — fork it, build on it, make it yours.
