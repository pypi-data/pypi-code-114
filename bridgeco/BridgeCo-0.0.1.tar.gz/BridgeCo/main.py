from base64 import b64encode
from httpx import get, post
from datetime import datetime
from dateutil.relativedelta import relativedelta


class BridgeAD:
    def __init__(self, token: str):
        self._organization = 'bridge-tech'
        self._project = 'Bridge%20Technology'
        self._token = b64encode(f':{token}'.encode()).decode()
        self._headers = {'Content-Type':'application/json','Authorization':f'Basic {self._token}'}

    def __endpoint_item(cls, item_type: str) -> str:
        """
            Cria um work item no respectivo projeto.
            https://docs.microsoft.com/en-us/rest/api/azure/devops/wit/work-items/create?view=azure-devops-rest-6.0
        """
        return f"https://dev.azure.com/{cls._organization}/{cls._project}/_apis/wit/workitems/${item_type}?api-version=6.0" 
    
    def __endpoint_iterations(cls, squad: str) -> str:
        """
            Retorna todos as iterations(sprints) de uma squad.
            https://docs.microsoft.com/en-us/rest/api/azure/devops/work/iterations/list?view=azure-devops-rest-6.0
        """
        return f'https://dev.azure.com/{cls._organization}/{cls._project}/{squad}/_apis/work/teamsettings/iterations?api-version=6.0'

    def __endpoint_tags(cls):
        """
            Retorna todas as tags de um projeto.
            https://docs.microsoft.com/en-us/rest/api/azure/devops/wit/tags/list?view=azure-devops-rest-6.0
        """
        return f'https://dev.azure.com/{cls._organization}/{cls._project}/_apis/wit/tags?api-version=6.0-preview.1'

    def __get(cls, url: str):
        """
            Método http get com `headers já configurados` para estabelecer conexão com os endpoints.
            :param url: Endereço do endpoint que receberá a solicitação.
            :type url: str
        """
        return get(url=url, headers=cls._headers)

    def __processing_interation(cls, response: dict):
        """
            Recebe um dicionário e retorna um list comprehension com as informações das iterações.
        """
        comprehension = [
            {
            'Iteration_Path': values['path'],
            'Iteration_Start_Date': values['attributes']['startDate'],
            'Iteration_End_Date': values['attributes']['finishDate'],
            'Iteration_State': values['attributes']['timeFrame'],
            } for values in response['value']
            ]
        return comprehension

    def __get_team_interations(self, squad: str):
        """
            Retorna todas iterations(sprints) de uma squad.
            :param squad: Nome de uma squad dentro da organização e projeto.
            :type squad: str
        """
        endpoint = self.__endpoint_iterations(squad)
        response = self.__get(endpoint).json()
        clean_response = self.__processing_interation(response)
        return clean_response

    def tags(self):
        """
            Retorna todas as tags de um projeto.
        """
        endpoint = self.__endpoint_tags()
        response = self.__get(endpoint).json()
        tags = [print(item['name']) for item in response['value']]

    def criar_item(self, titulo: str, tipo: str, atribuido: str, squad: str, tag: str, horas_previstas: str = 0, sprint_atual: bool = True, status: str = 'New', 
    descricao: str = '', pai: int = None, filho: int = None, modelo_contratacao: str = None, horas_consumidas: float = 0, horas_contratadas: float = 0):
        """
            Cria um item de trabalho no projeto Bridge Technology, suportando apenas os tipos: `Projeto`, `Produto`, `Entrega`, `Atividade`.
        """
        endpoint = self.__endpoint_item(tipo)
        iterations = self.__get_team_interations(squad)
        current = list(filter(lambda iteration: iteration['Iteration_State'] == 'current', iterations))[0]
        area_path = '\\'.join(current['Iteration_Path'].split('\\')[0:2])
        index_current = iterations.index(current)
        next_iteration = iterations[index_current + 1]
        iteration = current if sprint_atual == True else next_iteration
        data = [
            {
            "op": "add",
            "path": "/fields/System.Title",
            "value": titulo,
            },
            {
            "op": "add",
            "path": "/fields/System.AssignedTo",
            "value": atribuido,
            },
            {
            "op": "add",
            "path": "/fields/System.State",
            "value": status,
            },
            {
            "op": "add",
            "path": "/fields/System.AreaPath",
            "value": area_path,
            },
            {
            "op": "add",
            "path": "/fields/System.IterationPath",
            "value": iteration['Iteration_Path'],
            },
            {
            "op": "add",
            "path": "/fields/System.Tags",
            "value": tag,
            },
            {
            "op": "add",
            "path": "/fields/System.Description",
            "value": descricao,
            }
        ]

        if pai is not None:
            data.extend([
                {
                    "op": "add",
                    "path": "/relations/-",
                    "value": {
                        "rel": "System.LinkTypes.Hierarchy-Reverse",
                        "url": f"https://dev.azure.com/{self._organization}/{self._project}/_apis/wit/workitems/{pai}"}
                }])

        if filho is not None:
            data.extend([
                {
                    "op": "add",
                    "path": "/relations/-",
                    "value": {
                        "rel": "System.LinkTypes.Hierarchy-Forward",
                        "url": f"https://dev.azure.com/{self._organization}/{self._project}/_apis/wit/workitems/{filho}"}
                }])

        if tipo == 'Projeto':
            data.extend([
                {
                    "op": "add",
                    "path": "/fields/Custom.HorasContratadas",
                    "value": horas_contratadas,
                },
                {
                    "op": "add",
                    "path": "/fields/Custom.96767056-32a1-434a-a70f-9cd733ff55be", #Modelo de Contratação
                    "value": modelo_contratacao,
                }])

        if tipo in ('Produto', 'Entrega', 'Atividade'):
            data.extend([
                {
                    "op": "add",
                    "path": "/fields/Custom.fb18e9ab-15ca-4bac-8a8b-366be7b6f22d", #Data de inicio planejada 
                    "value": self.__convert_utc(iteration['Iteration_Start_Date']),
                },                
                {
                    "op": "add",
                    "path": "/fields/Custom.DatadeFimReal", #Data de fim real
                    "value": self.__convert_utc(iteration['Iteration_Start_Date'])
                }])

        if tipo in ('Projeto', 'Produto', 'Entrega', 'Atividade'):
            data.extend([

                {
                    "op": "add",
                    "path": "/fields/Custom.DatadeFimPlanejada", #Data de fim planejada 
                    "value": self.__convert_utc(iteration['Iteration_End_Date']),
                },
                {
                    "op": "add",
                    "path": "/fields/Custom.f361e24c-d296-4f3b-97a2-318ee884dbfb", #Data de inicio real
                    "value": self.__convert_utc(iteration['Iteration_Start_Date']),
                }])
        
        if tipo in ('Entrega', 'Atividade'):
            data.extend([
                {
                    "op": "add",
                    "path": "/fields/Custom.HorasPrevistas",
                    "value": horas_previstas
                }])
        
        if tipo == 'Atividade':
            data.extend([
                {
                    "op": "add",
                    "path": "/fields/Custom.HorasConsumidas",
                    "value": horas_consumidas
                }])

        response = post(url=endpoint, headers={'Content-Type':'application/json-patch+json', 'Authorization':f'Basic {self._token}'}, json=data)
        if response.status_code == 200:
            print(f"200 - {response.json()['id']}")
        else:
            raise Exception(response.status_code)
        
    @staticmethod
    def __convert_utc(item: str):
        """
            Converte um datetime GMT-3 em uma string UTC.
        """
        i = item.find('T')
        date = datetime.strptime(item[:i], "%Y-%m-%d") + relativedelta(hours = 3)
        return datetime.strftime(date, "%Y-%m-%dT%H:%M:%S.%fZ")