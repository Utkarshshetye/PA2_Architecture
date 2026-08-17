import matplotlib.pyplot as plt

benchmarks = ['Trace 1', 'Trace 2', 'Trace 3', 'Trace 4']
exclusive_speedup = [0.8105, 0.80125, 0.86432, 0.804876]

bar_width = 0.35
x = range(len(benchmarks))

plt.figure(figsize=(8,5))
bars = plt.bar(x, exclusive_speedup, width=bar_width, color='#90EE90', edgecolor='black', label='Speedup over Non-Inclusive')

plt.xlabel('Trace Files', fontsize=12)
plt.ylabel('Speedup', fontsize=12)
plt.title('Cache Speedup Comparison', fontsize=14)
plt.xticks(x, benchmarks)
plt.ylim(0.60, 0.90)
plt.legend()

for bar, value in zip(bars, exclusive_speedup):
    plt.text(bar.get_x() + bar.get_width()/2, value + 0.005, f'{value:.3f}', ha='center', va='bottom', fontsize=10)

plt.tight_layout()
plt.savefig('speedup_plot')