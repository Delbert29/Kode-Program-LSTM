from sklearn.preprocessing import MinMaxScaler
import numpy as np
import pandas as pd

def predict_sales(model, train, start_date, end_date, n_input=12, n_features=1):
    scaler = MinMaxScaler()
    scaler.fit(train)
    scaled_train = scaler.transform(train)

    # Menghitung jumlah bulan untuk rentang tanggal yang dimasukkan pengguna
    data_range = pd.date_range(start='2024-01-01', end='2026-12-31', freq='M')

    # Membuat DataFrame untuk hasil prediksi
    result_df = pd.DataFrame(data_range, columns=['Tanggal'])

    # Inisialisasi input_sequence dengan data terakhir dari rentang waktu sebelumnya
    initial_data = scaled_train[-n_input:]
    input_sequence = initial_data.reshape((1, n_input, n_features))
    predictions = []

    for i in range(len(data_range)):
        current_pred = model.predict(input_sequence)[0, 0]
        predictions.append(current_pred)

        input_sequence[0, :-1, 0] = input_sequence[0, 1:, 0]
        input_sequence[0, -1, 0] = scaled_train[i - n_input, 0]

    # Menambahkan hasil prediksi ke dalam DataFrame
    result_df['Penjualan'] = scaler.inverse_transform(np.array(predictions).reshape(-1, 1)).round().astype(int)
    result_prediction = result_df[(result_df['Tanggal'] >= start_date) & (result_df['Tanggal'] <= end_date)]

    return result_prediction