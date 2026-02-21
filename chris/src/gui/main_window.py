"""
Chris — Main GUI Window
A sleek, modern PySide6 interface that outclasses Nugget in every way.
"""

from __future__ import annotations
import sys
import os
from pathlib import Path
from typing import Optional

try:
    from PySide6.QtWidgets import (
        QApplication, QMainWindow, QWidget, QVBoxLayout, QHBoxLayout,
        QLabel, QPushButton, QScrollArea, QFrame, QCheckBox, QLineEdit,
        QSpinBox, QSlider, QComboBox, QProgressBar, QFileDialog,
        QStackedWidget, QSizePolicy, QToolButton, QMessageBox, QSplitter,
        QGroupBox, QTabWidget, QTextEdit, QListWidget, QListWidgetItem,
    )
    from PySide6.QtCore import (
        Qt, QThread, Signal, QTimer, QPropertyAnimation,
        QEasingCurve, QSize, QPoint, QRect,
    )
    from PySide6.QtGui import (
        QFont, QFontDatabase, QColor, QPalette, QIcon,
        QPixmap, QPainter, QLinearGradient, QBrush, QPen,
        QGuiApplication, QCursor,
    )
    HAS_QT = True
except ImportError:
    HAS_QT = False

from src.tweaks.tweaks import (
    ALL_TWEAKS, CHRIS_EXCLUSIVE, TweakType, Tweak,
    MOBILEGESTALT_TWEAKS, STATUSBAR_TWEAKS, SPRINGBOARD_TWEAKS,
    INTERNAL_TWEAKS, DAEMON_TWEAKS, FEATURE_FLAG_TWEAKS,
)
from src.devicemanagement.device_manager import DeviceManager, DeviceInfo


# ─── Stylesheet ───────────────────────────────────────────────────────────────

