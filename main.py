from atlas_poo.entities.empresa import Empresa
from atlas_poo.entities.projeto import Projeto
from atlas_poo.entities.unidade_de_medida import UnidadeDeMedida
from atlas_poo.entities.unidade_tarefa import UnidadeTarefa
from atlas_poo.entities.tarefa import Tarefa
from atlas_poo.entities.predecessao import Predecessao
from atlas_poo.enum.tipo_predecessao import TipoPredecessao


from datetime import date

cnpj = "95.471.308/0001-21"
empresa = Empresa("CEIA", cnpj)

implantacao_canteiro = Tarefa("Implantação do Canteiro", 1, date(2024, 7, 25)),
escavacao_talude = Tarefa("Escavação + Talude", 45, date(2024, 7, 26))


pavimento_0 = UnidadeDeMedida("Subsolo")

pavimento_0.addUnidadeTarefa(
    UnidadeTarefa(
        implantacao_canteiro
    )
)

latencia_em_dias = 1

pavimento_0.addUnidadeTarefa(
    UnidadeTarefa(
        escavacao_talude,
        [
            Predecessao(implantacao_canteiro, TipoPredecessao.IT, latencia_em_dias)
        ]
    ),
)


projeto = Projeto("Prédio CEIA")
projeto.dataInicio = date(2024, 7, 25)
projeto.previsaoTermino = date(2025, 4, 1)
projeto.addUnidadeDeMedida(
    pavimento_0
)

