import numpy as np

difficulty_pow = np.arange(10, 60, 10)
energy_per_hash = 3
hashes_per_block = difficulty_pow * 1_000_000
energy_pow = hashes_per_block * energy_per_hash

validators = 400
energy_pos = np.full(len(difficulty_pow), validators * 0.0005)

block_time_pow = 600
block_time_pos = 12
tx_per_block = 2000

tps_pow = tx_per_block / block_time_pow
tps_pos = tx_per_block / block_time_pos

print("Energy PoW:", energy_pow)
print("Energy PoS:", energy_pos)
print("TPS PoW:", tps_pow)
print("TPS PoS:", tps_pos)