STYLESHEET = """
QMainWindow, QWidget {
    background-color: #0A0A0F;
    color: #E8E8F0;
    font-family: 'SF Pro Display', 'Segoe UI Variable', 'Ubuntu', sans-serif;
}

/* Sidebar */
#sidebar {
    background-color: #0D0D14;
    border-right: 1px solid #1E1E2E;
    min-width: 220px;
    max-width: 220px;
}

#logo_label {
    font-size: 26px;
    font-weight: 800;
    color: #FFFFFF;
    letter-spacing: 3px;
    padding: 28px 24px 6px 24px;
}

#tagline_label {
    font-size: 10px;
    color: #4A4A6A;
    letter-spacing: 1px;
    padding: 0 24px 24px 24px;
}

/* Nav buttons */
#nav_btn {
    background: transparent;
    border: none;
    border-radius: 10px;
    padding: 11px 16px;
    text-align: left;
    font-size: 13px;
    color: #6060A0;
    margin: 1px 12px;
}
#nav_btn:hover {
    background-color: #141425;
    color: #C0C0FF;
}
#nav_btn[active="true"] {
    background: qlineargradient(x1:0,y1:0,x2:1,y2:0,
        stop:0 #2A1F5E, stop:1 #1A1535);
    color: #A78BFA;
    border-left: 3px solid #7C3AED;
    font-weight: 600;
}

/* Device card */
#device_card {
    background: qlineargradient(x1:0,y1:0,x2:0,y2:1,
        stop:0 #141420, stop:1 #0F0F1A);
    border: 1px solid #1E1E3A;
    border-radius: 14px;
    padding: 16px;
    margin: 8px 12px;
}
#device_name {
    font-size: 14px;
    font-weight: 700;
    color: #FFFFFF;
}
#device_ios {
    font-size: 11px;
    color: #5050A0;
}
#device_method {
    font-size: 10px;
    font-weight: 600;
    color: #7C3AED;
    background: #1A1040;
    border-radius: 6px;
    padding: 3px 8px;
}

/* Main content */
#content_area {
    background-color: #0A0A0F;
    padding: 24px;
}

#page_title {
    font-size: 22px;
    font-weight: 700;
    color: #FFFFFF;
    margin-bottom: 4px;
}
#page_subtitle {
    font-size: 12px;
    color: #4A4A6A;
    margin-bottom: 24px;
}

/* Tweak cards */
#tweak_card {
    background-color: #0F0F1C;
    border: 1px solid #1A1A30;
    border-radius: 12px;
    padding: 14px 18px;
    margin-bottom: 6px;
}
#tweak_card:hover {
    border-color: #2A2A50;
    background-color: #111120;
}
#tweak_card[new_feature="true"] {
    border-color: #2A1060;
    background-color: #0E0A1C;
}

#tweak_name {
    font-size: 13px;
    font-weight: 600;
    color: #E0E0F5;
}
#tweak_desc {
    font-size: 11px;
    color: #454565;
    margin-top: 2px;
}
#new_badge {
    font-size: 9px;
    font-weight: 700;
    color: #A78BFA;
    background: #1A0A40;
    border: 1px solid #3A1A80;
    border-radius: 5px;
    padding: 2px 7px;
    letter-spacing: 1px;
}
#risky_badge {
    font-size: 9px;
    font-weight: 700;
    color: #F87171;
    background: #2A0A0A;
    border: 1px solid #5A1A1A;
    border-radius: 5px;
    padding: 2px 7px;
    letter-spacing: 1px;
}

/* Toggle switch style checkbox */
QCheckBox {
    spacing: 8px;
    color: #9090C0;
    font-size: 13px;
}
QCheckBox::indicator {
    width: 42px;
    height: 24px;
    border-radius: 12px;
    background-color: #1A1A30;
    border: 1px solid #2A2A50;
}
QCheckBox::indicator:checked {
    background-color: #7C3AED;
    border-color: #7C3AED;
}
QCheckBox::indicator:hover {
    border-color: #5050A0;
}

/* Input fields */
QLineEdit, QSpinBox, QComboBox {
    background-color: #111120;
    border: 1px solid #1E1E3A;
    border-radius: 8px;
    padding: 8px 12px;
    color: #E0E0F5;
    font-size: 12px;
    min-width: 140px;
}
QLineEdit:focus, QSpinBox:focus, QComboBox:focus {
    border-color: #7C3AED;
    background-color: #130E25;
}

/* Category headers */
#category_header {
    font-size: 10px;
    font-weight: 700;
    color: #3A3A6A;
    letter-spacing: 2px;
    padding: 16px 0 8px 0;
}

/* Apply button */
#apply_btn {
    background: qlineargradient(x1:0,y1:0,x2:1,y2:0,
        stop:0 #7C3AED, stop:1 #5B21B6);
    border: none;
    border-radius: 12px;
    color: white;
    font-size: 14px;
    font-weight: 700;
    padding: 14px 32px;
    letter-spacing: 1px;
}
#apply_btn:hover {
    background: qlineargradient(x1:0,y1:0,x2:1,y2:0,
        stop:0 #8B5CF6, stop:1 #6D28D9);
}
#apply_btn:pressed {
    background: #4C1D95;
}
#apply_btn:disabled {
    background: #1A1A30;
    color: #3A3A6A;
}

/* Respring button */
#respring_btn {
    background: transparent;
    border: 1px solid #2A2A50;
    border-radius: 10px;
    color: #6060A0;
    font-size: 12px;
    padding: 10px 20px;
}
#respring_btn:hover {
    border-color: #5050A0;
    color: #A0A0E0;
}

/* Progress bar */
QProgressBar {
    background-color: #111120;
    border: none;
    border-radius: 6px;
    height: 6px;
    text-align: center;
    color: transparent;
}
QProgressBar::chunk {
    background: qlineargradient(x1:0,y1:0,x2:1,y2:0,
        stop:0 #7C3AED, stop:1 #A78BFA);
    border-radius: 6px;
}

/* Scrollbar */
QScrollBar:vertical {
    background: transparent;
    width: 6px;
    margin: 0;
}
QScrollBar::handle:vertical {
    background: #1E1E3A;
    border-radius: 3px;
    min-height: 30px;
}
QScrollBar::handle:vertical:hover {
    background: #3A3A6A;
}
QScrollBar::add-line:vertical, QScrollBar::sub-line:vertical {
    height: 0;
}

/* Section divider */
#divider {
    background-color: #141425;
    max-height: 1px;
    min-height: 1px;
    margin: 12px 0;
}

/* Status message */
#status_ok  { color: #34D399; font-size: 12px; }
#status_err { color: #F87171; font-size: 12px; }
#status_info{ color: #A78BFA; font-size: 12px; }

/* Connect button */
#connect_btn {
    background: #0F0F1C;
    border: 1px dashed #2A2A50;
    border-radius: 12px;
    color: #5050A0;
    font-size: 13px;
    padding: 20px;
}
#connect_btn:hover {
    border-color: #7C3AED;
    color: #A78BFA;
    background: #111120;
}

/* Tabs */
QTabWidget::pane {
    border: 1px solid #1A1A30;
    border-radius: 12px;
    background: #0F0F1C;
    top: -1px;
}
QTabBar::tab {
    background: transparent;
    border: none;
    color: #4A4A7A;
    padding: 10px 20px;
    font-size: 12px;
    font-weight: 600;
}
QTabBar::tab:selected {
    color: #A78BFA;
    border-bottom: 2px solid #7C3AED;
}
QTabBar::tab:hover {
    color: #8080C0;
}
"""


