Q10. Multi-GPU Load Balancer

Task: Given multiple GPUs with workloads, find the one with the least load to assign the next task.
Why: NVIDIA uses this logic in multi-GPU setups.

Example:
Loads = [40, 30, 60] → Assign next task to GPU with 30