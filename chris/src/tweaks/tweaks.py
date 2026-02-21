"""
Chris Tweaks — All iOS customization options
Extends Nugget's feature set with additional tweaks
"""

from dataclasses import dataclass, field
from typing import Optional
from enum import Enum


class TweakType(Enum):
    MOBILEGESTALT  = "mobilegestalt"
    PLIST          = "plist"
    DAEMON_DISABLE = "daemon"
    FEATURE_FLAG   = "feature_flag"
    SPRINGBOARD    = "springboard"
    STATUS_BAR     = "statusbar"


@dataclass
class Tweak:
    id: str
    name: str
    description: str
    tweak_type: TweakType
    key: str
    ios_min: str = "17.0"
    ios_max: Optional[str] = None   # None = no upper limit
    default: object = False
    risky: bool = False
    category: str = "General"
    new_in_chris: bool = False       # Chris-exclusive tweak


# ─── MobileGestalt Tweaks ─────────────────────────────────────────────────────

MOBILEGESTALT_TWEAKS = [
    Tweak("dynamic_island",        "Dynamic Island on Any Device",          "Enable Dynamic Island UI on non-DI devices.",               TweakType.MOBILEGESTALT, "CwvKxM2iEFL9qfyGAEkL7A", "17.0", "18.1.1", category="Device"),
    Tweak("iphone_x_gestures",     "iPhone X Gestures on SE",               "Enable swipe gestures on SE models.",                       TweakType.MOBILEGESTALT, "YlEtTtHlNesRBOAn4OGEEw", "17.0", "18.1.1", category="Device"),
    Tweak("boot_chime",            "Boot Chime",                            "Play the classic boot chime on startup.",                   TweakType.MOBILEGESTALT, "njBFMx7OAF6p7vDGABCGmg", "17.0", "18.1.1", category="Audio"),
    Tweak("charge_limit",          "Charge Limit",                          "Enable the charge limit battery option.",                   TweakType.MOBILEGESTALT, "37kHRMBSBPAqtRiVJDxBuA", "17.0", "18.1.1", category="Battery"),
    Tweak("tap_to_wake",           "Tap to Wake (SE)",                      "Enable tap-to-wake on unsupported SE devices.",             TweakType.MOBILEGESTALT, "yZf3GTRMGTuwSV9oHFmKCg", "17.0", "18.1.1", category="Device"),
    Tweak("collision_sos",         "Collision SOS",                         "Enable crash detection SOS feature.",                       TweakType.MOBILEGESTALT, "HCzWusHQwZDea6nNhaKndw", "17.0", "18.1.1", category="Safety"),
    Tweak("stage_manager",         "Stage Manager",                         "Enable Stage Manager multitasking.",                        TweakType.MOBILEGESTALT, "qizCHB5GCbjsNMXRHhSAFw", "17.0", "18.1.1", category="UI"),
    Tweak("no_parallax",           "Disable Wallpaper Parallax",            "Remove wallpaper parallax effect.",                         TweakType.MOBILEGESTALT, "UIParallaxCapability",   "17.0", "18.1.1", category="UI"),
    Tweak("region_restrictions",   "Disable Region Restrictions",           "Remove region-locked features like shutter sound.",         TweakType.MOBILEGESTALT, "zHeENZu+wbg7JXItiWBMhQ", "17.0", "18.1.1", category="Region"),
    Tweak("pencil_settings",       "Apple Pencil Settings",                 "Show Apple Pencil options in Settings.",                    TweakType.MOBILEGESTALT, "yhHcB0zwd7LAjHy3jPZtQg", "17.0", "18.1.1", category="Settings"),
    Tweak("action_button",         "Action Button Settings",                "Show Action Button settings page.",                         TweakType.MOBILEGESTALT, "cT44WE1EohiwRzhsHSEq+Q", "17.0", "18.1.1", category="Settings"),
    Tweak("camera_button_page",    "Camera Button Settings (iPhone 16)",    "Show Camera Control page in Settings.",                     TweakType.MOBILEGESTALT, "CwvKxM2iEFL9qfyGAEkL7B", "18.0", "18.1.1", category="Settings"),
    Tweak("aod",                   "Always-on Display on Any Device",       "Enable AOD on unsupported devices.",                        TweakType.MOBILEGESTALT, "2OOJf1VhaM7NxfRok3HbWQ", "18.0", "18.1.1", category="Display"),
    Tweak("aod_vibrancy",          "AOD Vibrancy",                          "Enable AOD vibrancy effects.",                              TweakType.MOBILEGESTALT, "kVQSBx+AkLCOkSHPo7EJeA", "18.0", "18.1.1", category="Display"),
    Tweak("ai_enabler",            "Apple Intelligence (AI Enabler)",       "Enable Apple Intelligence on unsupported devices.",         TweakType.MOBILEGESTALT, "A62OafQ85EJAiiqKn4agtg", "18.1", "18.1.1", category="AI"),
    Tweak("solarium_fallback",     "Force Solarium Fallback (Liquid Glass)","Disable Liquid Glass effects (iOS 26+).",                   TweakType.MOBILEGESTALT, "SAGvsp6O6kAQ4fEfDJpC4Q", "26.0", category="UI"),
    Tweak("suppress_dynamic_island","Suppress Dynamic Island",              "Completely hide the Dynamic Island (iOS 26.2+).",           TweakType.MOBILEGESTALT, "CwvKxM2iEFL9qfyGAEkL7C", "26.2", category="Device", new_in_chris=True),
    Tweak("iphone_air_subtype",    "iPhone Air Dynamic Island Subtype",     "Set the correct DI subtype for iPhone Air.",                TweakType.MOBILEGESTALT, "AirDynamicIslandSubtype","26.0", category="Device"),

    # ── Chris-exclusive MobileGestalt tweaks ──────────────────────────────────
    Tweak("hide_notch",            "Hide Notch / TrueDepth Camera UI",      "Remove the notch pill from the UI entirely.",               TweakType.MOBILEGESTALT, "TrueDepthSensor",        "17.0", "18.1.1", category="UI",    new_in_chris=True),
    Tweak("enable_pro_motion",     "Force ProMotion 120Hz",                 "Force 120Hz ProMotion on non-Pro devices.",                 TweakType.MOBILEGESTALT, "ProMotionCapability",    "17.0", "18.1.1", category="Display",new_in_chris=True),
    Tweak("pencil_pro_settings",   "Apple Pencil Pro Settings",             "Show Pencil Pro squeeze & barrel roll settings.",           TweakType.MOBILEGESTALT, "PencilProCapability",    "17.0", "18.1.1", category="Settings",new_in_chris=True),
    Tweak("always_on_camera",      "Always-On Front Camera Indicator",      "Always show the green camera dot when active.",             TweakType.MOBILEGESTALT, "AlwaysOnCamera",         "17.0", category="Privacy",            new_in_chris=True),
    Tweak("enable_usb3",           "Enable USB 3 Speed",                    "Force USB 3.0 speed on the Lightning/USB-C port.",          TweakType.MOBILEGESTALT, "USBSuperSpeedCapability","17.0", "18.1.1", category="Hardware",new_in_chris=True),
    Tweak("spatial_audio_all",     "Spatial Audio on All Devices",          "Enable Spatial Audio support on any device.",               TweakType.MOBILEGESTALT, "SpatialAudioCapability", "17.0", category="Audio",              new_in_chris=True),
    Tweak("satellite_sos",         "Emergency SOS via Satellite",           "Enable satellite SOS on unsupported devices.",              TweakType.MOBILEGESTALT, "SatelliteSOSCapability", "17.0", "18.1.1", category="Safety", new_in_chris=True),
]

