import numpy as np

computers = np.array([
    [400, 6, 16, 2.0, 2, 7], #PC1
    [700, 8, 16, 4.0, 2, 6],  # PC2
    [1000, 12, 32, 4.5, 3, 8],  # PC3
    [10000, 16, 64, 5.0, 4, 10]  # PC4
])


prices = computers[:, 0]
cores = computers[:, 1]
ram = computers[:, 2]
frequency = computers[:, 3]
hdd = computers[:, 4]
usb_ports = computers[:, 5]



def normalize(data, is_maximized=False):
    if is_maximized:

        return 1 / data
    else:

        return data / np.sum(data)



normalized_prices = normalize(prices, is_maximized=False)
normalized_cores = normalize(cores, is_maximized=True)
normalized_ram = normalize(ram, is_maximized=True)
normalized_frequency = normalize(frequency, is_maximized=True)
normalized_hdd = normalize(hdd, is_maximized=True)
normalized_usb_ports = normalize(usb_ports, is_maximized=True)


def Voronin(computers, normalized_prices, normalized_cores, normalized_ram, normalized_frequency, normalized_hdd,
            normalized_usb_ports):

    n_computers = len(computers)
    G = np.ones(6)

    scores = np.zeros(n_computers)
    for i in range(n_computers):
        normalized_data = [
            normalized_prices[i],
            normalized_cores[i],
            normalized_ram[i],
            normalized_frequency[i],
            normalized_hdd[i],
            normalized_usb_ports[i]
        ]

        score = 0
        for j in range(len(normalized_data)):
            score += G[j] * (1 - normalized_data[j]) ** -1
        scores[i] = score


    best_computer_idx = np.argmin(scores)
    return best_computer_idx, scores


best_computer_idx, scores = Voronin(computers, normalized_prices, normalized_cores, normalized_ram,normalized_frequency, normalized_hdd, normalized_usb_ports)

# Виводимо результати
print(f'Оцінки: {scores}')
print(f'Номер оптимального комп\'ютера: {best_computer_idx + 1}')
