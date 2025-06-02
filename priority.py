from datetime import datetime, timedelta

# Representasi tugas
class Task:
    def __init__(self, name, deadline, importance, duration):
        self.name = name
        self.deadline = deadline  # datetime object
        self.importance = importance  # 1-10
        self.duration = duration  # in hours
        self.urgency = self.calculate_urgency()
        self.profit = self.urgency * self.importance
        self.category = self.categorize()

    def calculate_urgency(self):    
        now = datetime.now()
        remaining_days = (self.deadline - now).days
        if remaining_days <= 0:
            return 10  # Sangat mendesak
        elif remaining_days <= 1:
            return 9
        elif remaining_days <= 2:
            return 7
        elif remaining_days <= 3:
            return 5
        elif remaining_days <= 7:
            return 3
        else:
            return 1  # Tidak mendesak


    def categorize(self):
        is_urgent = self.urgency >= 5
        is_important = self.importance >= 5

        if is_urgent and is_important:
            return 'Q1 (Do it now)'
        elif not is_urgent and is_important:
            return 'Q2 (Schedule it)'
        elif is_urgent and not is_important:
            return 'Q3 (Delegate it)'
        else:
            return 'Q4 (Delete it)'

# Fungsi greedy knapsack
def greedy_knapsack(tasks, max_hours_per_day):
    # Urutkan berdasarkan profit-to-weight ratio
    sorted_tasks = sorted(tasks, key=lambda x: x.profit / x.duration, reverse=True)
    selected_tasks = []
    total_time = 0

    for task in sorted_tasks:
        if total_time + task.duration <= max_hours_per_day:
            selected_tasks.append(task)
            total_time += task.duration

    return selected_tasks

# Contoh penggunaan
if __name__ == "__main__":
    tasks = [
        Task("Belajar AI", datetime.now() + timedelta(hours=8), 9, 2),
        Task("Laporan Kantor", datetime.now() + timedelta(days=2, hours=12), 7, 3),  # 2.5 hari
        Task("Main Game", datetime.now() + timedelta(days=5), 2, 1),
        Task("Bantu Teman", datetime.now() + timedelta(hours=4), 3, 2),
        Task("Proyek Kampus", datetime.now() + timedelta(days=1, hours=12), 8, 5),  # 1.5 hari
        Task("Membaca Buku", datetime.now() + timedelta(hours=12), 6, 1),
        Task("Olahraga", datetime.now() + timedelta(hours=6), 8, 1),
        Task("Masak Makan Siang", datetime.now() + timedelta(hours=2), 5, 1),
        Task("Meeting Online", datetime.now() + timedelta(hours=10), 7, 2),
        Task("Belanja Bulanan", datetime.now() + timedelta(days=1), 4, 2),
        Task("Menulis Blog", datetime.now() + timedelta(days=3), 6, 2),
        Task("Bersih-bersih Rumah", datetime.now() + timedelta(hours=18), 3, 2),
        Task("Mengerjakan PR", datetime.now() + timedelta(hours=5), 9, 1),
        Task("Menonton Webinar", datetime.now() + timedelta(days=2), 5, 2),
        Task("Menghubungi Keluarga", datetime.now() + timedelta(hours=7), 8, 1),
        Task("Membantu Adik", datetime.now() + timedelta(hours=3), 4, 1),
        Task("Membuat Presentasi", datetime.now() + timedelta(days=2, hours=6), 7, 2),  # 2.25 hari
        Task("Menyiram Tanaman", datetime.now() + timedelta(hours=1), 2, 0.5),
        Task("Membalas Email", datetime.now() + timedelta(hours=8), 6, 1),
        Task("Membuat Jadwal", datetime.now() + timedelta(hours=9), 5, 0.5),
        Task("Membaca Jurnal", datetime.now() + timedelta(days=1, hours=6), 7, 1),  # 1.25 hari
        Task("Membantu Orang Tua", datetime.now() + timedelta(hours=6), 8, 2),
        Task("Membuat Video", datetime.now() + timedelta(days=2), 6, 3),
        Task("Mencuci Baju", datetime.now() + timedelta(hours=4), 3, 1),
        Task("Mengerjakan Quiz", datetime.now() + timedelta(hours=2), 9, 1),
        Task("Diskusi Kelompok", datetime.now() + timedelta(hours=12), 7, 2),
        Task("Membaca Berita", datetime.now() + timedelta(hours=5), 4, 0.5),
    ]

    max_hours = 3  # Batas waktu pengerjaan harian

    selected = greedy_knapsack(tasks, max_hours)

    total_profit = sum(task.profit for task in selected)

    print(f"\nBatas waktu pengerjaan harian: {max_hours} jam")
    print(f"Total Profit: {total_profit:.2f}\n")

    print("=== Tugas Terpilih Hari Ini ===")
    for task in selected:
        print(f"- {task.name}: {task.duration} jam | Profit={task.profit:.2f} | Kategori: {task.category}")

    