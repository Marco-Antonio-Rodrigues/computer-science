package classes;

import java.util.HashMap;
import java.util.Map;

public class Aluno {
    private static int numeroAlunos = 0;
    private String nome;
    private int idade;
    private int matricula;
    private boolean ativo;
    private Map<String, String> nivelIdioma;

    public Aluno(String nome, int idade) {
        numeroAlunos++;
        this.nome = nome;
        this.idade = idade;
        this.matricula = (numeroAlunos*100);
        this.ativo = true;
        this.nivelIdioma = new HashMap<>();
    }

    public void setNome(String nome) {
        this.nome = nome;
    }

    public String getNome() {
        return this.nome;
    }

    public void setIdade(int idade) {
        this.idade = idade;
    }

    public int getIdade() {
        return this.idade;
    }

    public void setMatricula(int matricula) {
        this.matricula = matricula;
    }

    public int getMatricula() {
        return this.matricula;
    }

    public void setNivelIdioma(String idioma, String nivel) {
        this.nivelIdioma.put(idioma, nivel);
    }

    public String getNivelIdioma(String idioma) {
        return this.nivelIdioma.getOrDefault(idioma, "Aluno não estuda esse idioma");
    }

    public String toString() {
        return "Nome: " + this.nome + ", Idade: " + this.idade + ", Matrícula: " + this.matricula + ", Ativo: " + this.ativo;
    }
}