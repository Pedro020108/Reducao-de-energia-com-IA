import random

def gerar_tarefas(qtd=20):
    tarefas = []
    for i in range(qtd):
        tarefa = {
            "id": i + 1,
            "complexidade": random.choice(["baixa", "media", "alta"]),
            "erros": random.randint(0, 6),
            "tempo_min": random.randint(10, 140)
        }
        tarefas.append(tarefa)
    return tarefas

def acao_da_ia(tarefa):

    if tarefa["erros"] > 3 and tarefa["complexidade"] == "alta":
        return "Revisão de lógica (evita bugs críticos)"

    if tarefa["erros"] > 0:
        return "Checklist automático (reduz erros)"

    if tarefa["tempo_min"] > 60:
        return "Sugestão de código otimizado (reduz tempo)"

    return "Nenhuma ação necessária"

def impacto_energia(tarefa, acao):

    energia_inicial = tarefa["tempo_min"] * 0.0015

    if "Revisão" in acao:
        energia_final = energia_inicial * 0.70
    elif "Checklist" in acao:
        energia_final = energia_inicial * 0.85
    elif "Sugestão" in acao:
        energia_final = energia_inicial * 0.80
    else:
        energia_final = energia_inicial

    return energia_inicial, energia_final

def rodar_simulacao():
    tarefas = gerar_tarefas()

    relatorio = []
    energia_total_inicial = 0
    energia_total_final = 0

    for tarefa in tarefas:
        acao = acao_da_ia(tarefa)
        e_inicial, e_final = impacto_energia(tarefa, acao)

        energia_total_inicial += e_inicial
        energia_total_final += e_final

        relatorio.append({
            "id": tarefa["id"],
            "complexidade": tarefa["complexidade"],
            "erros": tarefa["erros"],
            "tempo_min": tarefa["tempo_min"],
            "acao_da_ia": acao,
            "energia_inicial_kwh": round(e_inicial, 4),
            "energia_final_kwh": round(e_final, 4),
        })

    economia = energia_total_inicial - energia_total_final
    economia_pct = (economia / energia_total_inicial) * 100

    print("\nRELATÓRIO FINAL\n")
    print(f"Energia Inicial Total: {energia_total_inicial:.4f} kWh")
    print(f"Energia Final Total:   {energia_total_final:.4f} kWh")
    print(f"Economia Total:        {economia:.4f} kWh")
    print(f"Economia Percentual:   {economia_pct:.2f}%\n")

    print("Sugestões da IA:")
    for item in relatorio:
        print(
            f"- Tarefa {item['id']}: {item['acao_da_ia']} "
            f"(Economia: {item['energia_inicial_kwh'] - item['energia_final_kwh']:.4f} kWh)"
        )

if __name__ == "__main__":
    rodar_simulacao()
