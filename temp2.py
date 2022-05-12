# from kubernetes import client, config
# import json
#
# # Configs can be set in Configuration class directly or using helper utility
# config.load_kube_config()
#
# v1 = client.CoreV1Api()
# print("Listing pods with their IPs:")
# pods = []
#
# # your code here
# ret = v1.list_pod_for_all_namespaces(watch=False)
# for pod in ret.items:
#     pod_config = {"node":pod.spec.node_name,"ip":pod.status.pod_ip,"namespace":pod.metadata.namespace,"name": pod.metadata.name,"status": pod.status.phase}
#     pods.append(pod_config)
#
# output = {"pods": pods}
# output = json.dumps(output)

from os import path

print(path.join(path.dirname(__file__), "job-free.yaml"))
