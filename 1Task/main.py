from rdflib import Graph, Namespace
graph = Graph()
graph.parse('C:\\Users\\DevDmytro\\Downloads\\countrues_info.ttl')

query = """
    SELECT DISTINCT ?country_neighbour_name (MAX(?country_neighbour_population) AS ?maxPopulation)
    WHERE {
        ?country :has_country_neighbour ?country_neighbour  ;
        :part_of_continent ?continent  .
        ?continent :continent_name ?continentName .
        ?country_neighbour :country_neighbour_value ?country_neighbour_value  .
        ?country_neighbour_value :population ?country_neighbour_population  .
        ?country_neighbour_value :country_name ?country_neighbour_name  .
        FILTER(STRSTARTS(?continentName, "Europe")).
    }
    GROUP BY ?country
        """

res = graph.query(query)
for row in res:
    print(f"country: {row}")