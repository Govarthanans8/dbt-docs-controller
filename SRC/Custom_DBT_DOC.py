import json
import argparse

def update_docs(manifest, nodes_to_update):
    """
    Update the docs value for specified nodes.
    Set docs to true for specified nodes and false for all other nodes.
    """
    for node_name, node_info in manifest['nodes'].items():
        if node_name in nodes_to_update:
            node_info['docs']['show'] = True
        else:
            node_info['docs']['show'] = False

def true_docs(manifest):
    """
    Set the docs value for all nodes to true.
    """
    for node_name, node_info in manifest['nodes'].items():
        node_info['docs']['show'] = True

def false_docs(manifest):
    """
    Set the docs value for all nodes to false.
    """
    for node_name, node_info in manifest['nodes'].items():
        node_info['docs']['show'] = False

def list_models(manifest):
    """
    List all models in the manifest file.
    """
    for node_name in manifest['nodes']:
        print(node_name)

def main(input_nodes):
    # Load the manifest.json file
    with open('target/manifest.json', 'r') as file:
        manifest = json.load(file)

    if 'true-all' in input_nodes:
        true_docs(manifest)
    elif 'false-all' in input_nodes:
        false_docs(manifest)
    elif 'list' in input_nodes:
        list_models(manifest)
        return
    else:
        update_docs(manifest, input_nodes)

    # Save the updated manifest.json file
    with open('target/manifest.json', 'w') as file:
        json.dump(manifest, file, indent=4)

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Update docs value in manifest.json for specified nodes.")
    parser.add_argument('nodes', metavar='N', type=str, nargs='+',
                        help='List of node names to update, "true-all" to set all docs values to true, "false-all" to set all docs values to false, or "list" to list all models')

    args = parser.parse_args()
    input_nodes = args.nodes

    main(input_nodes)