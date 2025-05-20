def main():
    print("=== Registro de Notas da Turma ===")
    print("Digite as notas dos alunos (0 a 10). Digite 'fim' para encerrar.")

    notas = []

    while True:
        entrada = input("Nota (ou 'fim' para sair): ").strip().lower()
        if entrada == 'fim':
            break

        # Usar uma única linha para validar e converter entrada
        if entrada.replace('.', '', 1).isdigit():  # aceita ponto decimal uma vez
            nota = float(entrada)
            if 0 <= nota <= 10:
                notas.append(nota)
            else:
                print("Nota inválida! Deve ser entre 0 e 10.")
        else:
            print("Entrada inválida! Digite um número ou 'fim'.")

    if notas:
        media = sum(notas) / len(notas)
        print(f"\nMédia da turma: {media:.2f}")
    else:
        print("\nNenhuma nota válida foi registrada.")

if __name__ == "__main__":
    main()

