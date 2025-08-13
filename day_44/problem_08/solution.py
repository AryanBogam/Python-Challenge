import time

def simulate_deployment():
    progress_steps = [20, 40, 60, 80, 100]
    
    for progress in progress_steps:
        if progress < 100:
            print(f"Deploying... {progress}%")
            time.sleep(1)
        else:
            print("Deployment complete")

print("Starting Azure deployment...")
simulate_deployment()

print("\n" + "="*30)

def track_deployment_progress(steps):
    """
    Tracks deployment with custom steps
    """
    for i, step in enumerate(steps):
        progress = ((i + 1) / len(steps)) * 100
        
        if progress < 100:
            print(f"Deploying... {int(progress)}% - {step}")
            time.sleep(0.5)
        else:
            print("Deployment complete")

deployment_steps = [
    "Creating resource group",
    "Setting up networking", 
    "Deploying virtual machine",
    "Installing software",
    "Final configuration"
]

print("Detailed deployment tracking:")
track_deployment_progress(deployment_steps)