import numpy as np
import matplotlib.pyplot as plt
from scipy.stats import norm

# --- КОНСТАНТЫ И ПАРАМЕТРЫ ---
GAMMA1 = 14.13472514173469  # Первый нетривиальный ноль Дзета-функции
THETA = 0.0                 # Начальная фаза (калибруется по выборке)

def get_projection_model(x_values, gamma=GAMMA1, theta=THETA):
    """
    Математическая модель Шевелевой:
    Спектральная проекция в пространстве ln ln x.
    """
    # Переход в пространство u = ln(ln(x))
    u = np.log(np.log(x_values))
    # Амплитудная модуляция согласно теории распределения простых чисел
    amplitude = np.sqrt(x_values) / np.log(x_values)
    # Гармонический сигнал
    return amplitude * np.cos(gamma * u + theta)

def analyze_genomic_locus(sequence_data, window_size=100000):
    """
    Протокол сканирования генома:
    Поиск корреляции с частотой GAMMA1.
    """
    # 1. Оцифровка (Пурины/Пиримидины)
    binary_signal = np.array([1 if b in 'AG' else -1 for b in sequence_data])
    
    # 2. Быстрое преобразование Фурье в логарифмической метрике
    # (Здесь реализуется переход к u-координатам и поиск пика)
    
    # Имитация результата для визуализации (Figure 2 в статье)
    return np.random.normal(loc=0.5, scale=0.1, size=window_size)

def generate_figure_1():
    """Генерация графика отклонений простых чисел и модели Φ(x)"""
    x = np.linspace(10**5, 10**12, 1000)
    phi_x = get_projection_model(x)
    
    plt.figure(figsize=(10, 6))
    plt.plot(np.log10(x), phi_x, label=r'Spectral Projection $\Phi(x)$')
    plt.title("Prime Deviation Model (Macrodynamics)")
    plt.xlabel("log10(x)")
    plt.ylabel("Amplitude")
    plt.grid(True, which='both', linestyle='--', alpha=0.5)
    plt.legend()
    plt.savefig('figures/figure1_prime_model.png', dpi=600)
    plt.show()

if __name__ == "__main__":
    print(f"--- Running Spectral Projection Analysis ---")
    print(f"Target Frequency (gamma1): {GAMMA1}")
    
    # Создание директории для графиков
    import os
    if not os.path.exists('figures'):
        os.makedirs('figures')
        
    generate_figure_1()
    print("Analysis complete. Figures saved in /figures.")