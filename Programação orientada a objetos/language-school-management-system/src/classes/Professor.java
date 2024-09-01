package classes;

import java.util.ArrayList;
import java.util.List;

public class Professor {
    private String nome;
    private int idade;
    private List<String> idiomas;
    private int id;

    public Professor(String nome, int idade, int id) {
        this.nome = nome;
        this.idade = idade;
        this.idiomas = new ArrayList<>();
        this.id = id;
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
    
    public void setIdiomas(String idioma) {
        this.idiomas.add(idioma);
    }

    public List<String> getIdiomas() {
        return this.idiomas;
    }
    
    public void setId(int id) {
        this.id = id;
    }

    public int getId() {
        return this.id;
    }

    public String toString() {
        return "Nome: " + this.nome + ", Idade: " + this.idade + ", Idioma: " + this.getIdiomas() + ", ID: " + this.id;
    }
}