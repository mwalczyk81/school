"""
Knowledge Representation and Reasoning Assignment

This assignment explores the principles of knowledge representation and reasoning in AI, including
symbolic logic, ontologies, semantic networks, and reasoning algorithms.

Focus areas:
a. Symbolic Logic and Rule-Based Systems
b. Ontologies and Semantic Networks in AI
c. Reasoning Algorithms and their Implementation
"""


def apply_modus_ponens(facts, rules):
    """
    Apply the Modus Ponens inference rule on a set of facts and rules to infer new facts.

    Parameters:
    facts (set): A set of strings representing known facts (e.g., {"A", "B"}).
    rules (list of tuples): A list of tuples representing implication rules (e.g., [("A", "B"), ("B", "C")])
                            where each tuple is (antecedent, consequent).

    Returns:
    new_facts (set): A set of newly inferred facts.
    """
    # Your code here
    inferred_facts = facts.copy()
    updated = True
    
    # I did not add the if check to break the loop because the while loop will break when updated is False
    while updated:
        updated = False
        
        for rule in rules:
            antecedent, consequent = rule
            
            if antecedent in inferred_facts and consequent not in inferred_facts:
                inferred_facts.add(consequent)
                updated = True
        
    return inferred_facts


def build_semantic_network(entities, relations):
    """
    Build a semantic network from a list of entities and relations.

    Parameters:
    entities (list): A list of entities (nodes) in the network.
    relations (list of tuples): A list of tuples representing relations between entities (e.g., [("A", "related_to", "B")]).

    Returns:
    semantic_network (dict): A dictionary representing the semantic network, where keys are entity names and
                              values are dictionaries of relations and their corresponding entities.
    """
    # Your code here
    semantic_network = {}
    
    for entity in entities:
        semantic_network[entity] = {}
        
    for relation in relations:
        entity1, rel, entity2 = relation
        
        if entity1 in semantic_network:
            
            if rel not in semantic_network[entity1]:
                # Skipping the empty list creation and appending by just assigning the list directly
                semantic_network[entity1][rel] = [entity2]
            
    return semantic_network


def forward_chaining(knowledge_base, query):
    """
    Implement the forward chaining algorithm for propositional logic to determine if the query can be inferred from the knowledge base.

    Parameters:
    knowledge_base (dict): A dictionary representing the knowledge base, with each key being a rule represented as a tuple of antecedents,
                           and the value being the consequent (e.g., {("A", "B"): "C"}).
    query (str): The fact to be checked against the knowledge base.

    Returns:
    inferred (bool): True if the query can be inferred from the knowledge base using forward chaining, False otherwise.
    """
    # Your code here
    inferred_facts = set()
    agenda = set()    
    
    # Not sure if there is a better way to do this, but it works and the tests pass
    for antecedents, consequent in knowledge_base.items():
        if all(antecedent in inferred_facts for antecedent in antecedents):
            agenda.add(consequent)
    
    while len(agenda) > 0:
        fact = agenda.pop()
        
        if fact == query:
            return True
        
        inferred_facts.add(fact)
        
        for antecedents, consequent in knowledge_base.items():            
            if all(antecedent in inferred_facts for antecedent in antecedents) and consequent not in inferred_facts:
                agenda.add(consequent)
    
    return False

