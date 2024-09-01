import java.io.FileWriter;
import java.io.IOException;
import java.io.PrintWriter;
import java.util.ArrayList;
import java.util.List;
import java.util.Scanner;

import classes.Aluno;
import classes.Aula;
import classes.Boleto;
import classes.Professor;
import classes.Turma;

public class App {
    public static void main(String[] args) throws Exception {
        System.out.println("\u001B[32m"+"Bem-vindo ao Sistema de Gerenciamento de Escolas de Idioma!"+ "\u001B[0m");
        
        // Criação dos objetos
        List<Aluno> alunos = new ArrayList<>();
        List<Professor> professores = new ArrayList<>();
        List<Turma> turmas = new ArrayList<>();
        List<Aula> aulas = new ArrayList<>();
        List<Boleto> boletos = new ArrayList<>();
        
        // Menu de seleção de ações
        Scanner scanner = new Scanner(System.in);
        int opcao = 0;
        
        while (opcao != 6) {
            System.out.println("Selecione a acao:");
            System.out.println("1. Cadastrar aluno");
            System.out.println("2. Criar turma");
            System.out.println("3. Agendar aulas");
            System.out.println("4. Gerar boleto");
            System.out.println("5. Visualizar alunos cadastrados");
            System.out.println("6. Sair");

            System.out.print("--> ");
            opcao = scanner.nextInt();
            
            switch (opcao) {
                case 1:
                    // Cadastrar aluno
                    scanner.nextLine(); // Limpar o buffer
                    System.out.println("Digite o nome do aluno:");
                    String nomeAluno = scanner.nextLine();
                    
                    System.out.println("Digite a idade do aluno:");
                    int idadeAluno = scanner.nextInt();
                                        
                    Aluno alunoNovo = new Aluno(nomeAluno, idadeAluno);
                    alunos.add(alunoNovo);
                    try {
                        PrintWriter writer = new PrintWriter(new FileWriter("alunos.txt"));
                        for (Aluno aluno : alunos) {
                            writer.println(aluno.toString());
                        }

                        writer.close();
                        System.out.println("Dados dos alunos salvos no arquivo com sucesso!");
                    } catch (IOException e) {
                        System.out.println("Erro ao salvar os dados dos alunos no arquivo: " + e.getMessage());
}
                    System.out.println("\u001B[32m"+"Aluno cadastrado com SUCESSO!"+ "\u001B[0m");
                    
                    break;
                case 2:
                    // Criar turma                    
                    Turma turma = new Turma();
                    System.out.println("\u001B[32m"+"Turma criada com SUCESSO!"+ "\u001B[0m");
                    turmas.add(turma);
                    break;
                    case 3:
                    // Agendar aulas
                    scanner.nextLine(); // Limpar o buffer
                    System.out.println("Digite a data da aula (dd/mm/aaaa):");
                    String dataAula = scanner.nextLine();
                    
                    System.out.println("Digite o horario da aula (hh:mm):");
                    String horarioAula = scanner.nextLine();

                    System.out.println("Digite o numero da sala :");
                    String input = scanner.nextLine();
                    int numeroSalaAula;
                    try {
                        numeroSalaAula = Integer.parseInt(input);
                    } catch (NumberFormatException e) {
                        System.out.println("Entrada inválida. Digite um número inteiro.");
                        break;
                    }
                    
                    System.out.println("Digite o codigo da turma :");
                    input = scanner.nextLine();
                    int numeroTurmaAula;
                    try {
                        numeroTurmaAula = Integer.parseInt(input);
                    } catch (NumberFormatException e) {
                        System.out.println("Entrada inválida. Digite um número inteiro.");
                        break;
                    }

                    Turma turmaAula = procurarTurmaPorNumero(turmas, numeroTurmaAula);
                    if (turmaAula== null) {
                        System.out.println("\u001B[33m" + "Turma nao encontrada, verifique os codigos das turmas cadastradas no sistema."+ "\u001B[0m");
                        break;
                    }

                    scanner.nextLine(); // Limpar o buffer
                    System.out.println("Digite o nome do professor:");
                    String nomeProfessor = scanner.nextLine();

                    Professor professorAula = procurarProfessorPorNome(professores, nomeProfessor);
                    
                    if (professorAula== null) {
                        System.out.println("\u001B[33m"+"Professor nao encontrado, verifique os professores cadastrados no sistema."+ "\u001B[0m");
                        break;
                    }

                    System.out.println("Digite a disciplina da aula:");
                    String disciplinaAula = scanner.nextLine();
                    
                    
                    Aula aula = new Aula(horarioAula,dataAula,numeroSalaAula,turmaAula,professorAula,disciplinaAula);
                    aulas.add(aula);
                    System.out.println("\u001B[32m"+"Aula agendada com SUCESSO!"+ "\u001B[0m");
                    
                    break;
                case 4:
                    System.out.println("Digite o valor do boleto:");
                    float valorBoleto = scanner.nextFloat();
                    
                    System.out.println("Digite a data de vencimento do boleto (dd/mm/aaaa):");
                    String dataVencimento = scanner.nextLine();
                    
                    scanner.nextLine(); // Limpar o buffer
                    System.out.println("Digite o nome do aluno Pagador:");
                    input = scanner.nextLine();
                    Aluno alunoPagador = procurarAlunoPorNome(alunos, input);
                    if (alunoPagador== null) {
                        System.out.println("\u001B[33m"+"Aluno nao encontrado, verifique os alunos cadastrados no sistema."+ "\u001B[0m");
                        break;
                    }
                    Boleto boleto = new Boleto(valorBoleto, alunoPagador, dataVencimento);
                    System.out.println("\u001B[32m"+"Boleto gerado com SUCESSO!"+ "\u001B[0m");
                    boletos.add(boleto);
                    break;
                case 5:
                    // Visualizar alunos cadastrados
                    if (alunos.isEmpty()) {
                        System.out.println("\u001B[33m" + "Nenhum aluno cadastrado." + "\u001B[0m");
                    }else {
                        System.out.println("\u001B[32m" + "Alunos cadastrados:" + "\u001B[0m");
                        for (Aluno aluno : alunos) {
                            System.out.println(aluno.toString());
                        }
                    }
                    break;
                case 6:
                    // Sair do programa
                    System.out.println("Saindo do programa...");
                    break;
                default:
                    System.out.println("Opção inválida. Selecione uma opção válida.");
                    break;
            }
            
            System.out.println(); 
        }
        
        scanner.close();
    }

    public static Professor procurarProfessorPorNome(List<Professor> professores, String nomeProcurado) {
        for (Professor professor : professores) {
            if (professor.getNome().equals(nomeProcurado)) {
                return professor; // Professor encontrado
            }
        }
        return null; // Professor não encontrado
    }

    public static Aluno procurarAlunoPorNome(List<Aluno> alunos, String nomeProcurado) {
        for (Aluno aluno : alunos) {
            if (aluno.getNome().equals(nomeProcurado)) {
                return aluno; // aluno encontrado
            }
        }
        return null; // aluno não encontrado
    }

    public static Turma procurarTurmaPorNumero(List<Turma> turmas, int turmaProcurada) {
        for (Turma turma : turmas) {
            if (turma.getCodigoTurma() == turmaProcurada) {
                return turma; // turma encontrado
            }
        }
        return null; // turma não encontrado
    }
}