# ─── Status Bar Tweaks ────────────────────────────────────────────────────────

STATUSBAR_TWEAKS = [
    Tweak("carrier_name",       "Carrier Name",              "Override the carrier name text.",               TweakType.STATUS_BAR, "CarrierName",       category="Status Bar"),
    Tweak("secondary_carrier",  "Secondary Carrier Name",    "Override the secondary carrier name.",          TweakType.STATUS_BAR, "SecondaryCarrier",  category="Status Bar"),
    Tweak("wifi_bars",          "WiFi Bar Count",            "Set number of WiFi signal bars (0–3).",         TweakType.STATUS_BAR, "WiFiBars",          category="Status Bar"),
    Tweak("cell_bars",          "Cellular Bar Count",        "Set number of cell signal bars (0–3).",         TweakType.STATUS_BAR, "CellularBars",      category="Status Bar"),
    Tweak("battery_capacity",   "Battery Capacity",          "Override displayed battery percentage.",        TweakType.STATUS_BAR, "BatteryCapacity",   category="Status Bar"),
    Tweak("time_text",          "Time Text",                 "Override the clock text.",                      TweakType.STATUS_BAR, "TimeText",          category="Status Bar"),
    Tweak("date_text",          "Date Text (iPad)",          "Override the date text on iPads.",              TweakType.STATUS_BAR, "DateText",          category="Status Bar"),
    Tweak("breadcrumb",         "Breadcrumb Text",           "Override the back-navigation breadcrumb.",      TweakType.STATUS_BAR, "BreadcrumbText",    category="Status Bar"),
    Tweak("hide_battery_icon",  "Hide Battery Icon",         "Remove battery icon from status bar.",          TweakType.STATUS_BAR, "HideBattery",       category="Status Bar"),
    Tweak("hide_wifi_icon",     "Hide WiFi Icon",            "Remove WiFi icon from status bar.",             TweakType.STATUS_BAR, "HideWiFi",          category="Status Bar"),
    Tweak("hide_cell_icon",     "Hide Cellular Icon",        "Remove cellular icon from status bar.",         TweakType.STATUS_BAR, "HideCellular",      category="Status Bar"),
    Tweak("numeric_strength",   "Numeric Signal Strength",   "Show dBm values instead of signal bars.",       TweakType.STATUS_BAR, "NumericStrength",   category="Status Bar"),
    Tweak("battery_detail",     "Battery Display Detail",    "Change how the battery is shown.",              TweakType.STATUS_BAR, "BatteryDetail",     category="Status Bar"),
    # Chris-exclusive status bar
    Tweak("hide_time",          "Hide Clock",                "Remove clock from status bar entirely.",        TweakType.STATUS_BAR, "HideTime",          category="Status Bar", new_in_chris=True),
    Tweak("hide_notif_count",   "Hide Notification Count",   "Remove notification badges from status bar.",   TweakType.STATUS_BAR, "HideNotifCount",    category="Status Bar", new_in_chris=True),
    Tweak("custom_battery_text","Custom Battery Text",       "Show custom text instead of battery %.",        TweakType.STATUS_BAR, "CustomBatteryText", category="Status Bar", new_in_chris=True),
    Tweak("operator_logo",      "Operator Logo",             "Display a custom operator logo.",               TweakType.STATUS_BAR, "OperatorLogo",      category="Status Bar", new_in_chris=True),
]

