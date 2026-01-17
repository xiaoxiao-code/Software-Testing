# orchard_ingestion_monitor.py - 智慧果园数据摄入监控仪表盘
import sys
import random
import datetime
import numpy as np
from collections import deque
import pyqtgraph as pg
from PyQt5 import QtWidgets, QtCore, QtGui


class OrchardSimulator:

    def __init__(self):
        # 基础数据定义
        self.tree_types = [
            "红富士苹果树", "赣南脐橙树",
            "黑叶荔枝树", "不知火丑橘",
            "黄金百香果", "巨峰葡萄"
        ]
        self.areas = ["区域A", "区域B", "区域C", "区域D"]  # 果园区域
        self.workers = ["王xx", "李xx", "0527", "张倩", "马俊"]  # 工作人员
        self.tick = 0

    def generate_batch(self):
        """生成混合业务数据流"""
        self.tick += 1

        # 模拟正弦波流量压力
        load_factor = (np.sin(self.tick * 0.1) + 1) * 15 + 2
        # 随机决定这一帧产生多少条日志
        log_count = int(load_factor + random.randint(0, 5))

        batch_logs = []
        success_count = 0
        fail_count = 0

        for _ in range(log_count):
            # 随机决定业务类型：果树上传、灌溉数据、环境快照、仓库日志
            event_type = random.choices(
                ['TREE', 'IRRIGATION', 'SNAPSHOT', 'WAREHOUSE'],
                weights=[60, 20, 10, 10]
            )[0]

            log_entry = self._create_log_entry(event_type)

            # 模拟高并发下的丢包/超时
            if log_entry['status'] != 'SUCCESS':
                fail_count += 1
            else:
                success_count += 1

            batch_logs.append(log_entry)

        return {
            "tps": success_count,
            "errors": fail_count,
            "logs": batch_logs
        }

    def _create_log_entry(self, event_type):
        """根据业务类型构造详细的JSON Payload"""
        current_time = datetime.datetime.now().strftime("%H:%M:%S.%f")[:-3]
        status = "SUCCESS"
        latency = random.randint(15, 120)

        # 模拟偶尔的网络波动
        if random.random() < 0.02:
            status = "TIMEOUT"
            latency = 5000

        payload = ""
        api_path = ""
        category = event_type

        if event_type == 'TREE':
            # 果树编号、名称、区域
            tree_id = f"T-{random.randint(10000, 99999)}"
            name = random.choice(self.tree_types)
            area = random.choice(self.areas)
            api_path = "/api/v1/digital_twin/tree/sync"
            payload = f"{{ 'id': '{tree_id}', 'name': '{name}', 'area': '{area}' }}"

        elif event_type == 'IRRIGATION':
            # 水源灌溉数据
            pool_level = round(random.uniform(40.0, 95.0), 1)
            consumption = random.choice([0, 0, 3, 5])  # 模拟间歇性消耗
            is_active = "ON" if random.random() > 0.8 else "OFF"
            api_path = "/api/v1/iot/irrigation/telemetry"
            payload = f"{{ 'pool_level': '{pool_level}%', 'valve': '{is_active}', 'daily_usage': '{consumption}L' }}"

        elif event_type == 'SNAPSHOT':
            # 图片Blob数据流 (环境面板截图)
            blob_url = "blob:https://gemini.google.com/0d26e04c-f4d1-42eb-872b..."
            temp = round(random.uniform(12.0, 28.0), 1)
            api_path = "/api/v1/monitor/snapshot/upload"
            payload = f"{{ 'img': '{blob_url[:30]}...', 'meta': 'Temp:{temp}C, Hum:77%' }}"

        elif event_type == 'WAREHOUSE':
            # 仓库人员操作
            worker = random.choice(self.workers)
            action = random.choice(["存放柠檬20斤", "取出化肥1袋", "开启仓库门", "巡检完成"])
            api_path = "/api/v1/warehouse/log"
            payload = f"{{ 'worker': '{worker}', 'action': '{action}' }}"

        return {
            "time": current_time,
            "category": category,
            "api": api_path,
            "payload": payload,
            "status": status,
            "latency": latency
        }


