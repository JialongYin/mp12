@app.route('/img-classification/free',methods=['POST'])
def post_free():
    body = request.get_json(force=True)
    # You can print body to check the arguments

    # You can put the free yaml file on the EC2 and load it here
    with open(path.join(path.dirname(__file__), "free-tier.yaml")) as f:
        # Look into the usage of yaml.safe_load()
        dep = yaml.safe_load(f)
        # print `dep` to see the structure

        # To-do: generate a random deployId
        # To-do: replace some attributes of `dep` with the arguments in `body`

        k8s_apps_v1 = client.BatchV1Api()
        resp = k8s_apps_v1.create_namespaced_job(
            body=dep, namespace="free-service")
        # print `resp` to see the response

    return "success"
