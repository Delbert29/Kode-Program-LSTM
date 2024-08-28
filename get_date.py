from datetime import datetime, timedelta

def get_input_date(start_month, end_month, year):
    # Mengonversi input bulan menjadi format 'MM'
    start_month = f"{start_month:02d}"
    end_month = f"{end_month:02d}"

    # Mengonversi input tahun menjadi format 'YYYY'
    year = str(year)

    # Membuat string format tanggal untuk start_date dan end_date
    start_date_str = f"{year}-{start_month}-01"
    
    # Menghitung jumlah hari dalam bulan end_month pada tahun yang diberikan
    last_day_of_end_month = (datetime(int(year), int(end_month) % 12 + 1, 1) - timedelta(days=1)).day

    # Format tanggal untuk end_date
    end_date_str = f"{year}-{end_month}-{last_day_of_end_month}"

    return start_date_str, end_date_str