# ─── Worker Thread ────────────────────────────────────────────────────────────

class ApplyWorker(QThread):
    progress = Signal(int, str)
    finished = Signal(bool, str)

    def __init__(self, lockdown, method, enabled_tweaks, mg_path):
        super().__init__()
        self.lockdown       = lockdown
        self.method         = method
        self.enabled_tweaks = enabled_tweaks
        self.mg_path        = mg_path

    def run(self):
        try:
            from src.restore.restore_engine import ChrisRestoreEngine
            engine = ChrisRestoreEngine(self.lockdown, self.method)
            ok, msg = engine.apply(
                self.enabled_tweaks,
                self.mg_path,
                progress=lambda p, m: self.progress.emit(p, m),
            )
            self.finished.emit(ok, msg)
        except Exception as e:
            self.finished.emit(False, str(e))


# ─── Tweak Card Widget ────────────────────────────────────────────────────────

class TweakCard(QWidget):
    def __init__(self, tweak: Tweak, parent=None):
        super().__init__(parent)
        self.tweak = tweak
        self.setObjectName("tweak_card")
        if tweak.new_in_chris:
            self.setProperty("new_feature", "true")

        layout = QHBoxLayout(self)
        layout.setContentsMargins(0, 0, 0, 0)
        layout.setSpacing(12)

        # Left: info
        info = QVBoxLayout()
        info.setSpacing(3)

        name_row = QHBoxLayout()
        name_row.setSpacing(6)
        name_lbl = QLabel(tweak.name)
        name_lbl.setObjectName("tweak_name")
        name_row.addWidget(name_lbl)

        if tweak.new_in_chris:
            badge = QLabel("CHRIS EXCLUSIVE")
            badge.setObjectName("new_badge")
            name_row.addWidget(badge)
        if tweak.risky:
            risky = QLabel("⚠ RISKY")
            risky.setObjectName("risky_badge")
            name_row.addWidget(risky)
        name_row.addStretch()
        info.addLayout(name_row)

        desc_lbl = QLabel(tweak.description)
        desc_lbl.setObjectName("tweak_desc")
        desc_lbl.setWordWrap(True)
        info.addWidget(desc_lbl)

        ios_range = f"iOS {tweak.ios_min}"
        if tweak.ios_max:
            ios_range += f" – {tweak.ios_max}"
        else:
            ios_range += "+"
        ios_lbl = QLabel(ios_range)
        ios_lbl.setStyleSheet("font-size:10px; color:#2A2A5A;")
        info.addWidget(ios_lbl)

        layout.addLayout(info, stretch=1)

        # Right: control
        self.control = self._make_control(tweak)
        layout.addWidget(self.control)

    def _make_control(self, tweak: Tweak) -> QWidget:
        if tweak.tweak_type == TweakType.DAEMON_DISABLE:
            cb = QCheckBox()
            return cb
        if tweak.tweak_type in (TweakType.MOBILEGESTALT, TweakType.FEATURE_FLAG,
                                 TweakType.SPRINGBOARD):
            # If key looks boolean, use checkbox; else use line edit
            if isinstance(tweak.default, bool):
                return QCheckBox()
            elif isinstance(tweak.default, int):
                sb = QSpinBox()
                sb.setRange(0, 9999)
                return sb
            else:
                le = QLineEdit()
                le.setPlaceholderText("Enter value…")
                return le
        if tweak.tweak_type == TweakType.STATUS_BAR:
            le = QLineEdit()
            le.setPlaceholderText("Enter value…")
            return le
        return QCheckBox()

    def get_value(self):
        if isinstance(self.control, QCheckBox):
            return self.control.isChecked()
        if isinstance(self.control, QLineEdit):
            return self.control.text()
        if isinstance(self.control, QSpinBox):
            return self.control.value()
        return None

    def is_enabled(self) -> bool:
        if isinstance(self.control, QCheckBox):
            return self.control.isChecked()
        if isinstance(self.control, QLineEdit):
            return bool(self.control.text().strip())
        if isinstance(self.control, QSpinBox):
            return self.control.value() != 0
        return False


