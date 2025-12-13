from evaluation.metrics import evaluate_run_log

metrics = evaluate_run_log("logs/crewai-2025-12-05-22-41-42.json")
print(metrics["global"])
for vm in metrics["versions"]:
    print(vm)