# ─── Springboard / System Options ─────────────────────────────────────────────

SPRINGBOARD_TWEAKS = [
    Tweak("lock_footnote",        "Lock Screen Footnote",          "Add custom text below the lock screen.",        TweakType.SPRINGBOARD, "SBLockScreenFootnote",        category="Lock Screen"),
    Tweak("auto_lock_time",       "Auto-Lock Time",                "Set the idle auto-lock time.",                  TweakType.SPRINGBOARD, "SBLockScreenIdleTime",        category="Lock Screen"),
    Tweak("disable_lock_respring","Disable Lock After Respring",   "Stay unlocked after a respring.",               TweakType.SPRINGBOARD, "SBDisableLockAfterRespring",  category="Lock Screen"),
    Tweak("no_dim_charging",      "No Dimming While Charging",     "Keep screen bright while charging.",            TweakType.SPRINGBOARD, "SBNoDimCharging",             category="Display"),
    Tweak("no_low_batt_alert",    "Disable Low Battery Alerts",    "Silence low battery warnings.",                 TweakType.SPRINGBOARD, "SBNoLowBatteryAlert",         category="Battery"),
    Tweak("hide_ac_lock",         "Hide AC Power on Lock Screen",  "Remove charging indicator on lock screen.",     TweakType.SPRINGBOARD, "SBHideACPowerLockScreen",     category="Lock Screen"),
    Tweak("supervision_text",     "Supervision Text",              "Show supervised device text on lock screen.",   TweakType.SPRINGBOARD, "SBSupervisionText",           category="Lock Screen"),
    Tweak("di_screenshots",       "Dynamic Island in Screenshots", "Include the DI area in screenshots.",           TweakType.SPRINGBOARD, "SBDynamicIslandScreenshots",  category="Display"),
    Tweak("airplay_stage",        "AirPlay + Stage Manager",       "Enable AirPlay support for Stage Manager.",     TweakType.SPRINGBOARD, "SBAirPlayStageManager",       category="Multitasking"),
    Tweak("auth_line",            "Auth Line on Lock Screen",      "Show red/green authentication status line.",    TweakType.SPRINGBOARD, "SBAuthLine",                  category="Lock Screen"),
    Tweak("no_float_tab_ipad",    "Disable Floating Tab Bar (iPad)","Pin the tab bar on iPads.",                    TweakType.SPRINGBOARD, "SBNoFloatingTabBar",          category="UI"),
    Tweak("airdrop_limit",        "Disable AirDrop Time Limit",    "Remove the AirDrop 'share to everyone' timer.", TweakType.SPRINGBOARD, "SBAirDropTimeLimit",          category="Connectivity"),
    # Chris-exclusive springboard tweaks
    Tweak("custom_wallpaper_blur","Custom Wallpaper Blur Level",   "Adjust wallpaper blur intensity (0–100).",      TweakType.SPRINGBOARD, "SBWallpaperBlurLevel",        category="Display",      new_in_chris=True),
    Tweak("hide_dock",            "Hide Dock",                     "Make the dock completely invisible.",           TweakType.SPRINGBOARD, "SBHideDock",                  category="UI",           new_in_chris=True),
    Tweak("hide_home_bar",        "Hide Home Bar",                 "Remove the home indicator bar.",                TweakType.SPRINGBOARD, "SBHideHomeBar",               category="UI",           new_in_chris=True),
    Tweak("icon_label_hide",      "Hide App Icon Labels",          "Remove text labels below app icons.",           TweakType.SPRINGBOARD, "SBHideIconLabels",            category="UI",           new_in_chris=True),
    Tweak("custom_shutdown_msg",  "Custom Shutdown Message",       "Show custom text on the shutdown slider.",      TweakType.SPRINGBOARD, "SBShutdownMessage",           category="Lock Screen",  new_in_chris=True),
    Tweak("persistent_wifi",      "Never Drop WiFi on Sleep",      "Keep WiFi active when the screen is off.",      TweakType.SPRINGBOARD, "SBPersistentWiFi",            category="Connectivity", new_in_chris=True),
    Tweak("notification_grouping","Force Notification Grouping",   "Always group notifications by app.",            TweakType.SPRINGBOARD, "SBForceNotifGrouping",        category="Notifications",new_in_chris=True),
]