# ─── Page: Tweak List ─────────────────────────────────────────────────────────

class TweakPage(QWidget):
    def __init__(self, tweaks: list[Tweak], title: str, subtitle: str, parent=None):
        super().__init__(parent)
        self.tweak_cards: dict[str, TweakCard] = {}

        outer = QVBoxLayout(self)
        outer.setContentsMargins(0, 0, 0, 0)

        title_lbl = QLabel(title)
        title_lbl.setObjectName("page_title")
        outer.addWidget(title_lbl)

        sub_lbl = QLabel(subtitle)
        sub_lbl.setObjectName("page_subtitle")
        outer.addWidget(sub_lbl)

        scroll = QScrollArea()
        scroll.setWidgetResizable(True)
        scroll.setFrameShape(QFrame.Shape.NoFrame)
        scroll.setHorizontalScrollBarPolicy(Qt.ScrollBarPolicy.ScrollBarAlwaysOff)

        container = QWidget()
        vbox = QVBoxLayout(container)
        vbox.setContentsMargins(0, 0, 12, 0)
        vbox.setSpacing(0)

        # Group by category
        categories: dict[str, list[Tweak]] = {}
        for t in tweaks:
            categories.setdefault(t.category, []).append(t)

        for cat, cat_tweaks in categories.items():
            cat_lbl = QLabel(cat.upper())
            cat_lbl.setObjectName("category_header")
            vbox.addWidget(cat_lbl)

            for tweak in cat_tweaks:
                card = TweakCard(tweak)
                self.tweak_cards[tweak.id] = card
                vbox.addWidget(card)

        vbox.addStretch()
        scroll.setWidget(container)
        outer.addWidget(scroll)

    def get_enabled_tweaks(self) -> dict[str, object]:
        result = {}
        for tweak_id, card in self.tweak_cards.items():
            if card.is_enabled():
                result[tweak_id] = card.get_value()
        return result


# ─── Page: Dashboard ──────────────────────────────────────────────────────────

