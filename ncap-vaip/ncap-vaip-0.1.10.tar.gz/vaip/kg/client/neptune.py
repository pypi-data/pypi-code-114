import json
import requests
from io import BytesIO
from rdflib.query import Result
from yurl import URL


class NeptuneClient:
    def __init__(self, endpoint="https://ncap-archive-neptune-dev."
                                "cluster-c4xlxig1zmvp.us-east-1.neptune.amazonaws.com/sparql",
                        port=8182):
        url = URL(endpoint).replace(port=port)
        self.endpoint = str(url)

    def bulk_load_neptune(self, obj_url, graph_name):
        headers = {'Content-Type': 'application/json'}
        params = {'update': f'LOAD <{obj_url}> INTO GRAPH <{graph_name}>'}
        r = requests.post(self.endpoint, params=params, headers=headers)
        return {'code': r.status_code, 'content': r.json()}

    def query(self, query):
        r = requests.post(self.endpoint, data={'query': query}, headers={"Accept": "application/sparql-results+json"})
        return {'code': r.status_code, 'content': Result.parse(BytesIO(r.content), format='json')}

    def update(self, statement):
        r = requests.post(self.endpoint, data={'update': statement})
        return {'code': r.status_code, 'content': r.json()}

    def create_graph(self, graph_name):
        update = f'CREATE GRAPH <{graph_name}>'
        return self.update(update)

    def drop_graph(self, graph_name):
        update = f'DROP GRAPH <{graph_name}>'
        return self.update(update)

    def insert_from_oaisrm(self, oaisrm, graph_name):
        nt = oaisrm.save_rdf_text(format="application/n-triples")
        update = f'INSERT DATA {{ GRAPH <{graph_name}> {{ {nt} }} }}'
        return self.update(update)

    def delete_from_oaisrm(self, oaisrm, graph_name):
        nt = oaisrm.save_rdf_text(format="application/n-triples")
        update = f'DELETE DATA {{ GRAPH <{graph_name}> {{ {nt} }} }}'
        return self.update(update)

    def load_into_oaisrm(self, oaisrm, query):
        response = self.query(query)
        results = response['content']
        for result in results:
            oaisrm.add(result[0], result[1], result[2])
        return oaisrm

    def compose_find_placeholder_sparql(self, root_iri, vaip_prefix, graph_name):
        start_iri = f"<{root_iri}>" if root_iri is not None else "?x"
        from_clause = f"FROM <{graph_name}>" if graph_name is not None else ""

        # The regex string in this query needs to be severely escaped for both python syntax (string formatting)
        # and for Neptune regular expressions (left curly braces are a special character).
        # ie., after formatting produces the string "^\\{\\{.+}}$"
        # (one backslash to escape the next backslash, which is then used to escape the curly brace in Neptune)
        sparql = f"""
        PREFIX vaip: <{vaip_prefix}>
        SELECT ?s ?o
        {from_clause}
        WHERE {{
            {start_iri} (rdf:|!rdf:)* ?s .
            ?s vaip:hasBits ?o .
            FILTER (isLiteral(?o) && regex(?o, "^\\\\{{\\\\{{.+}}}}$"))
        }}
        """
        return sparql

    def retrieve_placeholders(self, root_iri, vaip_prefix, graph_name):
        sparql = self.compose_find_placeholder_sparql(root_iri, vaip_prefix, graph_name)

        response = self.query(sparql)
        return response

    def compose_deep_node_tree_sparql(self, root_iri, graph_name):
        sparql = f"""
        CONSTRUCT {{
            <{root_iri}> ?p ?so.
            ?o ?p2 ?o2
        }}
        FROM <{graph_name}>
        WHERE
        {{
            {{
                ?o ?p2 ?o2.
                FILTER EXISTS {{
                    # The predicate pattern here is a property path matching "at least one of every predicate"
                    # the vaip: prefix here is arbitrary and could be any predicate URI
                    <{root_iri}> (rdf:|!rdf:)+ ?o
                }}
                # This extra filter removes all triples that are not NamedIndividuals (eg. our core ontology Classes, Properties etc)
                FILTER EXISTS {{
                    ?o rdf:type owl:NamedIndividual
                }}
            }}
            UNION {{
                <{root_iri}> ?p ?so
            }}
        }}
        """
        return sparql
    
    def retrieve_deep_node_tree(self, root_iri, graph_name):
        sparql = self.compose_deep_node_tree_sparql(root_iri, graph_name)

        response = self.query(sparql)
        return response

    def compose_process_template_config_sparql(self, template_iri, vaip_prefix, graph_name):
        sparql = f"""
            PREFIX vaip: <{vaip_prefix}>
            SELECT ?config
            FROM <{graph_name}>
            WHERE {{
                <{template_iri}> vaip:hasContentInformation ?o .
                ?o vaip:hasDataObject ?config_iri .
                ?config_iri vaip:hasBits ?config
            }}"""

        return sparql

    def retrieve_process_template_config(self, template_iri, vaip_prefix, graph_name):
        sparql = self.compose_process_template_config_sparql(template_iri, vaip_prefix, graph_name)

        x_template_config = None
        response = self.query(sparql)
        for rows in response['content']:
            x_template_config = rows[0]
            break

        x_template_config_object = {}
        if (x_template_config):
            # If we store the JSON as a string in the graph, then we can load it as an object and return it
            x_template_config_object = json.loads(x_template_config)

        return x_template_config_object

    def compose_downstream_process_templates_sparql(self, root_template_iri, vaip_prefix, graph_name, downstream_template_label):
        sparql = f"""
            PREFIX vaip: <{vaip_prefix}>
            SELECT ?ctx
            FROM <{graph_name}>
            WHERE {{
                <{root_template_iri}> vaip:hasContext ?ctx .
                ?ctx rdfs:label ?label.
                FILTER regex(str(?label), "{downstream_template_label}")
            }}
            """

        return sparql

    def retrieve_downstream_process_templates(self, root_template_iri, vaip_prefix, graph_name, downstream_template_label):
        sparql = self.compose_downstream_process_templates_sparql(root_template_iri, vaip_prefix, graph_name, downstream_template_label)

        process_templates = []
        response = self.query(sparql)

        for rows in response['content']:
            process_templates.append(rows[0])

        print(process_templates)
        return process_templates

    def compose_select_vaip_class_sparql(self, vaip_class, vaip_prefix, graph_name):
        sparql = f"""
            PREFIX vaip: <{vaip_prefix}>
            SELECT ?s ?label
            FROM <{graph_name}>
            WHERE {{
                ?s rdf:type {vaip_class} .
                ?s rdfs:label ?label
            }}
            """
        return sparql

    def compose_select_entity_by_uuid(self, uuid, vaip_prefix, graph_name):
        sparql = f"""
            PREFIX vaip: <{vaip_prefix}>
            SELECT ?label ?bits
            FROM <{graph_name}>
            WHERE {{
                ?s ?p ?o .FILTER regex(str(?s), {uuid}) 
                ?o vaip:hasDataObject ?do .
                ?do rdfs:label ?label .
                ?do vaip:hasBits ?bits 
            }}
            """
        return sparql

    def retrieve_entity_by_uuid(self, uuid, vaip_prefix, graph_name):
        sparql = self.compose_select_entity_by_uuid(uuid, vaip_prefix, graph_name)
        response = self.query(sparql)
        return response

    def retrieve_vaip_class(self, vaip_class, vaip_prefix, graph_name):
        sparql = self.compose_select_vaip_class_sparql(vaip_class, vaip_prefix, graph_name)
        response = self.query(sparql)
        # for rows in response['content']:
        #     print(rows[0])
        return response