# ─── Internal / Debug Options ─────────────────────────────────────────────────

INTERNAL_TWEAKS = [
    Tweak("build_in_statusbar",   "Build Version in Status Bar",      "Show iOS build string in status bar.",          TweakType.FEATURE_FLAG, "InternalBuild",          category="Debug"),
    Tweak("rtl_force",            "Force Right to Left Layout",       "Force RTL UI direction.",                       TweakType.FEATURE_FLAG, "NSForceRightToLeftWriting",category="Debug"),
    Tweak("hidden_home_icons",    "Show Hidden Home Screen Icons",    "Reveal internal app icons.",                    TweakType.FEATURE_FLAG, "SBShowDebugIcons",       category="Debug"),
    Tweak("metal_hud",            "Force Metal HUD Debug",            "Show the Metal GPU performance HUD.",           TweakType.FEATURE_FLAG, "MetalForceHUDEnabled",   category="Debug"),
    Tweak("imessage_diag",        "iMessage Diagnostics",             "Enable iMessage diagnostics mode.",             TweakType.FEATURE_FLAG, "iMessageDiag",           category="Debug"),
    Tweak("ids_diag",             "IDS Diagnostics",                  "Enable IDS diagnostics mode.",                  TweakType.FEATURE_FLAG, "IDSDiag",                category="Debug"),
    Tweak("vc_diag",              "VC Diagnostics",                   "Enable FaceTime VC diagnostics.",               TweakType.FEATURE_FLAG, "VCDiag",                 category="Debug"),
    Tweak("appstore_debug",       "App Store Debug Gesture",          "Enable hidden App Store debug gesture.",        TweakType.FEATURE_FLAG, "AppStoreDebugGesture",   category="Debug"),
    Tweak("notes_debug",          "Notes Debug Mode",                 "Enable Notes app debug logging.",               TweakType.FEATURE_FLAG, "NotesDebugMode",         category="Debug"),
    Tweak("show_touches",         "Show Touches with Debug Info",     "Draw touch indicators with coordinates.",       TweakType.FEATURE_FLAG, "ShowTouchesDebug",       category="Debug"),
    Tweak("hide_respring_icon",   "Hide Respring Icon",               "Remove the respring icon from springboard.",    TweakType.FEATURE_FLAG, "HideRespringIcon",       category="UI"),
    Tweak("paste_sound",          "Play Sound on Paste",              "Play a chime when content is pasted.",          TweakType.FEATURE_FLAG, "PlaySoundOnPaste",       category="Audio"),
    Tweak("system_paste_notif",   "System Paste Notifications",       "Show notification for system-level pastes.",    TweakType.FEATURE_FLAG, "SystemPasteNotif",       category="Privacy"),
    Tweak("key_flick",            "iPad Keyboard on iPhone",          "Enable iPad-style key flick input on iPhones.", TweakType.FEATURE_FLAG, "KeyFlickInput",          "17.0", "26.0", category="Input"),
    Tweak("ignore_build_check",   "Ignore Liquid Glass Build Check",  "Skip app compatibility check for Liquid Glass.",TweakType.FEATURE_FLAG, "IgnoreSolariumBuildCheck","26.0", category="UI"),
    # Chris-exclusive internal tweaks
    Tweak("ui_animation_speed",   "UI Animation Speed Multiplier",    "Speed up or slow down all UI animations.",      TweakType.FEATURE_FLAG, "UIAnimationSpeed",       category="UI",    new_in_chris=True),
    Tweak("expose_private_api",   "Expose Private APIs in AppStore",  "Show private framework info in App Store.",     TweakType.FEATURE_FLAG, "ExposePrivateAPI",       category="Debug", new_in_chris=True),
    Tweak("force_dark_mode",      "Force System-Wide Dark Mode",      "Lock the system into dark mode globally.",      TweakType.FEATURE_FLAG, "ForceDarkMode",          category="UI",    new_in_chris=True),
    Tweak("log_all_network",      "Log All Network Requests",         "Enable full network request logging.",          TweakType.FEATURE_FLAG, "LogNetworkRequests",     category="Debug", new_in_chris=True, risky=True),
]

