from kubernetes import client, config
from flask import Flask,request
from os import path
import yaml, random, string, json
import sys
import json

# Configs can be set in Configuration class directly or using helper utility
config.load_kube_config()
v1 = client.CoreV1Api()
app = Flask(__name__)
# app.run(debug = True)

@app.route('/config', methods=['GET'])
def get_config():
    pods = []

    # your code here
    ret = v1.list_pod_for_all_namespaces(watch=False)
    for pod in ret.items:
        pod_config = {"node":pod.spec.node_name,"ip":pod.status.pod_ip,"namespace":pod.metadata.namespace,"name": pod.metadata.name,"status": pod.status.phase}
        pods.append(pod_config)

    output = {"pods": pods}
    output = json.dumps(output)

    return output

@app.route('/img-classification/free',methods=['POST'])
def post_free():
    # your code here
    body = request.get_json(force=True)
    with open(path.join(path.dirname(__file__), "job-free.yaml")) as f:
        dep = yaml.safe_load(f)
        k8s_apps_v1 = client.BatchV1Api()
        resp = k8s_apps_v1.create_namespaced_job(
            body=dep, namespace="free-service")
    return "success"


@app.route('/img-classification/premium', methods=['POST'])
def post_premium():
    # your code here
    body = request.get_json(force=True)
    with open(path.join(path.dirname(__file__), "job-premium.yaml")) as f:
        dep = yaml.safe_load(f)
        k8s_apps_v1 = client.BatchV1Api()
        resp = k8s_apps_v1.create_namespaced_job(
            body=dep, namespace="default")
    return "success"


if __name__ == "__main__":
    app.run(host='0.0.0.0',port=5000)