class DashboardPage(QWidget):
    def __init__(self, device: Optional[DeviceInfo], parent=None):
        super().__init__(parent)
        layout = QVBoxLayout(self)
        layout.setContentsMargins(0, 0, 0, 0)
        layout.setSpacing(16)

        title = QLabel("Dashboard")
        title.setObjectName("page_title")
        layout.addWidget(title)

        sub = QLabel("Overview of your device and Chris features")
        sub.setObjectName("page_subtitle")
        layout.addWidget(sub)

        # Stats row
        stats_row = QHBoxLayout()
        stats = [
            ("Total Tweaks",     str(len(ALL_TWEAKS)),       "#7C3AED"),
            ("Chris Exclusive",  str(len(CHRIS_EXCLUSIVE)),  "#10B981"),
            ("Daemon Controls",  str(len(DAEMON_TWEAKS)),    "#F59E0B"),
            ("iOS Versions",     "17.0 – 26.x",              "#3B82F6"),
        ]
        for label, value, color in stats:
            card = self._stat_card(label, value, color)
            stats_row.addWidget(card)
        layout.addLayout(stats_row)

        # Chris vs Nugget comparison
        comp_title = QLabel("WHY CHRIS")
        comp_title.setObjectName("category_header")
        layout.addWidget(comp_title)

        comparisons = [
            ("✦", "More tweaks",         f"{len(ALL_TWEAKS)} total vs Nugget's ~80",           "#A78BFA"),
            ("✦", "Chris-exclusive",     f"{len(CHRIS_EXCLUSIVE)} features you won't find in Nugget", "#34D399"),
            ("✦", "All platforms",       "macOS, Windows, Linux — full support",                "#60A5FA"),
            ("✦", "More daemon control", f"{len(DAEMON_TWEAKS)} daemons vs Nugget's 17",        "#FBBF24"),
            ("✦", "Better UI",           "Dark glass design, smooth animations, clear layout",  "#F472B6"),
            ("✦", "Open source",         "MIT licensed, fork it and make it yours",             "#A78BFA"),
        ]

        for icon, label, desc, color in comparisons:
            row = QHBoxLayout()
            row.setSpacing(12)
            icon_lbl = QLabel(icon)
            icon_lbl.setStyleSheet(f"color:{color}; font-size:14px;")
            icon_lbl.setFixedWidth(20)
            row.addWidget(icon_lbl)
            lbl = QLabel(f"<b>{label}</b> — {desc}")
            lbl.setStyleSheet("font-size:13px; color:#8080C0;")
            row.addWidget(lbl, stretch=1)
            layout.addLayout(row)

        layout.addStretch()

    def _stat_card(self, label, value, color):
        card = QFrame()
        card.setObjectName("tweak_card")
        v = QVBoxLayout(card)
        v.setContentsMargins(16, 14, 16, 14)
        val_lbl = QLabel(value)
        val_lbl.setStyleSheet(f"font-size:24px; font-weight:800; color:{color};")
        v.addWidget(val_lbl)
        lbl_lbl = QLabel(label)
        lbl_lbl.setStyleSheet("font-size:11px; color:#4A4A7A;")
        v.addWidget(lbl_lbl)
        return card


# ─── Main Window ──────────────────────────────────────────────────────────────

class ChrisMainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Chris — iOS Customization")
        self.resize(1100, 740)
        self.setMinimumSize(900, 600)

        self.device_manager = DeviceManager()
        self.device: Optional[DeviceInfo] = None
        self.mg_path: Optional[Path] = None
        self._worker: Optional[ApplyWorker] = None

        self._build_ui()
        self._detect_device()

    # ── UI Construction ───────────────────────────────────────────────────────

    def _build_ui(self):
        central = QWidget()
        self.setCentralWidget(central)
        root = QHBoxLayout(central)
        root.setContentsMargins(0, 0, 0, 0)
        root.setSpacing(0)

        # Sidebar
        self.sidebar = self._build_sidebar()
        root.addWidget(self.sidebar)

        # Content stack
        self.stack = QStackedWidget()
        self.stack.setObjectName("content_area")

        self.pages: dict[str, QWidget] = {}
        self._add_page("dashboard",  DashboardPage(self.device),                             "dashboard")
        self._add_page("gestalt",    TweakPage(MOBILEGESTALT_TWEAKS,  "Hidden iOS Features","Unlock features Apple hid in MobileGestalt"),  "gestalt")
        self._add_page("statusbar",  TweakPage(STATUSBAR_TWEAKS,      "Status Bar",          "Customize every element of the status bar"),   "statusbar")
        self._add_page("springboard",TweakPage(SPRINGBOARD_TWEAKS,    "Springboard",         "Tweak lock screen, display & system options"),  "springboard")
        self._add_page("daemons",    TweakPage(DAEMON_TWEAKS,         "Disable Daemons",     "Kill background services to boost performance"),"daemons")
        self._add_page("internal",   TweakPage(INTERNAL_TWEAKS + FEATURE_FLAG_TWEAKS, "Internal & Debug", "Debug flags and feature switches"), "internal")

        # Right panel: stack + bottom bar
        right = QVBoxLayout()
        right.setContentsMargins(28, 24, 28, 20)
        right.setSpacing(16)
        right.addWidget(self.stack, stretch=1)
        right.addWidget(self._build_bottom_bar())

        right_widget = QWidget()
        right_widget.setLayout(right)
        root.addWidget(right_widget, stretch=1)

        self.setStyleSheet(STYLESHEET)
        self._nav_click("dashboard")

    def _add_page(self, key: str, widget: QWidget, nav_key: str):
        self.pages[key] = widget
        self.stack.addWidget(widget)

    def _build_sidebar(self) -> QWidget:
        sidebar = QWidget()
        sidebar.setObjectName("sidebar")
        sidebar.setFixedWidth(220)
        layout = QVBoxLayout(sidebar)
        layout.setContentsMargins(0, 0, 0, 0)
        layout.setSpacing(0)

        # Logo
        logo = QLabel("CHRIS")
        logo.setObjectName("logo_label")
        layout.addWidget(logo)

        tagline = QLabel("iOS DEVICE CUSTOMIZATION")
        tagline.setObjectName("tagline_label")
        layout.addWidget(tagline)

        # Divider
        div = QFrame()
        div.setObjectName("divider")
        layout.addWidget(div)

        # Nav items
        self._nav_buttons: dict[str, QPushButton] = {}
        nav_items = [
            ("dashboard",   "⬡  Dashboard"),
            ("gestalt",     "◈  Hidden Features"),
            ("statusbar",   "▤  Status Bar"),
            ("springboard", "⊞  Springboard"),
            ("daemons",     "⊗  Daemons"),
            ("internal",    "⚙  Internal & Debug"),
        ]
        for key, label in nav_items:
            btn = QPushButton(label)
            btn.setObjectName("nav_btn")
            btn.setProperty("active", "false")
            btn.clicked.connect(lambda checked=False, k=key: self._nav_click(k))
            btn.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))
            layout.addWidget(btn)
            self._nav_buttons[key] = btn

        layout.addStretch()

        # Device card
        self.device_card = self._build_device_card()
        layout.addWidget(self.device_card)

        return sidebar

    def _build_device_card(self) -> QWidget:
        card = QFrame()
        card.setObjectName("device_card")
        v = QVBoxLayout(card)
        v.setSpacing(5)

        self.dev_name_lbl = QLabel("No Device")
        self.dev_name_lbl.setObjectName("device_name")
        v.addWidget(self.dev_name_lbl)

        self.dev_ios_lbl = QLabel("Connect your iPhone or iPad")
        self.dev_ios_lbl.setObjectName("device_ios")
        self.dev_ios_lbl.setWordWrap(True)
        v.addWidget(self.dev_ios_lbl)

        self.dev_method_lbl = QLabel("—")
        self.dev_method_lbl.setObjectName("device_method")
        self.dev_method_lbl.hide()
        v.addWidget(self.dev_method_lbl)

        connect_btn = QPushButton("⟳  Refresh Device")
        connect_btn.setObjectName("respring_btn")
        connect_btn.clicked.connect(self._detect_device)
        connect_btn.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))
        v.addWidget(connect_btn)

        return card

    def _build_bottom_bar(self) -> QWidget:
        bar = QWidget()
        layout = QVBoxLayout(bar)
        layout.setContentsMargins(0, 0, 0, 0)
        layout.setSpacing(10)

        # MobileGestalt file row
        mg_row = QHBoxLayout()
        self.mg_label = QLabel("No MobileGestalt file selected")
        self.mg_label.setStyleSheet("font-size:11px; color:#3A3A6A;")
        mg_row.addWidget(self.mg_label, stretch=1)
        mg_btn = QPushButton("Browse…")
        mg_btn.setObjectName("respring_btn")
        mg_btn.setFixedWidth(90)
        mg_btn.clicked.connect(self._browse_mg)
        mg_btn.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))
        mg_row.addWidget(mg_btn)
        layout.addLayout(mg_row)

        # Progress bar
        self.progress_bar = QProgressBar()
        self.progress_bar.setValue(0)
        self.progress_bar.hide()
        layout.addWidget(self.progress_bar)

        # Status + buttons
        btn_row = QHBoxLayout()
        self.status_lbl = QLabel("")
        self.status_lbl.setObjectName("status_info")
        btn_row.addWidget(self.status_lbl, stretch=1)

        self.respring_btn = QPushButton("↺  Respring")
        self.respring_btn.setObjectName("respring_btn")
        self.respring_btn.setFixedWidth(110)
        self.respring_btn.clicked.connect(self._respring)
        self.respring_btn.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))
        btn_row.addWidget(self.respring_btn)

        self.apply_btn = QPushButton("Apply Tweaks  →")
        self.apply_btn.setObjectName("apply_btn")
        self.apply_btn.setFixedWidth(160)
        self.apply_btn.clicked.connect(self._apply_tweaks)
        self.apply_btn.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))
        btn_row.addWidget(self.apply_btn)

        layout.addLayout(btn_row)
        return bar

    # ── Navigation ────────────────────────────────────────────────────────────

    def _nav_click(self, key: str):
        for k, btn in self._nav_buttons.items():
            btn.setProperty("active", "true" if k == key else "false")
            btn.setStyle(btn.style())  # force style refresh
        if key in self.pages:
            self.stack.setCurrentWidget(self.pages[key])

    # ── Device Detection ──────────────────────────────────────────────────────

    def _detect_device(self):
        self.status_lbl.setObjectName("status_info")
        self.status_lbl.setText("Scanning for device…")
        QApplication.processEvents()

        self.device = self.device_manager.find_device()
        if self.device:
            self.dev_name_lbl.setText(self.device.name)
            self.dev_ios_lbl.setText(f"iOS {self.device.ios_version}  •  {self.device.model}")
            method = self.device_manager.restore_method()
            self.dev_method_lbl.setText(method)
            self.dev_method_lbl.show()
            self.status_lbl.setObjectName("status_ok")
            self.status_lbl.setText(f"✓  {self.device.name} connected via {method}")
            if not self.device.paired:
                self.status_lbl.setObjectName("status_info")
                self.status_lbl.setText("⬡  Demo mode — no device connected")
        else:
            self.dev_name_lbl.setText("No Device Found")
            self.dev_ios_lbl.setText("Connect iPhone/iPad via USB")
            self.dev_method_lbl.hide()
            self.status_lbl.setObjectName("status_err")
            self.status_lbl.setText("✕  No device found — check USB & trust prompt")

        # Force stylesheet refresh
        self.status_lbl.setStyle(self.status_lbl.style())

    # ── File Browser ──────────────────────────────────────────────────────────

    def _browse_mg(self):
        path, _ = QFileDialog.getOpenFileName(
            self, "Select MobileGestalt File", "", "Plist Files (*.plist);;All Files (*)"
        )
        if path:
            self.mg_path = Path(path)
            name = self.mg_path.name
            self.mg_label.setText(f"📄 {name}")
            self.mg_label.setStyleSheet("font-size:11px; color:#7C3AED;")

    # ── Apply ─────────────────────────────────────────────────────────────────

    def _collect_all_tweaks(self) -> dict[str, object]:
        result = {}
        for key, page in self.pages.items():
            if isinstance(page, TweakPage):
                result.update(page.get_enabled_tweaks())
        return result

    def _apply_tweaks(self):
        enabled = self._collect_all_tweaks()
        if not enabled:
            self.status_lbl.setObjectName("status_err")
            self.status_lbl.setText("✕  No tweaks enabled — toggle something first!")
            self.status_lbl.setStyle(self.status_lbl.style())
            return

        if not self.device:
            self.status_lbl.setObjectName("status_err")
            self.status_lbl.setText("✕  No device connected")
            self.status_lbl.setStyle(self.status_lbl.style())
            return

        self.apply_btn.setEnabled(False)
        self.progress_bar.setValue(0)
        self.progress_bar.show()
        self.status_lbl.setObjectName("status_info")
        self.status_lbl.setText(f"⬡  Applying {len(enabled)} tweak(s)…")
        self.status_lbl.setStyle(self.status_lbl.style())

        lockdown = self.device_manager.lockdown
        method   = self.device_manager.restore_method()

        self._worker = ApplyWorker(lockdown, method, enabled, self.mg_path)
        self._worker.progress.connect(self._on_progress)
        self._worker.finished.connect(self._on_done)
        self._worker.start()

    def _on_progress(self, pct: int, msg: str):
        self.progress_bar.setValue(pct)
        self.status_lbl.setText(f"  {msg}")

    def _on_done(self, ok: bool, msg: str):
        self.apply_btn.setEnabled(True)
        self.progress_bar.setValue(100 if ok else 0)
        QTimer.singleShot(2000, self.progress_bar.hide)
        if ok:
            self.status_lbl.setObjectName("status_ok")
            self.status_lbl.setText(f"✓  {msg}")
        else:
            self.status_lbl.setObjectName("status_err")
            self.status_lbl.setText(f"✕  {msg}")
        self.status_lbl.setStyle(self.status_lbl.style())

    # ── Respring ──────────────────────────────────────────────────────────────

    def _respring(self):
        if not self.device_manager.lockdown:
            self.status_lbl.setObjectName("status_err")
            self.status_lbl.setText("✕  No device connected")
            self.status_lbl.setStyle(self.status_lbl.style())
            return
        try:
            from pymobiledevice3.services.diagnostics import DiagnosticsService
            with DiagnosticsService(self.device_manager.lockdown) as d:
                d.restart()
            self.status_lbl.setObjectName("status_ok")
            self.status_lbl.setText("✓  Respringing device…")
        except Exception as e:
            self.status_lbl.setObjectName("status_err")
            self.status_lbl.setText(f"✕  Respring failed: {e}")
        self.status_lbl.setStyle(self.status_lbl.style())


# ─── Entry Point ──────────────────────────────────────────────────────────────

def launch():
    if not HAS_QT:
        print("ERROR: PySide6 is not installed.")
        print("Run:  pip install PySide6")
        sys.exit(1)

    app = QApplication(sys.argv)
    app.setApplicationName("Chris")
    app.setApplicationVersion("1.0.0")

    # High DPI
    app.setAttribute(Qt.ApplicationAttribute.AA_UseHighDpiPixmaps, True)

    window = ChrisMainWindow()
    window.show()
    sys.exit(app.exec())


if __name__ == "__main__":
    launch()