# ==========================================
# 2. 监控仪表盘 GUI (PyQt5 + PyQtGraph)
# ==========================================
class UnityBackendMonitor(QtWidgets.QMainWindow):
    """数字孪生系统监控仪表盘主窗口"""

    def __init__(self):
        super().__init__()
        self.setWindowTitle("Smart Orchard Digital Twin - Backend Monitor")
        # 初始尺寸作为备用，实际启动会最大化
        self.resize(1100, 850)

        # 样式表：极客黑 + 霓虹色点缀
        self.setStyleSheet("""
            QMainWindow {background-color: #0d0d0d; color: #e0e0e0;}
            QLabel {font-family: 'Segoe UI', sans-serif;}
        """)

        # 主布局
        central_widget = QtWidgets.QWidget()
        self.setCentralWidget(central_widget)
        layout = QtWidgets.QVBoxLayout(central_widget)

        # 顶部：实时TPS曲线
        pg.setConfigOption('background', '#1a1a1a')
        pg.setConfigOption('foreground', '#888888')

        # 标题栏
        title_layout = QtWidgets.QHBoxLayout()
        title_label = QtWidgets.QLabel("DIGITAL TWIN DATA INGESTION RATE (TPS)")
        title_label.setStyleSheet("color: #00ff99; font-weight: bold; font-size: 16px;")
        title_layout.addWidget(title_label)
        title_layout.addStretch()
        layout.addLayout(title_layout)

        # 图表控件
        self.graph_widget = pg.PlotWidget()
        self.graph_widget.showGrid(x=True, y=True, alpha=0.2)
        self.graph_widget.setLabel('left', 'Events / Sec')
        self.graph_widget.setYRange(0, 80)
        self.curve_tps = self.graph_widget.plot(pen=pg.mkPen('#00ff99', width=2), fillLevel=0, brush=(0, 255, 153, 30))
        layout.addWidget(self.graph_widget, stretch=3)

        # 底部：滚动日志流
        log_label = QtWidgets.QLabel("REAL-TIME EVENT STREAM [Sources: app Client, IoT Sensors, Cameras]")
        log_label.setStyleSheet(
            "color: #00ccff; font-weight: bold; margin-top: 10px; font-family: Consolas; font-size: 14px;")
        layout.addWidget(log_label)

        # 日志列表控件
        self.log_list = QtWidgets.QListWidget()
        self.log_list.setStyleSheet("""
            QListWidget {
                background-color: #000000;
                font-family: 'Consolas', 'Courier New', monospace;
                font-size: 11pt;
                border: 1px solid #333;
                outline: none;
            }
            QListWidget::item { padding: 4px; }
        """)
        self.log_list.setVerticalScrollMode(QtWidgets.QAbstractItemView.ScrollPerPixel)
        self.log_list.setHorizontalScrollBarPolicy(QtCore.Qt.ScrollBarAlwaysOff)
        layout.addWidget(self.log_list, stretch=5)

        self.simulator = OrchardSimulator()
        self.tps_buffer = deque(maxlen=150)
        self.timer = QtCore.QTimer()
        self.timer.timeout.connect(self.update_monitor)
        self.timer.start(80)

    def update_monitor(self):
        data = self.simulator.generate_batch()

        self.tps_buffer.append(data['tps'])
        self.curve_tps.setData(self.tps_buffer)

        for log in data['logs']:
            self.add_log_entry(log)

        self.log_list.scrollToBottom()
        if self.log_list.count() > 300:
            self.log_list.model().removeRows(0, 50)

    def add_log_entry(self, log):
        time_str = log['time']
        cat = log['category']
        status = log['status']
        payload = log['payload']
        latency = log['latency']

        display_text = f"[{time_str}] [{cat:<10}] {payload} | {latency}ms"

        item = QtWidgets.QListWidgetItem(display_text)
        color = QtGui.QColor("#ffffff")

        if status != "SUCCESS":
            color = QtGui.QColor("#ff3333")
            item.setText(display_text + " [CRITICAL FAILURE]")
        else:
            if cat == "TREE":
                color = QtGui.QColor("#00ff99")
            elif cat == "IRRIGATION":
                color = QtGui.QColor("#00ccff")
            elif cat == "SNAPSHOT":
                color = QtGui.QColor("#ffcc00")
            elif cat == "WAREHOUSE":
                color = QtGui.QColor("#bd93f9")

        item.setForeground(color)
        self.log_list.addItem(item)


if __name__ == '__main__':
    """应用启动入口"""
    app = QtWidgets.QApplication(sys.argv)
    app.setAttribute(QtCore.Qt.AA_EnableHighDpiScaling)
    monitor = UnityBackendMonitor()
    monitor.showMaximized()
    sys.exit(app.exec_())