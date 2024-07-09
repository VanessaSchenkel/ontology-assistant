from rdflib import Graph
from rdflib.namespace import RDF
from rasa_sdk import Action, Tracker
from rasa_sdk.executor import CollectingDispatcher
from rasa_sdk.events import SlotSet

VA = "http://www.semanticweb.org/vanessa.schenkel/ontologies/2024/6/virtual-assistents#"

class RDFGraph:
    def __init__(self):
        self.graph = Graph()
        self.graph.parse("/Users/vanessa.schenkel/mestrado/ontology-task-manager/onto-11", format="xml")

    def query_rdf(self, query):
        return self.graph.query(query)

rdf_graph = RDFGraph()

class ActionGreet(Action):
    def name(self):
        return "action_greet"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: dict) -> list:
        dispatcher.utter_message(text="Olá! Como posso ajudar você hoje?")
        return []

class ActionListCommands(Action):
    def name(self):
        return "action_list_commands"

    def run(self, dispatcher, tracker, domain):
        query = f"""
        PREFIX va: <{VA}>
        SELECT ?comando ?texto
        WHERE {{
          ?comando a va:Comando ;
                   va:commandText ?texto .
        }}
        """
        results = rdf_graph.query_rdf(query)
        commands = [f"{row.comando.split('#')[-1]}: {row.texto}" for row in results]

        if commands:
            dispatcher.utter_message(text="Seus comandos são:\n" + "\n".join(commands))
        else:
            dispatcher.utter_message(text="Não encontrei comandos.")
        return []

class ActionListTasks(Action):
    def name(self):
        return "action_list_tasks"

    def run(self, dispatcher, tracker, domain):
        query = f"""
        PREFIX va: <{VA}>
        SELECT ?tarefa ?dataConclusao
        WHERE {{
          ?tarefa a va:Tarefa ;
                  va:dueDate ?dataConclusao .
        }}
        """
        results = rdf_graph.query_rdf(query)
        tasks = [f"{row.tarefa.split('#')[-1]}: {row.dataConclusao}" for row in results]

        if tasks:
            dispatcher.utter_message(text="Suas tarefas são:\n" + "\n".join(tasks))
        else:
            dispatcher.utter_message(text="Não encontrei tarefas.")
        return []

class ActionListDevices(Action):
    def name(self):
        return "action_list_devices"

    def run(self, dispatcher, tracker, domain):
        query = f"""
        PREFIX va: <{VA}>
        SELECT ?dispositivo ?status
        WHERE {{
          ?dispositivo a va:Dispositivo ;
                       va:deviceStatus ?status .
        }}
        """
        results = rdf_graph.query_rdf(query)
        devices = [f"{row.dispositivo.split('#')[-1]}: {row.status}" for row in results]

        if devices:
            dispatcher.utter_message(text="Seus dispositivos são:\n" + "\n".join(devices))
        else:
            dispatcher.utter_message(text="Não encontrei dispositivos.")
        return []

class ActionListEvents(Action):
    def name(self):
        return "action_list_events"

    def run(self, dispatcher, tracker, domain):
        query = f"""
        PREFIX va: <{VA}>
        SELECT ?evento ?data
        WHERE {{
          ?evento a va:Evento ;
                  va:eventDate ?data .
        }}
        """
        results = rdf_graph.query_rdf(query)
        events = [f"{row.evento.split('#')[-1]}: {row.data}" for row in results]

        if events:
            dispatcher.utter_message(text="Seus eventos são:\n" + "\n".join(events))
        else:
            dispatcher.utter_message(text="Não encontrei eventos.")
        return []

class ActionListUsers(Action):
    def name(self):
        return "action_list_users"

    def run(self, dispatcher, tracker, domain):
        query = f"""
        PREFIX va: <{VA}>
        SELECT ?user ?userEmail
        WHERE {{
          ?user a va:Usuário .
          ?user va:userEmail ?userEmail .
        }}
        """
        results = rdf_graph.query_rdf(query)
        users = [f"{row.user.split('#')[-1]}: {row.userEmail}" for row in results]

        if users:
            dispatcher.utter_message(text="Seus usuários são:\n" + "\n".join(users))
        else:
            dispatcher.utter_message(text="Não encontrei usuários.")
        return []

class ActionListHighPriorityEvents(Action):
    def name(self):
        return "action_list_high_priority_events"

    def run(self, dispatcher, tracker, domain):
        query = f"""
        PREFIX va: <{VA}>
        SELECT ?event ?eventDate
        WHERE {{
          ?event a va:Evento .
          ?event va:priorityLevel ?priority .
          FILTER (?priority = "Alta") .
          ?event va:eventDate ?eventDate .
        }}
        """
        results = rdf_graph.query_rdf(query)
        events = [f"{row.event.split('#')[-1]}: {row.eventDate}" for row in results]

        if events:
            dispatcher.utter_message(text="Seus eventos com alta prioridade são:\n" + "\n".join(events))
        else:
            dispatcher.utter_message(text="Não encontrei eventos com alta prioridade.")
        return []
