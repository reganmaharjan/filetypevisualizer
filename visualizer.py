import os
import matplotlib.pyplot as plt
import pandas as pd

def summarize_folder_contents(folder_path):
    file_sizes = {}
    total_size = 0

    # Traverse the directory, and fill in the file_sizes dictionary
    for root, dirs, files in os.walk(folder_path):
        for file in files:
            file_path = os.path.join(root, file)
            _, ext = os.path.splitext(file)
            if ext not in file_sizes:
                file_sizes[ext] = 0
            file_sizes[ext] += os.path.getsize(file_path)
            total_size += os.path.getsize(file_path)

    return file_sizes, total_size

def visualize_data(file_sizes, total_size):
    # Convert total size to GB
    total_size_gb = total_size / (1024 ** 3)

    # Convert file sizes to GB
    file_sizes_gb = {k: v / (1024 ** 3) for k, v in file_sizes.items()}

    # Sort file sizes for consistent plotting
    sorted_sizes = dict(sorted(file_sizes_gb.items(), key=lambda item: item[1], reverse=True))

    # Pie chart for file types by size
    plt.figure(figsize=(10, 7))
    plt.pie(sorted_sizes.values(), labels=[f'{k} ({v/total_size_gb*100:.2f}%, {v:.2f} GB)' for k, v in sorted_sizes.items()], autopct='%1.1f%%')
    plt.title('Folder Content Size Distribution by File Type')
    plt.show()

    # Bar chart for direct size comparison
    plt.figure(figsize=(10, 7))
    plt.bar(range(len(sorted_sizes)), sorted_sizes.values(), tick_label=[k for k in sorted_sizes.keys()])
    plt.title('Total Size by File Type')
    plt.xticks(rotation=45)
    plt.ylabel('Size in GB')
    plt.show()

    # Save data to Excel
    df = pd.DataFrame(list(sorted_sizes.items()), columns=['File Type', 'Size (GB)'])
    df.to_excel('file_sizes.xlsx', index=False)

# Example usage
folder_path = 'E:\epaathlfs\epaath_tracking_files'
file_sizes, total_size = summarize_folder_contents(folder_path)
visualize_data(file_sizes, total_size)