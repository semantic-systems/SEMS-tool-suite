from pyvis.network import Network
import networkx as nx
import requests


def wikidata_uri_to_property_value(uri):
    # Extract the QID from the provided URI
    qid = uri.split("/")[-1]

    # Define the Wikidata API URL
    api_url = f"https://www.wikidata.org/w/api.php"

    # Define the parameters for the API request to fetch labels and descriptions
    params = {
        "action": "wbgetentities",
        "format": "json",
        "ids": qid,
        "languages": "en",
        "props": "labels|descriptions"
    }

    try:
        # Send a GET request to the Wikidata API
        response = requests.get(api_url, params=params)
        data = response.json()

        # Check if the response contains labels and descriptions
        entity_data = data.get("entities", {}).get(qid, {})
        if "labels" in entity_data and "descriptions" in entity_data:
            labels = entity_data["labels"]
            descriptions = entity_data["descriptions"]

            # Extract label and description values
            label = labels.get("en", {}).get("value", "Label not found")
            description = descriptions.get("en", {}).get("value", "Description not found")

            return label, description

    except Exception as e:
        print("Error:", e)

    return None, None


def visualization(graph):
    net = Network()

    net.add_node(0, label=graph['http://www.w3.org/2000/01/rdf-schema#comment'][0]["@value"],
                 title='http://www.w3.org/2000/01/rdf-schema#comment')
    label, description = wikidata_uri_to_property_value(graph["@type"][-1])
    net.add_node(1, label=label, title=description)
    net.add_edge(0, 1, title="type")
    net.add_node(2, label=graph['https://schema.coypu.org/global#hasPublisher'][0]["@value"])
    net.add_edge(0, 2, title="hasPublisher")
    net.add_node(3, label=graph['https://schema.coypu.org/global#hasTimestamp'][0]["@value"])
    net.add_edge(0, 3, title="hasTimestamp")
    counter = 3
    if 'https://schema.coypu.org/global#hasLocality' in graph:
        location_count = len(graph['https://schema.coypu.org/global#hasLocality'])
        for i in range(location_count):
            label, description = wikidata_uri_to_property_value(
                graph['https://schema.coypu.org/global#hasLocality'][i]["@id"])
            net.add_node(4 + i, label=label, title=description)
            net.add_edge(0, 4 + i, title="hasLocality")
        counter = 3 + location_count
    if 'https://schema.coypu.org/global#hasImpactOn' in graph:
        impact_count = len(graph['https://schema.coypu.org/global#hasImpactOn'])
        for i in range(impact_count):
            label, description = wikidata_uri_to_property_value(
                graph['https://schema.coypu.org/global#hasImpactOn'][i]["@id"])
            net.add_node(counter + i + 1, label=label, title=description)
            net.add_edge(0, counter + i + 1, title="hasImpactOn")

    net.toggle_physics(True)
    html = net.generate_html()
    html = html.replace("'", "\"")
    return f"""<iframe style="width: 100%; height: 600px;margin:0 auto" name="result" allow="midi; geolocation; microphone; camera; 
        display-capture; encrypted-media;" sandbox="allow-modals allow-forms 
        allow-scripts allow-same-origin allow-popups 
        allow-top-navigation-by-user-activation allow-downloads" allowfullscreen="" 
        allowpaymentrequest="" frameborder="0" srcdoc='{html}'></iframe>"""