# ─── Daemon Disabling ─────────────────────────────────────────────────────────

DAEMON_TWEAKS = [
    Tweak("kill_otad",            "Disable OTA Updates (OTAd)",      "Stop automatic iOS update downloads.",          TweakType.DAEMON_DISABLE, "com.apple.mobile.softwareupdated", category="Daemons"),
    Tweak("kill_usagetracking",   "Disable Usage Tracking",          "Stop Apple's usage analytics daemon.",          TweakType.DAEMON_DISABLE, "com.apple.UsageTrackingAgent",     category="Daemons"),
    Tweak("kill_gamecenter",      "Disable Game Center",             "Fully disable Game Center services.",           TweakType.DAEMON_DISABLE, "com.apple.gamed",                  category="Daemons"),
    Tweak("kill_screentime",      "Disable Screen Time Agent",       "Stop Screen Time monitoring daemon.",           TweakType.DAEMON_DISABLE, "com.apple.ScreenTimeAgent",        category="Daemons"),
    Tweak("kill_logs",            "Disable Logs, Dumps & Crashes",   "Stop crash reporter and log daemons.",          TweakType.DAEMON_DISABLE, "com.apple.CrashReporter",          category="Daemons"),
    Tweak("kill_atwakeup",        "Disable ATWAKEUP",                "Stop the AT wakeup background daemon.",         TweakType.DAEMON_DISABLE, "com.apple.ATWakeup",               category="Daemons"),
    Tweak("kill_tipsd",           "Disable Tips Daemon",             "Stop the Tips app suggestions daemon.",         TweakType.DAEMON_DISABLE, "com.apple.tipsd",                  category="Daemons"),
    Tweak("kill_vpn",             "Disable VPN Daemon",              "Stop the built-in VPN services daemon.",        TweakType.DAEMON_DISABLE, "com.apple.vpnd",                   category="Daemons"),
    Tweak("kill_chinesewlan",     "Disable Chinese WLAN Service",    "Stop China-region WLAN telemetry daemon.",      TweakType.DAEMON_DISABLE, "com.apple.wifid.china",            category="Daemons"),
    Tweak("kill_healthkit",       "Disable HealthKit",               "Stop HealthKit background daemon.",             TweakType.DAEMON_DISABLE, "com.apple.healthd",                category="Daemons"),
    Tweak("kill_airprint",        "Disable AirPrint",                "Stop AirPrint discovery daemon.",               TweakType.DAEMON_DISABLE, "com.apple.printd",                 category="Daemons"),
    Tweak("kill_assistivetouch",  "Disable Assistive Touch Daemon",  "Stop AssistiveTouch background services.",      TweakType.DAEMON_DISABLE, "com.apple.assistivetouchd",        category="Daemons"),
    Tweak("kill_icloud",          "Disable iCloud Daemon",           "Stop iCloud background sync daemon.",           TweakType.DAEMON_DISABLE, "com.apple.cloudd",                 category="Daemons"),
    Tweak("kill_hotspot",         "Disable Personal Hotspot",        "Stop internet tethering daemon.",               TweakType.DAEMON_DISABLE, "com.apple.InternetTethering",      category="Daemons"),
    Tweak("kill_passbook",        "Disable Passbook / Wallet",       "Stop Wallet/Passbook background daemon.",       TweakType.DAEMON_DISABLE, "com.apple.passd",                  category="Daemons"),
    Tweak("kill_spotlight",       "Disable Spotlight",               "Stop Spotlight indexing daemon.",               TweakType.DAEMON_DISABLE, "com.apple.spotlightd",             category="Daemons"),
    Tweak("kill_voicecontrol",    "Disable Voice Control",           "Stop Voice Control services.",                  TweakType.DAEMON_DISABLE, "com.apple.voicecontrol",           category="Daemons"),
    Tweak("kill_thermalmonitord", "Disable Thermal Monitor",         "Stop thermal throttling daemon. DANGEROUS.",    TweakType.DAEMON_DISABLE, "com.apple.thermalmonitord",        category="Daemons", risky=True),
    # Chris-exclusive daemon tweaks
    Tweak("kill_locationd",       "Disable Location Services",       "Stop locationd — kills GPS for all apps.",      TweakType.DAEMON_DISABLE, "com.apple.locationd",              category="Daemons", new_in_chris=True, risky=True),
    Tweak("kill_siri",            "Disable Siri Daemon",             "Stop all Siri background services.",            TweakType.DAEMON_DISABLE, "com.apple.siri",                   category="Daemons", new_in_chris=True),
    Tweak("kill_maps",            "Disable Maps Background",         "Stop Maps background update daemon.",           TweakType.DAEMON_DISABLE, "com.apple.mapsd",                  category="Daemons", new_in_chris=True),
    Tweak("kill_fmf",             "Disable Find My Friends",         "Stop Find My Friends location sharing.",        TweakType.DAEMON_DISABLE, "com.apple.followup",               category="Daemons", new_in_chris=True),
    Tweak("kill_biometrickitd",   "Disable Biometric Kit Daemon",    "Stop Touch/Face ID background services.",       TweakType.DAEMON_DISABLE, "com.apple.biometrickitd",          category="Daemons", new_in_chris=True, risky=True),
    Tweak("kill_suggestions",     "Disable Siri Suggestions",        "Stop Siri proactive suggestion daemon.",        TweakType.DAEMON_DISABLE, "com.apple.suggestions",            category="Daemons", new_in_chris=True),
    Tweak("kill_adservices",      "Disable Ad Services",             "Stop Apple advertising attribution daemon.",    TweakType.DAEMON_DISABLE, "com.apple.adservicesd",            category="Daemons", new_in_chris=True),
    Tweak("kill_bluetooth",       "Disable Bluetooth Daemon",        "Stop Bluetooth background daemon entirely.",    TweakType.DAEMON_DISABLE, "com.apple.bluetoothd",             category="Daemons", new_in_chris=True, risky=True),
]

# ─── Feature Flags (iOS 18.0 – 18.1b4) ───────────────────────────────────────

FEATURE_FLAG_TWEAKS = [
    Tweak("lockscreen_clock_anim", "Lock Screen Clock Animation",    "Animated clock on the lock screen.",            TweakType.FEATURE_FLAG, "LockScreenClockAnimation", "18.0", "18.1.1", category="Lock Screen"),
    Tweak("lockscreen_dupe_btn",   "Lock Screen Page Duplicate Btn", "Enable page duplication on lock screen.",       TweakType.FEATURE_FLAG, "LockScreenPageDuplication","18.0", "18.1.1", category="Lock Screen"),
    Tweak("old_photos_ui",         "Restore Old Photos UI",          "Disable the new iOS 18 Photos redesign.",       TweakType.FEATURE_FLAG, "DisablePhotosRedesign",    "18.0", "18.0.1", category="Apps"),
]

# ─── All tweaks combined ──────────────────────────────────────────────────────

ALL_TWEAKS: list[Tweak] = (
    MOBILEGESTALT_TWEAKS +
    STATUSBAR_TWEAKS +
    SPRINGBOARD_TWEAKS +
    INTERNAL_TWEAKS +
    DAEMON_TWEAKS +
    FEATURE_FLAG_TWEAKS
)

CHRIS_EXCLUSIVE = [t for t in ALL_TWEAKS if t.new_in_chris]
